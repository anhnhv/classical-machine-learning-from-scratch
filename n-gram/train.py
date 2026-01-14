from collections import defaultdict

def load_datasets(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip().lower() for line in file if line.strip()]

def train_model(data):
    counts = defaultdict(lambda: defaultdict(int))

    for line in data:
        words = line.split(" ")
        for i in range(len(words) - 1):
            prev_word = words[i]
            next_word = words[i + 1]
            counts[prev_word][next_word] += 1

    print(f"{counts}")
    # normalize
    bigram_prob = {}
    for prev_word, next_words in counts.items():
        total = sum(next_words.values())
        bigram_prob[prev_word] = {
            w: c / total for w, c in next_words.items()
        }

    print(f"{bigram_prob}")
    return bigram_prob

# data = load_datasets("datasets/example.txt")
# bigram_prob = train_model(data)