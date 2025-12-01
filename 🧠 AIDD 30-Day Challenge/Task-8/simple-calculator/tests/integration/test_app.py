import unittest
import subprocess
import os
import time

class TestApp(unittest.TestCase):

    def test_app_starts(self):
        # This is a very basic integration test to check if the app starts.
        # More sophisticated testing would involve a headless browser or Streamlit testing utilities.
        app_path = os.path.join(os.path.dirname(__file__), '..', 'calculator', 'app.py')
        command = ["streamlit", "run", app_path, "--server.headless", "true", "--server.port", "8502"]
        process = None
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(5)  # Give the app some time to start
            # Check if the process is still running, indicating it started successfully
            self.assertIsNone(process.poll(), "Streamlit app should be running")
        except Exception as e:
            self.fail(f"Streamlit app failed to start: {e}")
        finally:
            if process:
                process.terminate()
                process.wait(timeout=5)

if __name__ == '__main__':
    unittest.main()