# Log Analysis Script

This repository contains a Python script for analyzing web server log files. The script extracts key insights from the logs and saves the results in an Excel file (`log_analysis_results.xlsx`). This tool is useful for identifying high-traffic IPs, popular endpoints, and potential brute-force login attempts.

---

## **Features**

1. **Requests per IP**:  
   Counts the number of requests made by each IP address and sorts them in descending order of request count.

2. **Most Accessed Endpoint**:  
   Identifies the endpoint (e.g., `/home`, `/login`) accessed the highest number of times.

3. **Suspicious Activity Detection**:  
   Detects potential brute-force login attempts by flagging IP addresses with failed login attempts exceeding a configurable threshold.

4. **Results Saved to Excel**:  
   Outputs the results into an Excel file (`log_analysis_results.xlsx`) with the following sheets:
   - `Requests per IP`
   - `Endpoints Accessed`
   - `Suspicious Activity`

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/log-analysis-script.git
   cd log-analysis-script
