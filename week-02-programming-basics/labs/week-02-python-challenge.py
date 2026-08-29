# ==============================================================================
# DevOps Roadmap 2026 - Week 2 Python Automation Challenge
# File: week-02-python-challenge.py
#
# Scenario: Your production web server (Nginx) is spitting out access logs, and 
#           some applications are crashing. Your lead engineer wants you to automate 
#           the extraction of critical error events, calculate response distributions, 
#           and output an interactive summary report.
#
# Your Task: Complete the Python starter code below by implementing the missing 
#            logic. Use basic Python concepts (if/else, loops, and data structures).
# ==============================================================================

import os
import re
from collections import Counter, defaultdict

# ------------------------------------------------------------------------------
# MOCK LOG DATA FOR PRACTICE (In real-life, you would read from a live .log file)
# ------------------------------------------------------------------------------
MOCK_LOGS = [
    '192.168.1.50 - - [29/Aug/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 4522',
    '192.168.1.51 - - [29/Aug/2026:10:00:05 +0000] "POST /api/login HTTP/1.1" 401 120',
    '192.168.1.52 - - [29/Aug/2026:10:01:10 +0000] "GET /dashboard HTTP/1.1" 200 12040',
    '192.168.1.50 - - [29/Aug/2026:10:01:15 +0000] "GET /api/v1/users HTTP/1.1" 500 95',
    '192.168.1.53 - - [29/Aug/2026:10:02:00 +0000] "GET /favicon.ico HTTP/1.1" 404 0',
    '192.168.1.51 - - [29/Aug/2026:10:02:12 +0000] "POST /api/v1/payment HTTP/1.1" 500 230',
    '192.168.1.50 - - [29/Aug/2026:10:02:45 +0000] "GET /index.html HTTP/1.1" 200 4522',
    '192.168.1.54 - - [29/Aug/2026:10:03:01 +0000] "GET /api/v1/metrics HTTP/1.1" 200 8920',
    '192.168.1.52 - - [29/Aug/2026:10:03:10 +0000] "GET /dashboard HTTP/1.1" 304 0',
    '192.168.1.55 - - [29/Aug/2026:10:03:59 +0000] "POST /api/login HTTP/1.1" 200 120',
    '192.168.1.50 - - [29/Aug/2026:10:04:12 +0000] "GET /api/v1/users HTTP/1.1" 500 95',
]

def parse_log_line(line):
    """
    Helper function to parse a standard Nginx log line.
    Returns a dictionary containing: ip, method, endpoint, status_code, and bytes_sent.
    """
    # Regex matching group pattern
    pattern = r'(?P<ip>\S+) - - \[.*?\] "(?P<method>\S+) (?P<endpoint>\S+) \S+" (?P<status>\d+) (?P<bytes>\d+)'
    match = re.match(pattern, line)
    if match:
        return {
            'ip': match.group('ip'),
            'method': match.group('method'),
            'endpoint': match.group('endpoint'),
            'status_code': int(match.group('status')),
            'bytes_sent': int(match.group('bytes'))
        }
    return None

# ==============================================================================
# MISSION 1: PARSE ALL LOGS AND EXTRACT BASIC STATISTICS
# ==============================================================================
def analyze_logs(log_lines):
    """
    TODO: Iterate through the given list of log_lines, parse each one, and:
    1. Count total requests.
    2. Group requests by their status code (e.g. {200: 5, 500: 3, 404: 1...})
    3. Aggregate total bandwidth (sum of all bytes_sent).
    4. Find the most active IP address.
    
    Return a dictionary with these keys: 
    'total_requests', 'status_codes', 'total_bandwidth_bytes', 'most_active_ip'
    """
    stats = {
        'total_requests': 0,
        'status_codes': defaultdict(int),
        'total_bandwidth_bytes': 0,
        'most_active_ip': None
    }
    ip_counter = Counter()
    # --- WRITE YOUR CODE HERE ---
    # Hint: Use a loop to iterate through log_lines. Parse them with parse_log_line(line).
    # Use collections.Counter or a dictionary to find the most active IP.
    
    # PASS is a placeholder; delete it when writing your implementation
    for line in log_lines:

        entry = parse_log_line(line)

        if entry:
            stats['total_requests'] += 1
            stats['status_codes'][entry['status_code']] += 1
            stats['total_bandwidth_bytes'] += entry['bytes_sent']
            ip_counter[entry['ip']] += 1

    if ip_counter:
        stats['most_active_ip'] = ip_counter.most_common(1)[0][0]
    
    # ----------------------------
    return stats

