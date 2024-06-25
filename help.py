import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import Repository, HfFolder
from git import Repo

def main():
    # Retrieve the tokens and usernames from environment variables
    hf_token = os.getenv('HF_TOKEN')
    github_token = os.getenv('GITHUB_TOKEN')
    hf_username = os.getenv('HF_USERNAME')
    github_username = os.getenv('GITHUB_USERNAME')

    # Save the Hugging Face token
    HfFolder.save_token(hf_token)

    # Initialize a tokenizer and a model from scratch
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    # Save the model and tokenizer to a directory
    model_dir = "my-new-model"
    os.makedirs(model_dir, exist_ok=True)
    tokenizer.save_pretrained(model_dir)
    model.save_pretrained(model_dir)

    # Initialize or use existing git repository
    if not os.path.exists(os.path.join(model_dir, '.git')):
        print(f"Initializing a new git repository in {model_dir}")
        repo = Repo.init(model_dir)
    else:
        print(f"Directory {model_dir} is already a git repository")
        repo = Repo(model_dir)

    # Set remote origin
    if not repo.remotes:
        remote_url = f'https://{github_username}:{github_token}@github.com/{hf_username}/{repo_name}.git'
        repo.create_remote('origin', url=remote_url)
        print(f"Remote 'origin' set to {remote_url}")

    # Add and commit the model files
    repo.git.add(A=True)
    repo.index.commit("Initial commit of the model")

    # Push to the GitHub repository
    repo.remotes.origin.push(refspec='HEAD:main')

if __name__ == "__main__":
    main()
