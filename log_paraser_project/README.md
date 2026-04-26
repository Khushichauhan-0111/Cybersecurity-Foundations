**Log-Based Anomaly Detector**
# Overview
This module acts as the threat intelligence engine within the SOT suite. It performs automated log parsing to detect and mitigate brute-force attacks by identifying suspicious patterns in real-time.

# Key Features
1.Brute-Force Detection: Tracks failed login attempts per IP address and per user account.

2.Rule-Based Alerting: Triggers alerts when activity exceeds a defined security threshold (e.g., > 2 failures).

3.Intelligent Remediation: Provides context-aware security action plans based on the type of attack detected (e.g., SSH brute force vs. Ransomware/SMB activity).

# How it Works
1.Data Ingestion: The engine parses server_traffic.log line-by-line.

2.Threat Mapping: It identifies specific indicators of compromise (IoCs), such as "Unauthorized access" or "Failed login" attempts.

3.Threshold Analysis: It aggregates failed attempts and compares them against security policies to identify potential malicious actors.

# Setup & Execution
1.Ensure the log file server_traffic.log is located in the same directory.

2.Run the analyzer: python log_parser.py

3.Review the Incident Summary Report for detailed breakdown of targeted users and malicious IP addresses.

# Technical Notes
a.Extensibility: The detection logic is modular, allowing for future integration with ML-driven anomaly detection models.

b.Dependencies: Built using native Python libraries to ensure high portability and minimal system overhead.