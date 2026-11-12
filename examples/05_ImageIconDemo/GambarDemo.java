package examples.imageicondemo;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.io.File;

/**
 * Contoh 05: GambarDemo
 * Memuat, memeriksa, melakukan resize, dan menampilkan gambar pada JLabel.
 */
public class GambarDemo extends JFrame {

    private JLabel labelGambar;
    private JLabel labelKeterangan;

    public GambarDemo() {
        super("Demo Menampilkan Gambar dengan ImageIcon");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
    }

    private void initComponents() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBackground(Color.WHITE);

        // Path relatif ke file gambar
        String pathGambar = "assets/img/coffee.png";
        File fileGambar = new File(pathGambar);

        labelGambar = new JLabel("", SwingConstants.CENTER);

        // JEBAKAN UMUM: Memastikan file benar-benar ada sebelum dimuat
        if (fileGambar.exists()) {
            ImageIcon iconAsli = new ImageIcon(pathGambar);

            // Opsional: Melakukan scaling gambar agar pas dengan tampilan
            Image gambarTerskala = iconAsli.getImage().getScaledInstance(100, 100, Image.SCALE_SMOOTH);
            labelGambar.setIcon(new ImageIcon(gambarTerskala));
            labelGambar.setText("Ikon Kopi Berhasil Dimuat");
            labelGambar.setHorizontalTextPosition(SwingConstants.CENTER);
            labelGambar.setVerticalTextPosition(SwingConstants.BOTTOM);
        } else {
            // Penanganan graceful jika file tidak ditemukan
            labelGambar.setText("⚠️ Gambar tidak ditemukan di: " + pathGambar);
            labelGambar.setForeground(Color.RED);
        }

        labelKeterangan = new JLabel("Contoh gambar produk JavaCafe POS", SwingConstants.CENTER);
        labelKeterangan.setFont(new Font("Segoe UI", Font.ITALIC, 13));

        panel.add(labelGambar, BorderLayout.CENTER);
        panel.add(labelKeterangan, BorderLayout.SOUTH);

        add(panel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new GambarDemo().setVisible(true));
    }
}
