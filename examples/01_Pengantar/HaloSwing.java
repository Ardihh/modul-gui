package examples.pengantar;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.Font;

/**
 * Contoh 01: HaloSwing
 * Program GUI paling sederhana menggunakan Java Swing.
 */
public class HaloSwing {
    public static void main(String[] args) {
        // Menjalankan GUI di Event Dispatch Thread (EDT) untuk keamanan thread
        SwingUtilities.invokeLater(() -> {
            // 1. Membuat objek JFrame sebagai jendela utama
            JFrame frame = new JFrame("Aplikasi Pertama Saya - Java Swing");

            // 2. Menentukan aksi saat tombol close (X) ditekan
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            // 3. Menentukan ukuran jendela (lebar x tinggi dalam pixel)
            frame.setSize(400, 250);

            // 4. Meletakkan jendela tepat di tengah layar monitor
            frame.setLocationRelativeTo(null);

            // 5. Membuat komponen teks (JLabel) dengan alignment di tengah
            JLabel labelSalam = new JLabel("Halo Mahasiswa PBO! Selamat Datang di Swing.", SwingConstants.CENTER);
            labelSalam.setFont(new Font("Segoe UI", Font.BOLD, 14));

            // 6. Menambahkan label ke dalam frame
            frame.add(labelSalam);

            // 7. Menampilkan jendela ke layar pengguna
            frame.setVisible(true);
        });
    }
}
