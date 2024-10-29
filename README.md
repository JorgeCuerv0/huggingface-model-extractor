# Hugging Face Model Information Extractor

This project is a simple Python program that connects to the [Hugging Face Model Hub API](https://huggingface.co/docs/api-inference/index) to fetch and store information about specific models. It uses an API token to authenticate with Hugging Face's servers and extracts metadata about a model, such as the model name, task type, tags, and download count. The extracted data is then saved to a text file for easy access and analysis.

## Features

- **API Authentication**: Uses an environment variable for secure API authentication.
- **Data Extraction**: Retrieves key metadata fields about the `gpt2` model
- **File Output**: Saves extracted data into a structured text file for reference.

## Getting Started

### Prerequisites

- Python 3.6 or above
- [Requests library](https://docs.python-requests.org/en/master/): `pip install requests`
- [Python-dotenv](https://pypi.org/project/python-dotenv/): `pip install python-dotenv`

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JorgeCuerv0/huggingface-model-extractor
    cd your-repo
    ```

2. **Set up environment variables**:
    - Create a `.env` file in the project root directory.
    - Add your Hugging Face API token to `.env`:
      ```plaintext
      HUGGING_FACE_TOKEN=your_token_here
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the program to retrieve metadata about the `gpt2` model from Hugging Face:

```bash
python hf_api_example.py
