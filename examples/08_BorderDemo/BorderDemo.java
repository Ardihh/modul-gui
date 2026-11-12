package examples.borderdemo;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.border.Border;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;

/**
 * Contoh 08: BorderDemo
 * Memberikan padding, garis tepi, dan estetika visual menggunakan BorderFactory.
 */
public class BorderDemo extends JFrame {

    public BorderDemo() {
        super("Penerapan Border & Padding - JavaCafe");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
    }

    private void initComponents() {
        // Panel utama dengan EmptyBorder sebagai padding luar (20px di semua sisi)
        JPanel rootPanel = new JPanel(new BorderLayout(10, 10));
        rootPanel.setBackground(new Color(248, 250, 252));
        rootPanel.setBorder(BorderFactory.createEmptyBorder(20, 25, 20, 25));

        // 1. Kartu dengan Border Garis dan Padding Dalam (Compound Border)
        JPanel kartuKopi = new JPanel(new GridLayout(3, 1, 5, 5));
        kartuKopi.setBackground(Color.WHITE);

        Border garisLuar = BorderFactory.createLineBorder(new Color(203, 213, 225), 2);
        Border bantalanDalam = BorderFactory.createEmptyBorder(12, 15, 12, 15);
        // Menggabungkan garis luar dengan padding dalam
        kartuKopi.setBorder(BorderFactory.createCompoundBorder(garisLuar, bantalanDalam));

        JLabel title = new JLabel("Espresso Roast Single Origin", SwingConstants.LEFT);
        title.setFont(new Font("Segoe UI", Font.BOLD, 15));
        title.setForeground(new Color(15, 23, 42));

        JLabel subtitle = new JLabel("Perpaduan arabika gayo dengan aroma karamel pekat.", SwingConstants.LEFT);
        subtitle.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        subtitle.setForeground(new Color(100, 116, 139));

        JLabel harga = new JLabel("Harga: Rp 22.000", SwingConstants.LEFT);
        harga.setFont(new Font("Segoe UI", Font.BOLD, 14));
        harga.setForeground(new Color(180, 83, 9));

        kartuKopi.add(title);
        kartuKopi.add(subtitle);
        kartuKopi.add(harga);

        // Tombol aksi di bawah
        JButton btnPilih = new JButton("Pilih Menu Ini");
        btnPilih.setBackground(new Color(30, 58, 138));
        btnPilih.setForeground(Color.WHITE);
        btnPilih.setFont(new Font("Segoe UI", Font.BOLD, 13));
        btnPilih.setBorder(BorderFactory.createEmptyBorder(10, 15, 10, 15));

        rootPanel.add(kartuKopi, BorderLayout.CENTER);
        rootPanel.add(btnPilih, BorderLayout.SOUTH);

        add(rootPanel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new BorderDemo().setVisible(true));
    }
}
