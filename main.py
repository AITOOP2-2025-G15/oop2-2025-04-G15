import transcript
import Record
from transcript import transcribe_audio
from write import save_transcript

if __name__ == '__main__': 
    filename = Record.recording()
    #filenameは、ファイルの名前を参照する際の変数
    print(filename)
    
    #transcribed_textは、文字起こしされた文字用の変数
    transcribed_text = transcribe_audio(filename)

    save_transcript(transcribed_text)
