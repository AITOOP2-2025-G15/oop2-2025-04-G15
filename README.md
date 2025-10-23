# oop2-2025-04-G15
## リポジトリの目的
プログラムを起動したら10秒間音声を録音し，録音された内容を文字起こしして，テキストファイルに保存するアプリケーションをグループで作成する。
## 実行するのに必要なモジュール
- mlx_whisper
- pydub
- numpy
- ffmpeg
## 実行手順

## 作成者情報
- リーダー
qwertyuiop
- 作業者1
hypnen-cmd
- 作業者2
1018hiroto
- 作業者3
kouro0328
## 関数の仕様
### record.py<br>
- recording
10秒間音声を録音した後、生成されたファイルのパスを返す。
引数:なし
戻り値:生成されたファイルのパス名(str)
### transcript.py<br>
- transcribe_audio
指定された音声ファイルを文字起こしし、テキストを返す。
引数:file_path(ファイルのパス。str)
戻り値:文字起こしされたテキスト(str)
### write.py<br>
- save_transcript
引数として文字列を受け取り、ファイル名にタイムスタンプを付けてファイルに保存する。
引数:text(書き込むテキスト。str)
戻り値:なし
