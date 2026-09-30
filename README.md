# AWS Serverless Task Manager API

A beginner-friendly serverless Task Manager REST API built using AWS Lambda, API Gateway, and DynamoDB.

## Architecture

Postman → API Gateway → AWS Lambda → DynamoDB

## AWS Services Used

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## Features

- Create a task
- Get all tasks
- Update a task
- Delete a task
- CloudWatch logging

## API Endpoints

Base URL:

`https://qe6ujn41z3.execute-api.us-east-1.amazonaws.com/prod`

Resource:

`/tasks`

Supported methods:

- `POST /tasks` — Create a task
- `GET /tasks` — Get all tasks
- `PUT /tasks` — Update a task
- `DELETE /tasks` — Delete a task

## Database

DynamoDB table:

`TaskManager`

Partition key:

`task_id`

## Testing

The API was tested using Postman for all CRUD operations.

## Project Status

Completed ✅
