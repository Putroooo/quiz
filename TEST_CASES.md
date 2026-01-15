# Test Cases untuk Modul Login dan Register

## A. Test Cases untuk Modul Register

### TC-REG-001: Register dengan data valid lengkap
- **Deskripsi**: User melakukan registrasi dengan semua field diisi dengan benar
- **Input**: 
  - Name: "Test User"
  - Email: "testuser@test.com"
  - Username: "testuser"
  - Password: "Test123!"
  - Re-Password: "Test123!"
- **Expected Result**: Registrasi berhasil, user diarahkan ke index.php
- **Test Type**: Positive Test

### TC-REG-002: Register dengan field kosong
- **Deskripsi**: User mencoba registrasi dengan field kosong
- **Input**: Semua field kosong
- **Expected Result**: Menampilkan error "Data tidak boleh kosong !!"
- **Test Type**: Negative Test

### TC-REG-003: Register dengan password tidak sama
- **Deskripsi**: User mengisi password dan re-password yang berbeda
- **Input**: 
  - Name: "Test User"
  - Email: "testuser2@test.com"
  - Username: "testuser2"
  - Password: "Test123!"
  - Re-Password: "Different123!"
- **Expected Result**: Menampilkan error "Password tidak sama !!"
- **Test Type**: Negative Test

### TC-REG-004: Register dengan username yang sudah terdaftar
- **Deskripsi**: User mencoba registrasi dengan username yang sudah ada
- **Input**: 
  - Name: "New User"
  - Email: "newuser@test.com"
  - Username: "irul" (sudah terdaftar)
  - Password: "Test123!"
  - Re-Password: "Test123!"
- **Expected Result**: Menampilkan error "Username sudah terdaftar !!"
- **Test Type**: Negative Test

### TC-REG-005: Register dengan name kosong (bug testing)
- **Deskripsi**: Menguji apakah sistem mengizinkan registrasi dengan field name kosong
- **Input**: 
  - Name: "" (kosong)
  - Email: "emptyname@test.com"
  - Username: "emptyname"
  - Password: "Test123!"
  - Re-Password: "Test123!"
- **Expected Result**: Seharusnya menampilkan error, tetapi karena bug di kode (tidak ada validasi name), mungkin berhasil
- **Test Type**: Edge Case / Bug Detection

### TC-REG-006: Register dengan email tidak valid
- **Deskripsi**: User mengisi email dengan format yang salah
- **Input**: 
  - Name: "Test User"
  - Email: "invalidemail" (tanpa @)
  - Username: "testuser3"
  - Password: "Test123!"
  - Re-Password: "Test123!"
- **Expected Result**: HTML5 validation menolak submit atau sistem menolak
- **Test Type**: Negative Test

## B. Test Cases untuk Modul Login

### TC-LOG-001: Login dengan credentials yang benar
- **Deskripsi**: User login dengan username dan password yang terdaftar
- **Input**: 
  - Username: "irul"
  - Password: "password123" (sesuai database)
- **Expected Result**: Login berhasil, diarahkan ke index.php
- **Test Type**: Positive Test

### TC-LOG-002: Login dengan username salah
- **Deskripsi**: User login dengan username yang tidak terdaftar
- **Input**: 
  - Username: "usernotexist"
  - Password: "password123"
- **Expected Result**: Menampilkan error "Register User Gagal !!"
- **Test Type**: Negative Test

### TC-LOG-003: Login dengan password salah
- **Deskripsi**: User login dengan username benar tapi password salah
- **Input**: 
  - Username: "irul"
  - Password: "wrongpassword"
- **Expected Result**: Tidak ada redirect, tetap di halaman login
- **Test Type**: Negative Test

### TC-LOG-004: Login dengan field kosong
- **Deskripsi**: User mencoba login tanpa mengisi field
- **Input**: 
  - Username: ""
  - Password: ""
- **Expected Result**: Menampilkan error "Data tidak boleh kosong !!"
- **Test Type**: Negative Test

### TC-LOG-005: Login dengan username kosong
- **Deskripsi**: User login dengan hanya password diisi
- **Input**: 
  - Username: ""
  - Password: "password123"
- **Expected Result**: Menampilkan error "Data tidak boleh kosong !!"
- **Test Type**: Negative Test

### TC-LOG-006: Login dengan password kosong
- **Deskripsi**: User login dengan hanya username diisi
- **Input**: 
  - Username: "irul"
  - Password: ""
- **Expected Result**: Menampilkan error "Data tidak boleh kosong !!"
- **Test Type**: Negative Test

## C. Test Cases untuk Integrasi dan Security

### TC-INT-001: SQL Injection pada username
- **Deskripsi**: Menguji keamanan terhadap SQL injection
- **Input**: 
  - Username: "' OR '1'='1"
  - Password: "anything"
- **Expected Result**: Login gagal, tidak terjadi SQL injection
- **Test Type**: Security Test

### TC-INT-002: Redirect setelah login berhasil
- **Deskripsi**: Memastikan user diredirect ke halaman yang benar setelah login
- **Input**: Credentials valid
- **Expected Result**: URL berubah ke index.php (walaupun file tidak ada)
- **Test Type**: Integration Test

### TC-INT-003: Link navigasi dari login ke register
- **Deskripsi**: Menguji link "Register" pada halaman login
- **Input**: Klik link "Register"
- **Expected Result**: Diarahkan ke register.php
- **Test Type**: Integration Test

### TC-INT-004: Link navigasi dari register ke login
- **Deskripsi**: Menguji link "Login" pada halaman register
- **Input**: Klik link "Login"
- **Expected Result**: Diarahkan ke login.php
- **Test Type**: Integration Test

## D. Bug yang Ditemukan di Kode

1. **Bug di register.php line 33**: Variable `$nama` tidak terdefinisi, seharusnya `$name`
   ```php
   $query = "INSERT INTO users (username,name,email, password ) VALUES ('$username','$nama','$email','$pass')";
   ```

2. **Validasi name field**: Field name tidak divalidasi dengan benar, bisa kosong padahal dalam database ada constraint NOT NULL (sesuai note dari soal)

3. **Error message di login.php**: Message "Register User Gagal !!" seharusnya "Login Gagal !!" atau "Username tidak ditemukan !!"
