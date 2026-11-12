package examples.jpanelmodular;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;

/**
 * Contoh 03a: MenuPanel
 * Sebuah panel kustom yang menerima referensi frame induknya.
 */
public class MenuPanel extends JPanel {

    // Menyimpan referensi ke frame induk agar dapat memicu method pada frame
    private final AppFrame parentFrame;

    public MenuPanel(AppFrame parentFrame) {
        this.parentFrame = parentFrame;

        // Mengatur layout panel
        setLayout(new BorderLayout(10, 10));
        setBackground(new Color(241, 245, 249));

        initUI();
    }

    private void initUI() {
        JLabel titleLabel = new JLabel("Menu Pilihan JavaCafe", SwingConstants.CENTER);
        titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 16));
        add(titleLabel, BorderLayout.NORTH);

        JLabel descLabel = new JLabel("Silakan klik tombol di bawah untuk pesan:", SwingConstants.CENTER);
        add(descLabel, BorderLayout.CENTER);

        JButton orderButton = new JButton("Buka Form Pesanan");
        // Menggunakan referensi parentFrame untuk memanggil method di frame utama
        orderButton.addActionListener(e -> {
            parentFrame.tampilkanPesan("Tombol ditekan dari dalam MenuPanel!");
        });

        add(orderButton, BorderLayout.SOUTH);
    }
}
