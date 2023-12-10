import json
from langchain.llms import Bedrock
from langchain.prompts import PromptTemplate

def lambda_handler(event, context):
    print(json.dumps(event))
    
    prompt = '''
    Human: {country}の首都は？
    Assistant:
    '''
    
    country = event["queryStringParameters"]["country"]
    
    llm = Bedrock(
        region_name="us-east-1",
        model_id="anthropic.claude-v2:1"
    )
    
    answer = llm(prompt.format(country=country))
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json;charset=UTF-8",
        },
        "body": json.dumps({
            "answer": answer
        },ensure_ascii=False)
    }