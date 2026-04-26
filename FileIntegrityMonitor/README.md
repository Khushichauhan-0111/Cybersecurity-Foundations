**Forensic Monitoring System (FMS)**
# Overview
The Forensic Monitoring System (FMS) is an automated integrity checking engine designed to protect sensitive data records. By establishing a secure cryptographic baseline for critical assets, the system provides real-time alerts if unauthorized modifications occur, ensuring the integrity and auditability of sensitive information.

# Core Capabilities
Baseline Cryptographic Verification: Generates secure SHA-256 hashes for all files in the target directory to create a "known-good" state.

Forensic-Grade Detection: Continuously monitors directory contents for unauthorized changes.

Evidence Chain Protection: Specifically designed to detect modifications in high-stakes documents (e.g., healthcare records, inventory, and legal evidence), alerting administrators when the chain-of-custody is compromised.

Actionable Alerts: Provides granular risk reports, highlighting expected vs. actual states to simplify forensic investigations.

# How it Works
Baseline Creation: Upon first execution, the system scans the target directory and generates a secure cryptographic baseline for each file.

Integrity Scanning: During subsequent runs, the system recalculates the hashes of all files in the directory and compares them against the baseline.

Modification Alerting: If a file hash deviates from the baseline, the system logs a high-priority alert and identifies the specific risk to the evidence chain.

# Usage
Configure: Ensure the target directory path is correctly set in monitor.py.

Launch: Execute the monitor script: python monitor.py

Audit: Review the console output for integrity status or unauthorized modification alerts.

# Technical Scope
Integrity Enforcement: This tool demonstrates a foundational defense mechanism against unauthorized data tampering—a critical requirement for digital trust and regulatory compliance in legal and medical fields.

Extensibility: The system is designed to be integrated into broader automated security suites, providing forensic-level visibility into system changes.