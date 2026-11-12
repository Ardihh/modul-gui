package examples.cleancode;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.GridLayout;

/**
 * Contoh 11: FormCleanDemo
 * Penerapan prinsip Clean Code pada komponen GUI Swing:
 * 1. Komponen dideklarasikan di level class (private fields)
 * 2. Inisialisasi terstruktur lewat method terpisah
 * 3. Logika dipisah ke method hitung, simpan, reset
 * 4. Penggunaan Theme terpusat
 */
public class FormCleanDemo extends JFrame {

    // === 1. Deklarasi Komponen sebagai Atribut (Fields) di Atas Kelas ===
    private JLabel lblJudulMenu;
    private JLabel lblHargaDasar;
    private JCheckBox chkExtraShot;
    private JCheckBox chkSusuOat;
    private JLabel lblTotalBayar;
    private JButton btnHitung;
    private JButton btnReset;
    private JButton btnCheckout;

    // State data
    private final int hargaDasar = 25000;

    public FormCleanDemo() {
        super("Penerapan Clean Code GUI - JavaCafe");
        setSize(CafeTheme.WINDOW_WIDTH, CafeTheme.WINDOW_HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        // Tahapan inisialisasi yang teratur
        initComponents();
        setupLayout();
        setupEvents();
    }

    // === 2. Inisialisasi Properti Komponen ===
    private void initComponents() {
        lblJudulMenu = new JLabel("Caramel Macchiato Spesial", SwingConstants.CENTER);
        lblJudulMenu.setFont(CafeTheme.FONT_TITLE);
        lblJudulMenu.setForeground(CafeTheme.COLOR_PRIMARY);

        lblHargaDasar = new JLabel("Harga Dasar: Rp 25.000", SwingConstants.CENTER);
        lblHargaDasar.setFont(CafeTheme.FONT_SUBTITLE);
        lblHargaDasar.setForeground(CafeTheme.COLOR_TEXT_MUTED);

        chkExtraShot = new JCheckBox("Extra Espresso Shot (+Rp 5.000)");
        chkExtraShot.setFont(CafeTheme.FONT_BODY);
        chkExtraShot.setBackground(CafeTheme.COLOR_CARD_BG);

        chkSusuOat = new JCheckBox("Upgrade ke Oat Milk (+Rp 6.000)");
        chkSusuOat.setFont(CafeTheme.FONT_BODY);
        chkSusuOat.setBackground(CafeTheme.COLOR_CARD_BG);

        lblTotalBayar = new JLabel("Total: Rp 25.000", SwingConstants.CENTER);
        lblTotalBayar.setFont(CafeTheme.FONT_PRICE);
        lblTotalBayar.setForeground(CafeTheme.COLOR_ACCENT);

        btnHitung = new JButton("Hitung Total");
        btnHitung.setFont(CafeTheme.FONT_BUTTON);

        btnReset = new JButton("Reset");
        btnReset.setFont(CafeTheme.FONT_BUTTON);

        btnCheckout = new JButton("Checkout");
        btnCheckout.setFont(CafeTheme.FONT_BUTTON);
        btnCheckout.setBackground(CafeTheme.COLOR_PRIMARY);
        btnCheckout.setForeground(CafeTheme.COLOR_CARD_BG);
    }

    // === 3. Pengorganisasian Layout ===
    private void setupLayout() {
        JPanel rootPanel = new JPanel(new BorderLayout(10, 10));
        rootPanel.setBackground(CafeTheme.COLOR_BACKGROUND);
        rootPanel.setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));

        // Header Panel
        JPanel headerPanel = new JPanel(new GridLayout(2, 1, 4, 4));
        headerPanel.setBackground(CafeTheme.COLOR_BACKGROUND);
        headerPanel.add(lblJudulMenu);
        headerPanel.add(lblHargaDasar);

        // Options Panel
        JPanel optionsPanel = new JPanel(new GridLayout(3, 1, 6, 6));
        optionsPanel.setBackground(CafeTheme.COLOR_CARD_BG);
        optionsPanel.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(CafeTheme.COLOR_BORDER, 1),
                BorderFactory.createEmptyBorder(10, 15, 10, 15)
        ));
        optionsPanel.add(chkExtraShot);
        optionsPanel.add(chkSusuOat);
        optionsPanel.add(lblTotalBayar);

        // Buttons Panel
        JPanel buttonPanel = new JPanel(new GridLayout(1, 3, 8, 8));
        buttonPanel.setBackground(CafeTheme.COLOR_BACKGROUND);
        buttonPanel.add(btnHitung);
        buttonPanel.add(btnReset);
        buttonPanel.add(btnCheckout);

        rootPanel.add(headerPanel, BorderLayout.NORTH);
        rootPanel.add(optionsPanel, BorderLayout.CENTER);
        rootPanel.add(buttonPanel, BorderLayout.SOUTH);

        add(rootPanel);
    }

    // === 4. Pemasangan Event Listeners ===
    private void setupEvents() {
        btnHitung.addActionListener(e -> hitungDanPerbaruiTotal());
        btnReset.addActionListener(e -> aksiReset());
        btnCheckout.addActionListener(e -> aksiCheckout());
    }

    // === 5. Pemisahan Logika Bisnis ke Method Terpisah ===
    private int hitungTotal() {
        int total = hargaDasar;
        if (chkExtraShot.isSelected()) {
            total += 5000;
        }
        if (chkSusuOat.isSelected()) {
            total += 6000;
        }
        return total;
    }

    private void hitungDanPerbaruiTotal() {
        int total = hitungTotal();
        lblTotalBayar.setText(String.format("Total: Rp %,d", total).replace(',', '.'));
    }

    private void aksiReset() {
        chkExtraShot.setSelected(false);
        chkSusuOat.setSelected(false);
        lblTotalBayar.setText(String.format("Total: Rp %,d", hargaDasar).replace(',', '.'));
    }

    private void aksiCheckout() {
        int totalAkhir = hitungTotal();
        String pesan = String.format("Pesanan berhasil diproses!\nTotal yang dibayarkan: Rp %,d", totalAkhir).replace(',', '.');
        JOptionPane.showMessageDialog(this, pesan, "Transaksi Sukses", JOptionPane.INFORMATION_MESSAGE);
        aksiReset();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new FormCleanDemo().setVisible(true));
    }
}
