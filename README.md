
# Log Monitoring Application

This application parses a .csv formatted log file to monitor job and task durations. It identifies job start and end times using PIDs, calculates the duration of each job, and logs warnings or errors if the job exceeds specified time thresholds.

## Features

- Parses a log file with job entries.
- Tracks job durations using START and END timestamps.
- Logs:
  - Warnings for jobs > 5 minutes.
  - Errors for jobs > 10 minutes.
- Outputs a summary report.
- Tests using unittest python module

## Log Format

Each line in the log file should follow this format:
HH:MM:SS, job description, START|END, PID

## Usage

1. Place your `logs.log` file in the same directory as `log-monitor.py`.
2. Run the script in a terminal:

python3 log_monitor.py

You should have the results in `job_duration_report.txt` file.

3. Run `test_log_monitor.py` for testing the application. We have 3 scenarios: WARNING - 123 code (task A), ERROR - 456 (task B) code and the passing scenario, where we don't display anything.