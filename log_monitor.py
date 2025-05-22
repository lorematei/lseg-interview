#####################################################################
# The script is designed to monitor job durations and report any jobs that exceed specified thresholds. 
# The script is structured into several functions: reads and parses the logs.log file, calculates durations and generates messages,
# and writes the report to a file, in the end notifying the user by generationg a report file named job_duration_report.txt.
# It uses the datetime module to handle time calculations and the csv module to read the log file. 
# The script is designed to be run as a standalone program.
########################################################################

import csv
from datetime import datetime, timedelta

# Define thresholds for warnings and errors
WARNING = timedelta(minutes=5)
ERROR = timedelta(minutes=10)

def parse_log_file(file_path):
    """
    Reads the log file and returns a list of job events.
    Each event is a tuple: (timestamp, job description, status, PID)
    """
    events = []
    with open(file_path, 'r') as file:
        for line in csv.reader(file):
            time_str, desc, status, pid = [field.strip() for field in line]# Read and strip each field
            time = datetime.strptime(time_str, '%H:%M:%S')  # Convert string to datetime
            events.append((time, desc, status, pid))  # Store the parsed event
    return events

def calculate_durations(events):
    """
    Matches START and END events, calculates durations, and returns messages.
    Adds a warning if duration > 5 minutes, and an error if > 10 minutes.
    """
    start_times = {}  # Store in a dictionary start times by PID
    report = []       # Store in a list final report messages

    for time, desc, status, pid in events:
        print(f"Processing: {time}, {desc}, {status}, {pid}") # Debug print

        if status == 'START':
            start_times[pid] = (time, desc)  # Save start time and description
        elif status == 'END' and pid in start_times:
            start, desc = start_times.pop(pid)  # Retrieve and remove the start info
            duration = time - start             # Calculate job duration

            # Build the report message
            msg = f"{desc} (PID {pid}) took {duration}"
            if duration > ERROR:
                msg += " — ERROR: >10 min"
            elif duration > WARNING:
                msg += " — WARNING: >5 min"

            report.append(msg)  # Add message to report

    return report

def write_report(messages, output_path):
    """
    Writes the messages to a report file.
    Each message is written on a new line.
    """
    with open(output_path, 'w') as out:
        out.write("\n".join(messages))  # Join messages with newline characters

def main():
    """
    Main function to run the log monitoring process.
    """
    events = parse_log_file('logs.log')               # Step 1: Read and parse the log file
    print(f"Parsed {len(events)} events.")            # Debug print
    messages = calculate_durations(events)            # Step 2: Calculate durations and generate messages
    write_report(messages, 'job_duration_report.txt') # Step 3: Write the report to a file
    print("Report generated: job_duration_report.txt")# Step 4: Notify user

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
