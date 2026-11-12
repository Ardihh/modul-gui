package examples.jpanelmodular;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

/**
 * Contoh 03b: AppFrame
 * Frame utama yang menampung MenuPanel dan menyediakan method publik untuk dipanggil panel.
 */
public class AppFrame extends JFrame {

    private final MenuPanel menuPanel;

    public AppFrame() {
        super("Aplikasi Modular Swing - JavaCafe");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        // Mengirim 'this' (objek frame ini) ke constructor MenuPanel
        this.menuPanel = new MenuPanel(this);

        // Menambahkan panel ke frame
        add(menuPanel);
    }

    // Method publik yang bisa diakses oleh kelas panel anak
    public void tampilkanPesan(String pesan) {
        JOptionPane.showMessageDialog(this, pesan, "Informasi Frame", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new AppFrame().setVisible(true);
        });
    }
}
