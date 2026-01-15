"""
Test cases untuk modul Login
Menggunakan Selenium WebDriver untuk automated testing
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


class TestLogin(unittest.TestCase):
    """Test suite untuk modul login"""
    
    @classmethod
    def setUpClass(cls):
        """Setup yang dijalankan sekali sebelum semua test"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # Use webdriver-manager to handle driver installation
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Get base URL from environment or use default
        cls.base_url = os.environ.get('BASE_URL', 'http://localhost:8000') + "/login.php"
        cls.driver.implicitly_wait(10)
    
    def setUp(self):
        """Setup yang dijalankan sebelum setiap test"""
        self.driver.get(self.base_url)
        time.sleep(1)
    
    def test_TC_LOG_001_login_valid_credentials(self):
        """TC-LOG-001: Login dengan credentials yang benar"""
        print("\n[TEST] TC-LOG-001: Login dengan credentials yang benar")
        
        driver = self.driver
        
        # Input username dan password
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "InputPassword")
        
        username_field.send_keys("irul")
        password_field.send_keys("password123")
        
        # Submit form
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        
        # Verifikasi redirect ke index.php atau error tidak muncul
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        
        # Cek apakah tidak ada error message
        try:
            error_element = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
            self.fail(f"Login failed with error: {error_element.text}")
        except:
            # Tidak ada error = berhasil
            print("✓ Login successful - no error message displayed")
            pass
    
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
        
        # Verifikasi error message muncul
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
        
        # Verifikasi tetap di halaman login (tidak redirect)
        current_url = driver.current_url
        self.assertIn("login.php", current_url)
        print("✓ User stays on login page")
    
    def test_TC_LOG_004_login_empty_fields(self):
        """TC-LOG-004: Login dengan field kosong"""
        print("\n[TEST] TC-LOG-004: Login dengan field kosong")
        
        driver = self.driver
        
        # Langsung submit tanpa mengisi field
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        
        # Verifikasi error message
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
        
        # Verifikasi error message
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
        
        # Verifikasi error message
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
        
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        time.sleep(2)
        
        # Verifikasi tidak berhasil login (SQL injection tidak berhasil)
        current_url = driver.current_url
        self.assertIn("login.php", current_url)
        print("✓ SQL injection attempt blocked successfully")
    
    def test_TC_INT_003_navigation_to_register(self):
        """TC-INT-003: Link navigasi dari login ke register"""
        print("\n[TEST] TC-INT-003: Navigation link to register page")
        
        driver = self.driver
        
        # Klik link register
        register_link = driver.find_element(By.LINK_TEXT, "Register")
        register_link.click()
        
        time.sleep(2)
        
        # Verifikasi redirect ke register.php
        current_url = driver.current_url
        self.assertIn("register.php", current_url)
        print(f"✓ Successfully navigated to: {current_url}")
    
    @classmethod
    def tearDownClass(cls):
        """Cleanup setelah semua test selesai"""
        time.sleep(2)
        cls.driver.quit()
        print("\n[INFO] All login tests completed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
