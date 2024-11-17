from sklearn.metrics import accuracy_score, f1_score, classification_report
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm
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

# Initialize RoBERTa model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
num_labels = len(label_encoder.classes_)
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=num_labels).to(device)

# Hyperparameter tuning options
learning_rates = [1e-5, 2e-5, 3e-5]
batch_sizes = [8, 16]
max_lengths = [128, 256]
epochs_options = [3, 5]

# Open a file to save the tuning results
with open("roberta_hyperparameter_tuning_results.txt", "w") as f:
    for lr in tqdm(learning_rates):
        for batch_size in batch_sizes:
            for max_len in max_lengths:
                for epochs in epochs_options:
                    f.write(f"\nExperiment: LR={lr}, Batch Size={batch_size}, Max Length={max_len}, Epochs={epochs}\n")
                    
                    # Update dataset with new max length
                    train_dataset = TextDataset(train['headers'].tolist(), train_labels.tolist(), tokenizer, max_len=max_len)
                    test_dataset = TextDataset(test['headers'].tolist(), test_labels.tolist(), tokenizer, max_len=max_len)

                    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
                    test_loader = DataLoader(test_dataset, batch_size=batch_size)

                    # Define optimizer
                    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

                    # Training loop
                    model.train()
                    for epoch in range(epochs):
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
                        model.save_pretrained(f"models/roberta_LR{lr}_BS{batch_size}_ML{max_len}_EP{epochs}")
                        tokenizer.save_pretrained(f"models/roberta_LR{lr}_BS{batch_size}_ML{max_len}_EP{epochs}")
                    
                    # Write results to file
                    f.write(f"\nResults: LR={lr}, Batch Size={batch_size}, Max Length={max_len}, Epochs={epochs}\n")
                    f.write(f"Accuracy: {accuracy:.4f}, F1-score: {f1:.4f}\n")
                    f.write(report + "\n")
