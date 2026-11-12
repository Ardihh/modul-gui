package examples.cleancode;

import java.awt.Color;
import java.awt.Font;

/**
 * Kelas Utilitas Tema Terpusat (Design System)
 * Menyediakan konstanta statis untuk warna, font, dan ukuran
 * agar seluruh tampilan aplikasi konsisten dan mudah diubah sewaktu-waktu.
 */
public final class CafeTheme {

    // Konstruktor privat mencegah instansiasi kelas utilitas
    private CafeTheme() {}

    // Palet Warna Brand
    public static final Color COLOR_PRIMARY = new Color(30, 58, 138);     // Deep Navy
    public static final Color COLOR_PRIMARY_DARK = new Color(15, 23, 42); // Slate 900
    public static final Color COLOR_ACCENT = new Color(245, 158, 11);     // Warm Amber/Gold
    public static final Color COLOR_BACKGROUND = new Color(248, 250, 252);// Light Slate
    public static final Color COLOR_CARD_BG = Color.WHITE;
    public static final Color COLOR_TEXT_MAIN = new Color(15, 23, 42);
    public static final Color COLOR_TEXT_MUTED = new Color(100, 116, 139);
    public static final Color COLOR_BORDER = new Color(226, 232, 240);

    // Tipografi Standar
    public static final Font FONT_TITLE = new Font("Segoe UI", Font.BOLD, 18);
    public static final Font FONT_SUBTITLE = new Font("Segoe UI", Font.BOLD, 14);
    public static final Font FONT_BODY = new Font("Segoe UI", Font.PLAIN, 13);
    public static final Font FONT_BUTTON = new Font("Segoe UI", Font.BOLD, 13);
    public static final Font FONT_PRICE = new Font("Segoe UI", Font.BOLD, 16);

    // Dimensi Standar Window
    public static final int WINDOW_WIDTH = 520;
    public static final int WINDOW_HEIGHT = 350;
}
