### (B) `transcribe.py` (メインプログラム)
import mlx_whisper

def transcribe_audio(file_path: str) -> str:
    """
    指定された音声ファイルを文字起こしし、結果をファイルに保存する。
    """
    
    result = mlx_whisper.transcribe(
      file_path, path_or_hf_repo="whisper-base-mlx"
    )
    print(result["text"])
    result_text = str(result["text"])
    return result_text