from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import pandas as pd

# Load data
train = pd.read_csv('classifier/data/train.csv').dropna()
test = pd.read_csv('classifier/data/test.csv')
test = test[list(set(train.columns)-{'search'})].dropna()

# Encode labels
label_encoder = LabelEncoder()
train_labels = label_encoder.fit_transform(train['method_type'])
test_labels = label_encoder.transform(test['method_type'])

# Define experiments
experiments = {
    "headers_only": (train['headers'], test['headers']),
    "instruction_only": (train['instruction'], test['instruction']),
    "headers_instruction_combined": (train['headers'] + " " + train['instruction'], test['headers'] + " " + test['instruction'])
}

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
}

# Open a file to save the results
with open("results/trad_models_results.txt", "w") as f:
    
    # Run each experiment
    for exp_name, (train_texts, test_texts) in experiments.items():
        f.write(f"\nExperiment: {exp_name.replace('_', ' ').title()}\n")
        
        # Vectorize text
        vectorizer = TfidfVectorizer(max_features=5000)
        X_train = vectorizer.fit_transform(train_texts)
        X_test = vectorizer.transform(test_texts)
        
        # Store results
        results = {}
        
        # Train models and evaluate
        for model_name, model in models.items():
            # Train the model
            model.fit(X_train, train_labels)
            
            # Make predictions
            y_pred = model.predict(X_test)
            
            # Evaluate
            accuracy = accuracy_score(test_labels, y_pred)
            f1 = f1_score(test_labels, y_pred, average='weighted')
            report = classification_report(test_labels, y_pred, target_names=label_encoder.classes_)
            
            # Store results
            results[model_name] = {
                "Accuracy": accuracy,
                "F1": f1,
                "Report": report
            }
        
        # Write results to file
        for model_name, result in results.items():
            f.write(f"\n--- {model_name} on {exp_name.replace('_', ' ')} ---\n")
            f.write(f"Accuracy: {result['Accuracy']:.4f}, F1-score: {result['F1']:.4f}\n")
            f.write(result['Report'] + "\n")
