import subprocess
import requests
import json

def get_latest_logs():
    # Pulls the last event from audit logs specifically for our 'honeyfile_trap'
    raw_log = subprocess.check_output("ausearch -k honeyfile_trap --start recent -i | tail -n 20", shell=True)
    return raw_log.decode('utf-8')

def analyze_with_llama(log_data):
    url = "https://api.llama-provider.com/v1/completions" # Replace with your actual endpoint
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    
    prompt = f"Analyze these Linux audit logs. Differentiate between an accidental file open and malicious activity. Logs: {log_data}"
    
    # This is where your $110/month budget goes
    response = requests.post(url, headers=headers, json={"prompt": prompt, "model": "llama-3-70b"})
    return response.json()
