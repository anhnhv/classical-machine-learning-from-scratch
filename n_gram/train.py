from collections import defaultdict

def load_datasets(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip().lower() for line in file if line.strip()]

def train_model(path):
    data = load_datasets(path)
    counts = defaultdict(lambda: defaultdict(int))

    for line in data:
        words = line.split(" ")

        for i in range(len(words) - 1):
            prev_word = words[i]
            next_word = words[i + 1]
            counts[prev_word][next_word] += 1
            counts[next_word]  # ensure next_word is in counts, if not the last word will be missing

    # normalize
    bigram_prob = {}
    for prev_word, next_words in counts.items():
        total = sum(next_words.values())
        bigram_prob[prev_word] = {
            w: c / total for w, c in next_words.items()
        }

    print("Training completed.")
    print(f"Total unique words: {len(counts)}")

    return bigram_prob