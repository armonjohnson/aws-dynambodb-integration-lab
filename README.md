🗄️ AWS DynamoDB Integration Lab — Python (Boto3)
B — Background

This project is a hands-on AWS lab where I integrated Amazon DynamoDB using Python (Boto3) inside an EC2-based development environment.

The goal was to learn how to insert items into a DynamoDB table, retrieve items using a primary key, work with key/value pairs, and verify results using both the AWS Console and AWS CLI.

U — Understanding
Architecture

Python script → Boto3 Client → DynamoDB Table

EC2 instance used as development environment

AWS Services Used

Amazon DynamoDB

AWS EC2

AWS CLI

Boto3 SDK

🛠️ Build Steps (How I Completed the Lab)
1️⃣ Initialize Boto3 Client
import boto3
dynamo = boto3.client('dynamodb')

2️⃣ Insert a New Item (Danish) Into the Table
dynamo.put_item(
    TableName="LanguagesTable",
    Item={
        "Language": {"S": "Danish"},
        "Code": {"S": "da"}
    }
)

3️⃣ Retrieve the Newly Inserted Item
response = dynamo.get_item(
    TableName="LanguagesTable",
    Key={"Code": {"S": "da"}}
)

print(response['Item'])

🧪 Final Output

Expected & Received:

{'Language': {'S': 'Danish'}, 'Code': {'S': 'da'}}

⭐ What I Learned

How DynamoDB stores key/value data

Writing Python scripts using the Boto3 SDK

Inserting & retrieving items programmatically

Working with AWS Console + AWS CLI

📸 Screenshots
<img width="1920" height="1200" alt="Screenshot 2025-12-01 213103" src="https://github.com/user-attachments/assets/bab1b69f-a128-4421-b32c-d9d30512f687" />
<img width="1920" height="1200" alt="Screenshot 2025-12-01 213413" src="https://github.com/user-attachments/assets/ecc1ff36-b73e-4a84-b62b-ec911852bd5b" />
<img width="1920" height="1200" alt="Screenshot 2025-12-01 214047" src="https://github.com/user-attachments/assets/017312ca-f92c-4dd9-9881-9c13570962d9" /> 
<img width="1920" height="1200" alt="Screenshot 2025-12-01 214304" src="https://github.com/user-attachments/assets/3520f1aa-4c1d-4296-9fcf-453c57a7050b" /> 
<img width="1920" height="1200" alt="Screenshot 2025-12-01 215600" src="https://github.com/user-attachments/assets/b7bcce40-0ecf-48c8-9eb6-888ee8acbfe2" /> 
<img width="1920" height="1200" alt="Screenshot 2025-12-01 220333" src="https://github.com/user-attachments/assets/073ed604-ea12-4da7-8abd-a4212201714d" /> 
<img width="1920" height="1200" alt="Screenshot 2025-12-01 220425" src="https://github.com/user-attachments/assets/d4477cb3-1324-4ef8-9ac3-cc0b0a61122e" /> 
 <img width="1920" height="1200" alt="Screenshot 2025-12-01 220522" src="https://github.com/user-attachments/assets/2def7469-3f21-4ddf-8b3f-855d8fbae650" />
