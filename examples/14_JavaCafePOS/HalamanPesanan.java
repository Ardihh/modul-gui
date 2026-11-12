package examples.javacafepos;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.Image;
import java.io.File;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * HalamanPesanan (Halaman Detail Pesanan)
 * Mengelola pilihan add-on, kalkulasi total harga, tombol kembali, dan simpan order.
 */
public class HalamanPesanan extends JPanel {

    private final MainApp mainApp;

    // Data pesanan aktif
    private String namaMenuAktif = "Signature Caramel Macchiato";
    private int hargaDasarAktif = 28000;

    // Biaya opsi tambahan
    private final int BIAYA_EXTRA_SHOT = 5000;
    private final int BIAYA_OAT_MILK = 6000;
    private final int BIAYA_CARAMEL_DRIZZLE = 4000;

    // Komponen Tampilan (Fields di atas kelas)
    private JLabel lblJudulMenu;
    private JLabel lblHargaDasar;
    private JCheckBox chkExtraShot;
    private JCheckBox chkOatMilk;
    private JCheckBox chkCaramelDrizzle;
    private JLabel lblTotalDisplay;

    private JButton btnHitung;
    private JButton btnKembali;
    private JButton btnSimpan;

    private final NumberFormat formatRupiah = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("id-ID"));

    public HalamanPesanan(MainApp mainApp) {
        this.mainApp = mainApp;

        setLayout(new BorderLayout(10, 10));
        setBackground(CafeTheme.COLOR_BG);
        setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));

        initComponents();
        setupLayout();
        setupEvents();
    }

    private void initComponents() {
        lblJudulMenu = new JLabel("Detail Pesanan: " + namaMenuAktif, SwingConstants.CENTER);
        lblJudulMenu.setFont(CafeTheme.FONT_HEADER);
        lblJudulMenu.setForeground(CafeTheme.COLOR_PRIMARY);

        lblHargaDasar = new JLabel("Harga Dasar: " + formatUang(hargaDasarAktif), SwingConstants.CENTER);
        lblHargaDasar.setFont(CafeTheme.FONT_BODY);
        lblHargaDasar.setForeground(CafeTheme.COLOR_TEXT_MUTED);

        chkExtraShot = new JCheckBox("Extra Espresso Shot (+ " + formatUang(BIAYA_EXTRA_SHOT) + ")");
        chkExtraShot.setFont(CafeTheme.FONT_BODY);
        chkExtraShot.setBackground(CafeTheme.COLOR_CARD_BG);

        chkOatMilk = new JCheckBox("Ganti Oat Milk (+ " + formatUang(BIAYA_OAT_MILK) + ")");
        chkOatMilk.setFont(CafeTheme.FONT_BODY);
        chkOatMilk.setBackground(CafeTheme.COLOR_CARD_BG);

        chkCaramelDrizzle = new JCheckBox("Saus Caramel Drizzle (+ " + formatUang(BIAYA_CARAMEL_DRIZZLE) + ")");
        chkCaramelDrizzle.setFont(CafeTheme.FONT_BODY);
        chkCaramelDrizzle.setBackground(CafeTheme.COLOR_CARD_BG);

        lblTotalDisplay = new JLabel("Total: " + formatUang(hargaDasarAktif), SwingConstants.RIGHT);
        lblTotalDisplay.setFont(CafeTheme.FONT_PRICE);
        lblTotalDisplay.setForeground(CafeTheme.COLOR_ACCENT);

        btnHitung = new JButton("Hitung Total");
        btnHitung.setFont(CafeTheme.FONT_BUTTON);

        btnKembali = new JButton("⬅ Kembali");
        btnKembali.setFont(CafeTheme.FONT_BUTTON);

        btnSimpan = new JButton("Simpan Order");
        btnSimpan.setFont(CafeTheme.FONT_BUTTON);
        btnSimpan.setBackground(CafeTheme.COLOR_PRIMARY);
        btnSimpan.setForeground(Color.WHITE);
        btnSimpan.setFocusPainted(false);
    }

    private void setupLayout() {
        // Bagian Header
        JPanel pnlHeader = new JPanel(new GridLayout(2, 1, 3, 3));
        pnlHeader.setBackground(CafeTheme.COLOR_BG);
        pnlHeader.add(lblJudulMenu);
        pnlHeader.add(lblHargaDasar);

        // Bagian Pilihan Opsi & Total
        JPanel pnlCenter = new JPanel(new GridLayout(4, 1, 4, 4));
        pnlCenter.setBackground(CafeTheme.COLOR_CARD_BG);
        pnlCenter.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(CafeTheme.COLOR_BORDER, 1),
                BorderFactory.createEmptyBorder(10, 15, 10, 15)
        ));
        pnlCenter.add(chkExtraShot);
        pnlCenter.add(chkOatMilk);
        pnlCenter.add(chkCaramelDrizzle);
        pnlCenter.add(lblTotalDisplay);

        // Bagian Tombol Aksi
        JPanel pnlButtons = new JPanel(new GridLayout(1, 3, 8, 8));
        pnlButtons.setBackground(CafeTheme.COLOR_BG);
        pnlButtons.add(btnKembali);
        pnlButtons.add(btnHitung);
        pnlButtons.add(btnSimpan);

        add(pnlHeader, BorderLayout.NORTH);
        add(pnlCenter, BorderLayout.CENTER);
        add(pnlButtons, BorderLayout.SOUTH);
    }

    private void setupEvents() {
        // Tombol Hitung Total
        btnHitung.addActionListener(e -> perbaruiLabelTotal());

        // Tombol Kembali
        btnKembali.addActionListener(e -> {
            resetForm();
            mainApp.tampilkanHalaman(MainApp.HALAMAN_MENU);
        });

        // Tombol Simpan Order
        btnSimpan.addActionListener(e -> prosesSimpanOrder());
    }

    public void setMenu(String namaMenu, int hargaDasar) {
        this.namaMenuAktif = namaMenu;
        this.hargaDasarAktif = hargaDasar;
        lblJudulMenu.setText("Detail Pesanan: " + namaMenuAktif);
        lblHargaDasar.setText("Harga Dasar: " + formatUang(hargaDasarAktif));
        resetForm();
    }

    private int hitungTotal() {
        int total = hargaDasarAktif;
        if (chkExtraShot.isSelected()) total += BIAYA_EXTRA_SHOT;
        if (chkOatMilk.isSelected()) total += BIAYA_OAT_MILK;
        if (chkCaramelDrizzle.isSelected()) total += BIAYA_CARAMEL_DRIZZLE;
        return total;
    }

    private void perbaruiLabelTotal() {
        int total = hitungTotal();
        lblTotalDisplay.setText("Total: " + formatUang(total));
    }

    public void resetForm() {
        chkExtraShot.setSelected(false);
        chkOatMilk.setSelected(false);
        chkCaramelDrizzle.setSelected(false);
        lblTotalDisplay.setText("Total: " + formatUang(hargaDasarAktif));
    }

    private void prosesSimpanOrder() {
        int total = hitungTotal();

        // Memuat custom icon
        ImageIcon customIcon = null;
        String iconPath = "assets/img/coffee.png";
        if (new File(iconPath).exists()) {
            Image img = new ImageIcon(iconPath).getImage().getScaledInstance(48, 48, Image.SCALE_SMOOTH);
            customIcon = new ImageIcon(img);
        }

        String pesanSukses = String.format(
                "Pesanan Berhasil Disimpan!\n\nMenu: %s\nTotal Pembayaran: %s\n\nSilakan arahkan pelanggan ke kasir.",
                namaMenuAktif, formatUang(total)
        );

        JOptionPane.showMessageDialog(
                this,
                pesanSukses,
                "Order Sukses",
                JOptionPane.PLAIN_MESSAGE,
                customIcon
        );

        // Setelah simpan, reset form dan kembali ke katalog
        resetForm();
        mainApp.tampilkanHalaman(MainApp.HALAMAN_MENU);
    }

    private String formatUang(int nominal) {
        return formatRupiah.format(nominal);
    }
}
