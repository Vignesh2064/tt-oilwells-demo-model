import os
import shutil
from git import Repo
from huggingface_hub import Repository, HfFolder

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

    # Initialize Hugging Face Repository
    HfFolder.save_token(hf_token)
    repo = Repository(local_dir=repo_dir, clone_from=f"{hf_username}/{hf_repo_name}", use_auth_token=True)

    # Add all files and commit
    repo.git_add(auto_lfs_track=True)
    repo.git_commit("Add files from GitHub repository")

    # Push changes to Hugging Face Hub
    repo.git_push()

    print("Files pushed successfully to Hugging Face repository.")

if __name__ == "__main__":
    main()
