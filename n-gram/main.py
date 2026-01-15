from train import train_model

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
    left_side_score = bigram_prob(prev_word, word)
    right_side_score = bigram_prob(word, next_word)

    # print(f"Left score '({prev_word}|{word})={left_side_score}")
    # print(f"Right score '({word}|{next_word})={right_side_score}'")

    # if left_side_score == 0:
    #     return right_side_score

    # if right_side_score == 0:
    #     return left_side_score
    
    final_score = left_side_score + right_side_score

    return final_score

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

    return {
        "best_match": best_word,
        "score": best_score
    }

def print_output(sentence, prediction):
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    result = sentence.replace("_", f"{UNDERLINE}{prediction['best_match']}{RESET}")
    print(f"{result}, Score: {prediction['score']}")

def test():
    for case in TEST_CASES:
        sentence = case[0]
        prediction = predict_blank(sentence)
        print_output(sentence, prediction)

test()