import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import Repository, HfFolder
from git import Repo

def main():
    # Retrieve the token and username from environment variables
    hf_token = os.getenv('HF_TOKEN')
    username = os.getenv('USERNAME')
    repo_name = "tt-oilwells-demo-model"
    repo_id = f"{username}/{repo_name}"

    # Save the token
    HfFolder.save_token(hf_token)

    # Initialize a tokenizer and a model from scratch
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    # Save the model and tokenizer to a directory
    model_dir = repo_name
    tokenizer.save_pretrained(model_dir)
    model.save_pretrained(model_dir)

    # If the directory exists and is a git repository, use it
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    if not os.path.exists(os.path.join(model_dir, '.git')):
        print(f"Initializing a new git repository in {model_dir}")
        repo = Repo.init(model_dir)
    else:
        print(f"Directory {model_dir} is already a git repository")
        repo = Repo(model_dir)

    # Set the remote origin and push
    origin_exists = any(remote.name == 'origin' for remote in repo.remotes)
    if not origin_exists:
        repo.create_remote('origin', f'https://github.com/{username}/{repo_name}.git')

    # Add and commit the model files to the repository
    repo.git.add(A=True)
    repo.index.commit("Initial commit of the model")

    # Push the model to the GitHub repository
    repo.remotes.origin.push(refspec='HEAD:refs/heads/main')

if __name__ == "__main__":
    main()
