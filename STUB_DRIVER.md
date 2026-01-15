# Stub/Mock untuk Database Testing

## Stub untuk Testing Tanpa Database

Untuk testing tanpa database aktif, kita bisa membuat stub untuk koneksi database.

### koneksi_stub.php

```php
<?php
    // Stub untuk testing
    // Simulasi koneksi database tanpa koneksi sebenarnya
    
    class DatabaseStub {
        private $users = [
            [
                'id' => 1,
                'name' => '',
                'username' => 'irul',
                'email' => 'irul@irul.com',
                'password' => '$2y$10$D9yc9Mt0t8niCNO9di8ejOUPib46suwHghqFnJRKQJ3Z6uwRDxfw.'
            ],
            [
                'id' => 2,
                'name' => '',
                'username' => 'ahmad',
                'email' => 'ahmad@ahmad.com',
                'password' => '$2y$10$OWez2au.UMnz3yedD0BqH.bsOC374XoV9hMigepVzLyuq2jETHs2'
            ]
        ];
        
        public function query($sql) {
            // Simulasi query
            if (strpos($sql, 'SELECT') !== false) {
                // Return stub result
                return new ResultStub($this->users);
            }
            return true;
        }
        
        public function real_escape_string($string) {
            return addslashes($string);
        }
    }
    
    class ResultStub {
        private $data;
        private $index = 0;
        
        public function __construct($data) {
            $this->data = $data;
        }
        
        public function num_rows() {
            return count($this->data);
        }
        
        public function fetch_assoc() {
            if ($this->index < count($this->data)) {
                return $this->data[$this->index++];
            }
            return null;
        }
    }
    
    $con = new DatabaseStub();
?>
```

## Driver untuk Integration Testing

Driver adalah komponen yang mensimulasikan bagian sistem yang belum diimplementasi.

### index_driver.php

File ini mensimulasikan halaman index.php yang belum ada:

```php
<?php
session_start();

if (!isset($_SESSION['username'])) {
    header('Location: login.php');
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Driver</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <div class="alert alert-success">
            <h4>Login Successful!</h4>
            <p>Welcome, <?= htmlspecialchars($_SESSION['username']) ?>!</p>
            <p>This is a driver page for testing purposes.</p>
        </div>
        <a href="logout.php" class="btn btn-danger">Logout</a>
    </div>
</body>
</html>
```

### logout_driver.php

```php
<?php
session_start();
session_destroy();
header('Location: login.php');
exit();
?>
```

## Penggunaan Stub dan Driver

1. **Stub**: Digunakan untuk unit testing tanpa database
   - Replace `koneksi.php` dengan `koneksi_stub.php` saat testing
   - Mengembalikan data mock tanpa koneksi database sebenarnya

2. **Driver**: Digunakan untuk integration testing
   - `index_driver.php` mensimulasikan halaman dashboard yang sebenarnya
   - Memungkinkan testing flow login/register tanpa implementasi lengkap

## Cara Menggunakan dalam Testing

Untuk menggunakan stub, ubah require di file login.php dan register.php:

```php
// Untuk production
require('koneksi.php');

// Untuk testing dengan stub
// require('koneksi_stub.php');
```

Atau buat environment variable untuk switch antara real dan stub.
