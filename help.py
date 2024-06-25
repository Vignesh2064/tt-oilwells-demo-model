from transformers import AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import Repository, HfFolder
import os

def main():
    # Retrieve the token and username from environment variables
    hf_token = os.getenv('HF_TOKEN')
    username = os.getenv('USERNAME')
    repo_name = "my-new-model"
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

    # Create a new repository or clone an existing one
    repo = Repository(local_dir=model_dir, clone_from=repo_id, use_auth_token=hf_token)

    # Add and commit the model files to the repository
    repo.git_add(auto_lfs_track=True)
    repo.git_commit("Initial commit of the model")

    # Push the model to the Hugging Face Hub
    repo.git_push()

if __name__ == "__main__":
    main()
