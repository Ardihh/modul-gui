# -*- coding: utf-8 -*-
from generator_modules.utils import code_box, nav_buttons

def get_beranda():
    return f'''
    <article class="chapter-article active" id="beranda">
      <div class="chapter-badge">🌟 Selamat Datang • Modul Praktikum PBO</div>
      <h1 class="chapter-title">Modul 3: Graphical User Interface (GUI) dengan Java Swing</h1>
      <p class="chapter-lead">
        Selamat datang di laboratorium praktikum Pemrograman Berorientasi Objek. Pada modul ini, kita akan melompat dari aplikasi berbasis terminal teks hitam-putih (CLI) menuju pembangunan aplikasi visual desktop yang interaktif, elegan, dan siap digunakan oleh pengguna awam.
      </p>

      <div class="callout callout-info">
        <div class="callout-header">🏛️ Identitas Praktikum & Laboratorium</div>
        <p>
          <strong>Institusi:</strong> Program Studi Teknik Informatika, Fakultas Teknik, Universitas Mataram<br>
          <strong>Laboratorium:</strong> Laboratorium Komputer Dasar & Pemrograman<br>
          <strong>Koordinator / Asisten:</strong> M. Rizki Juniardi & Tim Asisten Praktikum PBO<br>
          <strong>Lingkungan Teknis:</strong> Java SE 17+ (LTS) / JDK 21 | IDE: IntelliJ IDEA / Apache NetBeans / VS Code
        </p>
      </div>

      <h2>🎯 Dari Console Menuju Antarmuka Visual</h2>
      <p>
        Pada Modul 1 dan Modul 2, Anda telah mempelajari pilar fundamental OOP: <em>Class & Object</em>, <em>Constructor</em>, <em>Encapsulation</em>, <em>Inheritance</em>, serta <em>Polymorphism & Interface</em>. Selama ini, seluruh output program dicetak ke baris konsol melalui <code>System.out.println()</code> dan input pengguna diketik melalui <code>Scanner</code>.
      </p>
      <p>
        Dalam industri nyata, pengguna akhir (end-user) berinteraksi melalui <strong>Antarmuka Grafis (GUI)</strong>: mereka melihat gambar produk, memilih opsi dengan mencentang kotak (<em>CheckBox</em>), menekan tombol untuk menghitung transaksi, dan melihat jendela konfirmasi pop-up.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">☕ Studi Kasus Panduan: JavaCafe POS</div>
        <p style="margin-bottom: 0.5rem; color: var(--text-main);">
          Untuk memastikan materi ini mudah dipahami secara konkret, seluruh bab dalam modul ini dirancang mengelilingi satu studi kasus utama yang konsisten: <strong>JavaCafe POS (Point of Sales Pemesanan Kafe)</strong>.
        </p>
        <ul class="objectives-list">
          <li><strong>Halaman Katalog Menu:</strong> Menampilkan foto menu minuman, nama racikan kopi, deskripsi rasa, dan harga dasar.</li>
          <li><strong>Halaman Formulir Pesanan:</strong> Kustomisasi minuman pelanggan dengan variasi topping / add-on menggunakan <code>JCheckBox</code> (Extra Shot, Oat Milk, dsb.).</li>
          <li><strong>Sistem Kalkulasi:</strong> Tombol "Hitung Total" yang mengakumulasi harga dasar + add-on terpilih dalam format mata uang Rupiah.</li>
          <li><strong>Feedback Transaksi:</strong> Kotak pop-up dialog <code>JOptionPane</code> konfirmasi sukses pesanan beserta ikon kafe kustom.</li>
          <li><strong>Arsitektur Layar Tunggal:</strong> Navigasi bolak-balik antara katalog dan pesanan menggunakan <code>CardLayout</code> di dalam jendela berukuran tetap (520x350 pixel).</li>
        </ul>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Cara Belajar Efektif di Modul Ini</div>
        <ol style="margin-bottom: 0; padding-left: 1.25rem;">
          <li><strong>Jalankan Semua Contoh:</strong> Setiap bab menyediakan kode program lengkap yang dapat langsung Anda unduh di folder <code>examples/</code> dan jalankan di IDE pilihan Anda.</li>
          <li><strong>Pahami Pola, Bukan Sekadar Menghafal Sintaks:</strong> Pahami mengapa sebuah method dipanggil dan bagaimana komponen saling berhubungan dalam hierarki objek OOP.</li>
          <li><strong>Uji Diri dengan Latihan & Kuis:</strong> Buka accordion petunjuk latihan mandiri di akhir setiap bab dan kerjakan Kuis Interaktif sebelum memulai lembar Jurnal.</li>
        </ol>
      </div>

      <div class="summary-card">
        <div class="summary-title">📌 Peta Jalan Belajar Modul 3</div>
        <ul class="summary-list">
          <li><strong>Fase 1 (Bab 1–3):</strong> Landasan GUI, Frame Utama (JFrame), dan Container Modular (JPanel).</li>
          <li><strong>Fase 2 (Bab 4–6):</strong> Komponen Teks/Tombol/Pilihan, Menangani Gambar (ImageIcon), dan Tata Letak (Layout Manager).</li>
          <li><strong>Fase 3 (Bab 7–10):</strong> Navigasi Halaman (CardLayout), Estetika Spasi (Border), Interaktivitas (Event Handling), dan Dialog Pop-Up (JOptionPane).</li>
          <li><strong>Fase 4 (Bab 11–14):</strong> Clean Code GUI & Sistem Tema, Logika Bisnis Kasir & Format Rupiah, Membaca Diagram UML, serta Teknik Debugging.</li>
        </ul>
      </div>

      {nav_buttons(None, None, 'bab-1', 'Bab 1: Pengantar GUI & Event-Driven')}
    </article>
    '''

