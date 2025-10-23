from datetime import datetime 
def save_transcript(text: str) -> None:
    output_file = "transcripts.txt"
    if not text.strip():
        print("")
        return
    timestamp = datetime.now().strftime("{[%Y/%m/%d %H:%M:%S]}")
    f = open(output_file, "a")
    f.write(f"{timestamp}\n{text}\n\n")

    print(f"文字起こし結果を {output_file} に保存")