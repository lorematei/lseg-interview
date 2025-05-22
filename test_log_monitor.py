import unittest
from datetime import datetime, timedelta
from log_monitor import calculate_durations  # Import the function we're testing

# Define a test case class that inherits from unittest.TestCase
class TestLogMonitor(unittest.TestCase):

    def test_warning_threshold(self):
        """
        Test a job that runs for 6 minutes (should trigger a WARNING).
        """
        events = [
            (datetime.strptime("10:00:00", "%H:%M:%S"), "task A", "START", "123"),
            (datetime.strptime("10:06:00", "%H:%M:%S"), "task A", "END", "123")
        ]
        result = calculate_durations(events)
        self.assertTrue("WARNING" in result[0])  # Check that the result contains a warning

    def test_error_threshold(self):
        """
        Test a job that runs for 11 minutes (should trigger an ERROR).
        """
        events = [
            (datetime.strptime("10:00:00", "%H:%M:%S"), "task B", "START", "456"),
            (datetime.strptime("10:11:00", "%H:%M:%S"), "task B", "END", "456")
        ]
        result = calculate_durations(events)
        self.assertTrue("ERROR" in result[0])  # Check that the result contains an error

    def test_no_warning_or_error(self):
        """
        Test a job that runs for 4 minutes (should not trigger anything).
        """
        events = [
            (datetime.strptime("10:00:00", "%H:%M:%S"), "task C", "START", "789"),
            (datetime.strptime("10:04:00", "%H:%M:%S"), "task C", "END", "789")
        ]
        result = calculate_durations(events)
        self.assertFalse("WARNING" in result[0])  # Should not contain a warning
        self.assertFalse("ERROR" in result[0])    # Should not contain an error

# Run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()
