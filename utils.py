import re
import json
import os

def load_raw_data(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def raw_data_to_datasets(raw_data):
    texts = []
    for line in raw_data:
        if line.strip():
            text = line.lower()
            # Remove unwanted characters
            text = ''.join(c for c in text if c.isalnum() or c.isspace())
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()
            texts.append(text)

    return texts

def write_datasets(file_path, datasets):
    file_name = file_path.format(lines=len(datasets))
    with open(file_name, 'w') as file:
        for line in datasets:
            file.write(line + '\n')

def save_trained_model(model, model_path):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, 'w') as file:
        json.dump(model, file)

def load_trained_model(model_path):
    with open(model_path, 'r') as file:
        return json.load(file)