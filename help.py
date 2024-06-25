import os
import shutil
from git import Repo
from huggingface_hub import HfApi

# GitHub repository details
github_username = "Vignesh2064"
github_repo_name = "tt-oilwells-demo-model"
github_repo_url = f"https://github.com/{github_username}/{github_repo_name}.git"

# Hugging Face repository details
hf_username = "Imvignesh"
hf_repo_name = "tt-oilwells-demo-model"
hf_token = os.getenv('HF_TOKEN')  # Ensure HF_TOKEN is set in your environment secrets

def main():
    # Clone the GitHub repository locally
    repo_dir = "github_repo"
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)
    Repo.clone_from(github_repo_url, repo_dir)

    # Initialize the Hugging Face API
    api = HfApi()

    # Create or use existing Hugging Face repository
    repo_id = f"{hf_username}/{hf_repo_name}"
    hf_repo = api.create_repo(repo_id, token=hf_token)

    # Upload files from GitHub repo to Hugging Face repo
    files_to_upload = os.listdir(repo_dir)
    for file_name in files_to_upload:
        file_path = os.path.join(repo_dir, file_name)
        api.upload_file(repo_id, file_path, token=hf_token)

    print("Files uploaded successfully to Hugging Face repository.")

if __name__ == "__main__":
    main()
