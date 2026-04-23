# IT360_Final_Project


## Team Members
- Winston Ceh
- Johnny Konnagel

# Project Idea
We are going to make a "Honeyfile" system that detects when someone opens up a file setup as a trap.
This would then grab the username or uid of the local user that opened it, and send the report to an administrative account. Then we would make the decision of verifying the user if they are a legitamite attacker or if someone accidentally opened the file.
The log of the alert will be ran through both a hashing and encryption algorithm to ensure data integrity as well as security of that data.
This project will be automated and report the log in a readable fashion after analysis by our AI API for easy readability with the target platform for this program is Linux.

## Tools Needed
- Kali Linux VM (Attacking machine)
- Ubuntu VM (Defender/Machine to run our program)
- OpenSSL for encryption
- Apache 2 Web Server

## Objectives
- Target Platform: Linux
- Artifacts Gathered: User activity/Network data
- Implementation Language: Python
- Output Format: Secure Containers/Structured Formats

## Usage of AI
AI will be used in this project by sending the log produced by our system to be read by one of the provided API's (likely Llama3.1). The purpose of AI in this case is to create a structured and written report on the alerts found by the honeyfile is a more readable format as well as the potential nature of the alert. Our goal for AI in this project is to better differentiate someone accidentally opening or accessing the honeyfile from someone who has malicious intent trying to do so.

## Deployment
To start the program, we will be using auditd to log and create our honeyfile rules, requiring the command
```
sudo apt install auditd && sudo systemctl start auditd
```
Afterwards, we will set the trap on a file we created using the rule:
```
sudo auditctl -w /path/to/file -p wa -k honeyfile_trap
```
The "-p wa" ruleset watches for permission and attribute changes to the file while "-k" adds a key to find logs easier.
The deployment.py script will then require the AI APIkey provided by Llama to be able to make the calls needed for the reports.
The script can then be run where logs could be checked.

