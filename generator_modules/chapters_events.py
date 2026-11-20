# -*- coding: utf-8 -*-
from generator_modules.utils import code_box, nav_buttons

def get_bab9a():
    return f'''
    <article class="chapter-article" id="bab-9a">
      <div class="chapter-badge">Bab 09A • Fondasi Event Handling</div>
      <h1 class="chapter-title">Fondasi Event Handling & 4 Gaya Penulisan Listener</h1>
      <p class="chapter-lead">
        Memahami Event-Driven Architecture sebagai penerapan nyata konsep Interface dan Polimorfisme OOP, membedah siklus kejadian (Event Model), mengekstrak informasi Event Object, serta membandingkan 4 gaya penulisan listener pada satu kasus yang sama.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Menjelaskan hubungan arsitektur Event Handling Swing dengan materi <strong>Interface & Polimorfisme</strong> (Modul 2).</li>
          <li>Menguraikan siklus <strong>Event Model</strong>: <em>Event Source</em>, <em>Event Object</em>, dan <em>Event Listener</em>.</li>
          <li>Mengekstrak informasi penting dari objek event: <code>getSource()</code>, <code>getActionCommand()</code>, koordinat, dan tombol keyboard.</li>
          <li>Mengimplementasikan 4 gaya penulisan listener pada satu kasus penghitung porsi kopi kafe.</li>
          <li>Mengelola banyak tombol dengan satu listener terpusat secara aman.</li>
        </ul>
      </div>

      <h2>1. Model Event: Analogi Bel Pintu Kafe</h2>
      <p>
        Pada aplikasi konsol prosedural (CLI), program berjalan secara diktator: program menentukan kapan giliran membaca input dan kapan mencetak output. Pada GUI, pengguna memegang kendali penuh. Program berada dalam kondisi pasif "mendengarkan" hingga terjadi suatu interaksi.
      </p>
      <p>
        Mekanisme ini bekerja melalui <strong>Tripartit Event Model</strong>:
      </p>
      <ul>
        <li>
          <strong>1. Event Source (Sumber Kejadian):</strong> Komponen visual yang disentuh pengguna, misalnya saklar bel pintu di depan kafe (objek <code>JButton</code>).
        </li>
        <li>
          <strong>2. Event Object (Informasi Kejadian):</strong> Saat saklar ditekan, sistem secara otomatis membungkus semua fakta kejadian ke dalam sebuah objek (misalnya <code>ActionEvent</code>). Objek ini memuat: siapa yang menekan, jam berapa, tombol apa yang ditekan, dsb.
        </li>
        <li>
          <strong>3. Event Listener (Pendengar Kejadian):</strong> Barista di dalam kafe yang telinganya siap mendengar bel pintu. Begitu sinyal tiba, barista segera bergerak membuatkan pesanan (method <code>actionPerformed()</code> dieksekusi).
        </li>
      </ul>

      <!-- SVG Event Flow Diagram -->
      <div class="event-flow-diagram">
        <div style="font-weight: 700; font-size: 0.95rem; color: var(--primary); text-align: center;">
          Siklus Arsitektur Event Dispatching di Java Swing
        </div>
        <div class="event-flow-steps">
          <div class="flow-step-node active-step">
            <div class="flow-step-num">Langkah 1</div>
            <div class="flow-step-title">Pengguna (User)</div>
            <div class="flow-step-desc">Klik tombol / Tekan keyboard</div>
          </div>
          <div class="flow-arrow-icon">&rarr;</div>
          <div class="flow-step-node">
            <div class="flow-step-num">Langkah 2</div>
            <div class="flow-step-title">Event Source</div>
            <div class="flow-step-desc">JButton / JTextField membuat Event Object</div>
          </div>
          <div class="flow-arrow-icon">&rarr;</div>
          <div class="flow-step-node">
            <div class="flow-step-num">Langkah 3</div>
            <div class="flow-step-title">Event Queue (EDT)</div>
            <div class="flow-step-desc">JVM antrekan event di Dispatch Thread</div>
          </div>
          <div class="flow-arrow-icon">&rarr;</div>
          <div class="flow-step-node active-step">
            <div class="flow-step-num">Langkah 4</div>
            <div class="flow-step-title">Event Listener</div>
            <div class="flow-step-desc">Method interface listener dipanggil</div>
          </div>
        </div>
      </div>

      <h2>2. Hubungan dengan OOP: Listener Adalah Interface!</h2>
      <p>
        Banyak pemula mengira <code>addActionListener</code> adalah "mantra ajaib". Padahal, ini adalah <strong>penerapan murni dari materi Interface & Polimorfisme</strong> yang telah Anda pelajari pada Modul 2!
      </p>
      <div class="callout callout-info">
        <div class="callout-header">💡 Mengapa Java Swing Menggunakan Interface untuk Event?</div>
        <p>
          Bayangkan jika Java menggunakan pewarisan kelas (<em>Inheritance</em>) untuk listener: karena Java hanya mendukung *Single Inheritance*, kelas <code>MainFrame</code> Anda tidak akan bisa mewarisi <code>JFrame</code> sekaligus mewarisi <code>ButtonListener</code>!
        </p>
        <p>
          Dengan menggunakan <strong>Interface</strong> (<em>Observer Pattern</em>):
        </p>
        <ul style="margin-bottom: 0;">
          <li><strong>Loose Coupling (Keterikatan Longgar):</strong> Tombol <code>JButton</code> tidak perlu tahu siapa yang mendengarkannya. Ia hanya tahu: <em>"Siapapun objek yang mendaftar ke saya asalkan mengimplementasikan kontrak interface <code>ActionListener</code>, saya jamin akan memanggil method <code>actionPerformed()</code>-nya saat saya diklik!"</em></li>
          <li><strong>Multiple Implementations:</strong> Satu kelas window di Java bebas mengimplementasikan 3, 5, atau 10 interface listener sekaligus (misal: <code>implements ActionListener, ItemListener, WindowListener</code>).</li>
        </ul>
      </div>

      <h2>3. Anatomi Objek Event: Menggali Informasi Aksi</h2>
      <p>
        Method pada interface listener selalu menerima parameter berupa objek event (misal <code>ActionEvent e</code>, <code>MouseEvent e</code>, <code>KeyEvent e</code>). Objek ini membawa method-method sakti:
      </p>
      <ul>
        <li><code>e.getSource()</code>: Mengembalikan referensi objek komponen pemancar aksi (bertipe <code>Object</code>). Dapat dibandingkan dengan operator <code>==</code> untuk mendeteksi komponen mana yang diklik: <code>if (e.getSource() == btnPesan)</code>.</li>
        <li><code>e.getActionCommand()</code>: Mengembalikan teks perintah (String). Secara default bernilai sama dengan teks pada tombol, kecuali diubah via <code>btn.setActionCommand("KODE_AKSI")</code>.</li>
        <li><code>e.getX()</code> dan <code>e.getY()</code>: (Pada <code>MouseEvent</code>) Mengembalikan titik koordinat piksel kursor mouse saat aksi berlangsung.</li>
        <li><code>e.getKeyChar()</code> dan <code>e.getKeyCode()</code>: (Pada <code>KeyEvent</code>) Mengetahui karakter huruf atau kode tombol hardware keyboard yang ditekan.</li>
      </ul>

      <h2>4. Empat Cara Menulis Listener pada Kasus yang Sama</h2>
      <p>
        Mari kita pelajari 4 cara berbeda dalam mengimplementasikan <code>ActionListener</code> pada satu studi kasus kecil yang identik: <strong>Counter Penambahan Porsi Kopi Espresso JavaCafe</strong>.
      </p>

      {code_box("examples/09_EventHandling/EmpatGayaListenerDemo.java", "EmpatGayaListenerDemo.java")}

      <h2>5. Matriks Perbandingan 4 Gaya Penulisan Listener</h2>
      <div style="overflow-x: auto;">
        <table class="matrix-table">
          <thead>
            <tr>
              <th>Gaya Penulisan</th>
              <th>Kelebihan</th>
              <th>Kekurangan</th>
              <th>Kapan Tepat Digunakan?</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Named Class (Kelas Terpisah)</strong></td>
              <td>Dapat digunakan ulang (reusable) di banyak tempat; memisahkan tampilan dengan logika bisnis secara tegas.</td>
              <td>Butuh mengoper referensi frame lewat constructor; file kode bertambah banyak.</td>
              <td>Logika aksi sangat panjang, rumit, atau perlu dipakai oleh beberapa form berbeda.</td>
            </tr>
            <tr>
              <td><strong>2. Implements di Frame (this)</strong></td>
              <td>Semua penanganan tombol terpusat di satu method <code>actionPerformed()</code>; tidak memakan alokasi objek baru.</td>
              <td>Method <code>actionPerformed()</code> menjadi sarang blok <code>if-else</code> panjang jika tombolnya ada puluhan.</td>
              <td>Form kasir sederhana dengan 2–4 tombol aksi terpusat.</td>
            </tr>
            <tr>
              <td><strong>3. Anonymous Inner Class</strong></td>
              <td>Logika aksi berada tepat di samping komponen tombol yang relevan; kompatibel di Java versi lama (Java 7 ke bawah).</td>
              <td>Sintaks bertele-tele (boilerplate code) dengan deklarasi kelas dan override method.</td>
              <td>Proyek warisan Java lama atau listener yang memiliki lebih dari 1 method abstract.</td>
            </tr>
            <tr>
              <td><strong>4. Lambda Expression & Method Ref</strong></td>
              <td><strong>Paling ringkas, modern, dan ekspresif.</strong> Mengeliminasi baris kode boilerplate; mudah dibaca.</td>
              <td>Hanya bisa digunakan pada <em>Functional Interface</em> (interface dengan tepat 1 abstract method).</td>
              <td><strong>Rekomendasi Utama Standar Modern (Java 8+)</strong> untuk aksi tombol 1–5 baris.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-tip">
        <div class="callout-header">💡 Rekomendasi Asisten untuk Praktikan</div>
        <p>
          Gunakan <strong>Gaya 4 (Lambda Expression)</strong> untuk aksi tombol ringkas: <code>btn.addActionListener(e -> hitungTotal());</code>. Jika aksi membutuhkan pengecekan banyak kondisi, buat method pembantu (seperti <code>hitungTotal()</code>) lalu panggil method tersebut dari dalam lambda!
        </p>
      </div>

      <h2>6. Satu Listener Melayani Banyak Tombol: getSource() vs getActionCommand()</h2>
      <p>
        Jika Anda menggunakan Gaya 2 (atau satu lambda untuk beberapa tombol), Anda perlu membedakan tombol mana yang sedang ditekan:
      </p>

      <div class="code-wrapper">
        <div class="code-header">
          <span class="file-name">Pembedaan Sumber Aksi</span>
        </div>
        <pre><code class="language-java">// CARA 1: Menggunakan getSource() (Membandingkan referensi objek komponen)
if (e.getSource() == btnTambah) {{
    tambahPorsi();
}} else if (e.getSource() == btnReset) {{
    resetPorsi();
}}

// CARA 2: Menggunakan getActionCommand() (Membandingkan string perintah)
String cmd = e.getActionCommand();
if ("TAMBAH".equals(cmd)) {{
    tambahPorsi();
}} else if ("RESET".equals(cmd)) {{
    resetPorsi();
}}</code></pre>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header">⚠️ Awas: Jebakan == vs .equals() pada String!</div>
        <p>
          <strong>Jangan pernah menulis:</strong> <code>if (e.getActionCommand() == "TAMBAH")</code>!<br>
          Operator <code>==</code> di Java membandingkan alamat memori (referensi objek). Jika String berasal dari input runtime yang berbeda, kondisi tersebut akan bernilai <code>false</code> meskipun teksnya bertuliskan "TAMBAH"!<br>
          <strong>Gunakan selalu:</strong> <code>"TAMBAH".equals(e.getActionCommand())</code>.
        </p>
      </div>

      <!-- Mockup Visual -->
      <div class="swing-mockup-container">
        <div class="swing-window" style="max-width: 520px; height: 320px;">
          <div class="swing-titlebar">
            <span class="swing-titlebar-title">☕ Perbandingan 4 Gaya Penulisan Listener - JavaCafe</span>
            <div class="swing-window-controls">
              <span class="swing-ctrl-dot swing-ctrl-min"></span>
              <span class="swing-ctrl-dot swing-ctrl-close"></span>
            </div>
          </div>
          <div class="swing-body" style="background: #f8fafc; padding: 1rem; justify-content: space-between;">
            <div style="background: #1e3a8a; color: white; border-radius: 6px; padding: 0.6rem; text-align: center;">
              <span style="font-size: 0.85rem; opacity: 0.9;">Pemesanan Espresso Shot</span><br>
              <strong style="font-size: 1.35rem; color: #fbbf24;">Total Porsi: 4 Cup</strong>
            </div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              <button class="swing-btn" type="button">1. Tambah via Named Class (Kelas Terpisah)</button>
              <button class="swing-btn" type="button">2. Tambah via Implements Frame (this)</button>
              <button class="swing-btn" type="button">3. Tambah via Anonymous Inner Class</button>
              <button class="swing-btn swing-btn-primary" type="button">4. Tambah via Lambda Expression (e -> ...)</button>
              <button class="swing-btn" type="button" style="background: #ef4444; color: white; border-color: #ef4444;">5. Reset Porsi via Method Reference</button>
            </div>
            <div style="font-size: 0.78rem; color: #64748b; font-style: italic; text-align: center;">
              Pemicu Terakhir: Gaya 4 (Lambda Expression)
            </div>
          </div>
        </div>
        <div class="mockup-caption">Visualisasi Tampilan Program EmpatGayaListenerDemo.java</div>
      </div>

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 9A.1</div>
        <p>
          Tambahkan tombol keenam pada <code>EmpatGayaListenerDemo.java</code> bernama <code>btnKurang</code> (Kurang 1 Porsi). Implementasikan tombol tersebut menggunakan <strong>Gaya 4 (Lambda Expression)</strong> dengan aturan: porsi tidak boleh berkurang di bawah 0!
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Tambahkan <code>JButton btnKurang = new JButton("Kurangi Porsi");</code>. Pasang listener:
            <code>btnKurang.addActionListener(e -> {{ if (jumlahPorsi > 0) {{ jumlahPorsi--; perbaruiLabelCounter(); }} }});</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 09A</div>
        <ul class="summary-list">
          <li>Event Handling di Swing adalah implementasi nyata dari <strong>Interface & Observer Pattern</strong> di OOP.</li>
          <li>Tripartit Event: <strong>Event Source</strong> (pemancar), <strong>Event Object</strong> (fakta kejadian), dan <strong>Event Listener</strong> (penanganan aksi).</li>
          <li>Empat gaya penulisan: Named Class, Implements Frame, Anonymous Inner Class, dan <strong>Lambda Expression</strong> (rekomendasi modern).</li>
          <li>Selalu gunakan <code>.equals()</code> saat membandingkan teks string pada <code>getActionCommand()</code>.</li>
        </ul>
      </div>

      {nav_buttons('bab-8', 'Bab 8: Kerapian Tampilan: Border', 'bab-9b', 'Bab 09B: Katalog Listener & Adapter')}
    </article>
    '''

