package examples.cardlayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;

/**
 * Contoh 07: NavigasiCardDemo
 * Berpindah antar-halaman secara mulus dalam satu JFrame menggunakan CardLayout.
 */
public class NavigasiCardDemo extends JFrame {

    // Kunci string untuk mengidentifikasi setiap kartu (halaman)
    public static final String HALAMAN_MENU = "MENU";
    public static final String HALAMAN_DETAIL = "DETAIL";

    private final CardLayout cardLayout;
    private final JPanel containerKartu;

    public NavigasiCardDemo() {
        super("Sistem Navigasi CardLayout - JavaCafe");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        // 1. Buat manajer CardLayout
        cardLayout = new CardLayout();

        // 2. Buat panel kontainer yang memegang CardLayout
        containerKartu = new JPanel(cardLayout);

        // 3. Buat halaman-halaman
        JPanel panelMenu = buatPanelMenu();
        JPanel panelDetail = buatPanelDetail();

        // 4. Daftarkan halaman ke containerKartu dengan nama pengenal
        containerKartu.add(panelMenu, HALAMAN_MENU);
        containerKartu.add(panelDetail, HALAMAN_DETAIL);

        // 5. Tambahkan container utama ke frame
        add(containerKartu);

        // 6. Tampilkan halaman awal
        tampilkanHalaman(HALAMAN_MENU);
    }

    // Method publik untuk memudahkan perpindahan kartu dari manapun
    public void tampilkanHalaman(String namaHalaman) {
        cardLayout.show(containerKartu, namaHalaman);
    }

    private JPanel buatPanelMenu() {
        JPanel panel = new JPanel(new BorderLayout(15, 15));
        panel.setBackground(new Color(240, 249, 255));

        JLabel title = new JLabel("Halaman 1: Katalog Menu Kafe", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 16));
        title.setForeground(new Color(3, 105, 161));

        JLabel info = new JLabel("<html><center>Pilih menu favorit Anda.<br>Klik tombol di bawah untuk membuka form pesanan.</center></html>", SwingConstants.CENTER);

        JButton btnKePesanan = new JButton("Buka Halaman Detail Pesanan ➔");
        btnKePesanan.setBackground(new Color(2, 132, 199));
        btnKePesanan.setForeground(Color.WHITE);
        btnKePesanan.setFocusPainted(false);

        // Aksi tombol untuk berpindah ke kartu DETAIL
        btnKePesanan.addActionListener(e -> tampilkanHalaman(HALAMAN_DETAIL));

        panel.add(title, BorderLayout.NORTH);
        panel.add(info, BorderLayout.CENTER);
        panel.add(btnKePesanan, BorderLayout.SOUTH);

        return panel;
    }

    private JPanel buatPanelDetail() {
        JPanel panel = new JPanel(new BorderLayout(15, 15));
        panel.setBackground(new Color(255, 251, 235));

        JLabel title = new JLabel("Halaman 2: Formulir Detail Pesanan", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 16));
        title.setForeground(new Color(180, 83, 9));

        JLabel info = new JLabel("<html><center>Di sini kasir memasukkan kustomisasi pesanan.<br>Bisa kembali lagi ke katalog kapan saja.</center></html>", SwingConstants.CENTER);

        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        JButton btnKembali = new JButton("⬅ Kembali ke Katalog");
        btnKembali.setBackground(new Color(217, 119, 6));
        btnKembali.setForeground(Color.WHITE);
        btnKembali.setFocusPainted(false);

        // Aksi tombol untuk kembali ke kartu MENU
        btnKembali.addActionListener(e -> tampilkanHalaman(HALAMAN_MENU));
        bottomPanel.add(btnKembali);

        panel.add(title, BorderLayout.NORTH);
        panel.add(info, BorderLayout.CENTER);
        panel.add(bottomPanel, BorderLayout.SOUTH);

        return panel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new NavigasiCardDemo().setVisible(true));
    }
}
