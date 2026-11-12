# -*- coding: utf-8 -*-
from generator_modules.utils import code_box, nav_buttons

def get_bab10():
    return f'''
    <article class="chapter-article" id="bab-10">
      <div class="chapter-badge">Bab 10 • Feedback Pengguna</div>
      <h1 class="chapter-title">Kotak Dialog Pop-Up dengan JOptionPane</h1>
      <p class="chapter-lead">
        Menampilkan pesan pop-up konfirmasi, peringatan stok, dan pemberitahuan transaksi sukses menggunakan JOptionPane.showMessageDialog, memahami sifat jendela modal, serta menyematkan Custom Icon bergambar produk.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Memahami konsep dialog modal (memblokir interaksi jendela induk hingga di-dismiss).</li>
          <li>Menguasai variasi parameter pada <code>JOptionPane.showMessageDialog()</code>.</li>
          <li>Membedakan tipe pesan: <code>INFORMATION_MESSAGE</code>, <code>WARNING_MESSAGE</code>, <code>ERROR_MESSAGE</code>, dan <code>PLAIN_MESSAGE</code>.</li>
          <li>Menyematkan ikon kustom (<code>ImageIcon</code>) pada kotak dialog sukses.</li>
        </ul>
      </div>

      <h2>1. Apa Itu JOptionPane & Sifat Modal?</h2>
      <p>
        <code>JOptionPane</code> adalah kelas utilitas bawaan Java Swing yang sangat praktis untuk memunculkan kotak dialog standar (pop-up).
      </p>
      <p>
        Secara default, dialog <code>JOptionPane</code> bersifat <strong>Modal</strong>: artinya, saat dialog ini muncul di layar, pengguna <em>tidak bisa</em> mengklik atau berinteraksi dengan jendela utama di belakangnya sampai mereka menekan tombol "OK" atau menutup dialog tersebut. Sifat ini sangat penting untuk memastikan pengguna benar-benar membaca konfirmasi transaksi atau peringatan error!
      </p>

      <h2>2. Anatomi Method showMessageDialog</h2>
      <p>
        Bentuk paling lengkap dari method ini menerima 5 parameter:
      </p>
      <p style="background: var(--bg-surface); padding: 0.75rem 1rem; border-left: 3px solid var(--primary-light); font-family: monospace; font-size: 0.88rem;">
        JOptionPane.showMessageDialog(<br>
        &nbsp;&nbsp;&nbsp;&nbsp;parentComponent,&nbsp;// Jendela induk (biasanya 'this')<br>
        &nbsp;&nbsp;&nbsp;&nbsp;message,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Isi teks pesan konfirmasi (bisa multiline dengan \\n)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;title,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Judul pada title bar dialog pop-up<br>
        &nbsp;&nbsp;&nbsp;&nbsp;messageType,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Jenis ikon standar (INFORMATION, WARNING, ERROR, PLAIN)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;icon&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Objek ImageIcon kustom (opsional)<br>
        );
      </p>

      <h2>3. Contoh Program: DialogDemo.java</h2>
      <p>Perhatikan berbagai variasi jenis dialog dan cara memasang custom icon:</p>

      {code_box("examples/10_DialogJOptionPane/DialogDemo.java", "DialogDemo.java")}

      <!-- Mockup Visual Dialog -->
      <div class="swing-mockup-container">
        <!-- Dialog Pop-up Mockup -->
        <div class="swing-window" style="max-width: 440px; border-radius: 8px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">Order Sukses</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #ffffff; padding: 1.5rem; gap: 1rem;">
            <div style="display: flex; gap: 1rem; align-items: center;">
              <!-- Custom Icon -->
              <div style="width: 52px; height: 52px; background: #1e3a8a; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <span style="font-size: 1.8rem;">☕</span>
              </div>
              <div>
                <p style="font-weight: 700; color: #0f172a; font-size: 0.95rem; margin-bottom: 0.25rem;">
                  Transaksi Pemesanan Kopi Berhasil Disimpan!
                </p>
                <p style="font-size: 0.88rem; color: #64748b;">
                  Total Pembayaran: <strong style="color: #b45309;">Rp 35.000</strong>
                </p>
              </div>
            </div>
            <div style="text-align: right; margin-top: 0.5rem;">
              <button class="swing-btn swing-btn-primary" type="button" style="padding: 0.4rem 1.75rem;">
                OK
              </button>
            </div>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Kotak Dialog Modal "Order Sukses" Lengkap dengan Custom Icon</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Teks Multiline dengan Baris Baru (\n)</div>
        <p>
          Anda dapat membuat pesan pop-up yang terstruktur rapi dengan menyisipkan karakter baris baru <code>\n</code>:
          <code>"Pesanan: Caramel Macchiato\nAdd-on: Extra Shot\nTotal Bayar: Rp 33.000"</code>. JOptionPane secara otomatis merender setiap baris dengan perataan yang rapi.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Hindari Mengisi parentComponent dengan 'null'</div>
        <p>
          Jika Anda menulis <code>JOptionPane.showMessageDialog(null, ...)</code>, kotak dialog akan berpusat di tengah layar monitor secara acak (bukan di atas aplikasi Anda). Lebih buruk lagi, dialog bisa tenggelam di balik jendela aplikasi jika pengguna beralih window! Selalu oper referensi <code>this</code> (objek frame atau panel) sebagai parameter pertama.
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 10.1</div>
        <p>
          Modifikasi dialog pada tombol ke-4 agar menampilkan rincian nama kasir yang melayani serta nomor nota pesanan (misal: <code>"Nota: #INV-2026-001\nKasir: Rizki"</code>).
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Cukup tambahkan teks tersebut ke dalam parameter <code>message</code> dengan concatenasi string atau <code>String.format(...)</code> sebelum memanggil <code>showMessageDialog</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 10</div>
        <ul class="summary-list">
          <li><code>JOptionPane.showMessageDialog</code> adalah cara standar tercepat untuk menampilkan feedback pop-up interaktif.</li>
          <li>Sifat <strong>Modal</strong> memastikan alur transaksi aman karena pengguna wajib menekan tombol sebelum melanjutkan.</li>
          <li>Parameter <code>messageType</code> menentukan ikon dan suara peringatan sistem bawaan.</li>
          <li>Menyematkan <code>ImageIcon</code> kustom memberikan identitas visual brand yang kuat pada dialog sukses transaksi.</li>
        </ul>
      </div>

      {nav_buttons('bab-9', 'Bab 9: Event Handling & ActionListener', 'bab-11', 'Bab 11: Clean Code & Tema Terpusat')}
    </article>
    '''

