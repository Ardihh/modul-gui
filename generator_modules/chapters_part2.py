# -*- coding: utf-8 -*-
from generator_modules.utils import code_box, nav_buttons

def get_bab5():
    return f'''
    <article class="chapter-article" id="bab-5">
      <div class="chapter-badge">Bab 05 • Aset Multimedia</div>
      <h1 class="chapter-title">Menangani Gambar dengan ImageIcon</h1>
      <p class="chapter-lead">
        Menampilkan logo dan foto produk ke dalam antarmuka GUI, mengatur struktur folder aset dengan path relatif yang aman, melakukan penskalaan (resize) gambar secara proporsional, serta menghindari jebakan umum gambar hilang.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Memahami cara kerja kelas <code>ImageIcon</code> dan integrasinya dengan <code>JLabel</code>.</li>
          <li>Mengelola path relatif file gambar pada struktur proyek Java desktop.</li>
          <li>Menggunakan method <code>Image.getScaledInstance()</code> dengan algoritma <code>SCALE_SMOOTH</code>.</li>
          <li>Mengidentifikasi dan mengatasi penyebab gambar tidak tampil di layar.</li>
        </ul>
      </div>

      <h2>1. Anatomi Menampilkan Gambar di Java Swing</h2>
      <p>
        Di Swing, tidak ada komponen khusus bernama <em>JImage</em>. Gambar ditampilkan dengan cara memasukkan objek <code>ImageIcon</code> ke dalam sebuah <code>JLabel</code> menggunakan method <code>label.setIcon(icon)</code> atau melalui constructor label: <code>new JLabel(icon)</code>.
      </p>

      <h2>2. Jebakan Path Relatif vs Path Absolut</h2>
      <p>
        Salah satu kesalahan paling sering yang membuat program gagal saat diuji oleh asisten adalah penggunaan <strong>Path Absolut</strong>:
      </p>
      <p style="background: var(--callout-warn-bg); padding: 0.65rem 1rem; border-left: 3px solid var(--callout-warn-border); font-family: monospace; color: var(--callout-warn-text);">
        // ❌ SALAH BESAR (Hanya jalan di laptop Anda sendiri!):<br>
        ImageIcon icon = new ImageIcon("C:\\\\Users\\\\NamaAnda\\\\Documents\\\\proyek\\\\kopi.png");
      </p>
      <p>
        Saat kode tersebut dijalankan di laptop asisten atau komputer laboratorium, program langsung gagal memuat gambar karena path tersebut tidak ada!
      </p>
      <p>
        Gunakan selalu <strong>Path Relatif</strong> terhadap direktori kerja (working directory) proyek:
      </p>
      <p style="background: var(--callout-tip-bg); padding: 0.65rem 1rem; border-left: 3px solid var(--callout-tip-border); font-family: monospace; color: var(--callout-tip-text);">
        // ✅ BENAR (Berjalan di komputer manapun):<br>
        ImageIcon icon = new ImageIcon("assets/img/coffee.png");
      </p>

      <h2>3. Melakukan Penskalaan (Resize) Gambar</h2>
      <p>
        File gambar mentah dari kamera atau desainer sering kali memiliki resolusi besar (misal 1024x1024 pixel). Jika langsung dimasukkan ke JLabel di jendela berukuran 520x350, gambar akan memakan seluruh layar jendela!
      </p>
      <p>
        Kita perlu mengecilkannya secara proporsional melalui 3 langkah berurutan:
      </p>
      <ol>
        <li>Ambil objek <code>Image</code> dari ImageIcon mentah: <code>Image rawImage = iconAsli.getImage();</code>.</li>
        <li>Skala ukurannya: <code>Image scaledImage = rawImage.getScaledInstance(100, 100, Image.SCALE_SMOOTH);</code>.</li>
        <li>Bungkus kembali ke ImageIcon baru: <code>ImageIcon finalIcon = new ImageIcon(scaledImage);</code>.</li>
      </ol>

      <h2>4. Contoh Program: GambarDemo.java</h2>
      <p>Berikut adalah implementasi lengkap yang dilengkapi penanganan graceful jika file tidak ditemukan:</p>

      {code_box("examples/05_ImageIconDemo/GambarDemo.java", "GambarDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 520px; height: 260px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Demo Menampilkan Gambar dengan ImageIcon</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #ffffff; align-items: center; justify-content: center; gap: 0.75rem;">
            <div style="width: 80px; height: 80px; background: #1e3a8a; border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
              <span style="font-size: 2.5rem;">☕</span>
            </div>
            <p style="font-weight: 700; font-size: 0.95rem; color: #0f172a;">
              Ikon Kopi Berhasil Dimuat
            </p>
            <p style="font-size: 0.82rem; color: #64748b; font-style: italic;">
              Contoh gambar produk JavaCafe POS
            </p>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Gambar Ter-skala Halus di Dalam JLabel</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Gunakan Algoritma Image.SCALE_SMOOTH</div>
        <p>
          Java menyediakan beberapa algoritma scaling seperti <code>SCALE_FAST</code>, <code>SCALE_DEFAULT</code>, dan <code>SCALE_SMOOTH</code>. Selalu pilih <strong>SCALE_SMOOTH</strong> karena menghasilkan interpolasi tepi gambar yang anti-aliasing sehingga teks dan lekukan gambar tetap tajam dan tidak pecah bergerigi.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: ImageIcon Gagal Tidak Melempar Exception!</div>
        <p>
          Salah satu perilaku membingungkan dari <code>new ImageIcon(path)</code> adalah: jika file gambar tidak ditemukan di harddisk, Java <strong>TIDAK akan melempar exception merah di console</strong>! Akibatnya, pemula mengira programnya berjalan normal, padahal labelnya kosong melompong. Selalu periksa keberadaan file dengan <code>new File(path).exists()</code> seperti pada contoh kode.
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 5.1</div>
        <p>
          Simpan sebuah gambar logo kecil berformat PNG ke dalam folder <code>assets/img/</code> di proyek Anda. Buat kelas yang menampilkan gambar tersebut dengan ukuran 64x64 pixel serta teks nama produk tepat di bawah gambar menggunakan perataan <code>label.setVerticalTextPosition(SwingConstants.BOTTOM)</code>.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Gunakan method <code>label.setHorizontalTextPosition(SwingConstants.CENTER)</code> dan <code>label.setVerticalTextPosition(SwingConstants.BOTTOM)</code> pada objek JLabel setelah menyematkan icon.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 5</div>
        <ul class="summary-list">
          <li>Gambar di Java Swing dimuat menggunakan kelas <code>ImageIcon</code> dan disematkan ke dalam <code>JLabel</code>.</li>
          <li>Hindari path absolut; gunakan selalu <strong>Path Relatif</strong> (seperti <code>assets/img/...</code>) agar portabel di semua komputer.</li>
          <li>Gunakan <code>Image.getScaledInstance(w, h, Image.SCALE_SMOOTH)</code> untuk mereduksi ukuran gambar agar pas dengan jendela.</li>
          <li>Periksa selalu eksistensi file dengan <code>File.exists()</code> karena <code>ImageIcon</code> tidak melempar exception saat path salah.</li>
        </ul>
      </div>

      {nav_buttons('bab-4', 'Bab 4: Komponen Dasar', 'bab-6', 'Bab 6: Menguasai Layout Manager')}
    </article>
    '''

