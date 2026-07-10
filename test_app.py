import os
import unittest

class TestArenaOpsAssistant(unittest.TestCase):

    def test_codebase_file_security(self):
        """
        Verify that the physical source file itself does not contain 
        hardcoded credentials, satisfying automated security scanners.
        """
        # We read the absolute path of the main app file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.join(current_dir, "app.py")
        
        with open(app_path, "r") as f:
            content = f.read()
            
        # Ensure that no raw API key strings are mistakenly written into the logic parameters
        self.assertNotIn("AIzaSy", content, 
                         msg="Security Breach: Raw Google API key structure detected in code file text!")

if __name__ == "__main__":
    unittest.main()
