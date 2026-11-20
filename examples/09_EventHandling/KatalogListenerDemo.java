package examples.eventhandling;

import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.DefaultListModel;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JSlider;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.SpinnerNumberModel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ItemEvent;

/**
 * Contoh 09B: KatalogListenerDemo
 * Menunjukkan implementasi berbagai interface listener penting di Java Swing:
 * 1. ItemListener (JCheckBox, JRadioButton, JComboBox)
 * 2. ChangeListener (JSlider, JSpinner)
 * 3. ListSelectionListener (JList)
 * 4. DocumentListener (JTextField - live text monitoring)
 */
public class KatalogListenerDemo extends JFrame {

    // Komponen
    private JCheckBox chkSusuOat;
    private JRadioButton rbDingin, rbPanas;
    private JComboBox<String> cmbUkuran;
    private JSlider sldGula;
    private JSpinner spnKuantitas;
    private JList<String> listBijiKopi;
    private JTextField txtCatatan;

    // Label hasil pemantauan
    private JLabel lblStatusItem;
    private JLabel lblStatusSlider;
    private JLabel lblStatusList;
    private JLabel lblStatusDokumen;

    public KatalogListenerDemo() {
        super("Katalog Interface Listener - JavaCafe");
        setSize(580, 520);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        initComponents();
        setupListeners();
    }

    private void initComponents() {
        JPanel root = new JPanel(new BorderLayout(10, 10));
        root.setBorder(BorderFactory.createEmptyBorder(12, 15, 12, 15));
        root.setBackground(new Color(248, 250, 252));

        JLabel title = new JLabel("Eksplorasi Interface Listener Swing", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 16));
        title.setForeground(new Color(30, 58, 138));
        root.add(title, BorderLayout.NORTH);

        // Grid tengah (4 baris kartu)
        JPanel gridCenter = new JPanel(new GridLayout(4, 1, 10, 10));
        gridCenter.setBackground(new Color(248, 250, 252));

        // 1. Panel ItemListener (CheckBox, Radio, ComboBox)
        JPanel pnlItem = new JPanel(new GridLayout(2, 2, 6, 6));
        pnlItem.setBorder(BorderFactory.createTitledBorder("1. ItemListener (State Changes)"));
        chkSusuOat = new JCheckBox("Susu Oat (+Rp 6.000)");
        rbDingin = new JRadioButton("Dingin (Ice)", true);
        rbPanas = new JRadioButton("Panas (Hot)");
        ButtonGroup bgSuhu = new ButtonGroup();
        bgSuhu.add(rbDingin);
        bgSuhu.add(rbPanas);
        cmbUkuran = new JComboBox<>(new String[]{"Regular (12 oz)", "Large (16 oz)", "Venti (20 oz)"});

        pnlItem.add(chkSusuOat);
        pnlItem.add(cmbUkuran);
        pnlItem.add(rbDingin);
        pnlItem.add(rbPanas);
        gridCenter.add(pnlItem);

        // 2. Panel ChangeListener (JSlider & JSpinner)
        JPanel pnlChange = new JPanel(new GridLayout(2, 2, 6, 6));
        pnlChange.setBorder(BorderFactory.createTitledBorder("2. ChangeListener (Slider & Spinner)"));
        sldGula = new JSlider(0, 100, 50);
        sldGula.setMajorTickSpacing(25);
        sldGula.setPaintTicks(true);
        spnKuantitas = new JSpinner(new SpinnerNumberModel(1, 1, 10, 1));
        lblStatusSlider = new JLabel("Level Gula: 50% | Cup: 1", SwingConstants.CENTER);
        lblStatusSlider.setFont(new Font("Segoe UI", Font.BOLD, 12));

        pnlChange.add(new JLabel("Tingkat Manis (% Gula):"));
        pnlChange.add(sldGula);
        pnlChange.add(new JLabel("Jumlah Pesanan (Porsi):"));
        pnlChange.add(spnKuantitas);
        gridCenter.add(pnlChange);

