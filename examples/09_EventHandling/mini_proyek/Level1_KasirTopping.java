package examples.eventhandling.mini_proyek;

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
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * Mini-Proyek Level 1: Kasir Topping Sederhana
 * Memadukan ItemListener (respons instan saat checkbox diklik)
 * dengan ActionListener (eksekusi tombol hitung dan simpan).
 */
public class Level1_KasirTopping extends JFrame {

    private final int HARGA_DASAR = 20000; // Caffe Latte Dasar
    private final int BIAYA_EXTRA_SHOT = 5000;
    private final int BIAYA_OAT_MILK = 6000;
    private final int BIAYA_SYRUP = 4000;

    private JCheckBox chkExtraShot;
    private JCheckBox chkOatMilk;
    private JCheckBox chkSyrup;
    private JLabel lblSubtotalLive;
    private JButton btnBayar;
    private JButton btnReset;

    private final NumberFormat nf = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("id-ID"));

    public Level1_KasirTopping() {
        super("Mini-Proyek 1: Kasir Topping (ItemListener + ActionListener)");
        setSize(480, 320);
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

        // Header
        JPanel pnlHeader = new JPanel(new GridLayout(2, 1, 3, 3));
        pnlHeader.setBackground(new Color(248, 250, 252));
        JLabel title = new JLabel("Pemesanan Caffe Latte", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 16));
        title.setForeground(new Color(30, 58, 138));
        JLabel lblDasar = new JLabel("Harga Dasar: " + nf.format(HARGA_DASAR), SwingConstants.CENTER);
        pnlHeader.add(title);
        pnlHeader.add(lblDasar);

        // Body: Checkboxes
        JPanel pnlAddon = new JPanel(new GridLayout(4, 1, 4, 4));
        pnlAddon.setBackground(Color.WHITE);
        pnlAddon.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(226, 232, 240), 1),
                BorderFactory.createEmptyBorder(8, 12, 8, 12)
        ));

        chkExtraShot = new JCheckBox("Extra Espresso Shot (+ " + nf.format(BIAYA_EXTRA_SHOT) + ")");
        chkOatMilk = new JCheckBox("Ganti Susu Oat (+ " + nf.format(BIAYA_OAT_MILK) + ")");
        chkSyrup = new JCheckBox("Sirup Vanilla (+ " + nf.format(BIAYA_SYRUP) + ")");
        chkExtraShot.setBackground(Color.WHITE);
        chkOatMilk.setBackground(Color.WHITE);
        chkSyrup.setBackground(Color.WHITE);

        lblSubtotalLive = new JLabel("Estimasi Total: " + nf.format(HARGA_DASAR), SwingConstants.RIGHT);
        lblSubtotalLive.setFont(new Font("Segoe UI", Font.BOLD, 14));
        lblSubtotalLive.setForeground(new Color(217, 119, 6));

        pnlAddon.add(chkExtraShot);
        pnlAddon.add(chkOatMilk);
        pnlAddon.add(chkSyrup);
        pnlAddon.add(lblSubtotalLive);

        // Footer: Buttons
        JPanel pnlButtons = new JPanel(new GridLayout(1, 2, 8, 8));
        pnlButtons.setBackground(new Color(248, 250, 252));
        btnReset = new JButton("Reset");
        btnBayar = new JButton("Bayar Sekarang");
        btnBayar.setBackground(new Color(30, 58, 138));
        btnBayar.setForeground(Color.WHITE);

        pnlButtons.add(btnReset);
        pnlButtons.add(btnBayar);

        root.add(pnlHeader, BorderLayout.NORTH);
        root.add(pnlAddon, BorderLayout.CENTER);
        root.add(pnlButtons, BorderLayout.SOUTH);

        add(root);
    }

    private void setupListeners() {
        // 1. ItemListener bersama untuk ketiga CheckBox (Live Update saat dicentang/dilepas)
        ItemListener itemHandler = e -> {
            int total = hitungTotal();
            lblSubtotalLive.setText("Estimasi Total: " + nf.format(total));
        };

        chkExtraShot.addItemListener(itemHandler);
        chkOatMilk.addItemListener(itemHandler);
        chkSyrup.addItemListener(itemHandler);

        // 2. ActionListener untuk Tombol Bayar
        btnBayar.addActionListener(e -> {
            int total = hitungTotal();
            String rincian = String.format("Pesanan Caffe Latte Berhasil!\nTotal Akhir: %s\nSilakan cetak struk.", nf.format(total));
            JOptionPane.showMessageDialog(this, rincian, "Transaksi Sukses", JOptionPane.INFORMATION_MESSAGE);
        });

        // 3. ActionListener untuk Tombol Reset
        btnReset.addActionListener(e -> {
            chkExtraShot.setSelected(false);
            chkOatMilk.setSelected(false);
            chkSyrup.setSelected(false);
            lblSubtotalLive.setText("Estimasi Total: " + nf.format(HARGA_DASAR));
        });
    }

    private int hitungTotal() {
        int total = HARGA_DASAR;
        if (chkExtraShot.isSelected()) total += BIAYA_EXTRA_SHOT;
        if (chkOatMilk.isSelected()) total += BIAYA_OAT_MILK;
        if (chkSyrup.isSelected()) total += BIAYA_SYRUP;
        return total;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Level1_KasirTopping().setVisible(true));
    }
}
