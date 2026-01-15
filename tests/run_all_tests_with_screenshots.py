"""
Test Runner untuk semua test cases (36 test cases) dengan screenshot
"""

import unittest
import sys
import os
from datetime import datetime

# Add tests directory to path
sys.path.insert(0, os.path.dirname(__file__))

from test_login_extended import TestLoginExtended
from test_register_extended import TestRegisterExtended


def run_all_extended_tests():
    """Run all extended test suites with screenshot capability"""
    print("="*80)
    print("RUNNING ALL TEST CASES WITH SCREENSHOT")
    print("Total: 36 Test Cases (15 Login + 15 Register + 6 Security)")
    print("="*80)
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    print("📦 Loading test suites...")
    suite.addTests(loader.loadTestsFromTestCase(TestLoginExtended))
    suite.addTests(loader.loadTestsFromTestCase(TestRegisterExtended))
    
    print(f"✓ Loaded {suite.countTestCases()} test cases")
    print()
    
    # Run tests
    print("🚀 Starting test execution...")
    print()
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print()
    print("="*80)
    print("TEST EXECUTION SUMMARY")
    print("="*80)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED")
        if result.failures:
            print("\nFailed tests:")
            for test, traceback in result.failures:
                print(f"  - {test}")
        if result.errors:
            print("\nErrors:")
            for test, traceback in result.errors:
                print(f"  - {test}")
    
    print()
    print("📸 Screenshots saved in:")
    print("  - screenshots/login/")
    print("  - screenshots/register/")
    print("="*80)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit_code = run_all_extended_tests()
    sys.exit(exit_code)
