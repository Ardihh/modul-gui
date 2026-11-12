package examples.komponendasar;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;

/**
 * Contoh 04: KomponenDemo
 * Mempelajari JLabel, JButton, dan JCheckBox serta properti visualnya.
 */
public class KomponenDemo extends JFrame {

    // 1. Deklarasi komponen sebagai atribut kelas
    private JLabel labelJudul;
    private JLabel labelStatus;
    private JCheckBox checkExtraShot;
    private JCheckBox checkSusuOat;
    private JButton btnPesan;

    public KomponenDemo() {
        super("Eksplorasi Komponen Dasar Swing");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
    }

    private void initComponents() {
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayout(5, 1, 8, 8));
        mainPanel.setBackground(new Color(248, 250, 252));

        // JLabel: Mengatur teks, font, warna, dan perataan
        labelJudul = new JLabel("Pilihan Kustomisasi Kopi", SwingConstants.CENTER);
        labelJudul.setFont(new Font("Segoe UI", Font.BOLD, 16));
        labelJudul.setForeground(new Color(15, 23, 42));

        // JCheckBox: Kotak centang untuk opsi opsional
        checkExtraShot = new JCheckBox("Tambahan Extra Espresso Shot (+Rp 5.000)");
        checkExtraShot.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        checkExtraShot.setBackground(new Color(248, 250, 252));

        checkSusuOat = new JCheckBox("Ganti ke Susu Oat Plant-Based (+Rp 7.000)");
        checkSusuOat.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        checkSusuOat.setBackground(new Color(248, 250, 252));

        // JButton: Tombol aksi dengan warna tema kustom
        btnPesan = new JButton("Konfirmasi Pilihan");
        btnPesan.setFont(new Font("Segoe UI", Font.BOLD, 13));
        btnPesan.setBackground(new Color(30, 58, 138)); // Deep Navy
        btnPesan.setForeground(Color.WHITE);
        btnPesan.setFocusPainted(false);

        labelStatus = new JLabel("Status: Belum ada opsi yang dipilih", SwingConstants.CENTER);
        labelStatus.setFont(new Font("Segoe UI", Font.ITALIC, 12));
        labelStatus.setForeground(new Color(100, 116, 139));

        // Event sederhana untuk melihat properti JCheckBox
        btnPesan.addActionListener(e -> {
            boolean extraShot = checkExtraShot.isSelected();
            boolean oatMilk = checkSusuOat.isSelected();
            labelStatus.setText(String.format("Pilihan: Extra Shot: %s | Susu Oat: %s",
                    extraShot ? "Ya" : "Tidak", oatMilk ? "Ya" : "Tidak"));
        });

        mainPanel.add(labelJudul);
        mainPanel.add(checkExtraShot);
        mainPanel.add(checkSusuOat);
        mainPanel.add(btnPesan);
        mainPanel.add(labelStatus);

        add(mainPanel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new KomponenDemo().setVisible(true));
    }
}
