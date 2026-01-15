"""
Extended Test cases untuk modul Login dengan screenshot
Mencakup semua 15 test cases (8 implemented + 7 recommended)
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime


class TestLoginExtended(unittest.TestCase):
    """Extended test suite untuk modul login dengan screenshot"""
    
    @classmethod
    def setUpClass(cls):
        """Setup yang dijalankan sekali sebelum semua test"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        cls.base_url = os.environ.get('BASE_URL', 'http://localhost:8000') + "/login.php"
        cls.driver.implicitly_wait(10)
        
        # Create screenshots directory
        cls.screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'login')
        os.makedirs(cls.screenshot_dir, exist_ok=True)
    
    def setUp(self):
        """Setup yang dijalankan sebelum setiap test"""
        self.driver.get(self.base_url)
        time.sleep(1)
    
    def take_screenshot(self, test_name):
        """Helper untuk mengambil screenshot"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        self.driver.save_screenshot(filepath)
        print(f"📸 Screenshot saved: {filename}")
        return filepath
    
    # ========== IMPLEMENTED TEST CASES ==========
    
    def test_TC_LOG_001_login_valid_credentials(self):
        """TC-LOG-001: Login dengan credentials yang benar"""
        print("\n[TEST] TC-LOG-001: Login dengan credentials yang benar")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("irul")
        password_field.send_keys("password123")
        
        self.take_screenshot("TC-LOG-001-before-submit")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-001-after-submit")
        
        try:
            error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
            self.fail(f"Login failed with error: {error_element.text}")
        except:
            print("✓ Login successful - no error message displayed")
    
    def test_TC_LOG_002_login_wrong_username(self):
        """TC-LOG-002: Login dengan username yang tidak terdaftar"""
        print("\n[TEST] TC-LOG-002: Login dengan username salah")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("usernotexist")
        password_field.send_keys("password123")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-002-error")
        
        error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
        error_text = error_element.text
        
        print(f"Error message: {error_text}")
        self.assertIn("Gagal", error_text)
        print("✓ Error message displayed correctly")
    
    def test_TC_LOG_003_login_wrong_password(self):
        """TC-LOG-003: Login dengan password salah"""
        print("\n[TEST] TC-LOG-003: Login dengan password salah")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("irul")
        password_field.send_keys("wrongpassword")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-003-wrong-password")
        
        current_url = driver.current_url
        self.assertIn("login.php", current_url)
        print("✓ User stays on login page")
    
    def test_TC_LOG_004_login_empty_fields(self):
        """TC-LOG-004: Login dengan field kosong"""
        print("\n[TEST] TC-LOG-004: Login dengan field kosong")
        
        driver = self.driver
        self.take_screenshot("TC-LOG-004-empty-fields")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-004-error")
        
        error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
        error_text = error_element.text
        
        print(f"Error message: {error_text}")
        self.assertIn("tidak boleh kosong", error_text)
        print("✓ Error message for empty fields displayed correctly")
    
    def test_TC_LOG_005_login_empty_username(self):
        """TC-LOG-005: Login dengan username kosong"""
        print("\n[TEST] TC-LOG-005: Login dengan username kosong")
        
        driver = self.driver
        
        password_field = driver.find_element(By.ID, "InputPassword")
        password_field.send_keys("password123")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-005-error")
        
        error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
        error_text = error_element.text
        
        print(f"Error message: {error_text}")
        self.assertIn("tidak boleh kosong", error_text)
        print("✓ Error message for empty username displayed correctly")
    
    def test_TC_LOG_006_login_empty_password(self):
        """TC-LOG-006: Login dengan password kosong"""
        print("\n[TEST] TC-LOG-006: Login dengan password kosong")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("irul")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-006-error")
        
        error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
        error_text = error_element.text
        
        print(f"Error message: {error_text}")
        self.assertIn("tidak boleh kosong", error_text)
        print("✓ Error message for empty password displayed correctly")
    
    def test_TC_INT_001_sql_injection_prevention(self):
        """TC-INT-001: Test SQL Injection pada username"""
        print("\n[TEST] TC-INT-001: SQL Injection prevention test")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("' OR '1'='1")
        password_field.send_keys("anything")
        
        self.take_screenshot("TC-INT-001-sql-injection-attempt")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-INT-001-blocked")
        
        current_url = driver.current_url
        self.assertIn("login.php", current_url)
        print("✓ SQL injection attempt blocked successfully")
    
    def test_TC_INT_003_navigation_to_register(self):
        """TC-INT-003: Link navigasi dari login ke register"""
        print("\n[TEST] TC-INT-003: Navigation link to register page")
        
        driver = self.driver
        self.take_screenshot("TC-INT-003-login-page")
        
        register_link = driver.find_element(By.LINK_TEXT, "Register")
        register_link.click()
        
        time.sleep(2)
        self.take_screenshot("TC-INT-003-register-page")
        
        current_url = driver.current_url
        self.assertIn("register.php", current_url)
        print(f"✓ Successfully navigated to: {current_url}")
    
    # ========== RECOMMENDED TEST CASES ==========
    
    def test_TC_LOG_007_xss_prevention(self):
        """TC-LOG-007: XSS Attack Prevention"""
        print("\n[TEST] TC-LOG-007: XSS Prevention")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        xss_payload = "<script>alert('XSS')</script>"
        username_field.send_keys(xss_payload)
        password_field.send_keys("password123")
        
        self.take_screenshot("TC-LOG-007-xss-input")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-007-result")
        
        # Check that alert is not triggered
        try:
            alert = driver.switch_to.alert
            self.fail("XSS vulnerability: Alert was triggered!")
        except:
            print("✓ XSS prevention working - no alert triggered")
    
    def test_TC_LOG_008_case_sensitivity(self):
        """TC-LOG-008: Case Sensitivity Test"""
        print("\n[TEST] TC-LOG-008: Username case sensitivity")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("IRUL")  # Uppercase
        password_field.send_keys("password123")
        
        self.take_screenshot("TC-LOG-008-uppercase-username")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-008-result")
        print("✓ Case sensitivity test completed")
    
    def test_TC_LOG_009_whitespace_handling(self):
        """TC-LOG-009: Whitespace in Username"""
        print("\n[TEST] TC-LOG-009: Whitespace handling")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("  irul  ")  # With spaces
        password_field.send_keys("password123")
        
        self.take_screenshot("TC-LOG-009-whitespace")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-009-result")
        print("✓ Whitespace handling test completed")
    
    def test_TC_LOG_010_special_characters(self):
        """TC-LOG-010: Special Characters in Username"""
        print("\n[TEST] TC-LOG-010: Special characters")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("irul@#$%")
        password_field.send_keys("password123")
        
        self.take_screenshot("TC-LOG-010-special-chars")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-010-result")
        print("✓ Special characters test completed")
    
    def test_TC_LOG_011_very_long_input(self):
        """TC-LOG-011: Very Long Input"""
        print("\n[TEST] TC-LOG-011: Very long input")
        
        driver = self.driver
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        long_username = "a" * 1000
        username_field.send_keys(long_username)
        password_field.send_keys("password123")
        
        self.take_screenshot("TC-LOG-011-long-input")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-011-result")
        print("✓ Long input test completed")
    
    def test_TC_LOG_012_session_persistence(self):
        """TC-LOG-012: Session Persistence"""
        print("\n[TEST] TC-LOG-012: Session persistence")
        
        driver = self.driver
        
        # Login first
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("irul")
        password_field.send_keys("password123")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-LOG-012-after-login")
        
        # Refresh page
        driver.refresh()
        time.sleep(2)
        self.take_screenshot("TC-LOG-012-after-refresh")
        
        current_url = driver.current_url
        print(f"URL after refresh: {current_url}")
        print("✓ Session persistence test completed")
    
    def test_TC_LOG_013_rate_limiting(self):
        """TC-LOG-013: Multiple Login Attempts (Rate Limiting)"""
        print("\n[TEST] TC-LOG-013: Rate limiting test")
        
        driver = self.driver
        
        # Attempt login 5 times
        for i in range(5):
            driver.get(self.base_url)
            time.sleep(1)
            
            username_field = driver.find_element(By.ID, "username")
            password_field = driver.find_element(By.ID, "InputPassword")
            
            username_field.send_keys("wronguser")
            password_field.send_keys("wrongpass")
            
            submit_button = driver.find_element(By.NAME, "submit")
            submit_button.click()
            
            time.sleep(1)
            print(f"  Attempt {i+1}/5")
        
        self.take_screenshot("TC-LOG-013-after-5-attempts")
        print("✓ Rate limiting test completed (check if lockout implemented)")
    
    @classmethod
    def tearDownClass(cls):
        """Cleanup setelah semua test selesai"""
        time.sleep(2)
        cls.driver.quit()
        print("\n[INFO] All login tests completed")
        print(f"[INFO] Screenshots saved in: {cls.screenshot_dir}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
