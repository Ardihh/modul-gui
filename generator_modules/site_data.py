# -*- coding: utf-8 -*-

NAV_SECTIONS = [
    {
        "title": "Orientasi Modul",
        "items": [
            {"id": "beranda", "num": "00", "title": "Beranda & Pengantar"}
        ]
    },
    {
        "title": "Materi Inti (Dasar ke Lanjut)",
        "items": [
            {"id": "bab-1", "num": "01", "title": "Pengantar GUI & Event-Driven"},
            {"id": "bab-2", "num": "02", "title": "Jendela Pertama: JFrame"},
            {"id": "bab-3", "num": "03", "title": "Container Modular: JPanel"},
            {"id": "bab-4", "num": "04", "title": "Komponen Dasar (Label, Button, CheckBox)"},
            {"id": "bab-5", "num": "05", "title": "Menangani Gambar: ImageIcon"},
            {"id": "bab-6", "num": "06", "title": "Menguasai Layout Manager"},
            {"id": "bab-7", "num": "07", "title": "Navigasi Halaman: CardLayout"},
            {"id": "bab-8", "num": "08", "title": "Kerapian Tampilan: Border"},
            {"id": "bab-9a", "num": "09A", "title": "Fondasi & 4 Gaya Listener"},
            {"id": "bab-9b", "num": "09B", "title": "Katalog Listener & Adapter"},
            {"id": "bab-9c", "num": "09C", "title": "Event Playground & 3 Mini-Proyek"},
            {"id": "bab-10", "num": "10", "title": "Dialog Pop-Up: JOptionPane"},
            {"id": "bab-11", "num": "11", "title": "Clean Code & Tema Terpusat"},
            {"id": "bab-12", "num": "12", "title": "Kalkulasi Harga & Format Rupiah"},
            {"id": "bab-13", "num": "13", "title": "Menerjemahkan UML ke Java Swing"},
            {"id": "bab-14", "num": "14", "title": "Panduan Debugging & Error Populer"}
        ]
    },
    {
        "title": "Evaluasi & Lampiran",
        "items": [
            {"id": "cheatsheet", "num": "📑", "title": "Cheat Sheet Ringkas"},
            {"id": "checklist", "num": "✅", "title": "Checklist Kesiapan Jurnal"},
            {"id": "kuis", "num": "🎯", "title": "Kuis Interaktif (20 Soal)"},
            {"id": "glosarium", "num": "📖", "title": "Glosarium Istilah"},
            {"id": "referensi", "num": "🔗", "title": "Daftar Referensi"}
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "question": "1. Apa perbedaan utama antara pustaka GUI Java AWT dan Java Swing?",
        "options": [
            "AWT adalah komponen lightweight murni Java, sedangkan Swing bergantung pada komponen native OS.",
            "Swing adalah komponen lightweight yang konsisten di semua sistem operasi, sedangkan AWT adalah heavyweight yang bergantung pada OS native.",
            "Swing hanya bisa berjalan di sistem operasi Windows, sedangkan AWT berjalan di Linux dan Mac.",
            "AWT memiliki komponen berawalan 'J' seperti JButton, sedangkan Swing menggunakan Button."
        ],
        "correct": 1,
        "explanation": "Java Swing bersifat 'lightweight' karena seluruh komponennya dirender langsung menggunakan Java 2D tanpa memanggil peer native sistem operasi, sehingga tampilan konsisten di semua platform."
    },
    {
        "question": "2. Mengapa pembuatan jendela dan komponen Swing direkomendasikan berada di dalam 'SwingUtilities.invokeLater(() -> {...})'?",
        "options": [
            "Agar ukuran memori RAM yang digunakan program otomatis berkurang 50%.",
            "Supaya semua proses rendering dan update GUI dieksekusi secara aman di Event Dispatch Thread (EDT) untuk mencegah race condition.",
            "Hanya sekadar formalitas sintaks dan tidak memiliki dampak teknis apapun.",
            "Untuk mempercepat waktu kompilasi kode Java pada compiler javac."
        ],
        "correct": 1,
        "explanation": "Komponen Swing tidak thread-safe. Seluruh manipulasi GUI wajib dilakukan di Event Dispatch Thread (EDT) menggunakan SwingUtilities.invokeLater guna menghindari konflik thread."
    },
    {
        "question": "3. Apa akibat yang terjadi jika Anda TIDAK memanggil 'frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)'?",
        "options": [
            "Program langsung error saat pertama kali dikompilasi.",
            "Jendela tidak akan memiliki tombol silang merah (X) di pojok kanan atas.",
            "Saat tombol silang (X) ditekan, jendela menghilang tetapi proses Java (JVM) tetap berjalan terus di background.",
            "Jendela akan otomatis membesar memenuhi satu layar penuh monitor (fullscreen)."
        ],
        "correct": 2,
        "explanation": "Default operasi close pada JFrame adalah HIDE_ON_CLOSE. Jika tidak diubah ke EXIT_ON_CLOSE, JVM tidak akan berhenti dan menjadi ghost process yang terus memakan memori komputer."
    },
    {
        "question": "4. Bagaimana cara paling elegan agar jendela JFrame otomatis tampil tepat di tengah layar monitor tanpa menghitung manual resolusi layar?",
        "options": [
            "frame.centerOnScreen(true);",
            "frame.setLocationRelativeTo(null); (dipanggil setelah setSize)",
            "frame.setBounds(0, 0, 520, 350);",
            "frame.setMiddle(true);"
        ],
        "correct": 1,
        "explanation": "Memanggil frame.setLocationRelativeTo(null) setelah frame.setSize(...) secara otomatis menghitung koordinat tengah monitor sesuai dimensi window yang sudah ditetapkan."
    },
    {
        "question": "5. Dalam arsitektur modular GUI, mengapa kelas panel turunan (extends JPanel) sebaiknya menerima referensi frame utama di constructor-nya?",
        "options": [
            "Agar panel bisa membuat instance JFrame baru setiap kali tombol diklik.",
            "Agar panel anak dapat memanggil method pada frame utama (misal untuk berpindah halaman atau update status) tanpa membuat objek jendela duplikat.",
            "Karena Java mewajibkan semua kelas JPanel memiliki parameter frame.",
            "Supaya warna latar belakang panel otomatis berubah menjadi putih."
        ],
        "correct": 1,
        "explanation": "Meneruskan referensi frame (Dependency Injection) memungkinkan panel anak berkomunikasi dua arah dengan frame induk (seperti memicu CardLayout.show) tanpa menciptakan jendela baru."
    },
    {
        "question": "6. Method apa yang digunakan untuk memeriksa apakah sebuah JCheckBox sedang dicentang oleh pengguna?",
        "options": [
            "checkBox.isClicked()",
            "checkBox.isSelected()",
            "checkBox.getCheckState()",
            "checkBox.isActive()"
        ],
        "correct": 1,
        "explanation": "Method isSelected() mengembalikan nilai boolean (true jika kotak dicentang, false jika tidak dicentang)."
    },
    {
        "question": "7. Layout Manager apa yang membagi kontainer menjadi 5 wilayah mata angin (NORTH, SOUTH, EAST, WEST, CENTER)?",
        "options": [
            "GridLayout",
            "FlowLayout",
            "BorderLayout",
            "CardLayout"
        ],
        "correct": 2,
        "explanation": "BorderLayout membagi ruang menjadi lima zona: NORTH, SOUTH, EAST, WEST, dan CENTER. Zona CENTER akan membesar otomatis mengisi sisa area."
    },
    {
        "question": "8. Apa yang terjadi jika Anda memasukkan dua komponen ke dalam region yang sama pada BorderLayout (misalnya menambahkan 2 tombol ke BorderLayout.CENTER)?",
        "options": [
            "Kedua tombol akan diletakkan berdampingan secara otomatis.",
            "Program akan melempar runtime exception OverlapLayoutException.",
            "Komponen kedua akan menimpa dan menyembunyikan komponen pertama.",
            "Kedua tombol akan otomatis digabung menjadi satu tombol besar."
        ],
        "correct": 2,
        "explanation": "Setiap region pada BorderLayout hanya mampu menampung tepat SATU komponen. Komponen baru yang ditambahkan ke region yang sama akan menimpa komponen lama. Solusinya: bungkus beberapa komponen ke dalam sebuah JPanel terlebih dahulu (Nested Layout)."
    },
    {
        "question": "9. Layout Manager apa yang bekerja seperti tumpukan kartu (stack) sehingga sangat cocok digunakan untuk navigasi antar-halaman dalam satu frame?",
        "options": [
            "StackLayout",
            "CardLayout",
            "PageLayout",
            "TabbedLayout"
        ],
        "correct": 1,
        "explanation": "CardLayout memperlakukan setiap komponen yang ditambahkan sebagai kartu dalam setumpuk kartu, di mana hanya satu kartu yang terlihat pada satu waktu melalui method show()."
    },
    {
        "question": "10. Kode mana yang benar untuk memberikan jarak bantalan (padding) dalam sebesar 15 pixel pada sebuah JPanel?",
        "options": [
            "panel.setPadding(15);",
            "panel.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));",
            "panel.setMargin(new Insets(15, 15, 15, 15));",
            "panel.addSpacing(15);"
        ],
        "correct": 1,
        "explanation": "Di Swing, cara standar memberi padding/margin adalah dengan memasang EmptyBorder menggunakan BorderFactory.createEmptyBorder(top, left, bottom, right)."
    },
    {
        "question": "11. Di antara opsi berikut, mana penulisan event handler modern yang paling ringkas untuk menangani klik JButton?",
        "options": [
            "button.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { doSomething(); } });",
            "button.addActionListener(e -> doSomething());",
            "button.onClick = () => doSomething();",
            "button.setEventListener(\"click\", doSomething);"
        ],
        "correct": 1,
        "explanation": "Sejak Java 8, ActionListener yang merupakan Functional Interface dapat ditulis sangat ringkas dan bersih menggunakan Lambda Expression: button.addActionListener(e -> ...)."
    },
    {
        "question": "12. Mengapa komponen GUI sebaiknya dideklarasikan sebagai atribut (field) privat di level kelas, BUKAN variabel lokal di dalam constructor?",
        "options": [
            "Agar memori komputer menjadi lebih hemat.",
            "Agar komponen tersebut dapat diakses dan dimanipulasi oleh method-method lain di luar constructor (misalnya method hitungTotal() atau resetForm()).",
            "Supaya komponen tersebut otomatis memiliki tampilan visual mode gelap.",
            "Karena compiler Java melarang pembuatan komponen di dalam constructor."
        ],
        "correct": 1,
        "explanation": "Jika komponen dideklarasikan sebagai variabel lokal di constructor, variabel tersebut akan hilang dari scope saat constructor selesai, sehingga method lain tidak bisa membaca atau mengubah nilainya."
    },
    {
        "question": "13. Manakah urutan kronologis yang BENAR saat pengguna mengklik satu tombol JButton dengan mouse?",
        "options": [
            "mouseClicked -> mousePressed -> mouseReleased -> actionPerformed",
            "mousePressed -> mouseReleased -> mouseClicked -> actionPerformed",
            "actionPerformed -> mousePressed -> mouseReleased -> mouseClicked",
            "mouseEntered -> actionPerformed -> mouseReleased -> mouseClicked"
        ],
        "correct": 1,
        "explanation": "Saat tombol mouse ditekan, terjadi mousePressed. Saat tombol dilepas, terjadi mouseReleased. Jika kedua aksi terjadi di area yang sama, terbentuk mouseClicked. Terakhir, jika komponen tersebut adalah JButton, Swing memicu actionPerformed."
    },
    {
        "question": "14. Mengapa antarmuka ActionListener TIDAK memiliki kelas pendamping 'ActionAdapter' di Java Swing?",
        "options": [
            "Karena tim pengembang Java lupa membuatnya saat merancang Java 1.1.",
            "Karena ActionListener hanya memiliki tepat 1 method (actionPerformed), sehingga kelas adapter tidak dibutuhkan.",
            "Karena ActionListener tidak kompatibel dengan kelas abstrak.",
            "Karena ActionAdapter digantikan oleh WindowAdapter."
        ],
        "correct": 1,
        "explanation": "Adapter class diciptakan sebagai kelas abstrak dengan implementasi kosong untuk mengurung interface yang memiliki BANYAK method (seperti MouseListener dengan 5 method, WindowListener dengan 7 method). Karena ActionListener hanya memiliki 1 method (SAM / Functional Interface), ia tidak membutuhkan adapter."
    },
    {
        "question": "15. Perhatikan potongan kode berikut:\nif (e.getActionCommand() == \"SIMPAN\") { ... }\nApa potensi bug berbahaya pada kode tersebut?",
        "options": [
            "Kode tidak akan bisa dikompilasi (compile-time error).",
            "Operator == membandingkan alamat memori (referensi objek), bukan konten teks String, sehingga kondisi bisa bernilai false meskipun teksnya sama. Seharusnya memakai .equals().",
            "getActionCommand() mengembalikan integer, bukan String.",
            "Variabel e tidak boleh dipanggil di dalam blok if."
        ],
        "correct": 1,
        "explanation": "Di Java, String adalah objek. Membandingkan String dengan operator == hanya memeriksa apakah kedua variabel menunjuk ke alamat memori yang sama persis. Selalu gunakan \"SIMPAN\".equals(e.getActionCommand()) untuk membandingkan isi nilai String!"
    },
    {
        "question": "16. Seorang mahasiswa mengeluh: 'Tombol saya ditekan sekali, tetapi pesan dialog sukses muncul DUA KALI berturut-turut!'. Apa penyebab paling umum masalah ini?",
        "options": [
            "Pengguna mengklik tombol terlalu keras.",
            "Mahasiswa memanggil method btn.addActionListener(...) sebanyak dua kali pada objek tombol yang sama.",
            "JFrame tidak mendukung event klik tunggal.",
            "JOptionPane secara otomatis selalu memunculkan dua jendela."
        ],
        "correct": 1,
        "explanation": "Swing mengizinkan pendaftaran multiple listener pada satu komponen. Jika addActionListener terpanggil dua kali (misal di constructor dan di method initComponents), maka kedua listener tersebut akan dieksekusi secara berurutan setiap kali tombol diklik."
    },
    {
        "question": "17. Apa yang terjadi jika Anda menulis proses yang memakan waktu lama (seperti Thread.sleep(10000) atau download file besar) langsung di dalam method actionPerformed()?",
        "options": [
            "Aplikasi otomatis membagi beban ke thread CPU lain secara paralel.",
            "GUI akan membeku total (freeze / Not Responding) dan tidak bisa diklik hingga proses tersebut selesai, karena Event Dispatch Thread (EDT) terblokir.",
            "Jendela JFrame akan otomatis menutup dengan sendirinya.",
            "Tombol akan berubah warna menjadi merah."
        ],
        "correct": 1,
        "explanation": "Seluruh event dan rendering GUI ditangani oleh satu thread tunggal: Event Dispatch Thread (EDT). Jika EDT dipaksa menjalankan loop berat atau Thread.sleep, ia tidak bisa merender ulang layar atau memproses klik lain, menyebabkan window 'hang' / freeze."
    },
    {
        "question": "18. Pada interface KeyListener, apa perbedaan mendasar antara method keyTyped() dengan keyPressed()?",
        "options": [
            "keyTyped dipicu saat tombol dilepas, keyPressed saat tombol ditekan.",
            "keyTyped hanya dipicu untuk karakter unicode yang dapat dicetak (huruf, angka, simbol), sedangkan keyPressed dipicu oleh SEMUA tombol keyboard (termasuk Shift, Ctrl, Alt, F1-F12, Panah).",
            "keyPressed hanya berlaku untuk tombol angka saja.",
            "Keduanya identik dan tidak ada perbedaannya."
        ],
        "correct": 1,
        "explanation": "keyPressed dan keyReleased mencatat penekanan fisik tombol hardware (menghasilkan getKeyCode() seperti KeyEvent.VK_SHIFT). Sedangkan keyTyped hanya dipicu jika penekanan tersebut menghasilkan karakter teks nyata (menghasilkan getKeyChar()). Tombol navigasi/modifier tidak memicu keyTyped."
    },
    {
        "question": "19. Bagaimana cara mencegah karakter huruf tertulis pada JTextField nomor meja yang hanya boleh menerima angka saat menggunakan KeyListener?",
        "options": [
            "Memanggil e.consume() pada method keyTyped() jika karakter yang ditekan bukan digit angka.",
            "Menghapus manual karakter menggunakan text.replace().",
            "Memanggil textField.setVisible(false).",
            "Mematikan fungsi keyboard pengguna."
        ],
        "correct": 0,
        "explanation": "Method e.consume() pada KeyEvent menginstruksikan sistem operasi bahwa event tersebut telah 'dikonsumsi' / dibatalkan secara internal, sehingga sistem tidak akan meneruskan karakter tersebut ke dalam kotak teks JTextField."
    },
    {
        "question": "20. Mengapa DocumentListener lebih direkomendasikan daripada KeyListener jika Anda ingin memantau perubahan teks JTextField secara real-time (seperti fitur live search atau penghitung karakter)?",
        "options": [
            "Karena DocumentListener lebih cepat dieksekusi oleh memori RAM.",
            "Karena DocumentListener mampu mendeteksi perubahan teks dari SEMUA sumber, termasuk saat teks di-Paste via mouse (klik kanan Paste) atau dihapus lewat Cut, yang sering lolos dari KeyListener.",
            "Karena KeyListener sudah berstatus deprecated di Java 17.",
            "Karena DocumentListener hanya butuh satu baris kode lambda."
        ],
        "correct": 1,
        "explanation": "KeyListener hanya mendengarkan keyboard fisik. Jika pengguna menempelkan teks menggunakan mouse (klik kanan -> Paste) atau operasi drag-and-drop, KeyListener TIDAK akan terpicu! Sebaliknya, DocumentListener melekat pada model data teks (Document) sehingga menangkap perubahan teks dari jalur manapun."
    }
]

GLOSSARY_ITEMS = [
    {"term": "AWT (Abstract Window Toolkit)", "def": "Pustaka GUI tertua di Java. Bersifat heavyweight karena setiap komponen bergantung pada implementasi native GUI sistem operasi underlying."},
    {"term": "Swing", "def": "Pustaka GUI lightweight murni Java yang dibangun di atas AWT. Menghasilkan antarmuka yang seragam dan fleksibel di semua platform tanpa bergantung native OS."},
    {"term": "EDT (Event Dispatch Thread)", "def": "Thread khusus di Java yang bertugas menangani seluruh rendering grafis dan pemrosesan event pengguna (klik, ketik). Seluruh manipulasi Swing wajib berjalan di thread ini."},
    {"term": "Event Source", "def": "Komponen GUI visual yang menjadi pemicu timbulnya suatu aksi pengguna (misalnya: JButton yang diklik, JCheckBox yang dicentang, atau JTextField yang diketik)."},
    {"term": "Event Object", "def": "Objek turunan java.util.EventObject (seperti ActionEvent, MouseEvent, KeyEvent) yang membawa rincian data tentang kejadian yang baru saja berlangsung."},
    {"term": "Event Listener", "def": "Interface yang mendefinisikan kontrak method penanganan aksi. Bertindak sebagai 'pendengar' yang akan dieksekusi oleh JVM saat event terkait tiba."},
    {"term": "Adapter Class", "def": "Kelas abstrak pembantu (seperti MouseAdapter, KeyAdapter, WindowAdapter) yang mengimplementasikan seluruh method dari interface listener dengan badan kosong ({}). Memungkinkan programmer hanya meng-override method yang benar-benar dibutuhkan."},
    {"term": "Functional Interface (SAM)", "def": "Interface yang hanya memiliki tepat SATU abstract method (Single Abstract Method). Karena sifatnya ini, ia dapat diimplementasikan secara instan menggunakan sintaks Lambda Expression (e -> ...). Contoh: ActionListener, ItemListener."},
    {"term": "DocumentListener", "def": "Interface pemantau mutasi data teks pada model dokumen Swing (PlainDocument). Menangkap perubahan teks akibat pengetikan, Paste mouse, penghapusan tombol Backspace, maupun Cut."},
    {"term": "JFrame", "def": "Jendela tingkat atas (top-level container) yang memiliki bingkai, judul, tombol minimize/maximize/close, dan menampung seluruh tampilan aplikasi desktop."},
    {"term": "JPanel", "def": "Container perantara generik yang digunakan untuk mengelompokkan sejumlah komponen GUI serta mengatur tata letaknya menggunakan Layout Manager."},
    {"term": "Layout Manager", "def": "Objek pengendali yang secara otomatis mengatur posisi, ukuran, dan penataan komponen di dalam sebuah container."},
    {"term": "BorderLayout", "def": "Layout manager pembagi wilayah 5 arah: NORTH, SOUTH, EAST, WEST, dan CENTER."},
    {"term": "CardLayout", "def": "Layout manager yang memperlakukan komponen sebagai tumpukan kartu yang dapat dibolak-balik (sangat ideal untuk navigasi multi-halaman)."},
    {"term": "JOptionPane", "def": "Kelas utilitas untuk memunculkan kotak dialog standar (pop-up) seperti pesan informasi, konfirmasi, input, atau peringatan."},
    {"term": "EmptyBorder", "def": "Border tak kasat mata yang berfungsi memberikan bantalan ruang (padding/margin) di sekitar komponen agar tidak menempel ke tepi."},
    {"term": "Dependency Injection", "def": "Pola perancangan di mana sebuah objek (misal panel) menerima dependensinya (misal frame utama) lewat parameter constructor."}
]

CHECKLIST_ITEMS = [
    "Saya memahami bahwa Event Listener di Swing adalah penerapan konsep INTERFACE dari materi OOP.",
    "Saya menguasai 4 gaya penulisan listener (Named Class, Implements di Frame, Anonymous Class, Lambda Expression).",
    "Saya selalu menggunakan .equals() (BUKAN ==) saat membandingkan teks String dari e.getActionCommand().",
    "Saya memahami peran Adapter Class (MouseAdapter, KeyAdapter, WindowAdapter) untuk menghindari penulisan method kosong.",
    "Saya memahami urutan siklus event mouse (mousePressed -> mouseReleased -> mouseClicked -> actionPerformed).",
    "Saya tahu perbedaan getKeyChar() (karakter terketik) vs getKeyCode() (tombol keyboard fisik).",
    "Saya menggunakan DocumentListener saat ingin memantau isi JTextField secara real-time tanpa kecolongan aksi paste mouse.",
    "Saya tidak pernah menaruh proses berat / Thread.sleep di dalam listener agar GUI tidak membeku (EDT freeze).",
    "Saya memeriksa kembali bahwa setiap komponen telah dipasangi listener via addXxxListener(...) dan tidak terdaftar dobel.",
    "Saya dapat menghubungkan status isSelected() JCheckBox dengan kalkulasi total transaksi kasir secara dinamis."
]

CHEATSHEET_DATA = [
    {
        "category": "Peta Komponen GUI ➔ Listener yang Cocok & Method",
        "rows": [
            ("JButton ➔ ActionListener", "Method: actionPerformed(ActionEvent e). Menangani klik tombol utama."),
            ("JCheckBox / JRadioButton ➔ ItemListener", "Method: itemStateChanged(ItemEvent e). Cek e.getStateChange() == ItemEvent.SELECTED."),
            ("JTextField (Tekan Enter) ➔ ActionListener", "Method: actionPerformed(ActionEvent e). Dipicu saat user menekan tombol Enter di dalam kolom teks."),
            ("JTextField (Perubahan Teks) ➔ DocumentListener", "Pasang pada getDocument(). Method: insertUpdate(), removeUpdate(), changedUpdate(). Live preview."),
            ("JTextField (Filter Angka) ➔ KeyListener / KeyAdapter", "Method: keyTyped(KeyEvent e) -> panggil e.consume() jika bukan digit Character.isDigit(c)."),
            ("JTextField (Placeholder) ➔ FocusListener / FocusAdapter", "Method: focusGained(FocusEvent e) & focusLost(FocusEvent e). Teks bantuan hilang/muncul."),
            ("JSlider / JSpinner ➔ ChangeListener", "Method: stateChanged(ChangeEvent e). Menangkap pergeseran slider nilai atau pemilih kuantitas."),
            ("JList ➔ ListSelectionListener", "Method: valueChanged(ListSelectionEvent e). Gunakan !e.getValueIsAdjusting() agar tidak double trigger."),
            ("JFrame ➔ WindowListener / WindowAdapter", "Method: windowClosing(WindowEvent e). Dialog konfirmasi pop-up saat menutup aplikasi."),
            ("JPanel / Card ➔ MouseListener / MouseAdapter", "Method: mouseEntered() & mouseExited() untuk efek hover warna, mouseClicked() untuk seleksi kartu.")
        ]
    },
    {
        "category": "JFrame (Jendela Utama)",
        "rows": [
            ("setTitle(String)", "Mengatur teks judul jendela pada title bar"),
            ("setSize(int w, int h)", "Menentukan dimensi lebar dan tinggi jendela dalam pixel"),
            ("setDefaultCloseOperation(int)", "Menentukan aksi saat ditutup (mis. JFrame.EXIT_ON_CLOSE)"),
            ("setLocationRelativeTo(null)", "Memposisikan jendela tepat di tengah layar monitor"),
            ("setResizable(false)", "Mengunci dimensi jendela agar tidak bisa diubah ukuran oleh pengguna"),
            ("setVisible(true)", "Menampilkan jendela ke layar (panggil paling akhir)"),
            ("add(Component)", "Menambahkan panel atau komponen ke jendela")
        ]
    },
    {
        "category": "JPanel (Container & Pengelompok)",
        "rows": [
            ("setLayout(LayoutManager)", "Menentukan tata letak komponen di dalam panel"),
            ("setBackground(Color)", "Mengubah warna latar belakang panel"),
            ("setBorder(Border)", "Memasang garis tepi atau padding menggunakan BorderFactory"),
            ("add(Component)", "Memasukkan komponen ke dalam panel"),
            ("add(Component, Object constraints)", "Memasukkan komponen dengan koordinat posisi (mis. BorderLayout.NORTH)")
        ]
    },
    {
        "category": "Komponen Dasar (JLabel, JButton, JCheckBox)",
        "rows": [
            ("label.setText(String)", "Mengubah teks pada label"),
            ("label.setIcon(Icon)", "Memasang gambar ikon pada label"),
            ("label.setHorizontalAlignment(SwingConstants.CENTER)", "Mengatur perataan teks label di tengah"),
            ("button.addActionListener(e -> {...})", "Menambahkan penanganan event saat tombol diklik"),
            ("button.setFocusPainted(false)", "Menghilangkan kotak garis putus-putus fokus pada tombol"),
            ("checkbox.isSelected()", "Membaca apakah kotak centang sedang aktif (true/false)"),
            ("checkbox.setSelected(boolean)", "Mengatur kotak centang aktif atau tidak aktif secara terprogram")
        ]
    },
    {
        "category": "CardLayout (Navigasi Antar Halaman)",
        "rows": [
            ("CardLayout card = new CardLayout()", "Membuat objek pengatur kartu bertumpuk"),
            ("container.add(panel, \"KARTU_ID\")", "Mendaftarkan halaman ke container dengan nama pengenal"),
            ("card.show(container, \"KARTU_ID\")", "Menampilkan kartu tertentu ke permukaan layar"),
            ("card.first(container) / card.next(container)", "Melompat ke kartu pertama atau kartu berikutnya")
        ]
    },
    {
        "category": "BorderFactory (Estetika & Padding)",
        "rows": [
            ("BorderFactory.createEmptyBorder(t, l, b, r)", "Membuat bantalan padding transparan (top, left, bottom, right)"),
            ("BorderFactory.createLineBorder(Color, thick)", "Membuat garis pembatas tepi dengan warna & ketebalan"),
            ("BorderFactory.createCompoundBorder(outer, inner)", "Menggabungkan garis luar dengan bantalan dalam")
        ]
    },
    {
        "category": "JOptionPane (Kotak Pesan Modal)",
        "rows": [
            ("JOptionPane.showMessageDialog(parent, msg, title, type)", "Menampilkan pop-up dialog dengan ikon standar"),
            ("JOptionPane.showMessageDialog(parent, msg, title, type, icon)", "Menampilkan pop-up dialog dengan custom ImageIcon"),
            ("JOptionPane.showConfirmDialog(parent, msg, title, optionType)", "Menampilkan dialog konfirmasi YES/NO"),
            ("JOptionPane.INFORMATION_MESSAGE", "Tipe dialog pesan informasi"),
            ("JOptionPane.WARNING_MESSAGE", "Tipe dialog pesan peringatan"),
            ("JOptionPane.ERROR_MESSAGE", "Tipe dialog pesan kesalahan/error")
        ]
    }
]
print("site_data.py updated successfully.")