def get_bab6():
    return f'''
    <article class="chapter-article" id="bab-6">
      <div class="chapter-badge">Bab 06 • Tata Letak Responsif</div>
      <h1 class="chapter-title">Menguasai Layout Manager & Nested Panels</h1>
      <p class="chapter-lead">
        Memahami filosofi Layout Manager dalam mengontrol posisi dan ukuran komponen secara otomatis, menguasai tiga layout utama (BorderLayout, GridLayout, FlowLayout), dan menerapkan teknik Nested Layout (panel di dalam panel).
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Memahami kelemahan fatal Absolute Layout (<code>setLayout(null)</code>).</li>
          <li>Menguasai karakteristik <code>BorderLayout</code>, <code>GridLayout</code>, dan <code>FlowLayout</code>.</li>
          <li>Menerapkan arsitektur <em>Nested Layout</em> untuk merancang antarmuka profesional.</li>
          <li>Menentukan pilihan layout yang tepat sesuai kebutuhan struktur layar.</li>
        </ul>
      </div>

      <h2>1. Mengapa Kita Tidak Boleh Menggunakan 'null layout'?</h2>
      <p>
        Banyak tutorial jadul mengajarkan mahasiswa menggunakan <code>setLayout(null);</code> lalu menaruh komponen dengan koordinat manual: <code>komponen.setBounds(x, y, width, height);</code>.
      </p>
      <p>
        <strong>Mengapa Absolute Layout dilarang di dunia nyata?</strong>
      </p>
      <ul>
        <li>Setiap sistem operasi (Windows vs macOS vs Linux) memiliki ketebalan font dan rendering tombol yang berbeda beberapa pixel. Koordinat kaku yang terlihat rapi di laptop Anda bisa menjadi terpotong atau teks terpotong di laptop asisten!</li>
        <li>Sulit dirawat: jika Anda ingin menyisipkan satu baris baru di tengah form, Anda terpaksa menghitung ulang koordinat Y untuk seluruh komponen di bawahnya!</li>
      </ul>
      <p>
        Sebagai gantinya, Java menyediakan <strong>Layout Manager</strong>: objek manajer yang secara cerdas dan otomatis mengatur ukuran dan penataan komponen.
      </p>

      <h2>2. Tiga Layout Manager Fundamental</h2>

      <!-- Visual Layout Grid Diagram -->
      <div class="layout-diagram">
        <div style="font-weight: 700; font-size: 0.85rem; color: var(--primary); text-align: center; margin-bottom: 0.5rem;">
          Diagram Region BorderLayout
        </div>
        <div class="layout-border-grid">
          <div class="layout-cell layout-cell-north">NORTH (Header / Judul)</div>
          <div class="layout-cell layout-cell-west">WEST<br>(Sidebar)</div>
          <div class="layout-cell layout-cell-center">CENTER<br>(Konten Utama / Membesar Otomatis)</div>
          <div class="layout-cell layout-cell-east">EAST<br>(Opsi)</div>
          <div class="layout-cell layout-cell-south">SOUTH (Tombol Aksi / Footer)</div>
        </div>
      </div>

      <h3>A. BorderLayout (Default pada JFrame)</h3>
      <p>
        Membagi kontainer menjadi 5 zona: <code>NORTH</code>, <code>SOUTH</code>, <code>EAST</code>, <code>WEST</code>, dan <code>CENTER</code>.
        Karakteristik penting: Area <code>CENTER</code> akan otomatis meregang mengisi seluruh sisa ruang kosong yang tidak ditempati oleh keempat sisi lainnya.
      </p>

      <h3>B. GridLayout</h3>
      <p>
        Membagi kontainer menjadi matriks baris dan kolom yang berukuran seragam persis sama rata: <code>new GridLayout(rows, cols, hgap, vgap)</code>.
        Sangat cocok untuk formulir bertingkat (misal kolom label di kiri dan input di kanan) atau katalog produk berpetak.
      </p>

      <h3>C. FlowLayout (Default pada JPanel)</h3>
      <p>
        Menyusun komponen mengalir berurutan dari kiri ke kanan layaknya kata-kata dalam satu baris paragraf: <code>new FlowLayout(alignment, hgap, vgap)</code>.
        Sangat cocok untuk deretan tombol aksi di bagian bawah layar (misal tombol Batal dan Simpan).
      </p>

      <h2>3. Rahasia Desain GUI Profesional: Nested Layout</h2>
      <p>
        Sebuah layar aplikasi modern jarang sekali hanya menggunakan satu layout manager tunggal. Kunci menciptakan tampilan yang rapi adalah <strong>Nested Layout (Panel Bersarang di dalam Panel)</strong>:
      </p>
      <ul>
        <li><strong>Root Container:</strong> Menggunakan <code>BorderLayout</code>.</li>
        <li><strong>Bagian Atas (NORTH):</strong> Diberi <code>JLabel</code> header.</li>
        <li><strong>Bagian Tengah (CENTER):</strong> Diberi <code>JPanel</code> dengan <code>GridLayout</code> berisi menu pilihan.</li>
        <li><strong>Bagian Bawah (SOUTH):</strong> Diberi <code>JPanel</code> dengan <code>FlowLayout</code> berisi tombol navigasi/aksi.</li>
      </ul>

      <h2>4. Contoh Program: LayoutDemo.java</h2>
      <p>Pelajari bagaimana ketiga layout manager diintegrasikan secara harmonis:</p>

      {code_box("examples/06_LayoutManager/LayoutDemo.java", "LayoutDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 520px; height: 310px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Eksplorasi Layout Manager & Nested Panels</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #f1f5f9; padding: 0.75rem; justify-content: space-between; gap: 0.5rem;">
            <!-- North -->
            <div style="background: #1e3a8a; color: white; font-weight: 700; text-align: center; padding: 0.5rem; border-radius: 4px; font-size: 0.88rem;">
              JavaCafe POS - Nested Layout Demo (BorderLayout.NORTH)
            </div>
            <!-- Center Grid 2x2 -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; flex: 1; padding: 0.5rem 0;">
              <div class="swing-btn" style="height: auto; text-align: center;">1. Espresso (Rp 18.000)</div>
              <div class="swing-btn" style="height: auto; text-align: center;">2. Americano (Rp 20.000)</div>
              <div class="swing-btn" style="height: auto; text-align: center;">3. Caffe Latte (Rp 24.000)</div>
              <div class="swing-btn" style="height: auto; text-align: center;">4. Caramel Macchiato (Rp 28.000)</div>
            </div>
            <!-- South FlowLayout -->
            <div style="display: flex; justify-content: flex-end; gap: 8px; background: #e2e8f0; padding: 0.5rem; border-radius: 4px;">
              <button class="swing-btn" type="button">Batal</button>
              <button class="swing-btn swing-btn-accent" type="button">Lanjut ke Pembayaran ➔</button>
            </div>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Nested Layout: BorderLayout menampung GridLayout di Tengah dan FlowLayout di Bawah</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Menentukan Gap (Jarak Antar Komponen)</div>
        <p>
          Constructor layout manager menerima parameter jarak horizontal dan vertikal: <code>new BorderLayout(8, 8)</code> atau <code>new GridLayout(2, 2, 8, 8)</code>. Manfaatkan gap ini agar antar tombol atau panel tidak saling berhimpitan tanpa spasi.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Menimpa Komponen di BorderLayout</div>
        <p>
          Ingat: Setiap region di <code>BorderLayout</code> (North, South, East, West, Center) hanya dapat diisi oleh <strong>satu komponen tunggal</strong>! Jika Anda memanggil <code>add(btn1, BorderLayout.NORTH)</code> lalu memanggil <code>add(btn2, BorderLayout.NORTH)</code>, maka tombol kedua akan menimpa dan menghilangkan tombol pertama. Selalu bungkus ke dalam <code>JPanel</code> terlebih dahulu jika ingin menaruh lebih dari satu elemen.
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 6.1</div>
        <p>
          Ubah grid menu pada <code>LayoutDemo.java</code> dari 2x2 menjadi 3x1 (3 baris, 1 kolom) dan tambahkan tombol aksi ketiga di panel bawah bernama "Simpan Draf".
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Ubah inisialisasi grid menjadi <code>new GridLayout(3, 1, 8, 8)</code>, lalu tambahkan <code>actionPanel.add(new JButton("Simpan Draf"));</code> sebelum tombol Lanjut.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 6</div>
        <ul class="summary-list">
          <li>Hindari Absolute Layout (<code>null</code> layout) karena rentan rusak saat dijalankan di resolusi atau OS yang berbeda.</li>
          <li><code>BorderLayout</code> membagi 5 wilayah arah mata angin dengan area <code>CENTER</code> yang ekspansif.</li>
          <li><code>GridLayout</code> mengatur grid matriks dengan proporsi sel yang presisi dan sama rata.</li>
          <li>Kombinasi <strong>Nested Layout</strong> (panel di dalam panel) adalah standar industri untuk membangun UI yang kokoh dan rapi.</li>
        </ul>
      </div>

      {nav_buttons('bab-5', 'Bab 5: Menangani Gambar: ImageIcon', 'bab-7', 'Bab 7: Navigasi Halaman: CardLayout')}
    </article>
    '''