def get_bab9b():
    return f'''
    <article class="chapter-article" id="bab-9b">
      <div class="chapter-badge">Bab 09B • Katalog Interface</div>
      <h1 class="chapter-title">Katalog Lengkap Interface Listener & Adapter Class</h1>
      <p class="chapter-lead">
        Menjelajahi ragam interface listener untuk berbagai interaksi pengguna: perubahan status item, gestur mouse, ketikan keyboard, fokus kursor, pergeseran slider, hingga siklus hidup jendela, serta bagaimana Adapter Class membebaskan kita dari penulisan method kosong.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Menguasai 10 interface listener esensial di Swing beserta komponen pasangannya.</li>
          <li>Membedakan status seleksi pada <code>ItemListener</code> via <code>ItemEvent.SELECTED</code> vs <code>DESELECTED</code>.</li>
          <li>Menangkap gestur fisik pengguna menggunakan <code>MouseListener</code>, <code>MouseMotionListener</code>, dan <code>KeyListener</code>.</li>
          <li>Memahami fungsi dan cara kerja <strong>Adapter Classes</strong> (<code>MouseAdapter</code>, <code>KeyAdapter</code>, <code>WindowAdapter</code>, <code>FocusAdapter</code>).</li>
        </ul>
      </div>

      <h2>1. Mengapa Ada Banyak Jenis Listener di Java Swing?</h2>
      <p>
        Setiap komponen visual memiliki jenis interaksi yang berbeda:
        Sebuah tombol diklik (Action), sebuah kotak centang diubah statusnya (Item), kursor mouse melintas di atas gambar (Mouse), atau pengguna mengetik angka di kolom input (Key/Document).
        Karena itu, Java Swing menyediakan antarmuka spesifik untuk masing-masing kebutuhan.
      </p>

      <h2>2. Katalog Interface Listener Esensial</h2>

      <!-- Sub-bab 1: ActionListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>🔘</span> 1. ActionListener (Aksi Penekanan Utama)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Saat pengguna menekan tombol <code>JButton</code>, menekan tombol <strong>Enter</strong> di <code>JTextField</code>, memilih menu di <code>JMenuItem</code>, atau memilih opsi di <code>JComboBox</code>.</p>
        <p><strong>Daftar Method:</strong> Hanya memiliki 1 method: <code>void actionPerformed(ActionEvent e)</code>.</p>
        <div class="code-wrapper">
          <pre><code class="language-java">// Menangani aksi Enter pada kolom pencarian
txtCari.addActionListener(e -> {{
    String kataKunci = txtCari.getText();
    System.out.println("Mencari menu: " + kataKunci);
}});</code></pre>
        </div>
        <p style="color: var(--callout-warn-text); font-size: 0.85rem; margin-bottom: 0;">
          <strong>⚠️ Jebakan Umum:</strong> Lupa memanggil <code>addActionListener</code> sehingga tombol terasa bisu dan tidak merespon saat diklik.
        </p>
      </div>

      <!-- Sub-bab 2: ItemListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>☑️</span> 2. ItemListener (Perubahan Status Seleksi)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Pada komponen yang memiliki status biner (terpilih / tidak terpilih): <code>JCheckBox</code>, <code>JRadioButton</code>, atau pemilihan item di <code>JComboBox</code>.</p>
        <p><strong>Daftar Method:</strong> <code>void itemStateChanged(ItemEvent e)</code>.</p>
        <div class="code-wrapper">
          <pre><code class="language-java">chkOatMilk.addItemListener(e -> {{
    if (e.getStateChange() == ItemEvent.SELECTED) {{
        System.out.println("Susu Oat ditambahkan (+Rp 6.000)");
    }} else if (e.getStateChange() == ItemEvent.DESELECTED) {{
        System.out.println("Susu Oat dibatalkan");
    }}
}});</code></pre>
        </div>
        <p style="color: var(--callout-warn-text); font-size: 0.85rem; margin-bottom: 0;">
          <strong>⚠️ Jebakan Umum:</strong> Mengira <code>itemStateChanged()</code> hanya dipanggil saat mencentang. Padahal method ini dipanggil <strong>DUA KALI</strong> saat pengguna mengganti pilihan RadioButton (1x untuk deselect item lama, 1x untuk select item baru). Selalu periksa dengan <code>e.getStateChange() == ItemEvent.SELECTED</code>!
        </p>
      </div>

      <!-- Sub-bab 3 & 4: MouseListener & MouseMotionListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>🖱️</span> 3 & 4. MouseListener & MouseMotionListener (Gestur Kursor)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Menghasilkan efek visual interaktif saat kursor melintas di atas kartu produk (hover), mendeteksi klik ganda (*double click*), atau menggambar pola latte art pada panel kanvas.</p>
        <p><strong>Daftar Method MouseListener:</strong></p>
        <ul style="margin-bottom: 0.5rem; font-family: monospace; font-size: 0.85rem;">
          <li>mouseClicked(MouseEvent e) - Terjadi setelah siklus pressed & released tuntas di titik yang sama</li>
          <li>mousePressed(MouseEvent e) - Tombol mouse mulai ditekan ke bawah</li>
          <li>mouseReleased(MouseEvent e) - Tombol mouse dilepaskan ke atas</li>
          <li>mouseEntered(MouseEvent e) - Kursor mouse memasuki area batas komponen</li>
          <li>mouseExited(MouseEvent e) - Kursor mouse keluar meninggalkan area komponen</li>
        </ul>
        <p><strong>Daftar Method MouseMotionListener:</strong></p>
        <ul style="margin-bottom: 0.5rem; font-family: monospace; font-size: 0.85rem;">
          <li>mouseMoved(MouseEvent e) - Kursor digerakkan di atas komponen</li>
          <li>mouseDragged(MouseEvent e) - Kursor digerakkan sambil menahan tombol klik</li>
        </ul>
      </div>

      <!-- Sub-bab 5: KeyListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>⌨️</span> 5. KeyListener (Ketikan Keyboard)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Memfilter karakter input (misal: nomor meja hanya boleh angka), shortcut keyboard (Esc untuk membatalkan form), atau navigasi game.</p>
        <p><strong>Daftar Method:</strong></p>
        <ul style="margin-bottom: 0.5rem; font-family: monospace; font-size: 0.85rem;">
          <li>keyPressed(KeyEvent e) - Tombol fisik ditekan (menghasilkan getKeyCode() mis. VK_ENTER, VK_F1, VK_ESCAPE)</li>
          <li>keyTyped(KeyEvent e) - Karakter teks unicode dihasilkan (menghasilkan getKeyChar() mis. 'a', '9', '%')</li>
          <li>keyReleased(KeyEvent e) - Tombol fisik dilepas</li>
        </ul>
        <div class="code-wrapper">
          <pre><code class="language-java">// Memfilter input agar hanya menerima angka:
txtPorsi.addKeyListener(new KeyAdapter() {{
    public void keyTyped(KeyEvent e) {{
        char c = e.getKeyChar();
        if (!Character.isDigit(c)) {{
            e.consume(); // Batalkan karakter non-angka!
        }}
    }}
}});</code></pre>
        </div>
      </div>

      <!-- Sub-bab 6: FocusListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>🎯</span> 6. FocusListener (Perpindahan Fokus Kursor)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Menciptakan efek teks <em>placeholder</em> bantuan pada kolom input atau memicu validasi saat pengguna selesai mengisi dan berpindah ke kolom berikutnya.</p>
        <p><strong>Daftar Method:</strong> <code>focusGained(FocusEvent e)</code> dan <code>focusLost(FocusEvent e)</code>.</p>
      </div>

      <!-- Sub-bab 7: DocumentListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>📝</span> 7. DocumentListener (Pemantauan Teks Real-Time)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Menghitung sisa karakter catatan pesanan atau memperbarui estimasi subtotal secara live saat teks diketik, di-paste, maupun di-delete.</p>
        <p><strong>Daftar Method:</strong> <code>insertUpdate(DocumentEvent e)</code>, <code>removeUpdate(DocumentEvent e)</code>, dan <code>changedUpdate(DocumentEvent e)</code>.</p>
        <p style="color: var(--callout-tip-text); font-size: 0.85rem; margin-bottom: 0;">
          <strong>💡 Keunggulan Utama:</strong> Berbeda dengan KeyListener, <code>DocumentListener</code> tetap terpicu meskipun teks diubah menggunakan mouse (klik kanan Paste atau Cut)! Pasang selalu via <code>textField.getDocument().addDocumentListener(...)</code>.
        </p>
      </div>

      <!-- Sub-bab 8: ChangeListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>🎚️</span> 8. ChangeListener (Slider & Spinner Nilai)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Memantau pergeseran nilai pada <code>JSlider</code> (tingkat kemanisan gula 0%–100%) atau <code>JSpinner</code> (kuantitas porsi).</p>
        <p><strong>Daftar Method:</strong> <code>void stateChanged(ChangeEvent e)</code>.</p>
      </div>

      <!-- Sub-bab 9: ListSelectionListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>📋</span> 9. ListSelectionListener (Seleksi Daftar JList)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Saat pengguna memilih baris dari daftar <code>JList</code> (misal memilih varian biji kopi: Gayo, Kintamani, Toraja) atau baris pada <code>JTable</code>.</p>
        <p><strong>Daftar Method:</strong> <code>void valueChanged(ListSelectionEvent e)</code>.</p>
        <p style="color: var(--callout-warn-text); font-size: 0.85rem; margin-bottom: 0;">
          <strong>⚠️ Trik Wajib:</strong> Selalu bungkus kode Anda dengan <code>if (!e.getValueIsAdjusting()) {{ ... }}</code> agar aksi tidak dieksekusi ganda saat mouse masih dalam proses klik geser!
        </p>
      </div>

      <!-- Sub-bab 10: WindowListener -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--primary); display: flex; align-items: center; gap: 0.5rem;">
          <span>🪟</span> 10. WindowListener (Siklus Hidup Jendela JFrame)
        </h3>
        <p><strong>Kapan Dipakai:</strong> Memunculkan kotak dialog konfirmasi pop-up saat tombol silang (X) ditekan agar transaksi kasir yang belum disimpan tidak hilang tak sengaja.</p>
        <p><strong>Daftar Method:</strong> <code>windowClosing()</code>, <code>windowOpened()</code>, <code>windowClosed()</code>, <code>windowIconified()</code>, <code>windowDeiconified()</code>, <code>windowActivated()</code>, <code>windowDeactivated()</code>.</p>
      </div>

      <h2>3. Masalah Interface Bloat & Solusi Penyelamat: Adapter Classes</h2>
      <p>
        Mari kita cermati masalah besar pada <code>WindowListener</code>: interface ini memiliki <strong>7 method abstract</strong>. Jika Anda mengimplementasikan interface <code>WindowListener</code> secara langsung hanya untuk menangani <code>windowClosing()</code>, Anda <strong>diwajibkan oleh compiler Java untuk menulis 6 method kosong lainnya</strong>:
      </p>

      <div class="code-wrapper">
        <div class="code-header"><span class="file-name">❌ Tanpa Adapter: Mengotori Kode dengan Method Kosong</span></div>
        <pre><code class="language-java">frame.addWindowListener(new WindowListener() {{
    public void windowClosing(WindowEvent e) {{ konfirmasiKeluar(); }}
    public void windowOpened(WindowEvent e) {{}}      // Kosong tak terpakai!
    public void windowClosed(WindowEvent e) {{}}      // Kosong tak terpakai!
    public void windowIconified(WindowEvent e) {{}}   // Kosong tak terpakai!
    public void windowDeiconified(WindowEvent e) {{}} // Kosong tak terpakai!
    public void windowActivated(WindowEvent e) {{}}   // Kosong tak terpakai!
    public void windowDeactivated(WindowEvent e) {{}} // Kosong tak terpakai!
}});</code></pre>
      </div>

      <p>
        Untuk menyelamatkan kita dari kode sampah di atas, Java Swing menyediakan <strong>Adapter Classes</strong> (seperti <code>WindowAdapter</code>, <code>MouseAdapter</code>, <code>KeyAdapter</code>, <code>FocusAdapter</code>).
      </p>
      <p>
        Adapter class adalah <em>abstract class</em> yang sudah mengimplementasikan seluruh method interface dengan kurung kurawal kosong <code>{{}}</code>. Anda cukup meng-<em>extends</em> adapter tersebut dan <strong>meng-override HANYA SATU method yang Anda butuhkan</strong>!
      </p>

      <div class="code-wrapper">
        <div class="code-header"><span class="file-name">✅ Dengan Adapter: Sangat Bersih & Fokus</span></div>
        <pre><code class="language-java">frame.addWindowListener(new WindowAdapter() {{
    @Override
    public void windowClosing(WindowEvent e) {{
        konfirmasiKeluar();
    }}
}});</code></pre>
      </div>

      <div class="callout callout-info">
        <div class="callout-header">💡 Mengapa ActionListener Tidak Memiliki Adapter?</div>
        <p>
          Perhatikan baik-baik: Ada <code>MouseAdapter</code>, <code>KeyAdapter</code>, dan <code>WindowAdapter</code>, tetapi <strong>TIDAK ADA</strong> <code>ActionAdapter</code>! Mengapa?
          Karena <code>ActionListener</code> hanya memiliki <strong>1 method tunggal</strong> (<code>actionPerformed</code>). Tidak ada method kosong yang perlu dihindari, dan sejak Java 8 ia langsung dapat ditulis sebagai satu baris lambda <code>e -> ...</code>!
        </p>
      </div>

      <h2>4. Contoh Kode Lengkap: KatalogListenerDemo.java & AdapterListenerDemo.java</h2>
      <p>Silakan pelajari kedua implementasi komprehensif berikut:</p>

      {code_box("examples/09_EventHandling/KatalogListenerDemo.java", "KatalogListenerDemo.java")}

      {code_box("examples/09_EventHandling/AdapterListenerDemo.java", "AdapterListenerDemo.java")}

      <div class="practice-box">
        <div class="practice-header">✏️ Latihan Mandiri 9B.1</div>
        <p>
          Gunakan <code>MouseAdapter</code> pada sebuah <code>JLabel</code> foto produk kopi agar saat kursor mouse melintas di atasnya (<code>mouseEntered</code>), teks keterangan menampilkan "Klik untuk zoom", dan saat kursor pergi (<code>mouseExited</code>), teks kembali normal.
        </p>
        <details class="hint-details">
          <summary>💡 Butuh Petunjuk?</summary>
          <div class="hint-content">
            Panggil <code>label.addMouseListener(new MouseAdapter() {{ public void mouseEntered(MouseEvent e) {{ label.setText("Klik untuk zoom"); }} public void mouseExited(MouseEvent e) {{ label.setText("Espresso Single"); }} }});</code>.
          </div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 09B</div>
        <ul class="summary-list">
          <li>Setiap komponen GUI berpasangan dengan listener yang sesuai karakteristik interaksinya.</li>
          <li><code>ItemListener</code> digunakan untuk status biner centang/seleksi (<code>ItemEvent.SELECTED</code> vs <code>DESELECTED</code>).</li>
          <li><code>DocumentListener</code> memantau perubahan data teks real-time secara holistik (termasuk aksi Paste/Cut mouse).</li>
          <li><strong>Adapter Classes</strong> (<code>MouseAdapter</code>, <code>KeyAdapter</code>, <code>WindowAdapter</code>) membebaskan pemrogram dari kewajiban menulis method-method kosong yang tidak diperlukan.</li>
        </ul>
      </div>

      {nav_buttons('bab-9a', 'Bab 09A: Fondasi & 4 Gaya Listener', 'bab-9c', 'Bab 09C: Event Playground & 3 Mini-Proyek')}
    </article>
    '''

