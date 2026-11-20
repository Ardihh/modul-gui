package examples.eventhandling.mini_proyek;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Cursor;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.KeyEventDispatcher;
import java.awt.KeyboardFocusManager;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * Mini-Proyek Level 3: JavaCafe Pro POS
 * Mengintegrasikan CardLayout, MouseListener (Hover & Klik Kartu),
 * Keyboard Shortcuts (Hotkeys F1 & F2), dan WindowListener (Konfirmasi Keluar).
 */
public class Level3_JavaCafeProPOS extends JFrame {

    public static final String HALAMAN_KATALOG = "KATALOG";
    public static final String HALAMAN_CHECKOUT = "CHECKOUT";

    private final CardLayout cardLayout = new CardLayout();
    private final JPanel containerKartu = new JPanel(cardLayout);

    // State transaksi
    private String menuTerpilih = "Belum ada menu dipilih";
    private int hargaTerpilih = 0;

    private JLabel lblStatusPilihan;
    private JLabel lblRincianCheckout;
    private final NumberFormat nf = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("id-ID"));

    public Level3_JavaCafeProPOS() {
        super("Mini-Proyek 3: JavaCafe Pro POS (CardLayout + Mouse + Keys + Window)");
        setSize(540, 390);
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupGlobalHotkeys();
        setupWindowProtection();
    }

    private void initComponents() {
        // Buat 2 halaman kartu
        JPanel pnlKatalog = buatPanelKatalog();
        JPanel pnlCheckout = buatPanelCheckout();

        containerKartu.add(pnlKatalog, HALAMAN_KATALOG);
        containerKartu.add(pnlCheckout, HALAMAN_CHECKOUT);

        add(containerKartu);
        cardLayout.show(containerKartu, HALAMAN_KATALOG);
    }

    private JPanel buatPanelKatalog() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(12, 15, 12, 15));
        panel.setBackground(new Color(248, 250, 252));

        // Header
        JPanel pnlHeader = new JPanel(new GridLayout(2, 1));
        pnlHeader.setBackground(new Color(248, 250, 252));
        JLabel title = new JLabel("Katalog Menu JavaCafe (Tekan F1: Katalog | F2: Bayar)", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 14));
        title.setForeground(new Color(30, 58, 138));

        lblStatusPilihan = new JLabel("Menu Aktif: Belum Ada", SwingConstants.CENTER);
        lblStatusPilihan.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblStatusPilihan.setForeground(new Color(217, 119, 6));

        pnlHeader.add(title);
        pnlHeader.add(lblStatusPilihan);
        panel.add(pnlHeader, BorderLayout.NORTH);

        // Body: 3 Kartu Menu Interaktif dengan MouseAdapter
        JPanel pnlGrid = new JPanel(new GridLayout(3, 1, 8, 8));
        pnlGrid.setBackground(new Color(248, 250, 252));

        pnlGrid.add(buatKartuMenuInteraktif("☕ Espresso Solo", 18000, "Espresso murni 30ml ekstra pekat"));
        pnlGrid.add(buatKartuMenuInteraktif("☕ Caramel Macchiato", 28000, "Espresso dengan saus karamel lezat"));
        pnlGrid.add(buatKartuMenuInteraktif("🍵 Matcha Fusion Latte", 26000, "Green tea matcha berpadu susu segar"));

        panel.add(pnlGrid, BorderLayout.CENTER);

        // Footer Button
        JButton btnKeCheckout = new JButton("Lanjut ke Kasir Pembayaran [F2] ➔");
        btnKeCheckout.setBackground(new Color(30, 58, 138));
        btnKeCheckout.setForeground(Color.WHITE);
        btnKeCheckout.setFont(new Font("Segoe UI", Font.BOLD, 13));
        btnKeCheckout.addActionListener(e -> bukaHalamanCheckout());
        panel.add(btnKeCheckout, BorderLayout.SOUTH);

        return panel;
    }

    private JPanel buatKartuMenuInteraktif(String nama, int harga, String desc) {
        JPanel kartu = new JPanel(new BorderLayout(8, 8));
        kartu.setBackground(Color.WHITE);
        kartu.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(226, 232, 240), 1),
                BorderFactory.createEmptyBorder(8, 12, 8, 12)
        ));
        kartu.setCursor(new Cursor(Cursor.HAND_CURSOR));

        JLabel lblNama = new JLabel(nama);
        lblNama.setFont(new Font("Segoe UI", Font.BOLD, 13));
        lblNama.setForeground(new Color(15, 23, 42));

        JLabel lblDesc = new JLabel(desc);
        lblDesc.setFont(new Font("Segoe UI", Font.PLAIN, 11));
        lblDesc.setForeground(Color.GRAY);

        JLabel lblHarga = new JLabel(nf.format(harga), SwingConstants.RIGHT);
        lblHarga.setFont(new Font("Segoe UI", Font.BOLD, 13));
        lblHarga.setForeground(new Color(180, 83, 9));

        kartu.add(lblNama, BorderLayout.WEST);
        kartu.add(lblDesc, BorderLayout.CENTER);
        kartu.add(lblHarga, BorderLayout.EAST);

        // =====================================================================
        // MouseAdapter pada Kartu: Efek Hover & Seleksi
        // =====================================================================
        kartu.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                kartu.setBackground(new Color(254, 243, 199)); // Kuning hover
                kartu.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createLineBorder(new Color(245, 158, 11), 2),
                        BorderFactory.createEmptyBorder(7, 11, 7, 11)
                ));
            }

            @Override
            public void mouseExited(MouseEvent e) {
                if (!menuTerpilih.equals(nama)) {
                    kartu.setBackground(Color.WHITE);
                    kartu.setBorder(BorderFactory.createCompoundBorder(
                            BorderFactory.createLineBorder(new Color(226, 232, 240), 1),
                            BorderFactory.createEmptyBorder(8, 12, 8, 12)
                    ));
                }
            }

            @Override
            public void mouseClicked(MouseEvent e) {
                menuTerpilih = nama;
                hargaTerpilih = harga;
                lblStatusPilihan.setText("Menu Aktif Terpilih: " + nama + " (" + nf.format(harga) + ")");
            }
        });

        return kartu;
    }

    private JPanel buatPanelCheckout() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));
        panel.setBackground(new Color(255, 251, 235));

        JLabel title = new JLabel("Konfirmasi Pembayaran Kasir", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 16));
        title.setForeground(new Color(180, 83, 9));
        panel.add(title, BorderLayout.NORTH);

        lblRincianCheckout = new JLabel("<html><center>Belum ada produk yang dipilih.<br>Silakan kembali ke katalog.</center></html>", SwingConstants.CENTER);
        lblRincianCheckout.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        panel.add(lblRincianCheckout, BorderLayout.CENTER);

        // Buttons
        JPanel pnlBtns = new JPanel(new GridLayout(1, 2, 8, 8));
        pnlBtns.setBackground(new Color(255, 251, 235));
        JButton btnKembali = new JButton("⬅ Kembali ke Katalog [F1]");
        JButton btnSelesai = new JButton("Selesaikan Pesanan ✓");
        btnSelesai.setBackground(new Color(22, 101, 52));
        btnSelesai.setForeground(Color.WHITE);

        btnKembali.addActionListener(e -> cardLayout.show(containerKartu, HALAMAN_KATALOG));
        btnSelesai.addActionListener(e -> {
            if (hargaTerpilih == 0) {
                JOptionPane.showMessageDialog(this, "Pilih menu terlebih dahulu!", "Peringatan", JOptionPane.WARNING_MESSAGE);
                return;
            }
            JOptionPane.showMessageDialog(this, "Order " + menuTerpilih + " Berhasil Disimpan!", "Sukses", JOptionPane.INFORMATION_MESSAGE);
            menuTerpilih = "Belum ada menu dipilih";
            hargaTerpilih = 0;
            lblStatusPilihan.setText("Menu Aktif: Belum Ada");
            cardLayout.show(containerKartu, HALAMAN_KATALOG);
        });

        pnlBtns.add(btnKembali);
        pnlBtns.add(btnSelesai);
        panel.add(pnlBtns, BorderLayout.SOUTH);

        return panel;
    }

    private void bukaHalamanCheckout() {
        if (hargaTerpilih == 0) {
            JOptionPane.showMessageDialog(this, "Silakan klik salah satu kartu menu terlebih dahulu!", "Info", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        lblRincianCheckout.setText(String.format("<html><center><h3>Ringkasan Pesanan</h3>Pesanan: <b>%s</b><br>Total Bayar: <font color='#b45309'><b>%s</b></font><br><br>Tekan [Enter] atau klik Selesaikan.</center></html>",
                menuTerpilih, nf.format(hargaTerpilih)));
        cardLayout.show(containerKartu, HALAMAN_CHECKOUT);
    }

    // =========================================================================
    // Keyboard Focus Dispatcher (Shortcut Hotkeys F1 & F2 Aktif di Seluruh Window)
    // =========================================================================
    private void setupGlobalHotkeys() {
        KeyboardFocusManager.getCurrentKeyboardFocusManager().addKeyEventDispatcher(new KeyEventDispatcher() {
            @Override
            public boolean dispatchKeyEvent(KeyEvent e) {
                if (e.getID() == KeyEvent.KEY_PRESSED) {
                    if (e.getKeyCode() == KeyEvent.VK_F1) {
                        cardLayout.show(containerKartu, HALAMAN_KATALOG);
                        return true;
                    } else if (e.getKeyCode() == KeyEvent.VK_F2) {
                        bukaHalamanCheckout();
                        return true;
                    }
                }
                return false;
            }
        });
    }

    // =========================================================================
    // WindowListener (Mencegah Kehilangan Data saat Window Ditutup)
    // =========================================================================
    private void setupWindowProtection() {
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                if (hargaTerpilih > 0) {
                    int konfirmasi = JOptionPane.showConfirmDialog(
                            Level3_JavaCafeProPOS.this,
                            "Masih ada pesanan aktif (" + menuTerpilih + ") yang belum dibayar!\nYakin ingin keluar dari kasir?",
                            "Peringatan Transaksi Aktif",
                            JOptionPane.YES_NO_OPTION,
                            JOptionPane.WARNING_MESSAGE
                    );
                    if (konfirmasi == JOptionPane.YES_OPTION) {
                        System.exit(0);
                    }
                } else {
                    System.exit(0);
                }
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Level3_JavaCafeProPOS().setVisible(true));
    }
}
