import os

# Define the folder structure
folders = [
    "code/config",
    "code/src",
    "code/script",
    "screenshots",
    "outputs",
    "logs"
]

# Define the files to be created
files = {
    "code/config/config.yaml": """dataset_url: "https://huggingface.co/datasets/sh0416/ag_news"
output_dir: "outputs/"
selected_words: ["president", "the", "Asia"]
""",
    "code/src/process_data.py": "",
    "code/src/process_data_all.py": "",
    "code/src/run.py": "",
    "code/script/run.sh": """#!/bin/bash
echo "Activating Conda Environment"
source activate uza

echo "Running Data Processing"
python code/src/process_data.py

echo "Done!"
""",
    "code/Dockerfile.Dockerfile": "",
    "code/github_build_action.yml": ""
}

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created directory: {folder}")

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Created file: {file_path}")

print("Project structure created successfully.")
