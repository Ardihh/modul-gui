package examples.eventhandling;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/**
 * Contoh 09C: AdapterListenerDemo
 * Menunjukkan keuntungan menggunakan Adapter Class:
 * Cukup meng-override method yang dibutuhkan saja tanpa dipaksa menulis method kosong!
 *
 * Menggunakan:
 * 1. MouseAdapter (efek hover & klik kartu kafe)
 * 2. KeyAdapter (shortcut keyboard & filter angka)
 * 3. FocusAdapter (placeholder cerdas)
 * 4. WindowAdapter (konfirmasi saat menutup aplikasi)
 */
public class AdapterListenerDemo extends JFrame {

    private JPanel cardMenu;
    private JLabel lblNamaMenu;
    private JTextField txtNomorMeja;
    private JLabel lblLogAksi;

    public AdapterListenerDemo() {
        super("Penerapan Adapter Classes - JavaCafe");
        setSize(520, 370);
        // Penting: DO_NOTHING_ON_CLOSE agar WindowAdapter yang mengontrol penutupan jendela
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupAdapters();
    }

    private void initComponents() {
        JPanel root = new JPanel(new BorderLayout(10, 10));
        root.setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));
        root.setBackground(new Color(248, 250, 252));

        JLabel title = new JLabel("Demo Adapter Class (Bebas Method Kosong)", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 15));
        title.setForeground(new Color(30, 58, 138));
        root.add(title, BorderLayout.NORTH);

        JPanel pnlCenter = new JPanel(new GridLayout(2, 1, 10, 10));
        pnlCenter.setBackground(new Color(248, 250, 252));

        // 1. Kartu Menu dengan MouseAdapter (Hover Effect)
        cardMenu = new JPanel(new BorderLayout());
        cardMenu.setBackground(Color.WHITE);
        cardMenu.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(203, 213, 225), 2),
                BorderFactory.createEmptyBorder(12, 15, 12, 15)
        ));

        lblNamaMenu = new JLabel("<html><b>☕ Caramel Macchiato</b><br><small>Arahkan kursor / klik kartu ini</small></html>", SwingConstants.CENTER);
        lblNamaMenu.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        cardMenu.add(lblNamaMenu, BorderLayout.CENTER);
        pnlCenter.add(cardMenu);

        // 2. Input Nomor Meja dengan FocusAdapter & KeyAdapter
        JPanel pnlInput = new JPanel(new GridLayout(2, 1, 4, 4));
        pnlInput.setBackground(new Color(248, 250, 252));
        pnlInput.add(new JLabel("Input Nomor Meja (Ketik angka saja, tekan Enter untuk cek):"));

        txtNomorMeja = new JTextField("Contoh: 04");
        txtNomorMeja.setForeground(Color.GRAY);
        txtNomorMeja.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        pnlInput.add(txtNomorMeja);
        pnlCenter.add(pnlInput);

        root.add(pnlCenter, BorderLayout.CENTER);

        // Footer Log
        lblLogAksi = new JLabel("Status: Arahkan mouse ke kartu atau klik tombol close (X)", SwingConstants.CENTER);
        lblLogAksi.setFont(new Font("Segoe UI", Font.ITALIC, 12));
        lblLogAksi.setForeground(new Color(100, 116, 139));
        root.add(lblLogAksi, BorderLayout.SOUTH);

        add(root);
    }

    private void setupAdapters() {
        // =====================================================================
        // 1. MouseAdapter pada Kartu Menu
        // Hanya meng-override mouseEntered, mouseExited, dan mouseClicked.
        // Tanpa adapter, kita terpaksa menulis mousePressed dan mouseReleased kosong!
        // =====================================================================
        cardMenu.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                // Efek hover: ubah warna latar kartu menjadi kuning lembut
                cardMenu.setBackground(new Color(254, 243, 199));
                cardMenu.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createLineBorder(new Color(245, 158, 11), 2),
                        BorderFactory.createEmptyBorder(12, 15, 12, 15)
                ));
                lblLogAksi.setText("MouseAdapter: mouseEntered pada kartu!");
            }

            @Override
            public void mouseExited(MouseEvent e) {
                // Kembalikan ke warna default
                cardMenu.setBackground(Color.WHITE);
                cardMenu.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createLineBorder(new Color(203, 213, 225), 2),
                        BorderFactory.createEmptyBorder(12, 15, 12, 15)
                ));
                lblLogAksi.setText("MouseAdapter: mouseExited dari kartu");
            }

            @Override
            public void mouseClicked(MouseEvent e) {
                lblLogAksi.setText(String.format("MouseAdapter: Kartu diklik pada koordinat (%d, %d)", e.getX(), e.getY()));
            }
        });

        // =====================================================================
        // 2. FocusAdapter pada JTextField untuk Placeholder Teks
        // =====================================================================
        txtNomorMeja.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (txtNomorMeja.getText().equals("Contoh: 04")) {
                    txtNomorMeja.setText("");
                    txtNomorMeja.setForeground(Color.BLACK);
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                if (txtNomorMeja.getText().trim().isEmpty()) {
                    txtNomorMeja.setText("Contoh: 04");
                    txtNomorMeja.setForeground(Color.GRAY);
                }
            }
        });

        // =====================================================================
        // 3. KeyAdapter pada JTextField untuk Validasi Angka & Tombol Enter
        // =====================================================================
        txtNomorMeja.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                char c = e.getKeyChar();
                // Tolak jika bukan digit angka
                if (!Character.isDigit(c)) {
                    e.consume(); // Mengabaikan input agar tidak tertulis di kolom
                    lblLogAksi.setText("KeyAdapter: Hanya boleh memasukkan angka untuk nomor meja!");
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    lblLogAksi.setText("KeyAdapter: Enter ditekan! Meja terverifikasi: " + txtNomorMeja.getText());
                }
            }
        });

        // =====================================================================
        // 4. WindowAdapter pada Frame untuk Dialog Konfirmasi Keluar
        // Menangani windowClosing tanpa perlu mengimplementasikan 6 method window lainnya!
        // =====================================================================
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                int jawaban = JOptionPane.showConfirmDialog(
                        AdapterListenerDemo.this,
                        "Apakah Anda yakin ingin menutup aplikasi kasir JavaCafe?",
                        "Konfirmasi Keluar",
                        JOptionPane.YES_NO_OPTION,
                        JOptionPane.QUESTION_MESSAGE
                );

                if (jawaban == JOptionPane.YES_OPTION) {
                    System.exit(0); // Tutup aplikasi
                } else {
                    lblLogAksi.setText("Penutupan dibatalkan oleh kasir.");
                }
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new AdapterListenerDemo().setVisible(true));
    }
}
