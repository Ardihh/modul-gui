# Modul 3: Graphical User Interface (GUI) dengan Java Swing

Website modul praktikum statis untuk mata kuliah **Pemrograman Berorientasi Objek (PBO)** Program Studi Teknik Informatika, Fakultas Teknik, Universitas Mataram.

Modul ini membimbing mahasiswa semester awal yang telah memahami dasar-dasar OOP (*Class*, *Object*, *Constructor*, *Inheritance*, *Encapsulation*, dan *Polymorphism*) untuk membangun antarmuka visual desktop modern menggunakan pustaka bawaan **Java Swing**.

---

## 🌟 Fitur Utama Modul

1. **Zero-Build & Zero-Dependency:**
   - 100% Native HTML5, CSS3, dan Vanilla JavaScript.
   - Tidak memerlukan Node.js, Webpack, Vite, NPM, atau framework apapun. Langsung aktif saat di-push ke GitHub Pages!
2. **Offline-Ready:**
   - Library syntax highlighting (Prism.js) dan style sudah di-bundling secara lokal di folder `assets/`.
   - Praktikan cukup melakukan *double-click* file `index.html` di komputer laboratorium tanpa butuh koneksi internet.
3. **Desain Modern & Ergonomis:**
   - Palet warna: **Deep Navy (`#0f172a`, `#1e3a8a`)** dipadu dengan aksen **Gold Amber (`#f59e0b`, `#fbbf24`)**.
   - Mode Gelap / Terang (Dark / Light Mode) dengan penyimpanan preferensi otomatis di `localStorage`.
   - Sidebar navigasi daftar isi *sticky*, indikator bab aktif, dan *reading progress bar*.
   - Mockup visual jendela Java Swing realistis yang dirender murni menggunakan CSS dan SVG (bukan screenshot statis).
4. **Alat Bantu Belajar Praktikan:**
   - **Tombol Salin Kode:** Salin contoh kode Java hanya dengan 1 kali klik.
   - **Pencarian Cepat Client-Side:** Tekan `Ctrl + K` atau klik tombol cari untuk menemukan konsep atau method secara instan.
   - **Event Playground Simulator:** Simulator interaktif browser berbasis JavaScript untuk mengamati urutan panggilan method event (`mousePressed` &rarr; `released` &rarr; `clicked` &rarr; `actionPerformed`) secara real-time.
   - **Kuis Pilihan Ganda Interaktif:** 20 soal evaluasi konsep GUI dengan skor otomatis, pembahasan mendalam, dan soal analisis bug kode.
   - **Checklist Kesiapan Jurnal:** Daftar periksa mandiri sebelum mahasiswa mulai mengerjakan tugas jurnal.
   - **Cheat Sheet Ringkas:** Tabel satu halaman berisi seluruh method sakti Swing dan layout manager.
   - **Aksesibel & Cetak-Ramah:** Dilengkapi stylesheet `@media print` sehingga praktikan dapat langsung mencetak atau menyimpan modul ke format PDF via browser (`Ctrl + P`).

---

## ☕ Studi Kasus Panduan: JavaCafe POS

Seluruh bab di dalam modul ini dirancang konsisten menggunakan studi kasus **"JavaCafe POS" (Point of Sales Pemesanan Kafe)**:
- **Katalog Menu:** Pilihan racikan minuman kopi (Espresso, Americano, Latte, Caramel Macchiato) dengan gambar dan harga dasar.
- **Detail Pesanan & Add-on:** Formulir kustomisasi opsi tambahan menggunakan `JCheckBox` (Extra Shot, Susu Oat, Sirup Vanilla, Topping Ice Cream).
- **Kalkulasi & Format Rupiah:** Pola komputasi kasir mengakumulasikan harga dasar + add-on dinamis dalam format mata uang Indonesia (`Locale.forLanguageTag("id-ID")`).
- **Navigasi Layar Tunggal:** Menggunakan `CardLayout` untuk berpindah bolak-balik antara katalog dan form pesanan di dalam jendela berdimensi tetap (520x350 pixel).
- **Arsitektur Clean Code:** Mengorganisasi komponen sebagai *field*, inisialisasi bertahap, dan kelas utilitas tema terpusat (`CafeTheme`).