# ==============================================================================
# MISSION 2: EXTRACT ERRORS (STATUS > 400) AND WRITE TO A REPORT
# ==============================================================================
def generate_error_report(log_lines, output_filepath="error_report.txt"):
    """
    TODO: Find all log lines that represent an error (HTTP status code > 400).
    Write those raw log lines to a file designated by output_filepath.
    
    Return the total number of errors captured.
    """
    error_count = 0
    
    # --- WRITE YOUR CODE HERE ---
    # Hint: Open the file in write mode ('w'). 
    # Iterate through log_lines, parse them, check the status code, and write if >= 400.
    
    with open(output_filepath, 'w') as report:
        for line in log_lines:
            entry = parse_log_line(line)

            if entry and entry['status_code'] > 400:
                report.write(line + '\n')
                error_count += 1
    
    # ----------------------------
    return error_count

# ==============================================================================
# DIAGNOSTIC TEST RUNNER (Do not modify this part)
# ==============================================================================
if __name__ == "__main__":
    print("🚀 Running Week 2 DevOps Automation Diagnostic Tests...\n")
    
    # -- TEST 1: LOG ANALYZER --
    print("[+] Test 1: Testing analyze_logs()...")
    results = analyze_logs(MOCK_LOGS)
    
    if not results or results.get('total_requests') == 0:
        print("❌ Test 1 Failed: analyze_logs() returned empty or incomplete stats.")
    else:
        print(f"   - Total Requests Parsed: {results['total_requests']} (Expected: 11)")
        print(f"   - Total Bandwidth: {results['total_bandwidth_bytes']} bytes (Expected: 30664)")
        print(f"   - Status Codes Breakdown: {dict(results['status_codes'])}")
        print(f"   - Most Active IP: '{results['most_active_ip']}' (Expected: '192.168.1.50')")
        
        if (results['total_requests'] == 11 and 
            results['total_bandwidth_bytes'] == 30664 and 
            results['status_codes'].get(500) == 3 and 
            results['most_active_ip'] == '192.168.1.50'):
            print("✅ Test 1 Passed! Your parsing and data modeling are fully correct.")
        else:
            print("❌ Test 1 Failed: Calculated statistics do not match expected outcomes.")
            
    print("-" * 50)
    
    # -- TEST 2: ERROR REPORT --
    print("[+] Test 2: Testing generate_error_report()...")
    report_file = "test_error_report.txt"
    if os.path.exists(report_file):
        os.remove(report_file)
        
    errors_found = generate_error_report(MOCK_LOGS, report_file)
    
    if errors_found == 0 or not os.path.exists(report_file):
        print("❌ Test 2 Failed: No error file written or returned count is 0.")
    else:
        with open(report_file, 'r') as f:
            lines_written = f.readlines()
            
        print(f"   - Reported Error Count: {errors_found} (Expected: 5)")
        print(f"   - Lines Written to File: {len(lines_written)} (Expected: 5)")
        
        if errors_found == 5 and len(lines_written) == 5:
            print("✅ Test 2 Passed! Your file I/O operations are working as intended.")
        else:
            print("❌ Test 2 Failed: File contents or error counts are incorrect.")
            
    if os.path.exists(report_file):
        os.remove(report_file)
        
    print("\n🎯 Diagnostic run complete. Fill in the 'pass' blocks to clear all tests!")
