import os # Allows me to access my .env file
import requests # Allows me to make requests to the API
from dotenv import load_dotenv  # Allows me to safley store my token from my .env file
import re # Allows me to use regular expressions

load_dotenv() # Loads the .env file
API_TOKEN = os.getenv("HUGGING_FACE_TOKEN")

# Set the Hugging Face Model Hub API endpoint
url = 'https://huggingface.co/api/models/gpt2'

# Set up authorization token
headers = {
    'Authorization' : f'Bearer {API_TOKEN}'
}

# Make the API request to get model information
response = requests.get(url, headers=headers)

# Checking if request was successful 
if response.status_code == 200:
    print('Success!')
    data = response.json()
    print(data)
        
    # Initialize a dictionary to store extracted items
    extracted_data = {}
    
    # Turn JSON into a string
    data_str = str(data)
    
    # Extracting the model name
    model_name = data.get("modelId", "N/A")
    # Adding the model name to the dictionary
    extracted_data["model_name"] = model_name
    
    # Extracting the model task
    pipeline_tag = data.get("pipeline_tag", "N/A")
    extracted_data['pipeline_tag'] = pipeline_tag    
    
    # Extracting the model tags
    tags = data.get("tags", [])
    extracted_data["tags"] = tags
    
    # Extracting download count
    download_count = data.get("downloads", "N/A")
    extracted_data['download_count'] = download_count
    
    pipeline_tag = data.get("pipeline_tag", "N/A")
    extracted_data['pipeline_tag'] = pipeline_tag    
    
    # Save data to text file
    with open('extracted_data.txt', 'w') as file:
        file.write("Model Information\n")
        file.write("="*20 + "\n")
        
        # For loop to write the extracted data to the file
        for key, value in extracted_data.items():
            file.write(f"{key}: {value}\n")
else:
    print("ERROR: ", response.status_code, response.text)

