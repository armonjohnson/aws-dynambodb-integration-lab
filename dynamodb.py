import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

###################################
# Challenge 1: Insert Danish entry
###################################

dynamodb.put_item(
    TableName="LanguagesTable",
    Item={
        "Code": {"S": "da"},
        "Language": {"S": "Danish"}
    }
)

###################################
# Challenge 2: Retrieve the entry for Danish
###################################

response = dynamodb.get_item(
    TableName="LanguagesTable",
    Key={
        "Code": {"S": "da"}
    }
)

print(response['Item'])
print("")  # formatting line
print(response['Item'])
print("")  # formatting line
