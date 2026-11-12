package examples.eventhandling;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Contoh 09: EventHandlingDemo
 * Membandingkan Anonymous Inner Class vs Lambda Expression dalam ActionListener,
 * serta membaca kondisi isSelected() pada JCheckBox.
 */
public class EventHandlingDemo extends JFrame {

    private JCheckBox chkSyrupVanilla;
    private JCheckBox chkJellyBoba;
    private JButton btnCekAnonymous;
    private JButton btnCekLambda;
    private JButton btnResetPilihan;
    private JLabel lblHasil;

    public EventHandlingDemo() {
        super("Event Handling & ActionListener - JavaCafe");
        setSize(520, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupEvents();
    }

    private void initComponents() {
        JPanel panel = new JPanel(new GridLayout(6, 1, 6, 6));
        panel.setBackground(new Color(248, 250, 252));

        JLabel title = new JLabel("Demo Event Handling (Topping Kopi)", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 15));

        chkSyrupVanilla = new JCheckBox("Sirup Vanilla (+Rp 4.000)");
        chkJellyBoba = new JCheckBox("Jelly Boba (+Rp 5.000)");

        btnCekAnonymous = new JButton("Periksa Pilihan (Cara 1: Anonymous Class)");
        btnCekLambda = new JButton("Periksa Pilihan (Cara 2: Lambda Expression)");
        btnResetPilihan = new JButton("Reset Semua CheckBox");

        lblHasil = new JLabel("Status: Belum ada event yang dipicu", SwingConstants.CENTER);
        lblHasil.setFont(new Font("Segoe UI", Font.BOLD, 13));
        lblHasil.setForeground(new Color(30, 58, 138));

        panel.add(title);
        panel.add(chkSyrupVanilla);
        panel.add(chkJellyBoba);
        panel.add(btnCekAnonymous);
        panel.add(btnCekLambda);
        panel.add(btnResetPilihan);

        add(panel);
    }

    private void setupEvents() {
        // Cara 1: Menggunakan Anonymous Inner Class (Gaya Lama Java 7 ke bawah)
        btnCekAnonymous.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                boolean vanilla = chkSyrupVanilla.isSelected();
                boolean boba = chkJellyBoba.isSelected();
                lblHasil.setText("[Anonymous] Vanilla: " + vanilla + " | Boba: " + boba);
            }
        });

        // Cara 2: Menggunakan Lambda Expression (Modern, Ringkas, Standar Java 8+)
        btnCekLambda.addActionListener(e -> {
            boolean vanilla = chkSyrupVanilla.isSelected();
            boolean boba = chkJellyBoba.isSelected();
            lblHasil.setText("[Lambda] Vanilla: " + vanilla + " | Boba: " + boba);
        });

        // Event untuk Reset: Mengembalikan state CheckBox ke tidak tercentang
        btnResetPilihan.addActionListener(e -> {
            chkSyrupVanilla.setSelected(false);
            chkJellyBoba.setSelected(false);
            lblHasil.setText("Pilihan telah di-reset!");
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new EventHandlingDemo().setVisible(true));
    }
}
