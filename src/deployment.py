import subprocess
import requests
import json
from google import genai
from google.genai import types
import pathlib

def get_latest_logs():
    # Pulls the last event from audit logs specifically for our 'honeyfile_trap'   
    raw_log = subprocess.check_output("ausearch -k honeyfile_trap --start recent -i | tail -n 200", shell=True)
    return raw_log
   
def honeypot_analysis():
    client = genai.Client(api_key = "AIzaSyAmUEAlRBaDZkFxD6SwdKh6mpYt6TSvAY0")
    log_data = get_latest_logs()
    response = client.models.generate_content (
        model = "gemini-3.1-flash-lite-preview",
        contents = [
                    types.Part.from_bytes(
                    data = log_data,
                    mime_type = "text/plain",
                    ),
                    "The provided logs is from a honeypot system on linux. Analyze the provided audit log and list the activity recorded tied to the users in a structured format."]
)
    print(response.text)
if __name__ == "__main__":
    honeypot_analysis()
