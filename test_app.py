import os
import unittest

class TestArenaOpsAssistant(unittest.TestCase):

    def test_codebase_file_security(self):
        """Verify codebase does not contain hardcoded API strings."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.join(current_dir, "app.py")
        with open(app_path, "r") as f:
            content = f.read()
        self.assertNotIn("AIzaSy", content, msg="Security Breach: Raw key structure exposed!")

    def test_environment_variable_loading(self):
        """Verify application logic correctly integrates with system environment variables."""
        api_key = os.getenv("GEMINI_API_KEY")
        self.assertIsNotNone(api_key, msg="Environment Error: GEMINI_API_KEY must be exported in runtime terminal context.")

if __name__ == "__main__":
    unittest.main()
