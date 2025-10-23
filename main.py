import Record, transcribe, write
if __name__ == '__main__':
    
    filename = Record.recording()
    #filenameは、ファイルの名前を参照する際の変数
    print(filename)
    transcribe()
    write()
