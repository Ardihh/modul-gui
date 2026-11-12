package examples.dialogjoptionpane;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Image;
import java.io.File;

/**
 * Contoh 10: DialogDemo
 * Menampilkan pesan konfirmasi, peringatan, dan dialog sukses dengan Custom Icon.
 */
public class DialogDemo extends JFrame {

    public DialogDemo() {
        super("Eksplorasi Dialog JOptionPane - JavaCafe");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
    }

    private void initComponents() {
        JPanel panel = new JPanel(new GridLayout(5, 1, 10, 10));
        panel.setBackground(new Color(248, 250, 252));

        JLabel title = new JLabel("Pilih Jenis Dialog JOptionPane", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 15));

        JButton btnInfo = new JButton("1. Tampilkan Dialog Informasi");
        JButton btnWarning = new JButton("2. Tampilkan Dialog Peringatan (Warning)");
        JButton btnError = new JButton("3. Tampilkan Dialog Error");
        JButton btnCustomIcon = new JButton("4. Tampilkan Dialog Sukses (Ikon Kustom)");

        // 1. Pesan Informasi
        btnInfo.addActionListener(e -> {
            JOptionPane.showMessageDialog(
                    this,
                    "Pesanan meja #04 telah masuk ke dapur barista.",
                    "Status Pesanan",
                    JOptionPane.INFORMATION_MESSAGE
            );
        });

        // 2. Pesan Peringatan
        btnWarning.addActionListener(e -> {
            JOptionPane.showMessageDialog(
                    this,
                    "Stok biji kopi Robusta tersisa kurang dari 500 gram!",
                    "Peringatan Stok",
                    JOptionPane.WARNING_MESSAGE
            );
        });

        // 3. Pesan Error
        btnError.addActionListener(e -> {
            JOptionPane.showMessageDialog(
                    this,
                    "Gagal memproses pembayaran. Saldo kartu tidak cukup.",
                    "Kesalahan Transaksi",
                    JOptionPane.ERROR_MESSAGE
            );
        });

        // 4. Dialog dengan Custom Icon (ImageIcon)
        btnCustomIcon.addActionListener(e -> {
            ImageIcon customIcon = null;
            String iconPath = "assets/img/coffee.png";
            if (new File(iconPath).exists()) {
                Image img = new ImageIcon(iconPath).getImage().getScaledInstance(48, 48, Image.SCALE_SMOOTH);
                customIcon = new ImageIcon(img);
            }

            JOptionPane.showMessageDialog(
                    this,
                    "Transaksi Pemesanan Kopi Berhasil Disimpan!\nTotal Pembayaran: Rp 35.000",
                    "Order Sukses",
                    JOptionPane.PLAIN_MESSAGE,
                    customIcon
            );
        });

        panel.add(title);
        panel.add(btnInfo);
        panel.add(btnWarning);
        panel.add(btnError);
        panel.add(btnCustomIcon);

        add(panel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new DialogDemo().setVisible(true));
    }
}
