import os
import json
from huggingface_hub import InferenceClient


def lambda_handler(event, context):
    # Get the user's message
    body = json.loads(event.get("body", "{}"))
    message = body.get("message", "")

    if not message:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Message is required"})
        }

    # Get Hugging Face token
    hf_token = os.environ.get("HF_TOKEN")

    # Create Hugging Face client
    client = InferenceClient(
        provider="auto",
        api_key=hf_token
    )

    # Send query to AI model
    response = client.chat_completion(
        model="openai/gpt-oss-120b:fastest",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        max_tokens=800
    )

    # Get AI response
    reply = response.choices[0].message.content
    if not reply:
        reply = "Sorry, I couldn't generate a response for that question. Please try asking in a different way."

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "reply": reply
        })
    }