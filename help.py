import os
from git import Repo
from huggingface_hub import Repository

# Define your GitHub and Hugging Face repository details
github_repo_url = "https://github.com/Vignesh2064/tt-oilwells-demo-model.git"
hf_username = "Imvignesh"
hf_repo_name = "tt-oilwells-demo-model"
hf_token = os.getenv('HF_TOKEN')  # Ensure HF_TOKEN is set in your environment secrets

def main():
    # Clone the GitHub repository locally
    repo_dir = "tt-oilwells-demo-model"
    Repo.clone_from(github_repo_url, repo_dir)
    os.chdir(repo_dir)

    # Initialize the Hugging Face repository
    hf_repo = Repository(local_dir=".", clone_from=f"https://huggingface.co/{hf_username}/{hf_repo_name}", use_auth_token=True)

    # Add all files, commit, and push to Hugging Face
    hf_repo.git_add()
    hf_repo.git_commit(message="Initial commit from GitHub repository")
    hf_repo.git_push()

    print("Files pushed successfully to Hugging Face repository.")

if __name__ == "__main__":
    main()