> [!NOTE]
> Modul ini dirancang membekali praktikan dengan **seluruh teknik dan konsep**, tanpa membocorkan studi kasus tugas jurnal (DNE DEVS).

---

## 📂 Struktur Repositori

```text
modul-gui/
├── .gitignore                         # Mengabaikan file *.class dan folder IDE
├── .nojekyll                          # Bypass Jekyll engine di GitHub Pages
├── README.md                          # Dokumentasi proyek & panduan deploy
├── index.html                         # Beranda & halaman utama aplikasi modul (SPA)
├── build_site.py                      # Skrip utilitas builder
├── generate_site.py                   # Generator utama penyusun index.html
├── generator_modules/                 # Modul-modul data konten bab & utilitas
│   ├── chapters_appendix.py           # Cheat sheet, checklist, kuis, glosarium, referensi
│   ├── chapters_part1.py              # Beranda, Bab 1 - Bab 4
│   ├── chapters_part2.py              # Bab 5 - Bab 9
│   ├── chapters_part3.py              # Bab 10 - Bab 14
│   ├── site_data.py                   # Data navigasi, kuis, glosarium, cheatsheet
│   └── utils.py                       # Helper escaping & pembungkus kode
├── assets/
│   ├── css/
│   │   ├── prism.min.css              # Tema syntax highlighting
│   │   └── style.css                  # Design system, Swing mockup, print stylesheet
│   ├── js/
│   │   ├── app.js                     # Router hash, theme engine, copy code, kuis, search
│   │   └── prism.min.js               # Java syntax highlighter (offline-ready)
│   └── img/
│       ├── coffee.png                 # Aset gambar contoh produk kafe
│       └── logo-lab.svg               # Logo vektor laboratorium & modul
└── examples/                          # 19 file source code Java asli (lulus javac)
    ├── 01_Pengantar/HaloSwing.java
    ├── 02_JFrameDasar/JendelaUtama.java
    ├── 03_JPanelModular/
    │   ├── AppFrame.java
    │   └── MenuPanel.java
    ├── 04_KomponenDasar/KomponenDemo.java
    ├── 05_ImageIconDemo/GambarDemo.java
    ├── 06_LayoutManager/LayoutDemo.java
    ├── 07_CardLayout/NavigasiCardDemo.java
    ├── 08_BorderDemo/BorderDemo.java
    ├── 09_EventHandling/
    │   ├── EmpatGayaListenerDemo.java # Perbandingan 4 gaya listener pada counter kafe
    │   ├── KatalogListenerDemo.java   # Demo ItemListener, ChangeListener, ListSelection
    │   ├── AdapterListenerDemo.java   # Demo MouseAdapter, KeyAdapter, WindowAdapter
    │   ├── EventHandlingDemo.java     # Demo dasar ActionListener & CheckBox
    │   └── mini_proyek/
    │       ├── Level1_KasirTopping.java     # Mini-proyek Level 1 (Item + Action)
    │       ├── Level2_FormValidasi.java     # Mini-proyek Level 2 (Doc + Key + Focus)
    │       └── Level3_JavaCafeProPOS.java   # Mini-proyek Level 3 (CardLayout + Mouse + Keys + Window)
    ├── 10_DialogJOptionPane/DialogDemo.java
    ├── 11_CleanCode/
    │   ├── CafeTheme.java
    │   └── FormCleanDemo.java
    ├── 12_KalkulasiRupiah/KasirHitungDemo.java
    ├── 13_UMLToCode/TiketKafeApp.java
    └── 14_JavaCafePOS/                # Aplikasi Mini Utuh JavaCafe POS
        ├── CafeTheme.java
        ├── HalamanMenu.java
        ├── HalamanPesanan.java
        └── MainApp.java
```

---

## 🚀 Cara Menjalankan Modul Secara Lokal