def get_bab11():
    return f'''
    <article class="chapter-article" id="bab-11">
      <div class="chapter-badge">Bab 11 • Arsitektur Bersih</div>
      <h1 class="chapter-title">Clean Code pada GUI & Sistem Tema Terpusat</h1>
      <p class="chapter-lead">
        Menghilangkan kode GUI yang kusut (spaghetti code) dengan mendeklarasikan komponen sebagai atribut privat, menerapkan inisialisasi bertahap, memecah logika bisnis ke method mandiri, serta membangun kelas utilitas tema (CafeTheme) sebagai Single Source of Truth.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Mendeklarasikan komponen GUI sebagai atribut privat (fields) di bagian atas kelas.</li>
          <li>Membagi proses pembuatan GUI menjadi 3 tahapan: <code>initComponents()</code>, <code>setupLayout()</code>, dan <code>setupEvents()</code>.</li>
          <li>Memecah alur komputasi ke method mandiri (<code>hitungTotal()</code>, <code>resetForm()</code>, <code>prosesCheckout()</code>).</li>
          <li>Membangun kelas utilitas tema dengan konstanta statis (warna brand, tipografi, ukuran jendela).</li>
        </ul>
      </div>

      <h2>1. Anatomi Kelas GUI yang Bersih (Clean Architecture)</h2>
      <p>
        Di awal belajar, mahasiswa kerap mencampur seluruh pembuatan tombol, peletakan panel, logika hitung, dan pesan dialog ke dalam satu method constructor raksasa. Hasilnya: kode menjadi sulit dilacak saat terjadi error!
      </p>
      <p>
        Struktur profesional kelas GUI Swing membagi kelas menjadi 5 zona teratur:
      </p>
      <ol>
        <li><strong>Zona 1 (Fields di Atas):</strong> Deklarasi seluruh komponen visual sebagai <code>private</code> atribut.</li>
        <li><strong>Zona 2 (Constructor Ramping):</strong> Hanya mengatur frame (size, close op, dsb.) dan memanggil method inisialisasi.</li>
        <li><strong>Zona 3 (initComponents):</strong> Khusus memberi warna, font, dan teks awal pada komponen.</li>
        <li><strong>Zona 4 (setupLayout):</strong> Khusus menyusun panel, border, dan hierarki tata letak.</li>
        <li><strong>Zona 5 (setupEvents & Helper Methods):</strong> Khusus menangani listener dan logika perhitungan bisnis.</li>
      </ol>

      <h2>2. Single Source of Truth: Kelas Tema Terpusat</h2>
      <p>
        Bayangkan Anda menulis warna <code>new Color(30, 58, 138)</code> di 20 tempat berbeda di aplikasi Anda. Tiba-tiba klien atau dosen meminta: <em>"Tolong ganti warna tema aplikasinya menjadi hijau hutan!"</em>. Anda terpaksa mencari dan mengedit 20 file satu per satu!
      </p>
      <p>
        Solusinya: <strong>Ciptakan Kelas Utilitas Tema Terpusat!</strong>
        Seluruh warna, font, dan dimensi disimpan sebagai <code>public static final</code> konstanta di satu kelas tunggal.
      </p>

      <h2>3. Contoh Program: CafeTheme.java</h2>
      <p>Kelas utilitas tema terpusat (Design System):</p>

      {code_box("examples/11_CleanCode/CafeTheme.java", "CafeTheme.java")}

      <h2>4. Contoh Program: FormCleanDemo.java</h2>
      <p>Penerapan arsitektur bersih yang mengonsumsi <code>CafeTheme</code>:</p>

      {code_box("examples/11_CleanCode/FormCleanDemo.java", "FormCleanDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 520px; height: 320px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Penerapan Clean Code GUI - JavaCafe</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #f8fafc; padding: 1.25rem; justify-content: space-between;">
            <!-- Header -->
            <div style="text-align: center;">
              <p style="font-weight: 800; color: #1e3a8a; font-size: 1.15rem;">Caramel Macchiato Spesial</p>
              <p style="font-size: 0.85rem; color: #64748b;">Harga Dasar: Rp 25.000</p>
            </div>
            <!-- Options Box -->
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.85rem 1rem; display: flex; flex-direction: column; gap: 0.4rem;">
              <div class="swing-checkbox-row">
                <span class="swing-checkbox-box checked">✓</span>
                <span>Extra Espresso Shot (+Rp 5.000)</span>
              </div>
              <div class="swing-checkbox-row">
                <span class="swing-checkbox-box"></span>
                <span>Upgrade ke Oat Milk (+Rp 6.000)</span>
              </div>
              <p style="font-weight: 800; color: #b45309; text-align: center; font-size: 1rem; margin-top: 0.4rem;">
                Total: Rp 30.000
              </p>
            </div>
            <!-- Buttons -->
            <div style="display: grid; grid-template-columns: 1fr 1fr 1.2fr; gap: 8px;">
              <button class="swing-btn" type="button">Hitung Total</button>
              <button class="swing-btn" type="button">Reset</button>
              <button class="swing-btn swing-btn-primary" type="button">Checkout</button>
            </div>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Tampilan Form yang Menggunakan Palet Tema Konsisten</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Pasang Private Constructor pada Kelas Theme</div>
        <p>
          Perhatikan baris <code>private CafeTheme() {{ }}</code> di kelas <code>CafeTheme</code>. Karena seluruh anggota di dalamnya adalah konstanta <code>static</code>, kita tidak ingin ada programmer yang membuat objek <code>new CafeTheme()</code> secara sia-sia di memori.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jebakan Variabel Komponen Lokal!</div>
        <p>
          Jika Anda menulis <code>JLabel lblJudul = new JLabel("...");</code> di dalam method <code>initComponents()</code> (dengan mencantumkan tipe <code>JLabel</code> di depannya), Anda sedang membuat <strong>variabel lokal baru</strong> yang menutupi atribut kelas! Akibatnya, atribut <code>this.lblJudul</code> tetap bernilai <code>null</code> dan akan melempar <code>NullPointerException</code> saat diakses oleh method lain!
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 11.1</div>
        <p>
          Buka <code>CafeTheme.java</code> dan tambahkan satu konstanta warna aksen baru bernama <code>COLOR_SUCCESS = new Color(34, 197, 94);</code>. Kemudian gunakan warna tersebut sebagai background tombol Checkout!
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Tambahkan field static di <code>CafeTheme</code>, lalu di <code>FormCleanDemo.java</code> ubah baris styling tombol checkout menjadi: <code>btnCheckout.setBackground(CafeTheme.COLOR_SUCCESS);</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 11</div>
        <ul class="summary-list">
          <li>Deklarasikan seluruh komponen GUI sebagai atribut privat (fields) di level kelas.</li>
          <li>Pisahkan inisialisasi menjadi tahapan: <code>initComponents</code>, <code>setupLayout</code>, dan <code>setupEvents</code>.</li>
          <li>Pecah alur bisnis ke method pembantu (<code>hitungTotal</code>, <code>resetForm</code>, <code>prosesCheckout</code>).</li>
          <li>Gunakan kelas utilitas tema statis terpusat untuk menjaga konsistensi visual dan kemudahan perawatan kode.</li>
        </ul>
      </div>

      {nav_buttons('bab-10', 'Bab 10: Dialog Pop-Up: JOptionPane', 'bab-12', 'Bab 12: Kalkulasi Harga & Format Rupiah')}
    </article>
    '''

