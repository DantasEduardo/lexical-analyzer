import src.tokeniza_words as tk
import src.get_data as get_data


def main() -> None:
    infos = {}
    texts = get_data.read_data("data.json")
    for key in texts.keys():
        infos[key] = tk.get_felings(set(texts[key]))
    
    return infos

if __name__ == "__main__":
    main()
