import pandas as pd
import argparse
import re

def count(log_file):
    # read the log file into a pandas DataFrame
     
    log_data = pd.read_csv(log_file, sep=" ", header=None, usecols=[0], names=["IP Address"])
    
    # count requests per IP address
    ip_address_count = log_data["IP Address"].value_counts().reset_index()
    ip_address_count.columns = ["IP Address", "Request Count"]
    
    return ip_address_count

def frequent_endpoints(log_file_path):
    
    with open(log_file_path, "r") as file:
        log_lines = file.readlines()
    
    endpoint_pattern = r'"[A-Z]+(.*?) HTTP/.*?"'
    endpoints = [re.search(endpoint_pattern, line).group(1) for line in log_lines if re.search(endpoint_pattern, line)]
    
    endpoint_counts = pd.Series(endpoints).value_counts().reset_index()
    endpoint_counts.columns = ["Endpoint", "Access Count"]
    
    frequent = endpoint_counts.loc[0]
    return pd.DataFrame(endpoint_counts,columns = ["Endpoint", "Access Count"]).head(1)

def brute_force_attempts(log_file_path, threshold=10):
    
    with open(log_file_path, "r") as file:
        log_lines = file.readlines()

    failure_pattern = r'HTTP/1\.\d" 401|Invalid credentials'
    failed_attempts = []

    for line in log_lines:
        if re.search(failure_pattern, line):
            ip_address = line.split()[0]  #
            failed_attempts.append(ip_address)

    failed_attempts_counts = pd.Series(failed_attempts).value_counts()

    # Filter IPs 
    suspicious_ips = failed_attempts_counts[failed_attempts_counts > threshold]
    return suspicious_ips.reset_index(name="Failed Login Attempts").rename(columns={"index": "IP Address"})

    
if __name__ == "__main__":
    
    log_file_path = input("Enter your file path : ")
    
    try:
        results = count(log_file_path)
        most_frequent = frequent_endpoints(log_file_path)
        brute_force = brute_force_attempts(log_file_path)
        
        with pd.ExcelWriter("log_analysis_results.xlsx", engine="xlsxwriter") as writer:
            results.to_excel(writer, sheet_name="Requests per IP", index=False)
            most_frequent.to_excel(writer, sheet_name="Endpoints Accessed", index=False)
            brute_force.to_excel(writer, sheet_name="Suspicious Activity", index=False)
        
        print("Analysis completed. Results saved to 'log_analysis_results.xlsx'.")

        
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: Log file '{log_file_path}' is empty or improperly formatted.")
    