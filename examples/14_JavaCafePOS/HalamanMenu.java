package examples.javacafepos;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.Image;
import java.io.File;

/**
 * HalamanMenu (Halaman Katalog)
 * Menampilkan daftar produk kopi yang dapat dipesan oleh pelanggan.
 */
public class HalamanMenu extends JPanel {

    private final MainApp mainApp;

    // Komponen visual
    private JLabel lblHeader;
    private JLabel lblIconKopi;
    private JLabel lblNamaMenu;
    private JLabel lblDeskripsi;
    private JLabel lblHarga;
    private JButton btnPesanSekarang;

    public HalamanMenu(MainApp mainApp) {
        this.mainApp = mainApp;

        setLayout(new BorderLayout(10, 10));
        setBackground(CafeTheme.COLOR_BG);
        setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));

        initComponents();
        setupLayout();
        setupEvents();
    }

    private void initComponents() {
        lblHeader = new JLabel("KATALOG MENU JAVACAFE", SwingConstants.CENTER);
        lblHeader.setFont(CafeTheme.FONT_HEADER);
        lblHeader.setForeground(CafeTheme.COLOR_PRIMARY);

        // Ikon Produk
        lblIconKopi = new JLabel("", SwingConstants.CENTER);
        String iconPath = "assets/img/coffee.png";
        if (new File(iconPath).exists()) {
            Image img = new ImageIcon(iconPath).getImage().getScaledInstance(64, 64, Image.SCALE_SMOOTH);
            lblIconKopi.setIcon(new ImageIcon(img));
        }

        lblNamaMenu = new JLabel("Signature Caramel Macchiato", SwingConstants.CENTER);
        lblNamaMenu.setFont(CafeTheme.FONT_SUBHEADER);
        lblNamaMenu.setForeground(CafeTheme.COLOR_TEXT_MAIN);

        lblDeskripsi = new JLabel("<html><center>Espresso lembut berpadu susu segar dan sirup vanilla,<br>diberi sentuhan saus karamel di atas busa susu.</center></html>", SwingConstants.CENTER);
        lblDeskripsi.setFont(CafeTheme.FONT_BODY);
        lblDeskripsi.setForeground(CafeTheme.COLOR_TEXT_MUTED);

        lblHarga = new JLabel("Harga: Rp 28.000", SwingConstants.CENTER);
        lblHarga.setFont(CafeTheme.FONT_PRICE);
        lblHarga.setForeground(CafeTheme.COLOR_ACCENT);

        btnPesanSekarang = new JButton("Pesan Minuman Ini ➔");
        btnPesanSekarang.setFont(CafeTheme.FONT_BUTTON);
        btnPesanSekarang.setBackground(CafeTheme.COLOR_PRIMARY);
        btnPesanSekarang.setForeground(Color.WHITE);
        btnPesanSekarang.setFocusPainted(false);
    }

    private void setupLayout() {
        // Kontainer kartu tengah
        JPanel cardPanel = new JPanel(new GridLayout(4, 1, 4, 4));
        cardPanel.setBackground(CafeTheme.COLOR_CARD_BG);
        cardPanel.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(CafeTheme.COLOR_BORDER, 1),
                BorderFactory.createEmptyBorder(10, 15, 10, 15)
        ));

        cardPanel.add(lblIconKopi);
        cardPanel.add(lblNamaMenu);
        cardPanel.add(lblDeskripsi);
        cardPanel.add(lblHarga);

        add(lblHeader, BorderLayout.NORTH);
        add(cardPanel, BorderLayout.CENTER);
        add(btnPesanSekarang, BorderLayout.SOUTH);
    }

    private void setupEvents() {
        // Tombol menuju ke halaman form pesanan
        btnPesanSekarang.addActionListener(e -> {
            mainApp.bukaHalamanPesanan("Signature Caramel Macchiato", 28000);
        });
    }
}
