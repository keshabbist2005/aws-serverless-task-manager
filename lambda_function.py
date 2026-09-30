import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TaskManager")


def lambda_handler(event, context):
    print("Task Manager API called")
    print("HTTP Method:", event.get("httpMethod"))

    method = event.get("httpMethod", "GET")

    # CREATE TASK
    if method == "POST":
        body = json.loads(event.get("body", "{}"))
        task_id = str(uuid.uuid4())

        item = {
            "task_id": task_id,
            "title": body.get("title", ""),
            "description": body.get("description", ""),
            "completed": False
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "body": json.dumps(item)
        }

    # LIST TASKS
    elif method == "GET":
        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response.get("Items", []))
        }

    # DELETE TASK
    elif method == "DELETE":
        body = json.loads(event.get("body", "{}"))
        task_id = body.get("task_id")

        table.delete_item(
            Key={"task_id": task_id}
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task deleted successfully"
            })
        }

    # UPDATE TASK
    elif method == "PUT":
        body = json.loads(event.get("body", "{}"))
        task_id = body.get("task_id")

        table.update_item(
            Key={"task_id": task_id},
            UpdateExpression="SET title = :title, description = :description, completed = :completed",
            ExpressionAttributeValues={
                ":title": body.get("title", ""),
                ":description": body.get("description", ""),
                ":completed": body.get("completed", False)
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task updated successfully"
            })
        }

    else:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Unsupported HTTP method"
            })
        }
