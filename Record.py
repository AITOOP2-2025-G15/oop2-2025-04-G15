import ffmpeg
import time
"""
    10秒間音声を録音し、生成されたファイルのパスを返す

    recording: str
    録音用の関数
"""


def recording() -> str:
    """
    10秒間音声を録音した後、生成されたファイルのパスを返す

    Return
    ----------
    output_file: str
    生成されたファイルのファイル名
    """
    # 録音時間（秒）
    duration = 10
    # 出力ファイル名
    output_file = 'python-audio-output.wav'

    try:
        print(f"{duration}秒間、マイクからの録音を開始します...")
        (
            ffmpeg
            .input(':0', format='avfoundation', t=duration)
            .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True)
        )
        print(f"録音が完了しました。{output_file}に保存されました。")
        return output_file

    except ffmpeg.Error as e:
        print(f"エラーが発生しました：{e.stderr.decode()}")
        return ""

    except Exception as e:
        print(f"予期せぬエラー：{e}")
        return ""
