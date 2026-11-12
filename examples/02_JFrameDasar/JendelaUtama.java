package examples.jframedesar;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.Color;
import java.awt.Font;

/**
 * Contoh 02: JendelaUtama
 * Menunjukkan praktik terbaik OOP dengan membuat kelas turunan dari JFrame.
 */
public class JendelaUtama extends JFrame {

    public JendelaUtama() {
        // Mengatur judul jendela melalui super constructor atau setTitle()
        super("JavaCafe POS - Sistem Kasir V1.0");

        // 1. Ukuran jendela: 520 x 350 pixel
        setSize(520, 350);

        // 2. Program berhenti total saat jendela ditutup
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 3. Jendela otomatis muncul di tengah layar monitor
        setLocationRelativeTo(null);

        // 4. Kunci ukuran agar pengguna tidak bisa mengubah dimensi jendela
        setResizable(false);

        // 5. Inisialisasi komponen tampilan
        initComponent();
    }

    private void initComponent() {
        JLabel labelSelamat = new JLabel("Selamat Datang di JavaCafe POS", SwingConstants.CENTER);
        labelSelamat.setFont(new Font("Segoe UI", Font.BOLD, 18));
        labelSelamat.setForeground(new Color(30, 41, 59));

        // Menambahkan label ke content pane JFrame
        add(labelSelamat);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JendelaUtama app = new JendelaUtama();
            // Menampilkan jendela
            app.setVisible(true);
        });
    }
}
