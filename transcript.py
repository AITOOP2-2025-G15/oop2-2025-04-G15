### (B) `transcribe.py` (メインプログラム)
import mlx_whisper
import os

def transcribe_audio(file_path: str, model_size: str):
    """
    指定された音声ファイルを文字起こしし、結果をファイルに保存する。
    """
    
    #入力ファイルの存在確認
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません: {file_path}")
        return

    result = mlx_whisper.transcribe(file_path, path_or_hf_repo="whisper-base-mlx")
    return result
