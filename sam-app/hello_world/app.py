import json
import os

TEST_VAR_1 = os.getenv(
    "TEST_VAR_1", default="if you see this, something went wrong")
TEST_VAR_2 = os.getenv(
    "TEST_VAR_2", default="if you see this, somethign went wrong")
TEST_VAR_3 = os.getenv(
    "TEST_VAR_3", default='Hello world 3 (os.getenv default)')

# import requests
# import pandas


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hi there",
            # "location": ip.text.replace("\n", "")
            "TEST_VAR_1": TEST_VAR_1,
            "TEST_VAR_2": TEST_VAR_2,
            "TEST_VAR_3": TEST_VAR_3,
        }),
    }
