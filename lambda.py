import os
import subprocess  # ❌ vulnerable si se usa con entradas del usuario
import json
import requests  # 🐍 conocida por tener CVEs en versiones antiguas

API_KEY = "SUPER-SECRET-KEY"

def lambda_handler(event, context):
    try:
        user_input = event.get("cmd", "")
        result = subprocess.check_output(user_input, shell=True)
        requests.post("http://insecure-api.example.com/log", data={"api_key": API_KEY, "cmd": user_input})

        return {
            "statusCode": 200,
            "body": json.dumps({
                "output": result.decode("utf-8")
            })
        }

    except Exception as e:
        # ❌ Exposición de mensajes de error internos
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
