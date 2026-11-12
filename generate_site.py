# -*- coding: utf-8 -*-
"""
Script Pembangun Utama index.html untuk Modul 3 GUI Java Swing
Teknik Informatika - Fakultas Teknik - Universitas Mataram
"""
import os
import html

from generator_modules.utils import get_code, code_box, nav_buttons

# Import modul bab & data
from generator_modules.site_data import NAV_SECTIONS
from generator_modules.chapters_part1 import get_beranda, get_bab1, get_bab2, get_bab3, get_bab4
from generator_modules.chapters_part2 import get_bab5, get_bab6, get_bab7, get_bab8, get_bab9
from generator_modules.chapters_part3 import get_bab10, get_bab11, get_bab12, get_bab13, get_bab14
from generator_modules.chapters_appendix import get_cheatsheet, get_checklist, get_kuis, get_glosarium, get_referensi

def build_sidebar():
    sidebar_html = ""
    for sec in NAV_SECTIONS:
        sidebar_html += f'<div class="sidebar-section-title">{sec["title"]}</div>\n'
        sidebar_html += '<ul class="nav-list">\n'
        for item in sec["items"]:
            active_class = "active" if item["id"] == "beranda" else ""
            sidebar_html += f'''
            <li>
              <a href="#{item["id"]}" class="nav-link {active_class}">
                <span class="badge-num">{item["num"]}</span>
                <span>{item["title"]}</span>
              </a>
            </li>
            '''
        sidebar_html += '</ul>\n'
    return sidebar_html

def build_index_html():
    sidebar_content = build_sidebar()
    
    full_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Modul Praktikum Pemrograman Berorientasi Objek: Modul 3 GUI dengan Java Swing. Dirancang untuk mahasiswa semester awal Teknik Informatika Universitas Mataram.">
  <meta name="author" content="M. Rizki Juniardi & Tim Asisten Praktikum PBO">
  <meta name="theme-color" content="#1e3a8a">
  <title>Modul 3 GUI Java Swing - Pemrograman Berorientasi Objek</title>
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/img/logo-lab.svg">
  
  <!-- CSS Stylesheets -->
  <link rel="stylesheet" href="assets/css/prism.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="reading-progress"></div>

  <!-- Header Navbar -->
  <header class="site-header">
    <div class="header-left">
      <button class="btn-sidebar-toggle" id="sidebar-toggle" type="button" aria-label="Buka Menu Navigasi">
        ☰
      </button>
      <a href="#beranda" class="brand-link">
        <img src="assets/img/logo-lab.svg" alt="Logo Lab PBO" class="brand-logo-img">
      </a>
    </div>
    <div class="header-right">
      <button class="search-trigger-btn" id="search-trigger" type="button" aria-label="Cari Materi">
        <span>🔍</span>
        <span>Cari Modul...</span>
        <kbd>Ctrl+K</kbd>
      </button>
      <button class="theme-toggle-btn" id="theme-toggle" type="button" title="Ganti Mode Gelap/Terang" aria-label="Ganti Tema">
        🌙
      </button>
    </div>
  </header>

  <!-- Layout Wrapper -->
  <div class="site-wrapper">
    
    <!-- Sidebar Navigation -->
    <aside class="site-sidebar" id="site-sidebar">
      {sidebar_content}
    </aside>

    <!-- Main Content Articles -->
    <main class="site-main">
      {get_beranda()}
      {get_bab1()}
      {get_bab2()}
      {get_bab3()}
      {get_bab4()}
      {get_bab5()}
      {get_bab6()}
      {get_bab7()}
      {get_bab8()}
      {get_bab9()}
      {get_bab10()}
      {get_bab11()}
      {get_bab12()}
      {get_bab13()}
      {get_bab14()}
      {get_cheatsheet()}
      {get_checklist()}
      {get_kuis()}
      {get_glosarium()}
      {get_referensi()}
    </main>

  </div>

  <!-- Client-Side Search Modal -->
  <div class="search-modal-backdrop" id="search-modal">
    <div class="search-modal">
      <div class="search-input-wrapper">
        <span>🔍</span>
        <input type="text" id="search-input" class="search-input" placeholder="Ketik kata kunci (mis. JFrame, layout, border, event)..." autocomplete="off">
        <kbd style="font-size: 0.75rem; color: var(--text-muted); background: var(--bg-primary); padding: 2px 6px; border-radius: 4px; border: 1px solid var(--border-color);">ESC</kbd>
      </div>
      <ul class="search-results-list" id="search-results">
        <li style="padding: 1.5rem; text-align: center; color: var(--text-muted);">
          Ketik kata kunci untuk mencari bab, konsep, atau komponen...
        </li>
      </ul>
    </div>
  </div>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-content">
      <div class="footer-credits">
        Modul Praktikum Pemrograman Berorientasi Objek (Java)<br>
        Laboratorium Komputer Dasar & Pemrograman • Program Studi Teknik Informatika<br>
        Fakultas Teknik • Universitas Mataram
      </div>
      <div>
        Disusun & Dikembangkan oleh: <span style="font-weight: 700; color: var(--primary);">M. Rizki Juniardi (Ardi)</span> & Tim Asisten Praktikum PBO
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center;">
        <span class="footer-badge-tag">Semester Ganjil 2024/2025</span>
        <span class="footer-badge-tag">Java SE 17+ (LTS)</span>
        <span class="footer-badge-tag">Diperbarui: November 2026</span>
      </div>
    </div>
  </footer>

  <!-- JavaScript Engine -->
  <script src="assets/js/prism.min.js"></script>
  <script src="assets/js/app.js"></script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("SUCCESS: index.html has been generated successfully!")

if __name__ == "__main__":
    build_index_html()
