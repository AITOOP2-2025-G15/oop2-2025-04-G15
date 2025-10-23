### (B) `transcribe.py` (メインプログラム)
import whisper
import os
import argparse
import torch
import time

def transcribe_audio(file_path: str, model_size: str):
    """
    指定された音声ファイルを文字起こしし、結果をファイルに保存する。
    """
    
    # --- 1. 入力ファイルの存在確認 ---
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません: {file_path}")
        return

    print(f"処理開始: '{file_path}'")
    start_time = time.time()

    # --- 2. 出力先の準備 ---
    output_dir = "transcripts"
    os.makedirs(output_dir, exist_ok=True) # "transcripts" フォルダがなければ作成

    # 出力ファイル名を決定 (例: audio_files/meeting.mp3 -> transcripts/meeting.txt)
    base_filename = os.path.basename(file_path) # "meeting.mp3"
    filename_without_ext = os.path.splitext(base_filename)[0] # "meeting"
    output_path = os.path.join(output_dir, f"{filename_without_ext}.txt")

    # --- 3. Whisperモデルのロード ---
    # GPU(CUDA or MPS)が使えるか確認し、使えるならGPUを、なければCPUを使用
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available(): # Apple Silicon (M1/M2/M3)
        device = "mps"
    else:
        device = "cpu"

    print(f"使用デバイス: {device}")
    print(f"Whisperモデル '{model_size}' をロード中... (初回はダウンロードに時間がかかります)")
    
    try:
        model = whisper.load_model(model_size, device=device)
    except Exception as e:
        print(f"モデルのロード中にエラーが発生しました: {e}")
        return

    # --- 4. 文字起こしの実行 ---
    print("文字起こしを実行中...")
    try:
        # fp16=False にするとCPUでも安定動作しやすくなります
        # deviceが"cpu"の場合は自動でfp16=Falseになりますが、明示的に指定
        use_fp16 = False if device == "cpu" else True
        
        result = model.transcribe(file_path, fp16=use_fp16, language="ja") # 日本語を指定
        
        transcribed_text = result["text"]
        
        return transcribed_text
        
        # # コンソールにも結果を一部表示（長い場合は省略）
        # print("\n--- 文字起こし結果 (冒頭100文字) ---")
        # print(transcribed_text[:100] + "...")
        # print("--------------------")

    except Exception as e:
        print(f"文字起こし中にエラーが発生しました: {e}")
        print("ffmpeg が正しくインストールされているか確認してください。")

if __name__ == "__main__":
    # --- 6. コマンドラインから引数を受け取る設定 ---
    parser = argparse.ArgumentParser(description="Whisperを使って音声ファイルを文字起こしします。")
    
    # 必須の引数: どのファイルを処理するか
    parser.add_argument(
        "audio_file", 
        type=str, 
        help="文字起こしする音声ファイルのパス (例: audio_files/meeting.mp3)"
    )
    
    # オプションの引数: どのモデルを使うか
    parser.add_argument(
        "--model", 
        type=str, 
        default="base", 
        choices=["tiny", "base", "small", "medium", "large"],
        help="使用するWhisperモデルのサイズ (default: base)"
    )

    args = parser.parse_args()
    
    # メインの関数を実行
    transcribe_audio(args.audio_file, args.model)