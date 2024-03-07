from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import json
import os
from dotenv import load_dotenv
from PIL import Image
import time
import shutil  # Import for creating and managing directories

'''
Authenticate
Authenticates your credentials and creates a client.
'''

load_dotenv()

subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
OCR: Read Images from JSON List in Input Directory and Store Results in Output Directory
This example reads image URLs from a JSON list in the "inputs" directory, extracts text, and saves the results in the "outputs" directory.
'''

# Define input and output directory paths
input_dir = "./inputs"
output_dir = "./outputs"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)  # Create 'outputs' directory only if it doesn't exist

# Load the JSON file containing image URLs
with open(os.path.join(input_dir, "image_urls.json"), "r") as f:
    image_urls = json.load(f)
    print(image_urls)

print("Processing images...")

for image_url in image_urls:
    # Get image URL
    url = image_url["link"]

    # Call API with URL
    read_response = computervision_client.read(url=url, raw=True)
    print(read_response)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text if successful
    if read_result.status == OperationStatusCodes.succeeded:
        output_text = ""
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                output_text += line.text + "\n"

        # Create the output file path and print the results
        output_file_path = os.path.join(output_dir, os.path.splitext(url.split("/")[-1])[0] + ".txt")
        with open(output_file_path, "w") as f:
            f.write(output_text)
        print(f"Text extracted from {url} and saved to {output_file_path}")

print("Finished processing images.")
