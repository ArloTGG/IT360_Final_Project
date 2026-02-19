# IT360_Final_Project


## Team Members
- Winston Ceh
- Johnny Konnagel

# Project Idea
We are going to make a "Honeyfile" system that detects when someone opens up a file setup as a trap.
This would then grab the IP, or username of the local user that opened it, and send the report to an administrative account. Then we would make the decision of verifying the IP or user if they are a legitamite attacker or if someone accidentally opened the file.
The log of the alert will be ran through both a hashing and encryption algorithm to ensure data integrity as well as security of that data.
This project will be automated and report the log in a readable fashion to a planned GUI for easy readability with the target platform for this program is Linux

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
  
