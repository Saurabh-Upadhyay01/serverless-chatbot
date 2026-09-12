# Serverless Chatbot Backend

## Assignment no. 7

Implement a serverless function that handles chatbot queries and integrates with an AI API.

## Description

This project implements a simple chatbot backend using AWS Lambda and the Hugging Face Inference API.

The AWS Lambda function receives a chatbot query, sends it to an AI model through the Hugging Face API, and returns the generated response.

## Architecture

User
↓
AWS Lambda
↓
Hugging Face Inference API
↓
AI Model
↓
Response

## Technologies Used

- AWS Lambda
- Python
- Hugging Face Inference API
- Hugging Face Hub Python Library

## Input

The Lambda function accepts a JSON request containing a message.

Example:

{
  "body": "{\"message\":\"What is serverless computing?\"}"
}

## Output

The function returns a JSON response containing the original message and the AI-generated reply.

Example:

{
  "statusCode": 200,
  "body": "{\"message\":\"What is serverless computing?\",\"reply\":\"...\"}"
}

## Environment Variable

The Hugging Face API token is stored securely in AWS Lambda as an environment variable:

HF_TOKEN

The token is not included in the source code or GitHub repository.

## Testing

The Lambda function was tested using the AWS Lambda Test feature and successfully returned an AI-generated response.

## Student

Student ID: 24UG00227
Assignment: 7 - Chatbot Backend