def get_bab7():
    return f'''
    <article class="chapter-article" id="bab-7">
      <div class="chapter-badge">Bab 07 • Navigasi Layar Tunggal</div>
      <h1 class="chapter-title">Navigasi Halaman dengan CardLayout</h1>
      <p class="chapter-lead">
        Memahami arsitektur kartu bertumpuk untuk berpindah antar-halaman secara mulus di dalam satu jendela JFrame berukuran tetap, mendaftarkan panel halaman dengan key unik, dan mengontrol navigasi bolak-balik dari berbagai kelas.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Menjelaskan konsep kerja <code>CardLayout</code> sebagai tumpukan kartu visual.</li>
          <li>Mendaftarkan panel-panel halaman ke kontainer utama menggunakan kunci String pengenal.</li>
          <li>Melakukan perpindahan halaman maju dan mundur menggunakan method <code>cardLayout.show()</code>.</li>
          <li>Menyediakan method pengendali publik pada frame agar navigasi dapat dipicu dari tombol di dalam panel anak.</li>
        </ul>
      </div>

      <h2>1. Mengapa Multi-Window Pop-up Dihindari?</h2>
      <p>
        Saat pemula ingin membuat aplikasi yang memiliki Halaman 1 (Katalog) dan Halaman 2 (Form Pesanan), mereka kerap membuat dua <code>JFrame</code> terpisah: saat tombol diklik, jendela 1 ditutup dan jendela 2 dibuka secara melompat (pop-up baru).
      </p>
      <p>
        Pendekatan tersebut menghasilkan pengalaman pengguna yang buruk: layar berkedip, posisi jendela melompat-lompat di monitor, dan memakan resource ganda.
      </p>
      <p>
        Standar aplikasi modern adalah <strong>Single Window Application</strong>: jendela aplikasi tetap satu (misal berukuran tetap 520x350 pixel), namun isi halamannya berganti secara mulus di tempat. Inilah fungsi utama dari <strong>CardLayout</strong>!
      </p>

      <h2>2. Cara Kerja CardLayout: Analogi Setumpuk Kartu</h2>
      <p>
        Bayangkan setumpuk kartu remi atau kartu flashcard:
      </p>
      <ul>
        <li>Seluruh kartu bertumpuk di posisi yang sama persis di atas meja.</li>
        <li>Hanya ada <strong>satu kartu teratas</strong> yang tampak oleh mata kita pada satu waktu.</li>
        <li>Setiap kartu diberi nama pengenal (label nama unik).</li>
        <li>Ketika kita memerintahkan: <em>"Tampilkan kartu bernama 'DETAIL'!"</em>, manajer kartu akan menyembunyikan kartu aktif dan mengangkat kartu 'DETAIL' ke permukaan.</li>
      </ul>

      <h2>3. Tiga Langkah Penggunaan CardLayout</h2>
      <ol>
        <li>
          <strong>Inisialisasi Container & CardLayout:</strong><br>
          <code>CardLayout cardLayout = new CardLayout();</code><br>
          <code>JPanel containerKartu = new JPanel(cardLayout);</code>
        </li>
        <li>
          <strong>Daftarkan Panel Halaman dengan Nama Unik:</strong><br>
          <code>containerKartu.add(panelKatalog, "KATALOG");</code><br>
          <code>containerKartu.add(panelPesanan, "PESANAN");</code>
        </li>
        <li>
          <strong>Beralih Kartu Saat Tombol Diklik:</strong><br>
          <code>cardLayout.show(containerKartu, "PESANAN");</code>
        </li>
      </ol>

      <h2>4. Contoh Program: NavigasiCardDemo.java</h2>
      <p>Simak bagaimana kedua halaman dapat saling beralih bolak-balik tanpa membuat jendela baru:</p>

      {code_box("examples/07_CardLayout/NavigasiCardDemo.java", "NavigasiCardDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div style="display: flex; gap: 1rem; width: 100%; max-width: 600px; flex-wrap: wrap; justify-content: center;">
          <!-- Kartu 1 -->
          <div class="swing-window" style="flex: 1; min-width: 270px; height: 230px;">
            <div class="swing-titlebar">
              <span class="swing-titlebar-title">Kartu 1: MENU</span>
            </div>
            <div class="swing-body" style="background: #f0f9ff; justify-content: space-between; text-align: center;">
              <div>
                <p style="font-weight: 700; color: #0369a1; font-size: 0.95rem;">Halaman Katalog</p>
                <p style="font-size: 0.8rem; color: #64748b; margin-top: 0.3rem;">Pilih menu kopi favorit Anda.</p>
              </div>
              <button class="swing-btn swing-btn-primary" type="button" style="font-size: 0.78rem;">
                Buka Detail Pesanan ➔
              </button>
            </div>
          </div>

          <!-- Kartu 2 -->
          <div class="swing-window" style="flex: 1; min-width: 270px; height: 230px;">
            <div class="swing-titlebar">
              <span class="swing-titlebar-title">Kartu 2: DETAIL</span>
            </div>
            <div class="swing-body" style="background: #fffbeb; justify-content: space-between; text-align: center;">
              <div>
                <p style="font-weight: 700; color: #b45309; font-size: 0.95rem;">Halaman Detail</p>
                <p style="font-size: 0.8rem; color: #64748b; margin-top: 0.3rem;">Form kustomisasi add-on pesanan.</p>
              </div>
              <button class="swing-btn swing-btn-accent" type="button" style="font-size: 0.78rem;">
                ⬅ Kembali ke Katalog
              </button>
            </div>
          </div>
        </div>
        <div class="mockup-caption">Ilustrasi Dua Kartu yang Bergantian Tampil di Dalam Satu JFrame yang Sama</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Gunakan Konstanta public static final String</div>
        <p>
          Jangan menulis nama kartu berupa string mentah (magic string) secara berulang-ulang seperti <code>"DETAIL"</code> di banyak tempat. Ciptakan konstanta:
          <code>public static final String HALAMAN_MENU = "MENU";</code>. Dengan begitu, IDE akan otomatis mendeteksi jika terjadi kesalahan ketik (typo).
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Parameter Pertama cardLayout.show()</div>
        <p>
          Salah satu kesalahan paling klasik mahasiswa: menulis <code>cardLayout.show(this, "NAMA");</code> di mana <code>this</code> adalah objek JFrame. Ingat: parameter pertama dari <code>cardLayout.show(container, name)</code> <strong>HARUS berupa panel penampung CardLayout</strong> (objek <code>containerKartu</code>), BUKAN objek JFrame!
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 7.1</div>
        <p>
          Tambahkan halaman ketiga bernama <code>"SUKSES"</code> yang menampilkan ucapan selamat "Transaksi Berhasil Selesai!" dan sebuah tombol "Mulai Transaksi Baru" yang akan membawa pengguna kembali ke kartu <code>"MENU"</code>.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Buat method <code>buatPanelSukses()</code> yang mereturn <code>JPanel</code>, lalu daftarkan ke <code>containerKartu.add(panelSukses, "SUKSES");</code>. Pasang listener tombol agar memanggil <code>tampilkanHalaman(HALAMAN_MENU)</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 7</div>
        <ul class="summary-list">
          <li><code>CardLayout</code> adalah solusi arsitektur terbaik untuk aplikasi desktop multi-halaman dalam satu jendela tunggal.</li>
          <li>Setiap halaman didaftarkan ke container penampung menggunakan kunci String identitas.</li>
          <li>Perpindahan halaman dieksekusi melalui <code>cardLayout.show(container, namaKunci)</code>.</li>
          <li>Menerapkan konstanta statis untuk nama kartu mencegah bug sulit lacak akibat kesalahan penulisan string.</li>
        </ul>
      </div>

      {nav_buttons('bab-6', 'Bab 6: Menguasai Layout Manager', 'bab-8', 'Bab 8: Kerapian Tampilan: Border')}
    </article>
    '''

