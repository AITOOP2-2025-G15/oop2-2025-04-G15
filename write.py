from datetime import datetime

def save_transcript(text: str) -> None:
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"transcript_{timestamp}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

    print(f"文字起こし結果を {output_file} に保存しました。")