def get_bab1():
    return f'''
    <article class="chapter-article" id="bab-1">
      <div class="chapter-badge">Bab 01 • Dasar Konseptual</div>
      <h1 class="chapter-title">Pengantar GUI & Pemrograman Berbasis Event</h1>
      <p class="chapter-lead">
        Mengenal perbedaan mendasar antara CLI dan GUI, sejarah AWT vs Swing, konsep Komponen vs Container, serta bagaimana Event-Driven Programming mengubah alur eksekusi kode Java.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Menjelaskan perbedaan alur eksekusi procedural CLI vs event-driven GUI.</li>
          <li>Membedakan karakteristik pustaka AWT (heavyweight) dengan Java Swing (lightweight).</li>
          <li>Memahami relasi hierarkis antara Komponen visual dan Wadah Container.</li>
          <li>Menjalankan program GUI pertama menggunakan Event Dispatch Thread (EDT).</li>
        </ul>
      </div>

      <h2>1. CLI vs GUI: Perubahan Paradigma Interaksi</h2>
      <p>
        Pada aplikasi konsol (CLI), alur eksekusi bersifat <strong>sekuensial dan prosedural</strong>. Program menentukan kapan pengguna harus menginput data:
      </p>
      <p style="background: var(--bg-surface); padding: 0.75rem 1rem; border-left: 3px solid var(--border-color); font-family: monospace;">
        Prompt Nama &rarr; Scanner membaca nama &rarr; Prompt Umur &rarr; Scanner membaca umur &rarr; Cetak hasil &rarr; Program Selesai.
      </p>
      <p>
        Sebaliknya, pada <strong>GUI (Graphical User Interface)</strong>, kendali berada di tangan pengguna! Pengguna bebas memilih: apakah ingin langsung menekan tombol, mencentang kotak, memilih gambar, atau menutup jendela. Program tidak lagi berjalan linier, melainkan berada dalam status <em>mendengarkan</em> (listening) dan baru bereaksi ketika terjadi suatu <strong>Event</strong> (kejadian). Paradigma ini disebut <strong>Event-Driven Programming</strong>.
      </p>

      <h2>2. AWT vs Java Swing: Mengapa Kita Menggunakan Swing?</h2>
      <p>
        Java memiliki dua pustaka GUI bawaan standar di dalam paket JDK:
      </p>
      <ul>
        <li>
          <strong>AWT (Abstract Window Toolkit):</strong> Pustaka generasi pertama (paket <code>java.awt</code>). Bersifat <em>Heavyweight</em> karena setiap tombol atau jendela meminjam komponen native milik sistem operasi (Windows, Linux, macOS). Akibatnya, tampilan aplikasi terlihat berbeda-beda di tiap OS dan kustomisasinya sangat terbatas.
        </li>
        <li>
          <strong>Java Swing:</strong> Pustaka generasi modern (paket <code>javax.swing</code>). Bersifat <em>Lightweight</em> karena ditulis murni 100% dalam Java dan digambar langsung di layar menggunakan Java 2D. Hasilnya: tampilan seragam, konsisten, mendukung sistem tema fleksibel, dan memiliki komponen yang jauh lebih kaya.
        </li>
      </ul>

      <div class="callout callout-info">
        <div class="callout-header">💡 Ciri Khas Penamaan Komponen Swing</div>
        <p>
          Seluruh komponen Swing diawali dengan huruf kapital <strong>'J'</strong> untuk membedakannya dari komponen AWT lama:
          <code>JFrame</code> (bukan <em>Frame</em>), <code>JButton</code> (bukan <em>Button</em>), <code>JLabel</code> (bukan <em>Label</em>), dan <code>JPanel</code> (bukan <em>Panel</em>).
        </p>
      </div>

      <h2>3. Konsep Komponen dan Container</h2>
      <p>
        Dalam merancang GUI, bayangkan sebuah meja kafe:
      </p>
      <ul>
        <li><strong>Container (Wadah):</strong> Adalah meja atau nampannya. Container bertugas menampung benda-benda lain. Contoh container: <code>JFrame</code> (jendela utama), <code>JPanel</code> (nampan penyekat).</li>
        <li><strong>Component (Komponen):</strong> Adalah cangkir kopi, piring kue, dan sendoknya. Komponen adalah elemen individual yang memiliki fungsi spesifik. Contoh: <code>JLabel</code> (label teks/gambar), <code>JButton</code> (tombol aksi), <code>JCheckBox</code> (pilihan centang).</li>
      </ul>

      <h2>4. Contoh Program Pertama: HaloSwing</h2>
      <p>
        Mari kita bedah kode program GUI paling sederhana yang menampilkan salam di layar desktop:
      </p>

      {code_box("examples/01_Pengantar/HaloSwing.java", "HaloSwing.java")}

      <h2>5. Bedah Baris Kode Kunci</h2>
      <ul>
        <li>
          <code>SwingUtilities.invokeLater(() -> {{ ... }});</code><br>
          Instruksi ini memastikan pembuatan jendela dijalankan di dalam <strong>Event Dispatch Thread (EDT)</strong>. Swing tidak bersifat <em>thread-safe</em>, sehingga seluruh operasi GUI wajib diserahkan ke EDT agar terhindar dari konflik proses.
        </li>
        <li>
          <code>JFrame frame = new JFrame("...");</code><br>
          Membuat objek jendela utama desktop lengkap dengan baris judul di bagian atas.
        </li>
        <li>
          <code>frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);</code><br>
          Menginstruksikan Java agar menghentikan total proses program (JVM) saat pengguna menekan tombol silang merah (X) di pojok jendela.
        </li>
        <li>
          <code>frame.setLocationRelativeTo(null);</code><br>
          Perintah sakti untuk memposisikan jendela tepat di titik koordinat tengah monitor pengguna secara otomatis.
        </li>
        <li>
          <code>frame.setVisible(true);</code><br>
          Secara default, objek frame diciptakan dalam keadaan tersembunyi (invisible) di memori. Method ini memunculkannya ke pandangan pengguna.
        </li>
      </ul>

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 400px; min-height: 180px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Aplikasi Pertama Saya - Java Swing</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="align-items: center; justify-content: center;">
            <p style="font-weight: 700; font-size: 0.95rem; color: #1e3a8a; text-align: center;">
              Halo Mahasiswa PBO! Selamat Datang di Swing.
            </p>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Tampilan Program HaloSwing.java pada Layar Pengguna</div>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jangan Lupa invokeLater!</div>
        <p>
          Menjalankan kode GUI langsung di thread <code>main</code> tanpa <code>SwingUtilities.invokeLater</code> dapat menyebabkan <em>intermittent rendering glitch</em> (jendela kadang kosong putih atau komponen terlambat digambar saat aplikasi bertambah kompleks).
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 1.1</div>
        <p>
          Jalankan <code>HaloSwing.java</code> di IDE Anda. Kemudian modifikasi program agar jendela memiliki ukuran lebar 480 pixel, tinggi 220 pixel, dan menampilkan salam khusus yang memuat nama dan NIM Anda sendiri!
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Cari baris <code>frame.setSize(400, 250);</code> dan sesuaikan nilainya menjadi <code>frame.setSize(480, 220);</code>. Lalu ubah teks di constructor <code>new JLabel(...)</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 1</div>
        <ul class="summary-list">
          <li>GUI menggunakan paradigma <strong>Event-Driven</strong> di mana program merespon aksi tak terduga dari pengguna.</li>
          <li><strong>Java Swing</strong> adalah pustaka GUI lightweight murni Java yang fleksibel dan konsisten lintas sistem operasi.</li>
          <li><strong>Container</strong> menampung <strong>Komponen</strong>; jendela tingkat teratas paling dasar adalah <code>JFrame</code>.</li>
          <li>Semua instansiasi dan pembaruan GUI wajib dieksekusi di <strong>Event Dispatch Thread (EDT)</strong> via <code>SwingUtilities.invokeLater</code>.</li>
        </ul>
      </div>

      {nav_buttons('beranda', 'Beranda & Pengantar', 'bab-2', 'Bab 2: Jendela Pertama: JFrame')}
    </article>
    '''

