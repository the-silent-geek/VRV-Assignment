Log Analysis Script
This repository contains a Python script for analyzing web server log files. The script extracts key insights from the logs and saves the results in an Excel file (log_analysis_results.xlsx). This tool is useful for identifying high-traffic IPs, popular endpoints, and potential brute-force login attempts.

Features
Requests per IP:
Counts the number of requests made by each IP address and sorts them in descending order of request count.

Most Accessed Endpoint:
Identifies the endpoint (e.g., /home, /login) accessed the highest number of times.

Suspicious Activity Detection:
Detects potential brute-force login attempts by flagging IP addresses with failed login attempts exceeding a configurable threshold.

Results Saved to Excel:
Outputs the results into an Excel file (log_analysis_results.xlsx) with the following sheets:

Requests per IP
Endpoints Accessed
Suspicious Activity
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/log-analysis-script.git
cd log-analysis-script
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the script using Python (version 3.8 or higher is recommended):

bash
Copy code
python log_analysis.py /path/to/logfile.log --threshold 10
Arguments:
log_file_path (required): Path to the web server log file.
--threshold (optional): Threshold for failed login attempts to flag as suspicious activity (default: 10).
