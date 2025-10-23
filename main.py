import transcript
import Record, write
from transcript import transcribe_audio
if __name__ == '__main__':
    
    filename = Record.recording()
    #filenameは、ファイルの名前を参照する際の変数
    print(filename)
    transcribed_text = transcribe_audio()
    write()
