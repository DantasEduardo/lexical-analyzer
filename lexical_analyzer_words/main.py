import src.tokeniza_words as tk
import src.get_data as get_data
import src.send_data as send_data

def main() -> None:
    infos = {}
    texts = get_data.read_data("data.json")
    for key in texts.keys():
        infos[key] = tk.get_felings(set(texts[key]))
    send_data.upload_data(infos)

if __name__ == "__main__":
    main()
 