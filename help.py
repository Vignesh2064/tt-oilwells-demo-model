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

    # Clone the Hugging Face repository to a different directory
    hf_repo_dir = "hf_repo"
    hf_repo = Repo.clone_from(f"https://huggingface.co/{hf_username}/{hf_repo_name}", hf_repo_dir, env={"HUGGINGFACE_TOKEN": hf_token})

    print("Hugging Face repository cloned successfully.")

if __name__ == "__main__":
    main()
