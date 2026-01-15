"""
Extended Test cases untuk modul Register dengan screenshot
Mencakup semua 15 test cases (7 implemented + 8 recommended)
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
import random
import string
import os
from datetime import datetime


class TestRegisterExtended(unittest.TestCase):
    """Extended test suite untuk modul register dengan screenshot"""
    
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
        
        cls.base_url = os.environ.get('BASE_URL', 'http://localhost:8000') + "/register.php"
        cls.driver.implicitly_wait(10)
        
        # Create screenshots directory
        cls.screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'register')
        os.makedirs(cls.screenshot_dir, exist_ok=True)
    
    def setUp(self):
        """Setup yang dijalankan sebelum setiap test"""
        self.driver.get(self.base_url)
        time.sleep(1)
    
    @staticmethod
    def generate_random_string(length=8):
        """Helper untuk generate random string"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    def take_screenshot(self, test_name):
        """Helper untuk mengambil screenshot"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        self.driver.save_screenshot(filepath)
        print(f"📸 Screenshot saved: {filename}")
        return filepath
    
    # ========== IMPLEMENTED TEST CASES ==========
    
    def test_TC_REG_001_register_valid_data(self):
        """TC-REG-001: Register dengan data valid lengkap"""
        print("\n[TEST] TC-REG-001: Register dengan data valid lengkap")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-001-valid-data")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-001-result")
        print("✓ Registration test completed")
    
    def test_TC_REG_002_register_empty_fields(self):
        """TC-REG-002: Register dengan field kosong"""
        print("\n[TEST] TC-REG-002: Register dengan field kosong")
        
        driver = self.driver
        self.take_screenshot("TC-REG-002-empty-fields")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-002-error")
        
        error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
        error_text = error_element.text
        
        print(f"Error message: {error_text}")
        self.assertIn("tidak boleh kosong", error_text)
        print("✓ Error message for empty fields displayed correctly")
    
    def test_TC_REG_003_register_password_mismatch(self):
        """TC-REG-003: Register dengan password tidak sama"""
        print("\n[TEST] TC-REG-003: Register dengan password tidak sama")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Different123!")
        
        self.take_screenshot("TC-REG-003-password-mismatch")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-003-error")
        
        error_text_elements = driver.find_elements(By.CSS_SELECTOR, ".text-danger")
        error_found = False
        
        for element in error_text_elements:
            if "tidak sama" in element.text:
                print(f"Error message: {element.text}")
                error_found = True
                break
        
        self.assertTrue(error_found, "Password mismatch error not found")
        print("✓ Password mismatch error displayed correctly")
    
    def test_TC_REG_004_register_existing_username(self):
        """TC-REG-004: Register dengan username yang sudah terdaftar"""
        print("\n[TEST] TC-REG-004: Register dengan username yang sudah terdaftar")
        
        driver = self.driver
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("New User")
        email_field.send_keys("newuser@test.com")
        username_field.send_keys("irul")  # Existing username
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-004-duplicate-username")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-004-error")
        
        error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
        error_text = error_element.text
        
        print(f"Error message: {error_text}")
        self.assertIn("sudah terdaftar", error_text)
        print("✓ Duplicate username error displayed correctly")
    
    def test_TC_REG_005_register_empty_name(self):
        """TC-REG-005: Register dengan name kosong (bug testing)"""
        print("\n[TEST] TC-REG-005: Register dengan name kosong")
        
        driver = self.driver
        unique_user = f"emptyname_{self.generate_random_string()}"
        
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-005-empty-name")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-005-result")
        print("✓ Empty name test completed (checking validation)")
    
    def test_TC_REG_006_register_invalid_email(self):
        """TC-REG-006: Register dengan email tidak valid"""
        print("\n[TEST] TC-REG-006: Register dengan email tidak valid")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys("invalidemail")  # No @
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-006-invalid-email")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-006-result")
        
        current_url = driver.current_url
        self.assertIn("register.php", current_url)
        print("✓ Invalid email format prevented (HTML5 validation)")
    
    def test_TC_INT_004_navigation_to_login(self):
        """TC-INT-004: Link navigasi dari register ke login"""
        print("\n[TEST] TC-INT-004: Navigation link to login page")
        
        driver = self.driver
        self.take_screenshot("TC-INT-004-register-page")
        
        login_link = driver.find_element(By.LINK_TEXT, "Login")
        login_link.click()
        
        time.sleep(2)
        self.take_screenshot("TC-INT-004-login-page")
        
        current_url = driver.current_url
        self.assertIn("login.php", current_url)
        print(f"✓ Successfully navigated to: {current_url}")
    
    # ========== RECOMMENDED TEST CASES ==========
    
    def test_TC_REG_007_email_duplicate(self):
        """TC-REG-007: Register dengan email yang sudah terdaftar"""
        print("\n[TEST] TC-REG-007: Email duplicate")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys("irul@irul.com")  # Existing email
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-007-duplicate-email")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-007-result")
        print("✓ Email duplicate test completed")
    
    def test_TC_REG_008_weak_password(self):
        """TC-REG-008: Register dengan password lemah"""
        print("\n[TEST] TC-REG-008: Weak password")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("123")  # Weak password
        repassword_field.send_keys("123")
        
        self.take_screenshot("TC-REG-008-weak-password")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-008-result")
        print("✓ Weak password test completed")
    
    def test_TC_REG_009_xss_in_name(self):
        """TC-REG-009: XSS Prevention in Name field"""
        print("\n[TEST] TC-REG-009: XSS in name field")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("John<script>alert(1)</script>")
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-009-xss-input")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-009-result")
        print("✓ XSS prevention test completed")
    
    def test_TC_REG_010_username_with_space(self):
        """TC-REG-010: Username dengan spasi"""
        print("\n[TEST] TC-REG-010: Username with space")
        
        driver = self.driver
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys("testspace@test.com")
        username_field.send_keys("test user")  # Space in username
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-010-username-space")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-010-result")
        print("✓ Username with space test completed")
    
    def test_TC_REG_011_email_case_sensitivity(self):
        """TC-REG-011: Email case sensitivity"""
        print("\n[TEST] TC-REG-011: Email case sensitivity")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys("TEST@TEST.COM")  # Uppercase email
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-011-uppercase-email")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-011-result")
        print("✓ Email case sensitivity test completed")
    
    def test_TC_REG_012_max_length_validation(self):
        """TC-REG-012: Maximum length validation"""
        print("\n[TEST] TC-REG-012: Max length validation")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        long_name = "A" * 300  # Very long name
        name_field.send_keys(long_name)
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-012-long-input")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-012-result")
        print("✓ Max length validation test completed")
    
    def test_TC_REG_013_numeric_username(self):
        """TC-REG-013: Numeric username"""
        print("\n[TEST] TC-REG-013: Numeric username")
        
        driver = self.driver
        numeric_user = str(random.randint(100000, 999999))
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("Test User")
        email_field.send_keys(f"user{numeric_user}@test.com")
        username_field.send_keys(numeric_user)  # Numeric username
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-013-numeric-username")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-013-result")
        print("✓ Numeric username test completed")
    
    def test_TC_REG_014_unicode_characters(self):
        """TC-REG-014: Unicode characters in name"""
        print("\n[TEST] TC-REG-014: Unicode characters")
        
        driver = self.driver
        unique_user = f"testuser_{self.generate_random_string()}"
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "InputEmail")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        repassword_field = driver.find_element(By.ID, "InputRePassword")
        
        name_field.send_keys("测试用户")  # Chinese characters
        email_field.send_keys(f"{unique_user}@test.com")
        username_field.send_keys(unique_user)
        password_field.send_keys("Test123!")
        repassword_field.send_keys("Test123!")
        
        self.take_screenshot("TC-REG-014-unicode-chars")
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        self.take_screenshot("TC-REG-014-result")
        print("✓ Unicode characters test completed")
    
    @classmethod
    def tearDownClass(cls):
        """Cleanup setelah semua test selesai"""
        time.sleep(2)
        cls.driver.quit()
        print("\n[INFO] All register tests completed")
        print(f"[INFO] Screenshots saved in: {cls.screenshot_dir}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