def get_bab12():
    return f'''
    <article class="chapter-article" id="bab-12">
      <div class="chapter-badge">Bab 12 • Logika Bisnis Kasir</div>
      <h1 class="chapter-title">Pola Perhitungan Harga & Format Mata Uang Rupiah</h1>
      <p class="chapter-lead">
        Menguasai pola komputasi kasir: akumulasi harga dasar produk ditambah opsi add-on dinamis, memformat angka integer ke format mata uang Rupiah standar Indonesia, serta mereset formulir kembali ke kondisi awal.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Menerapkan pola kalkulasi: <code>Total = Harga Dasar + Σ(Biaya Add-on Tercentang)</code>.</li>
          <li>Memformat bilangan numerik ke format mata uang Rupiah Indonesia (<code>Locale.forLanguageTag("id-ID")</code>).</li>
          <li>Membuat fitur Reset Formulir yang mengembalikan seluruh kontrol ke status default.</li>
          <li>Menyajikan rincian total transaksi secara dinamis pada label antarmuka.</li>
        </ul>
      </div>

      <h2>1. Pola Akumulasi Harga Kasir</h2>
      <p>
        Pola kalkulasi kasir pada aplikasi pemesanan bekerja secara kumulatif:
      </p>
      <ol>
        <li>Mulai dengan nilai <strong>Harga Dasar</strong> produk utama.</li>
        <li>Periksa setiap <code>JCheckBox</code> add-on menggunakan <code>isSelected()</code>.</li>
        <li>Jika tercentang, tambahkan biaya add-on tersebut ke variabel penampung total.</li>
        <li>Format angka total akhir menjadi teks Rupiah dan tampilkan ke <code>JLabel</code>.</li>
      </ol>

      <h2>2. Memformat Angka Menjadi Mata Uang Rupiah</h2>
      <p>
        Jangan pernah menampilkan angka mentah <code>28000</code> ke pengguna kasir! Antarmuka yang ramah pengguna selalu menyajikan angka dalam format mata uang: <code>Rp28.000,00</code> atau <code>Rp 28.000</code>.
      </p>
      <p>Ada dua pendekatan standar di Java:</p>

      <h3>Pendekatan A: Menggunakan NumberFormat (Standar Java Internasional)</h3>
      <p style="background: var(--bg-surface); padding: 0.65rem 1rem; border-left: 3px solid var(--primary-light); font-family: monospace;">
        NumberFormat nf = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("id-ID"));<br>
        String teksRupiah = nf.format(35000); // Hasil: "Rp35.000,00"
      </p>

      <h3>Pendekatan B: Menggunakan String.format (Kustom Tanpa Koma Desimal)</h3>
      <p style="background: var(--bg-surface); padding: 0.65rem 1rem; border-left: 3px solid var(--accent); font-family: monospace;">
        String teksRupiah = String.format("Rp %,d", 35000).replace(',', '.'); // Hasil: "Rp 35.000"
      </p>

      <h2>3. Pola Reset Formulir</h2>
      <p>
        Setelah pesanan berhasil disimpan, formulir harus dikembalikan ke kondisi default agar kasir siap melayani transaksi berikutnya:
      </p>
      <ul>
        <li>Seluruh checkbox add-on dimatikan: <code>chk.setSelected(false);</code>.</li>
        <li>Label ringkasan total dikembalikan ke harga dasar awal.</li>
      </ul>

      <h2>4. Contoh Program: KasirHitungDemo.java</h2>
      <p>Berikut adalah implementasi lengkap kalkulator kasir kopi:</p>

      {code_box("examples/12_KalkulasiRupiah/KasirHitungDemo.java", "KasirHitungDemo.java")}

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 500px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Pola Perhitungan & Format Rupiah - JavaCafe</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #f8fafc; padding: 1.25rem; gap: 0.75rem;">
            <div style="text-align: center;">
              <p style="font-weight: 800; color: #1e3a8a; font-size: 1.05rem;">Pemesanan: Ice Cafe Latte</p>
              <p style="font-size: 0.85rem; color: #64748b;">Harga Dasar: Rp22.000,00</p>
            </div>

            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.85rem; display: flex; flex-direction: column; gap: 0.35rem;">
              <div class="swing-checkbox-row">
                <span class="swing-checkbox-box checked">✓</span>
                <span>Extra Espresso Shot (+ Rp5.000,00)</span>
              </div>
              <div class="swing-checkbox-row">
                <span class="swing-checkbox-box"></span>
                <span>Caramel Drizzle (+ Rp4.000,00)</span>
              </div>
              <div class="swing-checkbox-row">
                <span class="swing-checkbox-box checked">✓</span>
                <span>Topping Vanilla Ice Cream (+ Rp8.000,00)</span>
              </div>
              <p style="font-weight: 800; color: #d97706; text-align: right; font-size: 1rem; margin-top: 0.5rem;">
                Total Saat Ini: Rp35.000,00
              </p>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr 1.3fr; gap: 8px;">
              <button class="swing-btn" type="button">Hitung Total</button>
              <button class="swing-btn" type="button">Reset</button>
              <button class="swing-btn swing-btn-primary" type="button">Simpan Order</button>
            </div>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Kalkulasi Harga Kasir dengan Format Mata Uang Rupiah Standar Indonesia</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Simpan Angka Asli di Variabel int / long</div>
        <p>
          Simpan selalu data harga dalam bentuk tipe data numerik asli (<code>int harga = 22000;</code>). Format teks mata uang hanya boleh dibuat pada saat Anda hendak mencetaknya ke <code>JLabel</code> atau <code>JOptionPane</code>.
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jangan Parse String dari Label!</div>
        <p>
          Jangan pernah mencoba menghitung harga dengan cara mengambil teks dari label (<code>label.getText()</code>), lalu menghapus tulisan "Rp" dan tanda titik dengan regex, lalu di-<code>Integer.parseInt</code>. Itu adalah anti-pattern yang sangat rapuh dan mudah melempar <code>NumberFormatException</code>!
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 12.1</div>
        <p>
          Tambahkan fitur diskon: jika total transaksi mencapai atau melebihi <strong>Rp 30.000</strong>, berikan potongan diskon langsung sebesar 10%! Tampilkan nominal diskon tersebut pada dialog konfirmasi saat tombol simpan ditekan.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Di method <code>hitungTotal()</code>, setelah menjumlahkan add-on, tambahkan pengecekan: <code>if (subtotal >= 30000) total = subtotal - (int)(subtotal * 0.10);</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 12</div>
        <ul class="summary-list">
          <li>Pola kalkulasi harga mengakumulasikan harga dasar dengan biaya masing-masing add-on yang tercentang.</li>
          <li>Gunakan <code>NumberFormat.getCurrencyInstance(Locale.forLanguageTag("id-ID"))</code> untuk format Rupiah otomatis.</li>
          <li>Metode <code>resetForm()</code> mengembalikan status centang dan teks harga ke nilai awal.</li>
          <li>Pertahankan data numerik di atribut angka; ubah ke string hanya saat rendering UI.</li>
        </ul>
      </div>

      {nav_buttons('bab-11', 'Bab 11: Clean Code & Tema Terpusat', 'bab-13', 'Bab 13: Menerjemahkan UML ke Java Swing')}
    </article>
    '''

