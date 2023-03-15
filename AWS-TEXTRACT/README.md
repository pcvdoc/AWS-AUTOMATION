# Lambda Function for Extracting Text and Table Data from PDFs using AWS Textract

This AWS Lambda function takes a PDF file uploaded to an S3 bucket as input and extracts both the text and table data using AWS Textract. It then searches for specific keys within the extracted text and creates a JSON file containing the key-value pairs. Additionally, the table data is saved in a separate JSON file. The processed PDF file is then moved to a "done" folder and the original file is deleted from the S3 bucket.

## Requirements
- Python 3.6+
- Boto3
- AWS Textract

## Usage
1. Create an S3 bucket for storing the PDF files.
2. Create an S3 trigger that is fired when a new PDF file is uploaded to the bucket.
3. Create an AWS Lambda function and attach the S3 trigger to it.
4. Paste the code from `lambda_function.py` into the code editor of the Lambda function.
5. Modify the `keys` list in the code to match the specific keys you want to search for.
6. Save and test the Lambda function.

## Code Overview
- The function first gets the bucket and file name from the S3 event trigger.
- It then calls AWS Textract to extract the text and table data from the PDF file.
- The extracted data is then processed to create a key-value map and table data map.
- The function searches for the specified keys in the key-value map and creates a JSON file with the key-value pairs.
- The table data is also saved in a separate JSON file.
- The processed PDF file is moved to the "done" folder and the original file is deleted from the S3 bucket.

## Improvements
- Add error handling for when the specified keys cannot be found in the extracted data.
- Allow for searching for keys with different capitalizations or with slight variations in spelling or wording.
- Add support for extracting other types of data, such as images or handwriting.
