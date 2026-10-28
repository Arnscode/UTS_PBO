# UTS PBO — sesuai struktur soal

Kedua file JSON mempertahankan struktur dari lembar UTS:
- `employee.json`: key `employees`, field `emp_id`, `name`, `base_salary`, `is_permanent`, `bonus_code`.
- `sensor_logs.json`: key `readings`, field `sensor_id`, `location`, `temperature`, `status`, `operator_id`.

## Struktur kode
- `BaseProcessor`: kelas induk untuk membaca JSON dan ekspor CSV.
- `EmployeeProcessor` dan `SensorProcessor`: kelas turunan yang meng-override `process_data()`.
- `runner_pipeline.py`: menjalankan kedua processor secara polimorfik.
- `main.py`: program utama.

## Menjalankan
Dari folder proyek, jalankan `python main.py`. Tidak perlu package eksternal.

## Konsep OOP
- Rule: status karyawan dibaca dari `is_permanent`; tindakan sensor ditandai berdasarkan `status` yang tersedia.
- Inheritance: kedua processor mewarisi `BaseProcessor`.
- Polymorphism: pemanggilan metode sama pada objek processor yang berbeda.
- Override: masing-masing processor menyediakan implementasi `process_data()` sendiri.
