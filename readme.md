# Quiz Pengupil - Login & Register Testing

Repository ini berisi implementasi testing untuk modul Login dan Register menggunakan Selenium WebDriver dengan CI/CD pipeline di GitHub Actions.

## 📋 Deskripsi

Project ini merupakan sistem login dan register sederhana berbasis PHP dan MySQL yang dilengkapi dengan automated testing menggunakan Selenium. Testing mencakup berbagai test cases untuk memastikan fungsionalitas login dan register bekerja dengan baik.

## 🔗 Link Repository

**Repository GitHub**: [https://github.com/Putroooo/quiz](https://github.com/Putroooo/quiz)

## 🧪 Test Cases

### Test Cases Login (8 test cases)
1. **TC-LOG-001**: Login dengan credentials yang benar
2. **TC-LOG-002**: Login dengan username yang tidak terdaftar
3. **TC-LOG-003**: Login dengan password salah
4. **TC-LOG-004**: Login dengan field kosong
5. **TC-LOG-005**: Login dengan username kosong
6. **TC-LOG-006**: Login dengan password kosong
7. **TC-INT-001**: Test SQL Injection prevention
8. **TC-INT-003**: Navigasi dari login ke register

### Test Cases Register (7 test cases)
1. **TC-REG-001**: Register dengan data valid lengkap
2. **TC-REG-002**: Register dengan field kosong
3. **TC-REG-003**: Register dengan password tidak sama
4. **TC-REG-004**: Register dengan username yang sudah terdaftar
5. **TC-REG-005**: Register dengan name kosong (bug testing)
6. **TC-REG-006**: Register dengan email tidak valid
7. **TC-INT-004**: Navigasi dari register ke login

**Total: 15 Test Cases**

Detail lengkap test cases dapat dilihat di [TEST_CASES.md](TEST_CASES.md)

## 🛠️ Teknologi yang Digunakan

- **Backend**: PHP 8.1
- **Database**: MySQL 8.0
- **Testing Framework**: Python Unittest
- **Automation Tool**: Selenium WebDriver 4.16.0
- **CI/CD**: GitHub Actions
- **Web Server**: PHP Built-in Server

## 📁 Struktur Project

```
quiz-pengupil/
├── .github/
│   └── workflows/
│       └── selenium-tests.yml    # GitHub Actions workflow
├── db/
│   └── quiz_pengupil.sql         # Database schema
├── tests/
│   ├── test_login.py             # Test cases untuk login
│   ├── test_register.py          # Test cases untuk register
│   └── run_tests.py              # Test runner
├── index.php                     # Dashboard (driver)
├── login.php                     # Halaman login
├── register.php                  # Halaman register
├── logout.php                    # Logout handler
├── koneksi.php                   # Database connection
├── style.css                     # Styling
├── requirements.txt              # Python dependencies
├── TEST_CASES.md                 # Dokumentasi test cases
├── STUB_DRIVER.md                # Dokumentasi stub & driver
└── README.md                     # Dokumentasi ini
```

## 🚀 Cara Menjalankan Locally

### Prerequisites
- PHP 8.x
- MySQL 8.x
- Python 3.11+
- Chrome Browser

### Setup

1. Clone repository
```bash
git clone https://github.com/Putroooo/quiz.git
cd quiz
```

2. Import database
```bash
mysql -u root -p quiz_pengupil < db/quiz_pengupil.sql
```

3. Konfigurasi database (jika perlu)
Edit file `koneksi.php` sesuai dengan konfigurasi MySQL Anda

4. Install Python dependencies
```bash
pip install -r requirements.txt
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

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow

Pipeline CI/CD otomatis berjalan pada:
- Push ke branch `main` atau `master`
- Pull request ke branch `main` atau `master`
- Manual trigger via workflow_dispatch

### Tahapan Pipeline

1. **Setup Environment**
   - Checkout code
   - Setup PHP 8.1
   - Setup Python 3.11
   - Setup MySQL 8.0 service

2. **Database Configuration**
   - Import database schema
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