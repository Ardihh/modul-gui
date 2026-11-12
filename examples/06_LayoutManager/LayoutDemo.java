package examples.layoutmanager;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;

/**
 * Contoh 06: LayoutDemo
 * Menggabungkan BorderLayout, GridLayout, dan FlowLayout (Nested Layout).
 */
public class LayoutDemo extends JFrame {

    public LayoutDemo() {
        super("Eksplorasi Layout Manager & Nested Panels");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initLayout();
    }

    private void initLayout() {
        // 1. Container Utama menggunakan BorderLayout
        JPanel mainPanel = new JPanel(new BorderLayout(8, 8));
        mainPanel.setBackground(new Color(241, 245, 249));

        // 2. BAGIAN ATAS (NORTH): Header
        JLabel headerLabel = new JLabel("JavaCafe POS - Nested Layout Demo", SwingConstants.CENTER);
        headerLabel.setFont(new Font("Segoe UI", Font.BOLD, 15));
        headerLabel.setOpaque(true);
        headerLabel.setBackground(new Color(30, 58, 138));
        headerLabel.setForeground(Color.WHITE);
        mainPanel.add(headerLabel, BorderLayout.NORTH);

        // 3. BAGIAN TENGAH (CENTER): Grid 2x2 Menu Minuman
        JPanel gridMenuPanel = new JPanel(new GridLayout(2, 2, 8, 8));
        gridMenuPanel.setBackground(new Color(241, 245, 249));

        JButton btn1 = new JButton("1. Espresso (Rp 18.000)");
        JButton btn2 = new JButton("2. Americano (Rp 20.000)");
        JButton btn3 = new JButton("3. Caffe Latte (Rp 24.000)");
        JButton btn4 = new JButton("4. Caramel Macchiato (Rp 28.000)");

        gridMenuPanel.add(btn1);
        gridMenuPanel.add(btn2);
        gridMenuPanel.add(btn3);
        gridMenuPanel.add(btn4);

        mainPanel.add(gridMenuPanel, BorderLayout.CENTER);

        // 4. BAGIAN BAWAH (SOUTH): FlowLayout untuk Tombol Aksi
        JPanel actionPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 10, 5));
        actionPanel.setBackground(new Color(226, 232, 240));

        JButton btnBatal = new JButton("Batal");
        JButton btnLanjut = new JButton("Lanjut ke Pembayaran");
        btnLanjut.setBackground(new Color(245, 158, 11));
        btnLanjut.setForeground(Color.BLACK);

        actionPanel.add(btnBatal);
        actionPanel.add(btnLanjut);

        mainPanel.add(actionPanel, BorderLayout.SOUTH);

        add(mainPanel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new LayoutDemo().setVisible(true));
    }
}
