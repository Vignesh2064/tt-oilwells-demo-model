# import statements
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import Repository, HfFolder
import os


def main():
    # Use secrets
    token = os.getenv('HF_TOKEN')
    username = os.getenv('USERNAME')
    repo_name = 'tt-oilwells-demo-model'
    repo_id = f'{username}/{repo_name}'

    # Save the token using HfFolder
    HfFolder.save_token(token)

    # Initialize a tokenizer and a model from scratch
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

    # Save the model and tokenizer to a directory
    tokenizer.save_pretrained(repo_name)
    model.save_pretrained(repo_name)


if __name__ == "__main__":
    main()
