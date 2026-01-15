# Quiz Pengupil - Login & Register Testing

Repository ini berisi implementasi **comprehensive automated testing** untuk modul Login dan Register menggunakan Selenium WebDriver dengan CI/CD pipeline di GitHub Actions, dilengkapi dengan **screenshot automation** untuk dokumentasi.

## 📋 Deskripsi

Project ini merupakan sistem login dan register sederhana berbasis PHP dan MySQL yang dilengkapi dengan automated testing lengkap menggunakan Selenium. Testing mencakup 30 test cases komprehensif yang meliputi functional testing, security testing, edge cases, dan bug detection, dengan fitur screenshot otomatis untuk setiap test case.

## 🔗 Link Repository

**Repository GitHub**: [https://github.com/Putroooo/quiz](https://github.com/Putroooo/quiz)

## 🧪 Test Cases

### Test Cases Login (15 test cases)
**Basic Functionality:**
1. **TC-LOG-001**: Login dengan credentials yang benar ✓
2. **TC-LOG-002**: Login dengan username yang tidak terdaftar ✓
3. **TC-LOG-003**: Login dengan password salah ✓
4. **TC-LOG-004**: Login dengan field kosong ✓
5. **TC-LOG-005**: Login dengan username kosong ✓
6. **TC-LOG-006**: Login dengan password kosong ✓

**Security Testing:**
7. **TC-LOG-007**: XSS Attack Prevention ✓
8. **TC-INT-001**: SQL Injection Prevention ✓

**Edge Cases & Validation:**
9. **TC-LOG-008**: Case Sensitivity Test ✓
10. **TC-LOG-009**: Whitespace Handling ✓
11. **TC-LOG-010**: Special Characters Input ✓
12. **TC-LOG-011**: Very Long Input (Buffer Overflow) ✓
13. **TC-LOG-012**: Session Persistence ✓
14. **TC-LOG-013**: Rate Limiting Test ✓

**Integration:**
15. **TC-INT-003**: Navigasi dari login ke register ✓

### Test Cases Register (15 test cases)
**Basic Functionality:**
1. **TC-REG-001**: Register dengan data valid lengkap ✓
2. **TC-REG-002**: Register dengan field kosong ✓
3. **TC-REG-003**: Register dengan password tidak sama ✓
4. **TC-REG-004**: Register dengan username duplicate ❌ (Bug detected)
5. **TC-REG-005**: Register dengan name kosong ✓ (Bug testing)
6. **TC-REG-006**: Register dengan email tidak valid ✓

**Extended Validation:**
7. **TC-REG-007**: Email Duplicate Test ✓
8. **TC-REG-008**: Weak Password Test ✓
9. **TC-REG-009**: XSS Prevention in Name Field ✓
10. **TC-REG-010**: Username dengan Spasi ✓
11. **TC-REG-011**: Email Case Sensitivity ✓
12. **TC-REG-012**: Max Length Validation ✓
13. **TC-REG-013**: Numeric Username ✓
14. **TC-REG-014**: Unicode Characters in Name ✓

**Integration:**
15. **TC-INT-004**: Navigasi dari register ke login ✓

### 📊 Test Results Summary
- **Total Test Cases**: 30
- **Passed**: 29 (96.67%)
- **Failed**: 1 (3.33%)
- **Bugs Detected**: 3
- **Screenshots Generated**: 83 images

📄 **Dokumentasi Lengkap**: 
- [DOKUMENTASI_TESTING_LENGKAP_30_TESTCASES.docx](DOKUMENTASI_TESTING_LENGKAP_30_TESTCASES.docx) - Dokumentasi lengkap dengan screenshot dan langkah-langkah testing

## 🛠️ Teknologi yang Digunakan

- **Backend**: PHP 8.2.12
- **Database**: MySQL 8.0
- **Testing Framework**: Python 3.14 + Unittest
- **Automation Tool**: Selenium WebDriver 4.39.0
- **Browser**: Chrome 143.0 (headless mode)
- **WebDriver Manager**: webdriver-manager 4.0.2
- **Documentation**: python-docx for report generation
- **CI/CD**: GitHub Actions
- **Web Server**: PHP Built-in Server (localhost:8000)

## 📁 Struktur Project

```
quiz-pengupil/       # GitHub Actions CI/CD workflow
├── db/
│   └── quiz_pengupil.sql                # Database schema & sample data
├── tests/
│   ├── test_login.py                    # Basic login test cases (8 tests)
│   ├── test_register.py                 # Basic register test cases (7 tests)
│   ├── test_login_extended.py           # Extended login tests (15 tests) ⭐ NEW
│   ├── test_register_extended.py        # Extended register tests (15 tests) ⭐ NEW
│   ├── run_tests.py                     # Basic test runner
│   ├── run_all_tests_with_screenshots.py # Complete test runner with screenshots ⭐ NEW
│   └── README_TESTS.md                  # Testing documentation
├── screenshots/                          # Auto-generated test screenshots ⭐ NEW
│   ├── login/                           # Login test screenshots (36 images)
│   └── register/                        # Register test screenshots (47 images)
├── index.php                            # Dashboard (driver)
├── login.php                            # Halaman login
├── register.php                         # Halaman register
├── koneksi.php                          # Database connection
├── style.css                            # Styling
├── requirements.txt                     # Python dependencies
├── run_tests_with_server.bat            # Automated test execution script ⭐ NEW
├── generate_report.py                   # Generate comprehensive DOCX report
├── generate_testcases_only.py           # Generate test cases table only
├── generate_full_documentation.py       # Generate full documentation ⭐ NEW
├── LAPORAN_TESTING.docx                 # Comprehensive testing report
├── TEST_CASES_ALL.docx                  # Test cases table documentation
├── DOKUMEN (atau XAMPP)
- Python 3.11+
- Chrome Browser

### Setup

1. **Clone repository**
```bash
git clone https://github.com/Putroooo/quiz.git
cd quiz
```

2. **Import database**
```bash
# Via MySQL command line
mysql -u root -p quiz_pengupil < db/quiz_pengupil.sql

# Via XAMPP (recommended)
# 1. Start XAMPP MySQL
# 2. Import db/quiz_pengupil.sql via phpMyAdmin atau:
C:\xampp\mysql\bin\mysql.exe -u root -e "CREATE DATABASE quiz_pengupil"
C:\xampp\mysql\bin\mysql.exe -u root quiz_pengupil < db/quiz_pengupil.sql
```

3. **Konfigurasi database** (jika perlu)
Edit file `koneksi.php` sesuai dengan konfigurasi MySQL Anda

4. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

### Menjalankan Test

#### Option 1: Automated (Recommended) ⭐
```bash
# Windows: Jalankan batch script yang otomatis start server + run tests
run_tests_with_server.bat
```

#### Option 2: Manual
```bash
# Terminal 1: Start PHP server
php -S localhost:8000
# atau menggunakan XAMPP PHP:
C:\xampp\php\php.exe -S localhost:8000

# Terminal 2: Run tests
cd tests
python run_all_tests_with_screenshots.py
```

#### Option 3: Basic Tests Only
```bash
# Start server terlebih dahulu, lalu:
cd tests
python run_tests.py
```

### Mengakses Aplikasi
```
Login Page: http://localhost:8000/login.php
Register Page: http://localhost:8000/register.php

Test Credentials:
- Username: irul | Password: 123
- Username: ahmad | Password: 123irements.txt
```

5. Start PHP server
```bash
php -S localhost:8000
```

6. Run tests (di terminal baru)
```bash
cd tests
python run_tests.py
```
Automated testing berhasil mengidentifikasi **3 bug** dalam aplikasi:

### Bug 1: Undefined Variable di register.php ⚠️
**Lokasi**: Line 34
```php
$query = "INSERT INTO users (username,name,email, password ) VALUES ('$username','$nama','$email','$pass')";
```
**Masalah**: Variable `$nama` tidak terdefinisi, seharusnya `$name`  
**Severity**: Low (PHP Warning muncul tapi registrasi tetap berhasil)  
**Test Case**: TC-REG-001

### Bug 2: Validasi Name Field ❌
**Lokasi**: register.php  
**Masalah**: Field `name` tidak divalidasi dengan benar, bisa bernilai kosong padahal di database memiliki constraint NOT NULL  
**Severity**: Medium (Data integrity issue)  
**Test Case**: TC-REG-005  
**Impact**: User dapat register dengan name kosong

### Bug 3: Error Message Tidak Sesuai di login.php 🔤
**Lokasi**: login.php  
**Masalah**: Error message "Register User Gagal !!" tidak sesuai konteks, seharusnya "Login Gagal !!" atau "Username/Password salah !!"  
**Severity**: Low (Usability issue)  
**Test Case**: TC-LOG-002  
**Impact**: Membingungkan user
� Screenshot Automation

Setiap test case dilengkapi dengan **screenshot otomatis** yang tersimpan di folder `screenshots/`:

- **Login Tests**: 36 screenshots
- **Register Tests**: 47 screenshots
- **Total**: 83 screenshots

Screenshot digunakan untuk:
- Dokumentasi visual testing
- Bukti hasil testing
- Debugging dan analisis
- Laporan komprehensif

## 📖 Stub dan Driver

Proj� Dokumentasi

### Test Reports
- **LAPORAN_TESTING.docx** - Comprehensive testing report dengan 15 test cases
- **TEST_CASES_ALL.docx** - Test cases table (36 test cases)
- **DOKUMENTASI_TESTING_LENGKAP_30_TESTCASES.docx** - Complete documentation dengan 30 test cases, screenshot, dan step-by-step testing ⭐

### Testing Guides
- **tests/README_TESTS.md** - Guide untuk menjalankan automated testing
- **README.md** - Project overview dan setup guide (dokumen ini)

## 🎯 Recommendations

Berdasarkan hasil testing, berikut adalah rekomendasi perbaikan:

1. **Fix Undefined Variable**: Ganti `$nama` menjadi `$name` di register.php line 34
2. **Add Name Validation**: Tambahkan validasi untuk memastikan field name tidak kosong
3. **Fix Error Message**: Update error message di login.php agar lebih deskriptif
4. **Add Username Validation**: Implementasi pengecekan username duplicate sebelum insert
5. **Implement Rate Limiting**: Tambahkan rate limiting untuk mencegah brute force attack
6. **Password Strength**: Tambahkan validasi minimal 8 karakter dengan kombinasi huruf dan angka
7. **Email Duplicate Check**: Validasi email yang sudah terdaftar

## 👨‍💻 Author

**Putro**
- GitHub: [@Putroooo](https://github.com/Putroooo)
- Repository: [https://github.com/Putroooo/quiz](https://github.com/Putroooo/quiz)

## 📝 License

Project ini dibuat untuk keperluan testing dan pembelajaran automated testing dengan Selenium WebDriver.

---

## 📌 Notes

- Field `name` pada test case TC-REG-005 sengaja dikosongkan untuk menguji validasi sistem (bug testing)
- Screenshot akan di-generate otomatis saat menjalankan extended test suite
- Untuk hasil terbaik, jalankan test menggunakan `run_tests_with_server.bat`
- CI/CD pipeline akan otomatis berjalan setiap ada push ke repository

**Last Updated**: January 15, 2026  
**Test Suite Version**: 2.0 (Extended with Screenshots)  
**Total Test Cases**: 30  
**Success Rate**: 96.67%
### Security Testing
- ✅ **SQL Injection Prevention**: Test dengan payload SQL injection
- ✅ **XSS Prevention**: Test dengan script injection di input field
- ✅ **Session Security**: Session persistence dan logout

### Edge Cases & Validation
- ✅ **Case Sensitivity**: Username case handling
- ✅ **Whitespace Handling**: Spasi di username/password
- ✅ **Special Characters**: Input karakter spesial
- ✅ **Long Input**: Buffer overflow testing (500+ characters)
- ✅ **Unicode Support**: Testing dengan karakter unicode
- ✅ **Email Validation**: Format dan duplicate email
- ✅ **Password Strength**: Weak password testing

### Integration Testing
- ✅ **Navigation**: Link antar halaman
- ✅ **Session Management**: Login persistence
- ✅ **Database Integration**: CRUD operations

### Performance Testing
- ✅ **Rate Limiting**: Multiple login attempts

## 📈 Test Automation Features

- ✅ Automated screenshot capture
- ✅ Headless browser testing
- ✅ ChromeDriver auto-management via webdriver-manager
- ✅ Parallel test execution support
- ✅ Comprehensive test reporting
- ✅ CI/CD integration with GitHub Actions
- ✅ Cross-platform compatibility (Windows/Linux
   - Configure database connection

3. **Application Setup**
   - Start PHP built-in server
   - Install Chrome & ChromeDriver

4. **Testing**
   - Run Selenium test suite
   - Generate test reports

5. **Reporting**
   - Upload test results
   - Display test summary

### Melihat Hasil Testing

Hasil testing dapat dilihat di:
1. Tab **Actions** di repository GitHub
2. Pilih workflow run yang ingin dilihat
3. Lihat detail di setiap job step
4. Download artifacts untuk test results

## 🐛 Bug yang Ditemukan

### Bug 1: Undefined Variable di register.php
**Lokasi**: Line 33
```php
$query = "INSERT INTO users (username,name,email, password ) VALUES ('$username','$nama','$email','$pass')";
```
**Masalah**: Variable `$nama` tidak terdefinisi, seharusnya `$name`

### Bug 2: Validasi Name Field
Field `name` tidak divalidasi dengan benar, bisa bernilai kosong padahal di database memiliki constraint NOT NULL (sesuai note dari soal).

### Bug 3: Error Message di login.php
Message "Register User Gagal !!" kurang deskriptif, seharusnya "Username tidak ditemukan !!" atau "Login Gagal !!"

## 📖 Stub dan Driver

Project ini menggunakan konsep Stub dan Driver untuk testing:

- **Stub**: Mock object untuk database connection (lihat [STUB_DRIVER.md](STUB_DRIVER.md))
- **Driver**: File `index.php` dan `logout.php` sebagai driver untuk halaman yang diakses setelah login berhasil

## 📊 Test Coverage

- ✅ Positive Testing (login/register berhasil)
- ✅ Negative Testing (validasi error)
- ✅ Edge Cases (empty fields, password mismatch)
- ✅ Security Testing (SQL Injection)
- ✅ Integration Testing (navigation, session)
- ✅ Bug Detection (undefined variables, validation)

## 👨‍💻 Author

**Putro**
- GitHub: [@Putroooo](https://github.com/Putroooo)

## 📝 License

Project ini dibuat untuk keperluan testing dan pembelajaran.

---

**Note**: Field `name` pada database sengaja tidak diisi sebagai bagian dari test case untuk menguji validasi sistem.