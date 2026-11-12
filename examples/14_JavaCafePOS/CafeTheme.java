package examples.javacafepos;

import java.awt.Color;
import java.awt.Font;

/**
 * Tema Terpusat untuk Aplikasi JavaCafe POS
 */
public final class CafeTheme {
    private CafeTheme() {}

    // Warna
    public static final Color COLOR_PRIMARY = new Color(30, 58, 138);       // Navy 800
    public static final Color COLOR_PRIMARY_DARK = new Color(15, 23, 42);   // Slate 900
    public static final Color COLOR_ACCENT = new Color(245, 158, 11);       // Amber 500
    public static final Color COLOR_ACCENT_HOVER = new Color(217, 119, 6);  // Amber 600
    public static final Color COLOR_BG = new Color(248, 250, 252);          // Slate 50
    public static final Color COLOR_CARD_BG = Color.WHITE;
    public static final Color COLOR_TEXT_MAIN = new Color(15, 23, 42);
    public static final Color COLOR_TEXT_MUTED = new Color(100, 116, 139);
    public static final Color COLOR_BORDER = new Color(226, 232, 240);

    // Font
    public static final Font FONT_HEADER = new Font("Segoe UI", Font.BOLD, 17);
    public static final Font FONT_SUBHEADER = new Font("Segoe UI", Font.BOLD, 14);
    public static final Font FONT_BODY = new Font("Segoe UI", Font.PLAIN, 13);
    public static final Font FONT_BUTTON = new Font("Segoe UI", Font.BOLD, 12);
    public static final Font FONT_PRICE = new Font("Segoe UI", Font.BOLD, 15);

    // Dimensi
    public static final int WINDOW_WIDTH = 520;
    public static final int WINDOW_HEIGHT = 350;
}