def get_bab13():
    return f'''
    <article class="chapter-article" id="bab-13">
      <div class="chapter-badge">Bab 13 • Rekayasa Perangkat Lunak</div>
      <h1 class="chapter-title">Membaca & Menerjemahkan UML Class Diagram ke Java Swing</h1>
      <p class="chapter-lead">
        Menghilangkan keraguan saat membaca soal praktikum: memahami anatomi diagram kelas UML, simbol visibilitas access modifier, tipe data atribut komponen GUI, relasi inheritance (extends) dan dependency, serta menyusun kerangka kode (skeleton).
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Membaca tiga kompartemen utama dalam kotak kelas UML (Nama, Atribut, Method).</li>
          <li>Menerjemahkan simbol visibilitas UML (<code>+</code>, <code>-</code>, <code>#</code>) ke access modifier Java.</li>
          <li>Mengidentifikasi relasi pewarisan (Inheritance) dan ketergantungan (Dependency) antar-kelas.</li>
          <li>Menyusun kerangka kode Java (skeleton) yang presisi dari diagram UML sebelum menulis logika detail.</li>
        </ul>
      </div>

      <h2>1. Mengapa Praktikum Menggunakan Diagram UML?</h2>
      <p>
        Dalam rekayasa perangkat lunak, <strong>Unified Modeling Language (UML) Class Diagram</strong> adalah bahasa visual universal arsitek software. Diagram ini mendokumentasikan spesifikasi kelas secara ringkas: apa saja atributnya, method apa yang harus disediakan, serta bagaimana hubungan antar-kelas.
      </p>

      <h2>2. Tabel Kamus Penerjemahan Simbol UML ke Java</h2>
      <table style="width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.92rem;">
        <thead>
          <tr style="background: var(--primary-subtle); border-bottom: 2px solid var(--primary-border);">
            <th style="padding: 0.75rem; text-align: left;">Notasi UML</th>
            <th style="padding: 0.75rem; text-align: left;">Arti / Makna</th>
            <th style="padding: 0.75rem; text-align: left;">Sintaks Kode Java</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 700; color: #ef4444;">- nama: Tipe</td>
            <td style="padding: 0.65rem;">Visibilitas Private</td>
            <td style="padding: 0.65rem; font-family: monospace;">private Tipe nama;</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 700; color: #22c55e;">+ aksi(): Tipe</td>
            <td style="padding: 0.65rem;">Visibilitas Public</td>
            <td style="padding: 0.65rem; font-family: monospace;">public Tipe aksi() {{ ... }}</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 700; color: #f59e0b;"># data: Tipe</td>
            <td style="padding: 0.65rem;">Visibilitas Protected</td>
            <td style="padding: 0.65rem; font-family: monospace;">protected Tipe data;</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 700;"><u>namaStatic</u></td>
            <td style="padding: 0.65rem;">Garis Bawah = Static</td>
            <td style="padding: 0.65rem; font-family: monospace;">public static ...</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 700;">Panah Segitiga Kosong</td>
            <td style="padding: 0.65rem;">Generalization / Inheritance</td>
            <td style="padding: 0.65rem; font-family: monospace;">public class Anak extends Induk</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 0.65rem; font-family: monospace; font-weight: 700;">Panah Putus-putus</td>
            <td style="padding: 0.65rem;">Dependency (Menggunakan kelas lain)</td>
            <td style="padding: 0.65rem; font-family: monospace;">Menerima objek kelas lain di method/constructor</td>
          </tr>
        </tbody>
      </table>

      <h2>3. Studi Kasus: Diagram UML TiketKafeApp</h2>
      <p>Perhatikan spesifikasi UML di bawah ini:</p>

      <pre style="background: var(--bg-surface); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: monospace; font-size: 0.88rem; line-height: 1.5;">
┌──────────────────────────────────────────────┐
│                 TiketKafeApp                 │
├──────────────────────────────────────────────┤
│ - judulEvent: String                         │
│ - hargaTiket: int                            │
│ - lblInfo: JLabel                            │
│ - btnBeli: JButton                           │
├──────────────────────────────────────────────┤
│ + TiketKafeApp()                             │
│ - initUI(): void                             │
│ + pesanTiket(): void                         │
│ + main(args: String[]): void                 │
└──────────────────────────────────────────────┘
                     │
                     ▼ extends
             ┌───────────────┐
             │    JFrame     │
             └───────────────┘
      </pre>

      <h2>4. Hasil Penerjemahan Kode: TiketKafeApp.java</h2>
      <p>Berikut adalah hasil terjemahan diagram di atas menjadi implementasi kode Java yang valid:</p>

      {code_box("examples/13_UMLToCode/TiketKafeApp.java", "TiketKafeApp.java")}

      <div class="callout callout-tip">
        <div class="callout-header">💡 Buat Kerangka Skeleton Terlebih Dahulu!</div>
        <p>
          Saat mengerjakan soal jurnal atau ujian berbasis UML: tulis seluruh nama kelas, deklarasi atribut dengan tipe datanya, dan kerangka method kosong (return default) terlebih dahulu. Setelah kerangka kelas bebas error kompilasi, barulah isi logika method satu per satu!
        </p>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 13.1</div>
        <p>
          Jika pada UML tertulis: <code>- chkMembership: JCheckBox</code> dan <code>+ hitungTotal(): int</code>, tuliskan bagaimana baris tersebut diterjemahkan ke dalam Java secara tepat!
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Tanda minus (<code>-</code>) berarti <code>private JCheckBox chkMembership;</code> dan tanda plus (<code>+</code>) berarti <code>public int hitungTotal() {{ ... }}</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 13</div>
        <ul class="summary-list">
          <li>Kotak kelas UML memuat: Nama Kelas di atas, Atribut di tengah, dan Method di bawah.</li>
          <li>Simbol <code>-</code> berarti <code>private</code>, sedangkan simbol <code>+</code> berarti <code>public</code>.</li>
          <li>Panah segitiga tertutup menunjukkan hubungan <strong>Inheritance</strong> (<code>extends</code>).</li>
          <li>Menyusun skeleton kerangka kode terlebih dahulu menjamin struktur program Anda 100% patuh pada spesifikasi soal.</li>
        </ul>
      </div>

      {nav_buttons('bab-12', 'Bab 12: Kalkulasi Harga & Format Rupiah', 'bab-14', 'Bab 14: Panduan Debugging & Error Populer')}
    </article>
    '''

