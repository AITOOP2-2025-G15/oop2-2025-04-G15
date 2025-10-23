from datetime import datetime 
def save_transcript(text: str, output_file: str = "transcripts.txt") -> None:
    if not text.strip():
        print("")
        return
timestamp = datatime.now().strftime("{[%Y/%m/%d %H:%M:%S]}")
with open(output_file, "write", encoding="utf-8") as f:
    f.write(f"{timestamp}\n{text}\n\n")

print(f"文字起こし結果を {output_file} に保存")