def get_bab2():
    return f'''
    <article class="chapter-article" id="bab-2">
      <div class="chapter-badge">Bab 02 • Jendela Utama</div>
      <h1 class="chapter-title">Membuat Jendela dengan JFrame</h1>
      <p class="chapter-lead">
        Menguasai konfigurasi properti dasar jendela aplikasi, menerapkan prinsip pewarisan OOP (Inheritance) dengan membuat kelas turunan JFrame, serta mengunci ukuran dan memposisikan window di tengah layar.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Memahami fungsi dan siklus hidup jendela <code>JFrame</code>.</li>
          <li>Menerapkan prinsip OOP dengan mendefinisikan kelas yang <code>extends JFrame</code>.</li>
          <li>Mengkonfigurasi 6 method esensial: <code>setTitle</code>, <code>setSize</code>, <code>setDefaultCloseOperation</code>, <code>setLocationRelativeTo</code>, <code>setResizable</code>, dan <code>setVisible</code>.</li>
          <li>Menjelaskan alasan teknis di balik penguncian dimensi jendela (fixed-size window).</li>
        </ul>
      </div>

      <h2>1. Mengapa Menggunakan 'extends JFrame'?</h2>
      <p>
        Pada Bab 1, kita membuat objek frame secara prosedural di method <code>main</code>: <code>JFrame frame = new JFrame();</code>. Cara tersebut cukup untuk demo mini, tetapi <strong>melanggar prinsip desain OOP</strong> saat aplikasi bertumbuh besar.
      </p>
      <p>
        Praktik terbaik di dunia industri adalah menerapkan <strong>Inheritance</strong>: kita mendefinisikan kelas aplikasi kita sendiri (misalnya <code>JendelaUtama</code> atau <code>MainApp</code>) sebagai turunan dari <code>JFrame</code>:
      </p>
      <p style="background: var(--bg-surface); padding: 0.75rem 1rem; border-left: 3px solid var(--primary-light); font-family: monospace;">
        public class JendelaUtama <strong>extends JFrame</strong> {{ ... }}
      </p>
      <p>
        Dengan cara ini, kelas <code>JendelaUtama</code> mewarisi seluruh kemampuan sebuah jendela, memiliki hak untuk mengonfigurasi dirinya sendiri di dalam constructor (<em>Encapsulation</em>), dan method <code>main</code> menjadi sangat bersih: hanya bertugas membuat satu objek dan memanggil <code>setVisible(true)</code>!
      </p>

      <h2>2. Enam Method Konfigurasi Wajib pada JFrame</h2>
      <p>Berikut adalah 6 konfigurasi fundamental yang harus selalu Anda ingat:</p>

      <table style="width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.92rem;">
        <thead>
          <tr style="background: var(--primary-subtle); border-bottom: 2px solid var(--primary-border);">
            <th style="padding: 0.75rem; text-align: left;">Method</th>
            <th style="padding: 0.75rem; text-align: left;">Parameter Contoh</th>
            <th style="padding: 0.75rem; text-align: left;">Fungsi & Perilaku</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 600;">setTitle(String)</td>
            <td style="padding: 0.65rem;">"JavaCafe POS"</td>
            <td style="padding: 0.65rem;">Mengatur teks judul pada title bar atas jendela.</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 600;">setSize(int, int)</td>
            <td style="padding: 0.65rem;">520, 350</td>
            <td style="padding: 0.65rem;">Menentukan lebar dan tinggi jendela dalam satuan pixel.</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 600;">setDefaultCloseOperation</td>
            <td style="padding: 0.65rem;">JFrame.EXIT_ON_CLOSE</td>
            <td style="padding: 0.65rem;">Menghentikan JVM saat jendela ditutup oleh pengguna.</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 600;">setLocationRelativeTo</td>
            <td style="padding: 0.65rem;">null</td>
            <td style="padding: 0.65rem;">Menempatkan jendela tepat di tengah monitor (wajib dipanggil setelah setSize).</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 600;">setResizable(boolean)</td>
            <td style="padding: 0.65rem;">false</td>
            <td style="padding: 0.65rem;">Mengunci ukuran agar pengguna tidak dapat memperbesar/mengecilkan window.</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 600;">setVisible(boolean)</td>
            <td style="padding: 0.65rem;">true</td>
            <td style="padding: 0.65rem;">Menampilkan frame ke layar (selalu panggil paling akhir).</td>
          </tr>
        </tbody>
      </table>

      <h2>3. Contoh Kode: JendelaUtama.java</h2>
      <p>
        Perhatikan bagaimana seluruh pengaturan jendela dibungkus rapi di dalam constructor kelas:
      </p>

      {code_box("examples/02_JFrameDasar/JendelaUtama.java", "JendelaUtama.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 520px; height: 260px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ JavaCafe POS - Sistem Kasir V1.0</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max" style="opacity: 0.35;" title="Disabled Resizable"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="align-items: center; justify-content: center; background: #f8fafc;">
            <p style="font-weight: 800; font-size: 1.15rem; color: #1e293b;">
              Selamat Datang di JavaCafe POS
            </p>
            <span style="font-size: 0.8rem; color: #64748b; background: #e2e8f0; padding: 3px 8px; border-radius: 4px;">
              Ukuran Terkunci: 520 x 350 px • Terpusat di Layar
            </span>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi JFrame Kustom dengan Ukuran Terkunci dan Posisi Terpusat</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Urutan Pemanggilan Sangat Penting!</div>
        <p>
          Selalu panggil <code>setLocationRelativeTo(null);</code> <strong>SETELAH</strong> <code>setSize(520, 350);</code>! Jika Anda memanggilnya sebelum <code>setSize</code>, Java menganggap ukuran jendela masih 0x0 pixel, sehingga posisi jendela akan meleset dari titik tengah monitor.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jangan Buat setVisible(true) di Constructor!</div>
        <p>
          Banyak mahasiswa terbiasa menulis <code>setVisible(true);</code> di baris terakhir constructor frame. Kebiasaan ini rawan memicu bug <em>thread race condition</em> pada subclass yang kompleks. Praktik terbaik: panggil <code>app.setVisible(true);</code> dari method <code>main</code> setelah objek frame selesai diinstansiasi secara utuh.
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 2.1</div>
        <p>
          Buatlah kelas baru bernama <code>JendelaKasir</code> yang extends <code>JFrame</code>. Atur judul menjadi <code>"Sistem Kasir Toko Kopi - Meja #01"</code>, dimensi window 500x320 pixel, kunci ukuran agar tidak bisa di-resize, dan pastikan posisinya muncul di tengah layar.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Gunakan pola yang sama persis dengan <code>JendelaUtama.java</code>. Ganti parameter <code>super(...)</code> dengan judul baru dan <code>setSize(500, 320)</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 2</div>
        <ul class="summary-list">
          <li>Pola <code>public class KelasKu extends JFrame</code> adalah standar OOP untuk membangun jendela desktop di Java.</li>
          <li><code>setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)</code> wajib dipasang agar proses JVM benar-benar berhenti saat window ditutup.</li>
          <li><code>setLocationRelativeTo(null)</code> menempatkan jendela di pusat layar secara otomatis.</li>
          <li><code>setResizable(false)</code> menjaga stabilitas tata letak komponen agar tidak berantakan ditarik oleh pengguna.</li>
        </ul>
      </div>

      {nav_buttons('bab-1', 'Bab 1: Pengantar GUI & Event-Driven', 'bab-3', 'Bab 3: Container Modular: JPanel')}
    </article>
    '''