Mahasiswa atau asisten dapat membuka modul ini secara lokal di komputer dengan dua cara mudah:

### Cara 1: Langsung Buka File (Paling Cepat)
Cukup cari file `index.html` di file manager (Windows Explorer / Finder) dan lakukan **Double Click**. Halaman akan langsung terbuka di browser (Chrome / Edge / Firefox) dan seluruh fitur (termasuk Dark Mode, navigasi bab, salin kode, dan kuis) berfungsi 100% normal tanpa kendala CORS.

### Cara 2: Menggunakan Server Statis Python
Jika Anda ingin menjalankannya via protokol HTTP lokal:
```bash
# Masuk ke direktori repositori
cd modul-gui

# Jalankan server bawaan Python
python -m http.server 8000
```
Buka browser dan akses alamat: [http://localhost:8000](http://localhost:8000).

---

## 🌐 Panduan Deploy ke GitHub Pages

Situs ini telah dirancang khusus agar otomatis aktif di GitHub Pages tanpa konfigurasi tambahan (adanya file `.nojekyll` menjamin aset folder `assets/` dimuat dengan sempurna):

1. **Push Perubahan ke Repositori GitHub:**
   ```bash
   git add .
   git commit -m "feat: rilis modul 3 GUI Java Swing lengkap"
   git push origin main
   ```
2. **Buka Halaman Pengaturan GitHub:**
   - Masuk ke tab **Settings** pada repositori GitHub Anda (`https://github.com/Ardihh/modul-gui/settings`).
3. **Pilih Menu Pages:**
   - Di bilah samping kiri (sidebar), klik menu **Pages** (di bawah kategori *Code and automation*).
4. **Konfigurasi Sumber Build and Deployment:**
   - Pada bagian **Build and deployment > Source**, pilih: `Deploy from a branch`.
   - Pada bagian **Branch**, pilih branch: `main` dan folder: `/ (root)`.
   - Klik tombol **Save**.
5. **Akses Situs Anda:**
   - Tunggu 1–2 menit hingga GitHub Actions selesai memproses deployment.
   - Situs modul Anda akan langsung aktif di URL:
     **`https://ardihh.github.io/modul-gui/`**

---

## ☕ Mengompilasi & Menjalankan Contoh Kode Java

Semua contoh program di folder `examples/` dirancang kompatibel dengan Java SE 17+ (LTS) hingga JDK 21+ dan telah lulus uji kompilasi `javac`.

Contoh menjalankan aplikasi mini utuh **JavaCafe POS**:
```bash
# Masuk ke folder contoh JavaCafe POS
cd examples/14_JavaCafePOS

# Kompilasi seluruh file Java
javac *.java

# Jalankan aplikasi kasir
java examples.javacafepos.MainApp
```

---

## ✏️ Cara Mengedit atau Memperbarui Konten Modul

Konten modul dikelola secara modular melalui Python di folder `generator_modules/`:
1. Edit teks materi di file terkait:
   - `generator_modules/chapters_part1.py` untuk Beranda & Bab 1–4.
   - `generator_modules/chapters_part2.py` untuk Bab 5–9.
   - `generator_modules/chapters_part3.py` untuk Bab 10–14.
   - `generator_modules/chapters_appendix.py` atau `site_data.py` untuk soal kuis, cheatsheet, dan checklist.
2. Jalankan ulang script pembangun:
   ```bash
   python generate_site.py
   ```
3. Commit dan push kembali perubahannya ke GitHub!

---

## 🏛️ Kredit & Tim Pengembang

- **Mata Kuliah:** Pemrograman Berorientasi Objek (Java)
- **Laboratorium:** Laboratorium Komputer Dasar & Pemrograman
- **Institusi:** Program Studi Teknik Informatika, Fakultas Teknik, Universitas Mataram
- **Penyusun & Asisten Praktikum:** M. Rizki Juniardi & Tim Asisten Praktikum PBO
- **Tahun Ajaran:** Semester Ganjil 2024/2025
