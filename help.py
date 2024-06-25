import os
from git import Repo

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

    # Add the Hugging Face repository as a remote
    hf_remote_url = f"https://huggingface.co/{hf_username}/{hf_repo_name}"
    repo = Repo(".")
    repo.create_remote("hf_origin", hf_remote_url)

    # Push the GitHub repository files to Hugging Face
    repo.git.add(".")
    repo.index.commit("Initial commit from GitHub repository")
    repo.git.push("--set-upstream", "hf_origin", "HEAD:main")

    print("Files pushed successfully to Hugging Face repository.")

if __name__ == "__main__":
    main()
