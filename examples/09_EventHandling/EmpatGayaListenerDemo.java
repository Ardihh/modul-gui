package examples.eventhandling;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Contoh 09A: EmpatGayaListenerDemo
 * Menunjukkan 4 cara berbeda dalam menulis ActionListener untuk kasus yang sama:
 * Counter Tambah Porsi Kopi JavaCafe.
 *
 * Gaya 1: Named Class terpisah (Outer / Inner Class biasa)
 * Gaya 2: Frame/Panel itu sendiri (implements ActionListener)
 * Gaya 3: Anonymous Inner Class
 * Gaya 4: Lambda Expression & Method Reference
 */
public class EmpatGayaListenerDemo extends JFrame implements ActionListener {

    private int jumlahPorsi = 0;
    private JLabel lblCounter;
    private JLabel lblStatusGaya;

    // Tombol untuk masing-masing gaya
    private JButton btnGaya1; // Named Class
    private JButton btnGaya2; // Implements di Frame
    private JButton btnGaya3; // Anonymous Inner Class
    private JButton btnGaya4; // Lambda Expression
    private JButton btnReset; // Method Reference

    public EmpatGayaListenerDemo() {
        super("Perbandingan 4 Gaya Penulisan Listener - JavaCafe");
        setSize(540, 380);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupListeners();
    }

    private void initComponents() {
        JPanel root = new JPanel(new BorderLayout(10, 10));
        root.setBackground(new Color(248, 250, 252));

        // Header Counter
        JPanel pnlHeader = new JPanel(new GridLayout(2, 1, 4, 4));
        pnlHeader.setBackground(new Color(30, 58, 138));

        JLabel lblJudul = new JLabel("Pemesanan Espresso Shot", SwingConstants.CENTER);
        lblJudul.setFont(new Font("Segoe UI", Font.BOLD, 15));
        lblJudul.setForeground(Color.WHITE);

        lblCounter = new JLabel("Total Porsi: 0 Cup", SwingConstants.CENTER);
        lblCounter.setFont(new Font("Segoe UI", Font.BOLD, 20));
        lblCounter.setForeground(new Color(251, 191, 36)); // Amber Gold

        pnlHeader.add(lblJudul);
        pnlHeader.add(lblCounter);

        // Body Buttons (Grid 5 baris)
        JPanel pnlButtons = new JPanel(new GridLayout(5, 1, 8, 8));
        pnlButtons.setBackground(new Color(248, 250, 252));

        btnGaya1 = new JButton("1. Tambah via Named Class (Kelas Terpisah)");
        btnGaya2 = new JButton("2. Tambah via Implements Frame (this)");
        btnGaya3 = new JButton("3. Tambah via Anonymous Inner Class");
        btnGaya4 = new JButton("4. Tambah via Lambda Expression (e -> ...)");
        btnReset = new JButton("5. Reset Porsi via Method Reference (this::reset)");

        btnGaya2.setActionCommand("TAMBAH_GAYA_2");
        btnReset.setBackground(new Color(239, 68, 68));
        btnReset.setForeground(Color.WHITE);

        pnlButtons.add(btnGaya1);
        pnlButtons.add(btnGaya2);
        pnlButtons.add(btnGaya3);
        pnlButtons.add(btnGaya4);
        pnlButtons.add(btnReset);

        // Footer Status
        lblStatusGaya = new JLabel("Pemicu Terakhir: Belum ada tombol ditekan", SwingConstants.CENTER);
        lblStatusGaya.setFont(new Font("Segoe UI", Font.ITALIC, 12));
        lblStatusGaya.setForeground(new Color(100, 116, 139));

        root.add(pnlHeader, BorderLayout.NORTH);
        root.add(pnlButtons, BorderLayout.CENTER);
        root.add(lblStatusGaya, BorderLayout.SOUTH);

        add(root);
    }

    private void setupListeners() {
        // =====================================================================
        // GAYA 1: Named Class Terpisah
        // Menggunakan objek dari kelas khusus yang mengimplementasikan ActionListener.
        // =====================================================================
        btnGaya1.addActionListener(new TambahPorsiNamedHandler(this));

        // =====================================================================
        // GAYA 2: Frame Itu Sendiri Mengimplementasikan ActionListener
        // Melewatkan 'this' ke addActionListener. Method actionPerformed()
        // milik frame ini yang akan dieksekusi saat tombol diklik.
        // =====================================================================
        btnGaya2.addActionListener(this);

        // =====================================================================
        // GAYA 3: Anonymous Inner Class
        // Menginstansiasi objek anonim dari interface ActionListener di tempat.
        // =====================================================================
        btnGaya3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                tambahPorsi();
                lblStatusGaya.setText("Pemicu: Gaya 3 (Anonymous Inner Class)");
            }
        });

        // =====================================================================
        // GAYA 4: Lambda Expression (Standar Modern Java 8+)
        // Paling ringkas karena ActionListener adalah Functional Interface (SAM).
        // =====================================================================
        btnGaya4.addActionListener(e -> {
            tambahPorsi();
            lblStatusGaya.setText("Pemicu: Gaya 4 (Lambda Expression)");
        });

        // =====================================================================
        // BONUS GAYA 4b: Method Reference (this::resetPorsi)
        // Menunjuk langsung ke method yang memiliki signature kompatibel.
        // =====================================================================
        btnReset.addActionListener(this::resetPorsi);
    }

    // Method pembantu untuk menambah porsi
    public void tambahPorsi() {
        jumlahPorsi++;
        perbaruiLabelCounter();
    }

    // Method pembantu yang dipanggil oleh Method Reference
    private void resetPorsi(ActionEvent e) {
        jumlahPorsi = 0;
        perbaruiLabelCounter();
        lblStatusGaya.setText("Pemicu: Method Reference (Reset ke 0)");
    }

    private void perbaruiLabelCounter() {
        lblCounter.setText("Total Porsi: " + jumlahPorsi + " Cup");
    }

    public void setStatusGaya(String status) {
        lblStatusGaya.setText(status);
    }

    // =========================================================================
    // Implementasi Method dari Interface ActionListener (untuk GAYA 2)
    // Menunjukkan cara SATU listener melayani banyak tombol via getSource() / getActionCommand()
    // =========================================================================
    @Override
    public void actionPerformed(ActionEvent e) {
        // Cara A: Memeriksa referensi objek sumber (e.getSource() == btnGaya2)
        if (e.getSource() == btnGaya2) {
            tambahPorsi();
            lblStatusGaya.setText("Pemicu: Gaya 2 (Frame implements ActionListener - getSource)");
        }

        // Cara B: Memeriksa ActionCommand String (Wajib pakai .equals, BUKAN == !)
        if ("TAMBAH_GAYA_2".equals(e.getActionCommand())) {
            // Bisa digunakan jika tombol tidak disimpan sebagai atribut kelas
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new EmpatGayaListenerDemo().setVisible(true));
    }
}

/**
 * Kelas terpisah untuk GAYA 1 (Named Class)
 * Menerima referensi frame agar dapat memanggil method pada frame.
 */
class TambahPorsiNamedHandler implements ActionListener {
    private final EmpatGayaListenerDemo frame;

    public TambahPorsiNamedHandler(EmpatGayaListenerDemo frame) {
        this.frame = frame;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        frame.tambahPorsi();
        frame.setStatusGaya("Pemicu: Gaya 1 (Named Class TambahPorsiNamedHandler)");
    }
}
