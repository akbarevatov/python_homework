import os
import requests

# GitHub repository details
owner = "S-H-A-K-H-Z-O-D"
repo = "Python_homework"
folder_path = "lesson-16/data/flights"  # The folder we want to download
save_dir = "flights"  # Local folder to save files

# GitHub API URL to get the file list
api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}"

# Create the local directory
os.makedirs(save_dir, exist_ok=True)

# Fetch the folder contents
response = requests.get(api_url)
if response.status_code != 200:
    print("Failed to fetch folder contents. Possible reasons: rate limit exceeded or incorrect folder path.")
    exit()

# Parse JSON response
files = response.json()

# Download each file
for file in files:
    if file["type"] == "file":  # Only download files, ignore subfolders
        file_name = file["name"]
        file_url = file["download_url"]
        file_path = os.path.join(save_dir, file_name)

        print(f"Downloading {file_name}...")
        file_response = requests.get(file_url)
        
        if file_response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(file_response.content)
            print(f"Saved: {file_path}")
        else:
            print(f"Failed to download: {file_name}")

print("All files downloaded successfully!")
