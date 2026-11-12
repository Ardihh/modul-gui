package examples.javacafepos;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import java.awt.CardLayout;

/**
 * MainApp (Driver Window)
 * Frame utama berukuran 520x350 dengan sistem navigasi CardLayout.
 */
public class MainApp extends JFrame {

    // Pengenal kartu untuk CardLayout
    public static final String HALAMAN_MENU = "KATALOG_MENU";
    public static final String HALAMAN_PESANAN = "DETAIL_PESANAN";

    private final CardLayout cardLayout;
    private final JPanel containerKartu;

    private final HalamanMenu halamanMenu;
    private final HalamanPesanan halamanPesanan;

    public MainApp() {
        super("JavaCafe POS - Sistem Pemesanan Kafe");

        // 1. Ukuran proporsional sesuai standar GUI desktop ringkas (520x350)
        setSize(CafeTheme.WINDOW_WIDTH, CafeTheme.WINDOW_HEIGHT);

        // 2. Berhenti saat jendela ditutup
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 3. Tampil tepat di tengah layar
        setLocationRelativeTo(null);

        // 4. Kunci ukuran jendela
        setResizable(false);

        // 5. Inisialisasi CardLayout & Container
        cardLayout = new CardLayout();
        containerKartu = new JPanel(cardLayout);

        // 6. Inisialisasi halaman-halaman dengan mengoper 'this' sebagai referensi frame utama
        halamanMenu = new HalamanMenu(this);
        halamanPesanan = new HalamanPesanan(this);

        // 7. Daftarkan kartu
        containerKartu.add(halamanMenu, HALAMAN_MENU);
        containerKartu.add(halamanPesanan, HALAMAN_PESANAN);

        // 8. Tambahkan container utama ke JFrame
        add(containerKartu);

        // 9. Tampilkan halaman menu awal
        tampilkanHalaman(HALAMAN_MENU);
    }

    /**
     * Berpindah antar-halaman menggunakan CardLayout
     */
    public void tampilkanHalaman(String namaHalaman) {
        cardLayout.show(containerKartu, namaHalaman);
    }

    /**
     * Membuka halaman pesanan dengan membawa data produk yang dipilih
     */
    public void bukaHalamanPesanan(String namaMenu, int hargaDasar) {
        halamanPesanan.setMenu(namaMenu, hargaDasar);
        tampilkanHalaman(HALAMAN_PESANAN);
    }

    public static void main(String[] args) {
        // Eksekusi di Event Dispatch Thread (EDT)
        SwingUtilities.invokeLater(() -> {
            MainApp app = new MainApp();
            app.setVisible(true);
        });
    }
}
