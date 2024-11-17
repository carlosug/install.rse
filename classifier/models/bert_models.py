from sklearn.metrics import accuracy_score, f1_score, classification_report
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import random
import torch

# Set seeds for reproducibility
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)

# Load data
train = pd.read_csv('classifier/data/train.csv').dropna()
test = pd.read_csv('classifier/data/test.csv')
test = test[list(set(train.columns)-{'search'})].dropna()

# Encode labels
label_encoder = LabelEncoder()
train_labels = label_encoder.fit_transform(train['method_type'])
test_labels = label_encoder.transform(test['method_type'])

# Save label encoder
np.save('label_encoder.npy', label_encoder.classes_)

train['method_type'] = train_labels
test['method_type'] = test_labels

# Define dataset class
class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=128):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        inputs = self.tokenizer(text, truncation=True, padding='max_length', max_length=self.max_len, return_tensors="pt")
        inputs = {key: val.squeeze(0) for key, val in inputs.items()}  # Remove batch dim
        inputs['labels'] = torch.tensor(label, dtype=torch.long)
        return inputs

# Set up device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize models and tokenizers with num_labels
num_labels = len(label_encoder.classes_)
models = {
    "bert": (BertTokenizer.from_pretrained('bert-base-uncased'), BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=num_labels).to(device)),
    "roberta": (RobertaTokenizer.from_pretrained('roberta-base'), RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=num_labels).to(device)),
    "scibert": (AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased'), AutoModelForSequenceClassification.from_pretrained('allenai/scibert_scivocab_uncased', num_labels=num_labels).to(device))
}

# Define parameters
BATCH_SIZE = 16
MAX_LEN = 128
EPOCHS = 3

# Define experiments
experiments = {
    "headers_only": (train['headers'], test['headers']),
    "instruction_only": (train['instruction'], test['instruction']),
    "headers_instruction_combined": (train['headers'] + " " + train['instruction'], test['headers'] + " " + test['instruction'])
}

# Open a file to save the results
with open("results/bert_experiment_results.txt", "w") as f:
    
    # Train and evaluate for each model and experiment
    for exp_name, (train_texts, test_texts) in experiments.items():
        f.write(f"\nExperiment: {exp_name.replace('_', ' ').title()}\n")
        
        for model_name, (tokenizer, model) in models.items():
            f.write(f"\nTraining {model_name} on {exp_name.replace('_', ' ')}...\n")

            # Prepare datasets
            train_dataset = TextDataset(train_texts.tolist(), train_labels.tolist(), tokenizer, max_len=MAX_LEN)
            test_dataset = TextDataset(test_texts.tolist(), test_labels.tolist(), tokenizer, max_len=MAX_LEN)

            train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
            test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE)

            # Define optimizer
            optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

            # Training loop
            model.train()
            for epoch in range(EPOCHS):
                for batch in train_loader:
                    # Move batch to device
                    batch = {key: val.to(device) for key, val in batch.items()}
                    optimizer.zero_grad()
                    outputs = model(**batch)
                    loss = outputs.loss
                    loss.backward()
                    optimizer.step()

            # Evaluation
            model.eval()
            predictions, true_labels = [], []
            with torch.no_grad():
                for batch in test_loader:
                    batch = {key: val.to(device) for key, val in batch.items()}  # Move batch to device
                    outputs = model(**batch)
                    logits = outputs.logits
                    predictions.extend(torch.argmax(logits, dim=1).cpu().numpy())
                    true_labels.extend(batch['labels'].cpu().numpy())

            # Convert numeric labels back to original labels
            predicted_labels = label_encoder.inverse_transform(predictions)
            true_labels_original = label_encoder.inverse_transform(true_labels)

            # Calculate evaluation metrics
            accuracy = accuracy_score(true_labels_original, predicted_labels)
            f1 = f1_score(true_labels_original, predicted_labels, average='weighted')
            report = classification_report(true_labels_original, predicted_labels)
            
            # If f1 > 0.7, save the model and tokenizer
            if f1 > 0.7:
                model.save_pretrained(f"models/{model_name}_{exp_name}_model")
                tokenizer.save_pretrained(f"models/{model_name}_{exp_name}_tokenizer")
            
            # Write results to file
            f.write(f"\nResults for {model_name} on {exp_name.replace('_', ' ')}:\n")
            f.write(f"Accuracy: {accuracy:.4f}, F1-score: {f1:.4f}\n")
            f.write(report + "\n")
