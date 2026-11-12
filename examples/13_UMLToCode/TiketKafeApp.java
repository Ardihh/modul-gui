package examples.umltocode;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.Font;

/**
 * Contoh 13: TiketKafeApp
 * Hasil penerjemahan UML Class Diagram sederhana menjadi implementasi kode Java Swing.
 *
 * UML Representasi:
 * ┌──────────────────────────────────────────────┐
 * │               TiketKafeApp                   │
 * ├──────────────────────────────────────────────┤
 * │ - judulEvent: String                         │
 * │ - hargaTiket: int                            │
 * │ - lblInfo: JLabel                            │
 * │ - btnBeli: JButton                           │
 * ├──────────────────────────────────────────────┤
 * │ + TiketKafeApp()                             │
 * │ - initUI(): void                             │
 * │ + pesanTiket(): void                         │
 * │ + main(args: String[]): void                 │
 * └──────────────────────────────────────────────┘
 *                     │
 *                     ▼ extends
 *             ┌───────────────┐
 *             │    JFrame     │
 *             └───────────────┘
 */
public class TiketKafeApp extends JFrame {

    // Atribut privat sesuai visibilitas (-) pada UML
    private final String judulEvent = "Live Acoustic Music Night";
    private final int hargaTiket = 50000;
    private JLabel lblInfo;
    private JButton btnBeli;

    // Konstruktor publik sesuai visibilitas (+) pada UML
    public TiketKafeApp() {
        super("Pemesanan Tiket Acara Kafe - Dari UML ke Kode");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initUI();
    }

    // Method privat (-) untuk inisialisasi tampilan
    private void initUI() {
        JPanel panel = new JPanel(new BorderLayout(15, 15));

        lblInfo = new JLabel(
                String.format("<html><center><h3>%s</h3>Harga Tiket Masuk: Rp %,d<br>(Sudah termasuk 1 Welcome Drink)</center></html>",
                        judulEvent, hargaTiket),
                SwingConstants.CENTER
        );
        lblInfo.setFont(new Font("Segoe UI", Font.PLAIN, 14));

        btnBeli = new JButton("Pesan Tiket Acara Sekarang");
        btnBeli.setFont(new Font("Segoe UI", Font.BOLD, 14));
        btnBeli.addActionListener(e -> pesanTiket());

        panel.add(lblInfo, BorderLayout.CENTER);
        panel.add(btnBeli, BorderLayout.SOUTH);

        add(panel);
    }

    // Method publik (+) untuk memproses tiket
    public void pesanTiket() {
        String info = String.format("Tiket berhasil dipesan untuk:\n\"%s\"\nTotal Bayar: Rp %,d",
                judulEvent, hargaTiket);
        JOptionPane.showMessageDialog(this, info, "Konfirmasi Tiket", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TiketKafeApp().setVisible(true));
    }
}
