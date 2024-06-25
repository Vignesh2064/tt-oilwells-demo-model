import os
import shutil
from git import Repo
from huggingface_hub import Repository

# GitHub repository details
github_username = "Vignesh2064"
github_repo_name = "tt-oilwells-demo-model"
github_repo_url = f"https://github.com/{github_username}/{github_repo_name}.git"

# Hugging Face repository details
hf_username = "Imvignesh"
hf_repo_name = "tt-oilwells-demo-model"

def main():
    # Clone the GitHub repository
    repo_dir = "github_repo"
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)
    Repo.clone_from(github_repo_url, repo_dir)

    # Initialize or use existing Hugging Face repository
    hf_repo = Repository()
    hf_repo.clone_from(f"{hf_username}/{hf_repo_name}")

    # Copy files from GitHub repo to Hugging Face repo
    files_to_copy = os.listdir(repo_dir)
    for file_name in files_to_copy:
        shutil.copy(os.path.join(repo_dir, file_name), hf_repo_name)

    # Add, commit, and push to Hugging Face repo
    hf_repo.git_add("*")
    hf_repo.git_commit("Initial commit from GitHub repo")
    hf_repo.git_push()

if __name__ == "__main__":
    main()
