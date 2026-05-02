# IT360_Final_Project


## Team Members
- Winston Ceh
- Johnny Konnagel

# Project Idea
We are going to make a "Honeyfile" system that detects when someone opens up a file setup as a trap.
This would then grab the username or uid of the local user that opened it, and send the report to an administrative account. This account can now run the "deployment.py" file which will generate a structured report of the most recent actions caught by the honeyfile.
The log of the alert will be ran through both a hashing and encryption algorithm to ensure data integrity as well as security of that data.
This project will be automated and report the log in a readable fashion after analysis by our AI API for easy readability with the target platform for this program is Linux.

## Tools Needed
- Kali Linux VM (Attacking machine)
- Ubuntu VM (Defender/Machine to run our program)
- Cryptography libraries from Fernet
- Genai libraries from Google

## Objectives
- Target Platform: Linux
- Artifacts Gathered: User activity
- Implementation Language: Python
- Output Format: Secure Containers/Structured Formats

## Usage of AI
AI will be used in this project by sending the log produced by our system to be read by an API (Gemini3.1). The purpose of AI in this case is to create a structured and written report on the alerts found by the honeyfile is a more readable format as well as the potential nature of the alert. Our goal for AI in this project is to better list and check the actions of users in the system caught by our honeyfile trap.

# Overview
```
/docs
---report.pdf       Where the project report is stored
/src
---deployment.py    Where the audit log is analyzed and the API call is made
---log_hash.py      Audit log hashing and encryption
/README.md
```

## Deployment
Download and unzip the files into your desired location. Some libraries are necessary for our files so we will need to install 2 using pip3:
```
pip3 install cryptography
pip3 install google-genai
```
To start the program, we will be using auditd to log and create our honeyfile rules, requiring the command
```
sudo apt install auditd && sudo systemctl start auditd
```
Afterwards, we will set the trap on a file we created using the rule:
```
sudo auditctl -w /path/to/file -p wa -k honeyfile_trap
```
Afterwards, create and start a venv environment within the download folder using:
```
python3 -m venv .venv
source .venv/bin/activate
```
You can now run either "deployment.py" and "log_hash.py" in your venv environment using:
```
python deployment.py
sudo python log_hash.py
```
NOTE: You will need to run "log_hash.py" in sudo as it encrypts files located within the /var folders
The deployment.py script will then require the AI APIkey provided by Gemini to be able to make the calls needed for the reports.
The script can then be run where logs could be checked.

# Demo Video
https://youtu.be/1P-m7Qih7_s
