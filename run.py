from n_gram.main import test_model
from n_gram.train import train_model
from utils import save_trained_model, load_trained_model

# model = train_model("datasets/train-989944.txt")
# save_trained_model(model, "models/bigram/model.json")

test_model("models/bigram/model.json")