def get_bab3():
    return f'''
    <article class="chapter-article" id="bab-3">
      <div class="chapter-badge">Bab 03 • Arsitektur Modular</div>
      <h1 class="chapter-title">Container Fleksibel dengan JPanel</h1>
      <p class="chapter-lead">
        Mencegah penumpukan kode pada satu file dengan membuat kelas panel khusus (extends JPanel), memahami peran container perantara, serta menghubungkan panel anak dengan frame induk melalui passing referensi constructor (Dependency Injection).
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Memahami perbedaan peran antara top-level container (<code>JFrame</code>) dan intermediate container (<code>JPanel</code>).</li>
          <li>Mendefinisikan kelas komponen modular dengan mewarisi <code>JPanel</code> (<code>extends JPanel</code>).</li>
          <li>Menerapkan teknik passing referensi objek frame induk ke dalam constructor kelas panel anak.</li>
          <li>Menghubungkan interaksi antara panel anak dan frame utama secara bersih tanpa membuat objek duplikat.</li>
        </ul>
      </div>

      <h2>1. Masalah "God Class" pada Pemula GUI</h2>
      <p>
        Kesalahan paling umum yang dilakukan mahasiswa saat pertama kali membuat GUI adalah menaruh <strong>semua hal</strong> di dalam satu file <code>JFrame</code>: deklarasi 50 tombol, 20 label, layouting 3 halaman berbeda, dan semua event listener ditulis berjejal dalam satu file hingga mencapai ribuan baris!
      </p>
      <p>
        Hal ini menciptakan apa yang disebut dalam software engineering sebagai <em>God Class</em> (kelas monster yang serba tahu dan serba mengatur), yang sangat rapuh, sulit dibaca, dan hampir mustahil diperbaiki jika ada bug.
      </p>

      <h2>2. Solusi: Arsitektur Modular Berbasis JPanel</h2>
      <p>
        Solusi elegannya adalah membagi tampilan menjadi modul-modul terpisah:
      </p>
      <ul>
        <li><code>AppFrame.java</code>: Khusus bertindak sebagai bingkai jendela utama dan pengatur alur halaman.</li>
        <li><code>MenuPanel.java</code>: Khusus menangani tampilan katalog menu (turunan dari <code>JPanel</code>).</li>
        <li><code>PesananPanel.java</code>: Khusus menangani formulir detail pesanan dan kustomisasi (turunan dari <code>JPanel</code>).</li>
      </ul>

      <h2>3. Pola Passing Referensi Frame Induk (Dependency Injection)</h2>
      <p>
        Pertanyaan krusial: <em>"Jika panel berada di kelas terpisah, bagaimana tombol di dalam <code>MenuPanel</code> bisa memberitahu <code>AppFrame</code> untuk berpindah halaman atau menampilkan dialog?"</em>
      </p>
      <p>
        Jawabannya: <strong>Kirimkan referensi frame utama lewat parameter constructor panel!</strong>
      </p>
      <p style="background: var(--bg-surface); padding: 0.75rem 1rem; border-left: 3px solid var(--accent); font-family: monospace;">
        // Di dalam MenuPanel.java<br>
        private final AppFrame parentFrame;<br><br>
        public MenuPanel(<strong>AppFrame parentFrame</strong>) {{<br>
        &nbsp;&nbsp;&nbsp;&nbsp;this.parentFrame = parentFrame;<br>
        }}
      </p>
      <p>
        Dengan menyimpan referensi <code>parentFrame</code>, objek panel anak dapat memanggil method publik milik frame kapan saja saat tombol di panel ditekan!
      </p>

      <h2>4. Contoh Kode Implementasi</h2>
      <p>Perhatikan keterhubungan antara kedua kelas di bawah ini:</p>

      {code_box("examples/03_JPanelModular/MenuPanel.java", "MenuPanel.java (Panel Anak)")}

      {code_box("examples/03_JPanelModular/AppFrame.java", "AppFrame.java (Frame Induk)")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 520px; height: 260px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Aplikasi Modular Swing - JavaCafe</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #f1f5f9; padding: 1.5rem; justify-content: space-between;">
            <div>
              <p style="font-weight: 700; font-size: 1.05rem; color: #0f172a; text-align: center;">
                Menu Pilihan JavaCafe
              </p>
              <p style="font-size: 0.88rem; color: #64748b; text-align: center; margin-top: 0.5rem;">
                Silakan klik tombol di bawah untuk pesan:
              </p>
            </div>
            <div style="text-align: center;">
              <button class="swing-btn swing-btn-primary" type="button" style="padding: 0.6rem 1.5rem;">
                Buka Form Pesanan (Pemicu Event ke Parent Frame)
              </button>
            </div>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi MenuPanel yang Berada di Dalam AppFrame</div>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jangan Buat 'new AppFrame()' di Dalam Panel!</div>
        <p>
          Banyak mahasiswa melakukan kesalahan fatal ini: saat ingin memanggil method pada frame utama dari dalam tombol panel, mereka menulis:
          <code>new AppFrame().tampilkanPesan("...");</code>.<br>
          <strong>Dampaknya fatal:</strong> Baris tersebut akan membuat jendela aplikasi baru yang kedua! Gunakan selalu variabel referensi <code>parentFrame</code> yang diterima lewat constructor.
        </p>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Pasang Kata Kunci 'final' pada Field Referensi</div>
        <p>
          Deklarasikan field referensi frame dengan <code>private final AppFrame parentFrame;</code>. Kata kunci <code>final</code> menjamin bahwa referensi tersebut tidak akan sengaja tertimpa objek lain setelah diisi melalui constructor.
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 3.1</div>
        <p>
          Buatlah kelas panel kedua bernama <code>KonfirmasiPanel</code> yang juga <code>extends JPanel</code> dan menerima <code>AppFrame parentFrame</code> di constructor-nya. Tambahkan tombol "Kembali ke Menu Utama" yang saat diklik memanggil method <code>parentFrame.tampilkanPesan("Kembali ke menu!");</code>.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Struktur kelas <code>KonfirmasiPanel</code> persis seperti <code>MenuPanel</code>. Anda hanya perlu mengganti teks label dan tombol aksi serta teks pesan yang dikirimkan.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 3</div>
        <ul class="summary-list">
          <li><code>JPanel</code> berfungsi sebagai intermediate container untuk mengelompokkan elemen antarmuka secara modular.</li>
          <li>Memecah aplikasi menjadi kelas-kelas turunan <code>JPanel</code> (<code>extends JPanel</code>) mencegah terciptanya <em>God Class</em> yang berantakan.</li>
          <li>Teknik <strong>Passing Constructor Reference</strong> memungkinkan panel anak memanggil method kontroler di frame induk secara bersih.</li>
          <li>Jangan pernah membuat instansiasi frame baru (<code>new MainFrame()</code>) di dalam panel anak.</li>
        </ul>
      </div>

      {nav_buttons('bab-2', 'Bab 2: Jendela Pertama: JFrame', 'bab-4', 'Bab 4: Komponen Dasar')}
    </article>
    '''