        // 3. Panel ListSelectionListener (JList Biji Kopi)
        JPanel pnlList = new JPanel(new BorderLayout(5, 5));
        pnlList.setBorder(BorderFactory.createTitledBorder("3. ListSelectionListener (JList Single Selection)"));
        DefaultListModel<String> modelList = new DefaultListModel<>();
        modelList.addElement("Arabika Aceh Gayo (Floral & Fruity)");
        modelList.addElement("Arabika Kintamani Bali (Citrus Acid)");
        modelList.addElement("Toraja Kalosi (Earthy & Dark Chocolate)");
        listBijiKopi = new JList<>(modelList);
        listBijiKopi.setSelectedIndex(0);
        JScrollPane scrollList = new JScrollPane(listBijiKopi);
        lblStatusList = new JLabel("Biji Terpilih: Arabika Aceh Gayo");
        pnlList.add(scrollList, BorderLayout.CENTER);
        pnlList.add(lblStatusList, BorderLayout.SOUTH);
        gridCenter.add(pnlList);

        // 4. Panel DocumentListener (JTextField Live Typing)
        JPanel pnlDoc = new JPanel(new BorderLayout(5, 5));
        pnlDoc.setBorder(BorderFactory.createTitledBorder("4. DocumentListener (Real-time Typing)"));
        txtCatatan = new JTextField();
        lblStatusDokumen = new JLabel("Catatan Barista: 0 karakter");
        lblStatusDokumen.setFont(new Font("Segoe UI", Font.ITALIC, 12));
        pnlDoc.add(txtCatatan, BorderLayout.CENTER);
        pnlDoc.add(lblStatusDokumen, BorderLayout.SOUTH);
        gridCenter.add(pnlDoc);

        root.add(gridCenter, BorderLayout.CENTER);

        // Footer Ringkasan
        lblStatusItem = new JLabel("ItemEvent: Susu Oat belum dipilih", SwingConstants.CENTER);
        lblStatusItem.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblStatusItem.setForeground(new Color(180, 83, 9));
        root.add(lblStatusItem, BorderLayout.SOUTH);

        add(root);
    }

    private void setupListeners() {
        // =====================================================================
        // 1. ItemListener pada JCheckBox
        // getStateChange() membedakan saat dicentang (SELECTED) vs dilepas (DESELECTED)
        // =====================================================================
        chkSusuOat.addItemListener(e -> {
            if (e.getStateChange() == ItemEvent.SELECTED) {
                lblStatusItem.setText("ItemEvent: Susu Oat DIPILIH (+Rp 6.000)");
            } else {
                lblStatusItem.setText("ItemEvent: Susu Oat DIBATALKAN");
            }
        });

        // ItemListener pada JComboBox
        cmbUkuran.addItemListener(e -> {
            if (e.getStateChange() == ItemEvent.SELECTED) {
                lblStatusItem.setText("ItemEvent Ukuran: " + e.getItem());
            }
        });

        // =====================================================================
        // 2. ChangeListener pada JSlider & JSpinner
        // =====================================================================
        sldGula.addChangeListener(e -> {
            int val = sldGula.getValue();
            int porsi = (Integer) spnKuantitas.getValue();
            lblStatusSlider.setText("Level Gula: " + val + "% | Cup: " + porsi);
        });

        spnKuantitas.addChangeListener(e -> {
            int val = sldGula.getValue();
            int porsi = (Integer) spnKuantitas.getValue();
            lblStatusSlider.setText("Level Gula: " + val + "% | Cup: " + porsi);
        });

        // =====================================================================
        // 3. ListSelectionListener pada JList
        // getValueIsAdjusting() memastikan event hanya diproses sekali setelah klik selesai
        // =====================================================================
        listBijiKopi.addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                String selected = listBijiKopi.getSelectedValue();
                lblStatusList.setText("Biji Terpilih: " + selected);
            }
        });

        // =====================================================================
        // 4. DocumentListener pada JTextField
        // Memantau penambahan teks (insertUpdate), penghapusan (removeUpdate), dan format (changedUpdate)
        // =====================================================================
        txtCatatan.getDocument().addDocumentListener(new DocumentListener() {
            @Override
            public void insertUpdate(DocumentEvent e) {
                updateCharCount();
            }

            @Override
            public void removeUpdate(DocumentEvent e) {
                updateCharCount();
            }

            @Override
            public void changedUpdate(DocumentEvent e) {
                updateCharCount();
            }

            private void updateCharCount() {
                int length = txtCatatan.getText().length();
                lblStatusDokumen.setText("Catatan Barista: " + length + " karakter (Live preview: \"" + txtCatatan.getText() + "\")");
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new KatalogListenerDemo().setVisible(true));
    }
}