def get_bab14():
    return f'''
    <article class="chapter-article" id="bab-14">
      <div class="chapter-badge">Bab 14 • Troubleshooting</div>
      <h1 class="chapter-title">Panduan Debugging & Mengatasi Error Populer Swing</h1>
      <p class="chapter-lead">
        Daftar diagnosis cepat dan solusi praktis untuk lima kesalahan paling umum yang dialami praktikan saat membuat aplikasi GUI Swing: NullPointerException, komponen gaib, tombol tidak merespon, layout bertumpuk, dan gambar hilang.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Mendiagnosis dan memperbaiki <code>NullPointerException</code> pada komponen GUI.</li>
          <li>Mengatasi masalah komponen tidak muncul di layar (invisible component).</li>
          <li>Mencari penyebab tombol yang dapat ditekan tetapi tidak memicu reaksi apapun.</li>
          <li>Memperbaiki layout yang menimpa atau membuat komponen gepeng.</li>
        </ul>
      </div>

      <h2>Tabel Diagnosis Error Populer & Solusi Cepat</h2>

      <div style="display: flex; flex-direction: column; gap: 1.5rem; margin: 2rem 0;">
        
        <!-- Error 1 -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #ef4444; border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: #ef4444; font-size: 1.05rem;">
            💥 1. java.lang.NullPointerException saat Menjalankan Program
          </h3>
          <p><strong>Gejala:</strong> Program langsung crash merah di console saat pertama kali dijalankan atau saat sebuah method dipanggil.</p>
          <p><strong>Penyebab Utama:</strong> Komponen sudah dideklarasikan di atribut kelas (misal: <code>private JLabel lblTotal;</code>), tetapi Anda lupa menginisialisasinya dengan kata kunci <code>new</code> (<code>lblTotal = new JLabel(...)</code>) sebelum memanggil method-nya seperti <code>lblTotal.setText(...)</code>.</p>
          <p style="background: var(--callout-tip-bg); padding: 0.5rem 0.75rem; border-radius: 4px; color: var(--callout-tip-text); font-size: 0.88rem;">
            <strong>Solusi:</strong> Periksa nomor baris crash di stack trace terminal. Pastikan objek tersebut sudah di-<code>new</code> terlebih dahulu sebelum baris tersebut dieksekusi.
          </p>
        </div>

        <!-- Error 2 -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #f59e0b; border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: #d97706; font-size: 1.05rem;">
            👻 2. Komponen Gaib (Sudah Dibuat tapi Tidak Tampil di Layar)
          </h3>
          <p><strong>Gejala:</strong> Tidak ada error merah di console, tetapi tombol atau checkbox yang Anda buat tidak tampak sama sekali di jendela aplikasi.</p>
          <p><strong>Penyebab Utama:</strong> Anda sudah menginstansiasi komponen dengan <code>new JButton(...)</code>, tetapi Anda <strong>lupa menambahkannya ke dalam container</strong> menggunakan method <code>add(komponen)</code>!</p>
          <p style="background: var(--callout-tip-bg); padding: 0.5rem 0.75rem; border-radius: 4px; color: var(--callout-tip-text); font-size: 0.88rem;">
            <strong>Solusi:</strong> Pastikan setiap komponen yang diinisialisasi dipanggil dengan <code>panel.add(komponen)</code> atau <code>add(komponen)</code>.
          </p>
        </div>

        <!-- Error 3 -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #3b82f6; border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: #1e3a8a; font-size: 1.05rem;">
            🔇 3. Tombol Bisu (Dapat Diklik tapi Tidak Ada Reaksi Apapun)
          </h3>
          <p><strong>Gejala:</strong> Tombol tampak normal di antarmuka, bisa ditekan secara visual, tetapi perhitungan tidak berjalan dan tidak ada dialog pop-up yang muncul.</p>
          <p><strong>Penyebab Utama:</strong> Anda sudah membuat method logika perhitungan, tetapi lupa menyambungkannya ke tombol melalui <code>btn.addActionListener(...)</code>.</p>
          <p style="background: var(--callout-tip-bg); padding: 0.5rem 0.75rem; border-radius: 4px; color: var(--callout-tip-text); font-size: 0.88rem;">
            <strong>Solusi:</strong> Tambahkan baris <code>btnSimpan.addActionListener(e -> prosesSimpan());</code> di method inisialisasi event Anda.
          </p>
        </div>

        <!-- Error 4 -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #8b5cf6; border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: #6d28d9; font-size: 1.05rem;">
            🥞 4. Layout Gepeng atau Komponen Saling Menimpa
          </h3>
          <p><strong>Gejala:</strong> Tombol tampak melebar satu layar penuh, atau tombol pertama menghilang saat tombol kedua ditambahkan.</p>
          <p><strong>Penyebab Utama:</strong> Anda memasukkan beberapa komponen ke dalam <code>BorderLayout</code> tanpa menentukan posisi (sehingga semuanya menumpuk di <code>CENTER</code> secara default) atau menaruh lebih dari satu komponen ke region yang sama.</p>
          <p style="background: var(--callout-tip-bg); padding: 0.5rem 0.75rem; border-radius: 4px; color: var(--callout-tip-text); font-size: 0.88rem;">
            <strong>Solusi:</strong> Masukkan komponen-komponen tersebut ke dalam sebuah <code>JPanel</code> yang menggunakan <code>FlowLayout</code> atau <code>GridLayout</code> terlebih dahulu, baru kemudian masukkan panel tersebut ke BorderLayout!
          </p>
        </div>

        <!-- Error 5 -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #ec4899; border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: #be185d; font-size: 1.05rem;">
            🖼️ 5. Gambar ImageIcon Tidak Muncul di Komputer Lain
          </h3>
          <p><strong>Gejala:</strong> Gambar muncul saat dijalankan di komputer Anda, namun hilang saat proyek dijalankan di laptop asisten.</p>
          <p><strong>Penyebab Utama:</strong> Penggunaan path absolut (<code>C:\\Users\\...</code>) atau kesalahan letak direktori kerja (working directory) saat IDE mengeksekusi program.</p>
          <p style="background: var(--callout-tip-bg); padding: 0.5rem 0.75rem; border-radius: 4px; color: var(--callout-tip-text); font-size: 0.88rem;">
            <strong>Solusi:</strong> Gunakan path relatif (<code>assets/img/kopi.png</code>) dan letakkan folder <code>assets/</code> sejajar dengan root folder proyek Anda.
          </p>
        </div>

      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 14</div>
        <ul class="summary-list">
          <li><code>NullPointerException</code> selalu berarti Anda mencoba menggunakan objek yang belum di-<code>new</code>.</li>
          <li>Komponen tidak akan muncul di layar jika Anda lupa memanggil <code>container.add(komponen)</code>.</li>
          <li>Tombol tidak akan merespon jika tidak didaftarkan ke <code>addActionListener</code>.</li>
          <li>Gunakan selalu <strong>Nested Panel</strong> untuk mencegah komponen saling menimpa pada <code>BorderLayout</code>.</li>
        </ul>
      </div>

      {nav_buttons('bab-13', 'Bab 13: Menerjemahkan UML ke Java Swing', 'cheatsheet', 'Evaluasi: Cheat Sheet Ringkas')}
    </article>
    '''

print("chapters_part3.py ready.")
