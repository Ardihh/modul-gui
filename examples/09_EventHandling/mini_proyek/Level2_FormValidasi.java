package examples.eventhandling.mini_proyek;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

/**
 * Mini-Proyek Level 2: Form Validasi Real-Time
 * Memadukan DocumentListener, KeyListener, dan FocusListener
 * untuk menciptakan form input yang interaktif, cerdas, dan aman dari salah ketik.
 */
public class Level2_FormValidasi extends JFrame {

    private JTextField txtNama;
    private JTextField txtMeja;
    private JLabel lblPreviewNama;
    private JLabel lblCharCount;
    private JLabel lblStatusMeja;
    private JButton btnDaftar;

    public Level2_FormValidasi() {
        super("Mini-Proyek 2: Validasi Form Real-Time (Document, Key, Focus)");
        setSize(520, 380);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupListeners();
    }

    private void initComponents() {
        JPanel root = new JPanel(new BorderLayout(10, 10));
        root.setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));
        root.setBackground(new Color(248, 250, 252));

        JLabel title = new JLabel("Registrasi Meja & Kartu Pesanan", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 16));
        title.setForeground(new Color(30, 58, 138));
        root.add(title, BorderLayout.NORTH);

        // Body Form
        JPanel pnlForm = new JPanel(new GridLayout(6, 1, 4, 4));
        pnlForm.setBackground(new Color(248, 250, 252));

        // 1. Input Nama
        pnlForm.add(new JLabel("1. Nama Pemesan (Maksimal 20 Karakter):"));
        txtNama = new JTextField();
        pnlForm.add(txtNama);

        // Preview & Counter Nama
        JPanel pnlSubNama = new JPanel(new GridLayout(1, 2));
        pnlSubNama.setBackground(new Color(248, 250, 252));
        lblPreviewNama = new JLabel("Kartu: [Nama Pemesan]");
        lblPreviewNama.setFont(new Font("Segoe UI", Font.BOLD, 11));
        lblPreviewNama.setForeground(new Color(30, 58, 138));
        lblCharCount = new JLabel("0/20 Karakter", SwingConstants.RIGHT);
        lblCharCount.setFont(new Font("Segoe UI", Font.PLAIN, 11));
        lblCharCount.setForeground(Color.GRAY);
        pnlSubNama.add(lblPreviewNama);
        pnlSubNama.add(lblCharCount);
        pnlForm.add(pnlSubNama);

        // 2. Input Nomor Meja
        pnlForm.add(new JLabel("2. Nomor Meja (Hanya Angka 1-99):"));
        txtMeja = new JTextField("Nomor meja...");
        txtMeja.setForeground(Color.GRAY);
        pnlForm.add(txtMeja);

        lblStatusMeja = new JLabel("Status Meja: Belum diisi", SwingConstants.LEFT);
        lblStatusMeja.setFont(new Font("Segoe UI", Font.ITALIC, 11));
        lblStatusMeja.setForeground(Color.GRAY);
        pnlForm.add(lblStatusMeja);

        root.add(pnlForm, BorderLayout.CENTER);

        // Footer Button
        btnDaftar = new JButton("Simpan & Konfirmasi Meja");
        btnDaftar.setBackground(new Color(30, 58, 138));
        btnDaftar.setForeground(Color.WHITE);
        btnDaftar.setFont(new Font("Segoe UI", Font.BOLD, 13));
        root.add(btnDaftar, BorderLayout.SOUTH);

        add(root);
    }

    private void setupListeners() {
        // =====================================================================
        // 1. DocumentListener pada txtNama (Live Preview & Penghitung Karakter)
        // =====================================================================
        txtNama.getDocument().addDocumentListener(new DocumentListener() {
            @Override
            public void insertUpdate(DocumentEvent e) { updateNama(); }
            @Override
            public void removeUpdate(DocumentEvent e) { updateNama(); }
            @Override
            public void changedUpdate(DocumentEvent e) { updateNama(); }

            private void updateNama() {
                String nama = txtNama.getText();
                int len = nama.length();
                lblCharCount.setText(len + "/20 Karakter");

                if (len > 20) {
                    lblCharCount.setForeground(Color.RED);
                    lblPreviewNama.setText("⚠️ Nama terlalu panjang!");
                    lblPreviewNama.setForeground(Color.RED);
                } else if (nama.trim().isEmpty()) {
                    lblCharCount.setForeground(Color.GRAY);
                    lblPreviewNama.setText("Kartu: [Nama Pemesan]");
                    lblPreviewNama.setForeground(new Color(30, 58, 138));
                } else {
                    lblCharCount.setForeground(new Color(22, 101, 52));
                    lblPreviewNama.setText("Kartu: " + nama);
                    lblPreviewNama.setForeground(new Color(30, 58, 138));
                }
            }
        });

        // =====================================================================
        // 2. FocusAdapter pada txtMeja (Placeholder Cerdas)
        // =====================================================================
        txtMeja.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (txtMeja.getText().equals("Nomor meja...")) {
                    txtMeja.setText("");
                    txtMeja.setForeground(Color.BLACK);
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                if (txtMeja.getText().trim().isEmpty()) {
                    txtMeja.setText("Nomor meja...");
                    txtMeja.setForeground(Color.GRAY);
                    lblStatusMeja.setText("Status Meja: Wajib diisi!");
                    lblStatusMeja.setForeground(Color.RED);
                } else {
                    lblStatusMeja.setText("Status Meja: Meja #" + txtMeja.getText() + " Valid ✓");
                    lblStatusMeja.setForeground(new Color(22, 101, 52));
                }
            }
        });

        // =====================================================================
        // 3. KeyAdapter pada txtMeja (Filter Hanya Angka & Batas 2 Digit)
        // =====================================================================
        txtMeja.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                char c = e.getKeyChar();
                // Hanya izinkan digit angka
                if (!Character.isDigit(c)) {
                    e.consume(); // batalkan karakter non-angka
                    return;
                }
                // Batasi panjang maksimal 2 digit
                if (txtMeja.getText().length() >= 2 && !txtMeja.getText().equals("Nomor meja...")) {
                    e.consume();
                }
            }
        });

        // =====================================================================
        // 4. ActionListener pada Tombol Konfirmasi
        // =====================================================================
        btnDaftar.addActionListener(e -> {
            String nama = txtNama.getText().trim();
            String meja = txtMeja.getText().trim();

            if (nama.isEmpty() || nama.length() > 20 || meja.isEmpty() || meja.equals("Nomor meja...")) {
                JOptionPane.showMessageDialog(this,
                        "Mohon lengkapi formulir dengan benar:\n- Nama 1-20 karakter\n- Nomor meja valid (angka)",
                        "Validasi Gagal", JOptionPane.WARNING_MESSAGE);
                return;
            }

            JOptionPane.showMessageDialog(this,
                    String.format("Meja Berhasil Dipesan!\nNama: %s\nNomor Meja: %s", nama, meja),
                    "Sukses", JOptionPane.INFORMATION_MESSAGE);
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Level2_FormValidasi().setVisible(true));
    }
}