def get_bab4():
    return f'''
    <article class="chapter-article" id="bab-4">
      <div class="chapter-badge">Bab 04 • Elemen Interaktif</div>
      <h1 class="chapter-title">Komponen Dasar: JLabel, JButton, dan JCheckBox</h1>
      <p class="chapter-lead">
        Menguasai anatomi tiga komponen visual paling esensial dalam aplikasi kasir dan formulir: JLabel (teks dan gambar), JButton (tombol aksi), serta JCheckBox (pilihan add-on independen) lengkap dengan kustomisasi font, warna, dan perataan.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Mengkonfigurasi <code>JLabel</code>: manipulasi teks, font, warna, dan perataan horizontal (<code>SwingConstants</code>).</li>
          <li>Mengkonfigurasi <code>JButton</code>: styling warna latar belakang, warna teks, dan menghilangkan outline focus.</li>
          <li>Menggunakan <code>JCheckBox</code> untuk opsi checklist/add-on yang dapat dipilih secara bebas.</li>
          <li>Membaca status pilihan pengguna dengan method <code>isSelected()</code>.</li>
        </ul>
      </div>

      <h2>1. JLabel: Menampilkan Teks & Keterangan</h2>
      <p>
        <code>JLabel</code> adalah komponen pasif (read-only) yang digunakan untuk menyajikan judul, teks petunjuk, rincian harga, atau gambar status:
      </p>
      <ul>
        <li><code>setText(String text)</code>: Mengubah teks label secara dinamis saat runtime.</li>
        <li><code>setFont(Font font)</code>: Mengatur jenis huruf (font family, style, size), contoh: <code>new Font("Segoe UI", Font.BOLD, 16)</code>.</li>
        <li><code>setForeground(Color color)</code>: Mengubah warna huruf teks.</li>
        <li><code>setHorizontalAlignment(SwingConstants.CENTER)</code>: Mengatur posisi teks (LEFT, CENTER, RIGHT).</li>
      </ul>

      <h2>2. JButton: Tombol Aksi Pengguna</h2>
      <p>
        <code>JButton</code> adalah komponen aktif yang memicu proses komputasi saat diklik oleh pengguna:
      </p>
      <ul>
        <li><code>setBackground(Color color)</code>: Mengatur warna latar belakang tombol.</li>
        <li><code>setForeground(Color color)</code>: Mengatur warna teks di dalam tombol.</li>
        <li><code>setFocusPainted(false)</code>: Menghilangkan garis putus-putus fokus saat tombol diklik (membuat tombol terlihat lebih rapi dan modern).</li>
      </ul>

      <h2>3. JCheckBox: Kotak Centang Opsi Add-on</h2>
      <p>
        <code>JCheckBox</code> adalah kotak pilihan dengan status biner (tercentang / tidak tercentang). Berbeda dengan RadioButton yang hanya mengizinkan memilih 1 opsi dalam grup, <strong>JCheckBox bersifat independen</strong>: pengguna bisa mencentang nol opsi, satu opsi, atau semua opsi sekaligus.
      </p>
      <p>
        Karakteristik inilah yang menjadikannya pilihan sempurna untuk opsi <strong>Add-on / Topping</strong> pada aplikasi pemesanan makanan/minuman kafe!
      </p>
      <ul>
        <li><code>isSelected()</code>: Mengembalikan nilai <code>true</code> jika kotak sedang dicentang, atau <code>false</code> jika kosong.</li>
        <li><code>setSelected(boolean b)</code>: Mengubah status centang secara programatik (sangat berguna untuk fitur Reset Form).</li>
      </ul>

      <h2>4. Contoh Program: KomponenDemo.java</h2>
      <p>Perhatikan deklarasi komponen sebagai atribut kelas dan cara membaca status centang saat tombol diklik:</p>

      {code_box("examples/04_KomponenDasar/KomponenDemo.java", "KomponenDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 480px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Eksplorasi Komponen Dasar Swing</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #f8fafc; padding: 1.5rem; gap: 0.85rem;">
            <p style="font-weight: 700; font-size: 1.05rem; color: #0f172a; text-align: center;">
              Pilihan Kustomisasi Kopi
            </p>
            
            <div class="swing-checkbox-row">
              <span class="swing-checkbox-box checked">✓</span>
              <span>Tambahan Extra Espresso Shot (+Rp 5.000)</span>
            </div>

            <div class="swing-checkbox-row">
              <span class="swing-checkbox-box"></span>
              <span>Ganti ke Susu Oat Plant-Based (+Rp 7.000)</span>
            </div>

            <button class="swing-btn swing-btn-primary" type="button" style="width: 100%; padding: 0.6rem;">
              Konfirmasi Pilihan
            </button>

            <p style="font-size: 0.82rem; font-style: italic; color: #64748b; text-align: center;">
              Pilihan: Extra Shot: Ya | Susu Oat: Tidak
            </p>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Interaksi JLabel, JCheckBox, dan JButton</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Menghilangkan Garis Fokus Tombol</div>
        <p>
          Secara default, Java Swing menampilkan garis putus-putus di sekeliling teks tombol saat tombol aktif. Selalu sertakan perintah:
          <code>button.setFocusPainted(false);</code> agar tombol terlihat bersih menyerupai aplikasi desktop modern.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: JLabel Transparan Secara Default</div>
        <p>
          Jika Anda memanggil <code>label.setBackground(Color.BLUE)</code> namun warna latar label tidak berubah sama sekali, penyebabnya adalah properti <em>opaque</em> (kedap cahaya) pada JLabel bernilai <code>false</code> secara default. Panggil <code>label.setOpaque(true);</code> terlebih dahulu sebelum mewarnai background label!
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 4.1</div>
        <p>
          Tambahkan opsi checkbox ketiga pada form: <code>"Sirup Hazelnut (+Rp 4.000)"</code>. Kemudian modifikasi event tombol agar menampilkan status ketiga opsi tersebut pada label keterangan di bawahnya!
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Deklarasikan <code>private JCheckBox checkHazelnut;</code> di atribut kelas, inisialisasi di <code>initComponents</code>, tambahkan ke <code>mainPanel.add(checkHazelnut)</code>, lalu baca statusnya via <code>checkHazelnut.isSelected()</code> di dalam listener tombol.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 4</div>
        <ul class="summary-list">
          <li><code>JLabel</code> digunakan untuk menyajikan teks informatif dan gambar dengan perataan fleksibel.</li>
          <li><code>JButton</code> adalah pemicu aksi utama yang dapat dikustomisasi warna latar, teks, dan status fokusnya.</li>
          <li><code>JCheckBox</code> adalah kontrol kotak centang independen yang sangat pas untuk fitur penambahan add-on produk.</li>
          <li>Gunakan <code>isSelected()</code> untuk mengecek centang dan <code>setSelected(boolean)</code> untuk mereset status centang.</li>
        </ul>
      </div>

      {nav_buttons('bab-3', 'Bab 3: Container Modular: JPanel', 'bab-5', 'Bab 5: Menangani Gambar: ImageIcon')}
    </article>
    '''

print("chapters_part1.py ready.")
