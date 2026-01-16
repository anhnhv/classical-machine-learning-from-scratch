import re

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

input_file_path = "raw-data/train.tsv"
output_file_path = "datasets/train-{lines}.txt"

raw_data = load_raw_data(input_file_path)
datasets = raw_data_to_datasets(raw_data)
write_datasets(output_file_path, datasets)
