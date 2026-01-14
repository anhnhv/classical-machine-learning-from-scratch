from main import train_model

BIGRAM_PROB = train_model("datasets/example.txt")

TEST_CASES = [
    ["this _ a dog"],
    ["_ is a dog"],
    ["this is _ big cat"],
    ["this is a big _"],
]

def bigram_prob(prev_word, next_word):
    return BIGRAM_PROB.get(prev_word, {}).get(next_word, 0)


def score(word, prev_word, next_word):
    if bigram_prob(prev_word, word) == 0:
        return bigram_prob(word, next_word)

    if bigram_prob(word, next_word) == 0:
        return bigram_prob(prev_word, word)

    return bigram_prob(prev_word, word) * bigram_prob(word, next_word)


def predict_blank(sentence):
    words = sentence.split()
    blank_index = words.index("_")
    prev_word = words[blank_index - 1] if blank_index > 0 else None
    next_word = words[blank_index + 1] if blank_index < len(words) - 1 else None

    candidates = BIGRAM_PROB.keys()
    best_word = None
    best_score = -1

    for candidate in candidates:
        current_score = score(candidate, prev_word, next_word)
        if current_score > best_score:
            best_score = current_score
            best_word = candidate

    return best_word


def test():
    for case in TEST_CASES:
        sentence = case[0]
        prediction = predict_blank(sentence)
        print(f"Sentence: '{sentence}' => Predicted word: '{prediction}'")

test()