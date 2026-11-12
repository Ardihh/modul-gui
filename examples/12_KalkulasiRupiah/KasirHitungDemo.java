package examples.kalkulasirupiah;

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
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * Contoh 12: KasirHitungDemo
 * Pola perhitungan harga, add-on dinamis, pemformatan mata uang Rupiah, dan reset formulir.
 */
public class KasirHitungDemo extends JFrame {

    // Konstanta harga
    private final int HARGA_DASAR = 22000;
    private final int HARGA_EXTRA_SHOT = 5000;
    private final int HARGA_EXTRA_CARAMEL = 4000;
    private final int HARGA_ICE_CREAM = 8000;

    // Komponen GUI
    private JLabel lblMenu;
    private JLabel lblRingkasanHarga;
    private JCheckBox chkShot;
    private JCheckBox chkCaramel;
    private JCheckBox chkIceCream;
    private JButton btnHitung;
    private JButton btnReset;
    private JButton btnSimpan;

    // Formatter Rupiah Indonesia (Locale id-ID)
    private final NumberFormat formatRupiah = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("id-ID"));

    public KasirHitungDemo() {
        super("Pola Perhitungan & Format Rupiah - JavaCafe");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupEvents();
    }

    private void initComponents() {
        JPanel root = new JPanel(new BorderLayout(12, 12));
        root.setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));
        root.setBackground(new Color(248, 250, 252));

        // Header
        JPanel pnlHeader = new JPanel(new GridLayout(2, 1, 4, 4));
        pnlHeader.setBackground(new Color(248, 250, 252));
        lblMenu = new JLabel("Pemesanan: Ice Cafe Latte", SwingConstants.CENTER);
        lblMenu.setFont(new Font("Segoe UI", Font.BOLD, 17));
        lblMenu.setForeground(new Color(30, 58, 138));

        JLabel lblSub = new JLabel("Harga Dasar: " + formatUang(HARGA_DASAR), SwingConstants.CENTER);
        lblSub.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        pnlHeader.add(lblMenu);
        pnlHeader.add(lblSub);

        // Body: Checkboxes Add-on
        JPanel pnlAddon = new JPanel(new GridLayout(4, 1, 6, 6));
        pnlAddon.setBackground(Color.WHITE);
        pnlAddon.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(226, 232, 240), 1),
                BorderFactory.createEmptyBorder(10, 15, 10, 15)
        ));

        chkShot = new JCheckBox("Extra Espresso Shot (+ " + formatUang(HARGA_EXTRA_SHOT) + ")");
        chkCaramel = new JCheckBox("Caramel Drizzle (+ " + formatUang(HARGA_EXTRA_CARAMEL) + ")");
        chkIceCream = new JCheckBox("Topping Vanilla Ice Cream (+ " + formatUang(HARGA_ICE_CREAM) + ")");
        chkShot.setBackground(Color.WHITE);
        chkCaramel.setBackground(Color.WHITE);
        chkIceCream.setBackground(Color.WHITE);

        lblRingkasanHarga = new JLabel("Total Saat Ini: " + formatUang(HARGA_DASAR), SwingConstants.RIGHT);
        lblRingkasanHarga.setFont(new Font("Segoe UI", Font.BOLD, 15));
        lblRingkasanHarga.setForeground(new Color(217, 119, 6));

        pnlAddon.add(chkShot);
        pnlAddon.add(chkCaramel);
        pnlAddon.add(chkIceCream);
        pnlAddon.add(lblRingkasanHarga);

        // Footer: Buttons
        JPanel pnlFooter = new JPanel(new GridLayout(1, 3, 10, 10));
        pnlFooter.setBackground(new Color(248, 250, 252));

        btnHitung = new JButton("Hitung Total");
        btnReset = new JButton("Reset");
        btnSimpan = new JButton("Simpan Order");
        btnSimpan.setBackground(new Color(30, 58, 138));
        btnSimpan.setForeground(Color.WHITE);

        pnlFooter.add(btnHitung);
        pnlFooter.add(btnReset);
        pnlFooter.add(btnSimpan);

        root.add(pnlHeader, BorderLayout.NORTH);
        root.add(pnlAddon, BorderLayout.CENTER);
        root.add(pnlFooter, BorderLayout.SOUTH);

        add(root);
    }

    private void setupEvents() {
        // Tombol Hitung
        btnHitung.addActionListener(e -> {
            int total = hitungTotal();
            lblRingkasanHarga.setText("Total Saat Ini: " + formatUang(total));
        });

        // Tombol Reset
        btnReset.addActionListener(e -> resetForm());

        // Tombol Simpan
        btnSimpan.addActionListener(e -> {
            int total = hitungTotal();
            String rincian = "Terima kasih!\nPesanan Ice Cafe Latte telah disimpan.\nTotal Bayar: " + formatUang(total);
            JOptionPane.showMessageDialog(this, rincian, "Order Sukses", JOptionPane.INFORMATION_MESSAGE);
            resetForm();
        });
    }

    // Method pembantu untuk menghitung total
    private int hitungTotal() {
        int total = HARGA_DASAR;
        if (chkShot.isSelected()) {
            total += HARGA_EXTRA_SHOT;
        }
        if (chkCaramel.isSelected()) {
            total += HARGA_EXTRA_CARAMEL;
        }
        if (chkIceCream.isSelected()) {
            total += HARGA_ICE_CREAM;
        }
        return total;
    }

    // Method pembantu untuk mereset seluruh form ke nilai awal
    private void resetForm() {
        chkShot.setSelected(false);
        chkCaramel.setSelected(false);
        chkIceCream.setSelected(false);
        lblRingkasanHarga.setText("Total Saat Ini: " + formatUang(HARGA_DASAR));
    }

    // Method utilitas untuk format rupiah yang rapi (mis. Rp22.000)
    private String formatUang(int nominal) {
        // Menggunakan NumberFormat Locale Indonesia
        return formatRupiah.format(nominal);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new KasirHitungDemo().setVisible(true));
    }
}
