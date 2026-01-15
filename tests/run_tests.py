"""
Test Runner - Menjalankan semua test cases
"""

import unittest
import sys
import os

# Add tests directory to path
sys.path.insert(0, os.path.dirname(__file__))

from test_login import TestLogin
from test_register import TestRegister


def run_all_tests():
    """Run all test suites"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(TestRegister))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