def get_bab9c():
    return f'''
    <article class="chapter-article" id="bab-9c">
      <div class="chapter-badge">Bab 09C • Praktik & Simulasi</div>
      <h1 class="chapter-title">Event Playground Interaktif & 3 Mini-Proyek Kasir Terpadu</h1>
      <p class="chapter-lead">
        Mengamati urutan kronologis eksekusi event Swing secara langsung di browser melalui simulator Event Playground, mendalami 3 mini-proyek kasir bertingkat di folder examples, serta menaklukkan 9 latihan mandiri dan jebakan maut event handling.
      </p>

      <div class="objectives-card">
        <div class="objectives-title">🎯 Tujuan Pembelajaran</div>
        <ul class="objectives-list">
          <li>Mengamati urutan firing event mouse (<code>pressed &rarr; released &rarr; clicked &rarr; action</code>) dan keyboard via simulator visual.</li>
          <li>Membedah dan menjalankan 3 mini-proyek kasir bertingkat (Level 1, 2, dan 3) yang menggabungkan berbagai listener.</li>
          <li>Menyelesaikan latihan mandiri bertingkat (Mudah, Sedang, Menantang) untuk menguji kesiapan logika.</li>
          <li>Mendeteksi dan menghindari 4 kesalahan maut penulisan listener yang sering memicu error atau GUI membeku (*freeze*).</li>
        </ul>
      </div>

      <h2>1. Live Simulator: Swing Event Playground</h2>
      <p>
        Karena program Java Swing dieksekusi di desktop, simulator interaktif di bawah ini dibuat menggunakan Vanilla JavaScript untuk mensimulasikan persis bagaimana JVM menangkap dan menembakkan event ke listener secara real-time.
      </p>
      <p>
        <strong>Cobalah berinteraksi dengan elemen-elemen di bawah:</strong> Klik tombol, gerakkan mouse di area bertitik, atau ketik teks pada kolom input. Amati bagaimana konsol terminal mencatat urutan method yang dipanggil!
      </p>

      <!-- Event Playground Interactive Container -->
      <div class="playground-container">
        <div class="playground-header">
          <div class="playground-header-title">
            <span>🎮</span>
            <span>Swing Event Playground Simulator</span>
          </div>
          <span class="playground-badge-sim">Live Real-Time Simulator</span>
        </div>

        <div class="playground-body">
          <!-- Interactive Components Box -->
          <div class="playground-interactive-box">
            <div class="playground-interactive-title">Komponen Interaktif Tiruan Swing</div>

            <!-- 1. Tombol Simulasi -->
            <div>
              <label style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 0.25rem;">
                A. Uji Klik JButton:
              </label>
              <button class="sim-button" id="sim-btn" type="button" style="width: 100%;">
                ☕ Klik Saya (JButton Pesan Kopi)
              </button>
            </div>

            <!-- Sequence Badges Mouse -->
            <div class="event-sequence-box">
              <div class="event-sequence-title">Urutan Event Mouse Terpicu:</div>
              <div class="sequence-tags-list">
                <span class="sequence-badge" id="seq-mp">1. mousePressed</span>
                <span style="color: var(--text-muted);">&rarr;</span>
                <span class="sequence-badge" id="seq-mr">2. mouseReleased</span>
                <span style="color: var(--text-muted);">&rarr;</span>
                <span class="sequence-badge" id="seq-mc">3. mouseClicked</span>
                <span style="color: var(--text-muted);">&rarr;</span>
                <span class="sequence-badge" id="seq-ap" style="border: 1px solid #f59e0b;">4. actionPerformed</span>
              </div>
            </div>

            <!-- 2. Kanvas Mouse Hover -->
            <div>
              <label style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 0.25rem;">
                B. Uji MouseMotion / Hover JPanel:
              </label>
              <div class="sim-interactive-area" id="sim-area">
                Arahkan kursor atau gerakkan mouse di dalam kotak ini (mouseEntered, mouseMoved, mouseExited)
              </div>
              <div style="display: flex; gap: 0.5rem; margin-top: 0.25rem;">
                <span class="sequence-badge" id="seq-me">mouseEntered</span>
                <span class="sequence-badge" id="seq-mx">mouseExited</span>
              </div>
            </div>

            <!-- 3. Input Teks Real-Time -->
            <div>
              <label style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 0.25rem;">
                C. Uji Pengetikan JTextField:
              </label>
              <input type="text" class="sim-input-box" id="sim-input" placeholder="Ketik nama kopi di sini...">
            </div>

            <!-- Sequence Badges Keyboard -->
            <div class="event-sequence-box">
              <div class="event-sequence-title">Urutan Event Keyboard & Document:</div>
              <div class="sequence-tags-list">
                <span class="sequence-badge" id="seq-kp">1. keyPressed</span>
                <span style="color: var(--text-muted);">&rarr;</span>
                <span class="sequence-badge" id="seq-kt">2. keyTyped</span>
                <span style="color: var(--text-muted);">&rarr;</span>
                <span class="sequence-badge" id="seq-doc">DocumentEvent</span>
                <span style="color: var(--text-muted);">&rarr;</span>
                <span class="sequence-badge" id="seq-kr">3. keyReleased</span>
              </div>
            </div>
          </div>

          <!-- Console Logger Box -->
          <div class="playground-console-box">
            <div class="console-topbar">
              <span class="console-topbar-title">📟 JVM Event Queue Terminal Log</span>
              <button class="btn-clear-console" id="btn-clear-sim-log" type="button">Bersihkan Log</button>
            </div>
            <div class="console-log-content" id="console-log-content">
              <div style="color: #64748b; font-style: italic;">
                Menunggu interaksi pengguna... Klik tombol, gerakkan mouse di atas kanvas, atau ketik teks di sebelah kiri untuk melihat event diproses.
              </div>
            </div>
          </div>
        </div>

        <!-- Java Code Matcher Pane -->
        <div class="playground-java-pane">
          <div class="playground-java-title">💻 Padanan Kode Java Swing Asli:</div>
          <pre style="margin: 0; background: #0f172a; padding: 0.75rem; border-radius: 6px; font-size: 0.82rem;"><code class="language-java" id="playground-java-code">// Lakukan aksi pada simulator di atas untuk melihat potongan kode Java yang menangani event tersebut...</code></pre>
        </div>
      </div>

      <h2>2. Tiga Mini-Proyek Kasir Terpadu (Bertingkat)</h2>
      <p>
        Untuk melihat bagaimana seluruh listener ini berkolaborasi dalam arsitektur aplikasi kasir yang utuh, pelajari dan jalankan 3 mini-proyek bertingkat yang telah disediakan di folder <code>examples/09_EventHandling/mini_proyek/</code>:
      </p>

      <!-- Proyek Level 1 -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #22c55e; border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 2rem;">
        <h3 style="margin-top: 0; color: #166534;">
          Level 1: Kasir Topping Dinamis (ItemListener + ActionListener)
        </h3>
        <p><strong>Fokus Pembelajaran:</strong> Kolaborasi dua listener berbeda pada satu alur belanja. <code>ItemListener</code> langsung memperbarui estimasi subtotal setiap kali checkbox topping dicentang atau dilepas, sedangkan <code>ActionListener</code> memproses transaksi akhir saat tombol bayar ditekan.</p>
        {code_box("examples/09_EventHandling/mini_proyek/Level1_KasirTopping.java", "Level1_KasirTopping.java")}
      </div>

      <!-- Proyek Level 2 -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #3b82f6; border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 2rem;">
        <h3 style="margin-top: 0; color: #1e3a8a;">
          Level 2: Form Validasi Real-Time (DocumentListener + KeyListener + FocusListener)
        </h3>
        <p><strong>Fokus Pembelajaran:</strong> Menciptakan formulir yang cerdas dan anti-salah-ketik. <code>DocumentListener</code> memberikan live-preview nama pemesan di kartu member dan menghitung batas kuota karakter. <code>KeyAdapter</code> menyaring nomor meja agar hanya bisa diketik digit angka, dan <code>FocusAdapter</code> menghadirkan teks placeholder interaktif.</p>
        {code_box("examples/09_EventHandling/mini_proyek/Level2_FormValidasi.java", "Level2_FormValidasi.java")}
      </div>

      <!-- Proyek Level 3 -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 5px solid #f59e0b; border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 2rem;">
        <h3 style="margin-top: 0; color: #b45309;">
          Level 3: JavaCafe Pro POS (CardLayout + MouseListener + Hotkeys + WindowListener)
        </h3>
        <p><strong>Fokus Pembelajaran:</strong> Arsitektur sistem kasir kafe profesional. Menggunakan <code>MouseAdapter</code> untuk efek hover warna saat kursor melintas di atas kartu menu kopi, shortcut keyboard global (F1 untuk membuka katalog, F2 untuk kasir bayar), dan <code>WindowAdapter</code> (mencegah penutupan window tak sengaja jika masih ada transaksi aktif yang belum dibayar).</p>
        {code_box("examples/09_EventHandling/mini_proyek/Level3_JavaCafeProPOS.java", "Level3_JavaCafeProPOS.java")}
      </div>

      <h2>3. Kotak Awas: Empat Kesalahan Maut Event Handling</h2>

      <div style="display: flex; flex-direction: column; gap: 1rem; margin: 1.5rem 0;">
        <div class="callout callout-warn" style="margin: 0;">
          <div class="callout-header">⚠️ 1. Lupa addActionListener</div>
          <p>Tombol sudah dibuat dan method logika perhitungan sudah rapi, namun saat tombol diklik tidak ada reaksi apa-apa. Selalu telusuri baris inisialisasi: apakah <code>btn.addActionListener(...)</code> sudah terpanggil?</p>
        </div>

        <div class="callout callout-warn" style="margin: 0;">
          <div class="callout-header">⚠️ 2. Listener Terdaftar Ganda (Double Firing)</div>
          <p>Dialog sukses muncul dua kali berturut-turut saat tombol ditekan sekali. Ini terjadi jika Anda tidak sengaja memanggil <code>addActionListener</code> dua kali pada objek tombol yang sama (misal di constructor dan di method <code>setupEvents()</code>).</p>
        </div>

        <div class="callout callout-warn" style="margin: 0;">
          <div class="callout-header">⚠️ 3. Menaruh Proses Berat di Listener Bikin GUI Membeku (EDT Freeze)</div>
          <p>Seluruh event dieksekusi di satu thread: <strong>Event Dispatch Thread (EDT)</strong>. Jika Anda memanggil <code>Thread.sleep(5000)</code> atau membaca file harddisk raksasa di dalam <code>actionPerformed()</code>, jendela aplikasi akan menjadi putih, membeku, dan berstatus <em>"Not Responding"</em> karena EDT dilarang merender layar selama proses tersebut!</p>
        </div>

        <div class="callout callout-warn" style="margin: 0;">
          <div class="callout-header">⚠️ 4. Salah Pilih: keyTyped vs keyPressed</div>
          <p>Jika Anda ingin mendeteksi tombol <strong>Panah, Shift, Ctrl, atau tombol F1–F12</strong>, jangan gunakan <code>keyTyped</code>! Tombol modifier hardware tidak menghasilkan karakter teks sehingga tidak memicu <code>keyTyped</code>. Gunakan selalu <code>keyPressed</code> dengan <code>e.getKeyCode() == KeyEvent.VK_...</code>.</p>
        </div>
      </div>

      <h2>4. Sembilan Latihan Mandiri Bertingkat</h2>

      <!-- Tingkat Dasar -->
      <h3 style="color: #166534;">🟢 Tingkat Dasar (Mudah)</h3>
      <div class="practice-box">
        <div class="practice-header">Latihan 9C.1: Toggle Label Teks</div>
        <p>Buat tombol yang saat diklik pertama kali mengubah teks label menjadi "Buka", dan saat diklik kedua kali kembali menjadi "Tutup" (Gunakan boolean flag status).</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Deklarasikan atribut <code>private boolean isOpen = false;</code>. Di dalam listener tombol: <code>isOpen = !isOpen; label.setText(isOpen ? "Buka" : "Tutup");</code>.</div>
        </details>
      </div>

      <div class="practice-box">
        <div class="practice-header">Latihan 9C.2: Live Subtotal CheckBox</div>
        <p>Buat 2 JCheckBox topping kafe. Setiap kali kotak dicentang atau dihilangkan centangnya, cetak status terbaru ke konsol menggunakan <code>ItemListener</code>.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Gunakan <code>chk.addItemListener(e -> System.out.println(chk.getText() + ": " + (e.getStateChange() == ItemEvent.SELECTED)));</code>.</div>
        </details>
      </div>

      <div class="practice-box">
        <div class="practice-header">Latihan 9C.3: Tombol Batal Reset Form</div>
        <p>Buat tombol "Batal" yang saat diklik mengosongkan teks di JTextField dan mematikan semua centang di JCheckBox.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Panggil <code>textField.setText("");</code> dan <code>checkBox.setSelected(false);</code> di dalam ActionListener tombol Batal.</div>
        </details>
      </div>

      <!-- Tingkat Menengah -->
      <h3 style="color: #1e3a8a;">🟡 Tingkat Menengah (Sedang)</h3>
      <div class="practice-box">
        <div class="practice-header">Latihan 9C.4: Filter Karakter Hanya Huruf</div>
        <p>Pada kolom input nama kasir, gunakan <code>KeyAdapter</code> dan method <code>keyTyped</code> agar pengguna sama sekali tidak bisa mengetik angka!</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Di <code>keyTyped(KeyEvent e)</code>, periksa: <code>if (Character.isDigit(e.getKeyChar())) e.consume();</code>.</div>
        </details>
      </div>

      <div class="practice-box">
        <div class="practice-header">Latihan 9C.5: Live Character Counter</div>
        <p>Gunakan <code>DocumentListener</code> pada kolom catatan pesanan agar label di bawahnya selalu menampilkan sisa karakter yang tersedia dari batas maksimal 50 karakter.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Di method <code>insertUpdate</code> dan <code>removeUpdate</code>, hitung: <code>int sisa = 50 - txt.getText().length(); lbl.setText("Sisa: " + sisa);</code>.</div>
        </details>
      </div>

      <div class="practice-box">
        <div class="practice-header">Latihan 9C.6: Konfirmasi Exit dengan WindowAdapter</div>
        <p>Cegah jendela aplikasi tertutup langsung saat tombol silang (X) ditekan. Tampilkan pop-up dialog konfirmasi <code>JOptionPane.showConfirmDialog</code>.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Atur <code>setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);</code> lalu override <code>windowClosing(WindowEvent e)</code> pada <code>WindowAdapter</code>.</div>
        </details>
      </div>

      <div class="practice-box">
        <div class="practice-header">Latihan 9C.7: Efek Hover Kartu dengan MouseAdapter</div>
        <p>Saat mouse melintas di atas JPanel kartu produk, ubah warna background panel menjadi kuning muda, dan kembalikan ke putih saat kursor keluar.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Gunakan <code>mouseEntered(MouseEvent e) -> panel.setBackground(new Color(254, 243, 199));</code> dan <code>mouseExited(MouseEvent e) -> panel.setBackground(Color.WHITE);</code>.</div>
        </details>
      </div>

      <!-- Tingkat Lanjut -->
      <h3 style="color: #b45309;">🔴 Tingkat Lanjut (Menantang)</h3>
      <div class="practice-box">
        <div class="practice-header">Latihan 9C.8: Hotkeys Navigasi Keyboard Global</div>
        <p>Implementasikan shortcut keyboard: jika pengguna menekan tombol <strong>Escape</strong> di manapun di dalam aplikasi, sistem otomatis kembali ke halaman katalog awal pada CardLayout.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Gunakan <code>KeyboardFocusManager.getCurrentKeyboardFocusManager().addKeyEventDispatcher(...)</code> untuk menangkap tombol Escape tanpa tergantung komponen mana yang sedang fokus.</div>
        </details>
      </div>

      <div class="practice-box">
        <div class="practice-header">Latihan 9C.9: Pelacak Koordinat Kursor Dinamis</div>
        <p>Tambahkan <code>MouseMotionListener</code> pada sebuah panel kosong yang secara real-time mencetak koordinat kursor (X, Y) pada sebuah JLabel status di footer.</p>
        <details class="hint-details">
          <summary>💡 Petunjuk</summary>
          <div class="hint-content">Di dalam <code>mouseMoved(MouseEvent e)</code>, perbarui teks label: <code>lblStatus.setText("Koordinat: X=" + e.getX() + ", Y=" + e.getY());</code>.</div>
        </details>
      </div>

      <div class="summary-card">
        <div class="summary-title">📝 Ringkasan Bab 09C</div>
        <ul class="summary-list">
          <li>Siklus klik tombol mouse melibatkan 4 tahapan sekuensial: <code>mousePressed &rarr; mouseReleased &rarr; mouseClicked &rarr; actionPerformed</code>.</li>
          <li>Kolaborasi listener (seperti <code>ItemListener</code> untuk live preview dan <code>ActionListener</code> untuk transaksi) menghasilkan antarmuka yang sangat responsif.</li>
          <li>Hindari proses pemrosesan berat di dalam listener agar Event Dispatch Thread (EDT) tidak mengalami *starvation* yang membuat aplikasi freeze.</li>
          <li>Gunakan <code>WindowAdapter</code> dengan <code>DO_NOTHING_ON_CLOSE</code> untuk melindungi data transaksi kasir yang belum tersimpan.</li>
        </ul>
      </div>

      {nav_buttons('bab-9b', 'Bab 09B: Katalog Listener & Adapter', 'bab-10', 'Bab 10: Dialog Pop-Up: JOptionPane')}
    </article>
    '''

print("chapters_events.py ready.")