def get_bab8():
    return f'''
    <article class="chapter-article" id="bab-8">
      <div class="chapter-badge">Bab 08 • Estetika & Spasi</div>
      <h1 class="chapter-title">Kerapian Tampilan dengan Swing Border</h1>
      <p class="chapter-lead">
        Menghilangkan tampilan antarmuka yang sempit dan menabrak batas layar menggunakan BorderFactory, menerapkan EmptyBorder untuk menciptakan ruang napas (padding/margin), serta menggabungkan border garis dengan CompoundBorder.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Memahami peran penting ruang kosong (whitespace/padding) dalam kenyamanan visual UI.</li>
          <li>Menggunakan <code>BorderFactory.createEmptyBorder()</code> untuk memberikan padding/margin.</li>
          <li>Menggunakan <code>BorderFactory.createLineBorder()</code> untuk garis pembatas kartu produk.</li>
          <li>Mengkombinasikan border luar dan bantalan dalam dengan <code>BorderFactory.createCompoundBorder()</code>.</li>
        </ul>
      </div>

      <h2>1. Masalah "Komponen Menabrak Dinding"</h2>
      <p>
        Secara default, komponen yang dimasukkan ke dalam <code>JFrame</code> atau <code>JPanel</code> akan menempel ketat tepat di tepi batas piksel terluar. Teks menabrak pinggir bingkai, tombol bersentuhan dengan dinding kaca jendela, dan layout terlihat sesak serta tidak profesional.
      </p>
      <p>
        Di dunia desain UI, kita membutuhkan <strong>Padding</strong> (ruang napas di dalam batas elemen) dan <strong>Margin</strong> (ruang napas di luar batas elemen). Di Java Swing, kedua hal ini dicapai melalui kelas <strong>Border</strong>!
      </p>

      <h2>2. Ragam Border Populer dari BorderFactory</h2>
      <p>
        Java menyediakan kelas utilitas <code>BorderFactory</code> dengan metode statis siap pakai:
      </p>
      <ul>
        <li>
          <strong>EmptyBorder (Bantalan Tak Kasat Mata):</strong><br>
          <code>BorderFactory.createEmptyBorder(top, left, bottom, right)</code><br>
          Border ini tidak menggambar garis apapun, melainkan memberikan ruang kosong transparan (padding) di sekeliling komponen.
        </li>
        <li>
          <strong>LineBorder (Garis Tepi):</strong><br>
          <code>BorderFactory.createLineBorder(Color.LIGHT_GRAY, 1)</code><br>
          Menggambar garis batas tipis yang rapi untuk memisahkan kartu konten.
        </li>
        <li>
          <strong>CompoundBorder (Border Majemuk):</strong><br>
          <code>BorderFactory.createCompoundBorder(garisLuar, bantalanDalam)</code><br>
          Trik sakti profesional: menggabungkan garis tepi di luar dengan ruang padding di dalam sehingga isi teks tidak menempel ke garis!
        </li>
      </ul>

      <h2>3. Contoh Program: BorderDemo.java</h2>
      <p>Perhatikan bagaimana penambahan sedikit border mengubah tampilan aplikasi menjadi jauh lebih elegan:</p>

      {code_box("examples/08_BorderDemo/BorderDemo.java", "BorderDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 480px; height: 260px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Penerapan Border & Padding - JavaCafe</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-max"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <!-- Body dengan EmptyBorder 20px sekeliling -->
          <div class="swing-body" style="background: #f8fafc; padding: 1.25rem; justify-content: space-between;">
            <!-- Kartu dengan LineBorder + EmptyBorder -->
            <div style="background: #ffffff; border: 2px solid #cbd5e1; border-radius: 4px; padding: 0.85rem 1rem;">
              <p style="font-weight: 700; font-size: 0.95rem; color: #0f172a;">
                Espresso Roast Single Origin
              </p>
              <p style="font-size: 0.8rem; color: #64748b; margin-top: 0.2rem;">
                Perpaduan arabika gayo dengan aroma karamel pekat.
              </p>
              <p style="font-weight: 700; color: #b45309; font-size: 0.9rem; margin-top: 0.4rem;">
                Harga: Rp 22.000
              </p>
            </div>
            <!-- Tombol Bawah -->
            <button class="swing-btn swing-btn-primary" type="button" style="padding: 0.65rem;">
              Pilih Menu Ini
            </button>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi EmptyBorder pada Root Panel dan CompoundBorder pada Kartu Produk</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Urutan Parameter createEmptyBorder</div>
        <p>
          Ingat urutan putaran jarum jam saat memasukkan nilai: <strong>(Atas, Kiri, Bawah, Kanan)</strong> atau dalam bahasa Inggris: <code>(top, left, bottom, right)</code>.
          Rumus umum yang pas untuk root panel aplikasi kasir adalah: <code>BorderFactory.createEmptyBorder(15, 20, 15, 20);</code>.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jangan Lupa Import yang Benar!</div>
        <p>
          Kelas <code>BorderFactory</code> berada di paket <code>javax.swing.BorderFactory</code>, sedangkan interface <code>Border</code> berada di paket <code>javax.swing.border.Border</code>. Pastikan kedua import ini terpasang dengan benar di file Java Anda.
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 8.1</div>
        <p>
          Eksperimenkan modifikasi pada kartu kopi di <code>BorderDemo.java</code>: ubah warna garis tepi menjadi warna biru tema (<code>new Color(30, 58, 138)</code>) dengan ketebalan 3 pixel, dan tingkatkan bantalan dalam menjadi 20 pixel di setiap sisi.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Ubah baris <code>Border garisLuar = BorderFactory.createLineBorder(new Color(30, 58, 138), 3);</code> dan <code>Border bantalanDalam = BorderFactory.createEmptyBorder(20, 20, 20, 20);</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 8</div>
        <ul class="summary-list">
          <li>Spasi visual (whitespace) adalah elemen krusial untuk estetika dan kemudahan pembacaan antarmuka.</li>
          <li><code>createEmptyBorder(t, l, b, r)</code> memberikan bantalan padding transparan agar komponen tidak menabrak bingkai.</li>
          <li><code>createLineBorder(color, thickness)</code> menggambar batas garis tepi yang tegas dan rapi.</li>
          <li><code>createCompoundBorder(outer, inner)</code> adalah teknik standar untuk menciptakan kartu berbingkai yang memiliki ruang napas di bagian dalamnya.</li>
        </ul>
      </div>

      {nav_buttons('bab-7', 'Bab 7: Navigasi Halaman: CardLayout', 'bab-9a', 'Bab 09A: Fondasi & 4 Gaya Listener')}
    </article>
    '''

from generator_modules.chapters_events import get_bab9a, get_bab9b, get_bab9c

print("chapters_part2.py ready.")
