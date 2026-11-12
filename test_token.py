
import os
from dotenv import load_dotenv
from huggingface_hub import whoami

load_dotenv(override=True)

token = os.getenv("HF_TOKEN")

if not token:
    print("Token not found!")
else:
    print("Token loaded:", True)

    try:
        user = whoami(token=token)
        print("Authenticated Hugging Face account:", user["name"])
    except Exception as error:
        print("Authentication error:", error)
