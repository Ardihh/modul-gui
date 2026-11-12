# -*- coding: utf-8 -*-
from generator_modules.utils import nav_buttons
from generator_modules.site_data import CHEATSHEET_DATA, CHECKLIST_ITEMS, QUIZ_QUESTIONS, GLOSSARY_ITEMS

def get_cheatsheet():
    tables_html = ""
    for sec in CHEATSHEET_DATA:
        rows_html = ""
        for method, desc in sec["rows"]:
            rows_html += f'''
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.65rem; font-family: monospace; font-weight: 600; color: var(--primary);">{method}</td>
              <td style="padding: 0.65rem; color: var(--text-main);">{desc}</td>
            </tr>
            '''
        tables_html += f'''
        <div style="margin-bottom: 2rem; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--card-shadow);">
          <div style="background: var(--primary-subtle); padding: 0.75rem 1.25rem; font-weight: 700; color: var(--primary); font-size: 1rem; border-bottom: 1px solid var(--primary-border);">
            📦 {sec["category"]}
          </div>
          <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem;">
            <thead>
              <tr style="background: var(--bg-primary); text-align: left; font-size: 0.8rem; text-transform: uppercase; color: var(--text-muted);">
                <th style="padding: 0.65rem 1.25rem; width: 45%;">Method / Sintaks</th>
                <th style="padding: 0.65rem 1.25rem;">Kegunaan & Efek</th>
              </tr>
            </thead>
            <tbody>
              {rows_html}
            </tbody>
          </table>
        </div>
        '''

    return f'''
    <article class="chapter-article" id="cheatsheet">
      <div class="chapter-badge">📑 Lembar Referensi Cepat</div>
      <h1 class="chapter-title">Cheat Sheet Ringkas Java Swing</h1>
      <p class="chapter-lead">
        Rangkuman satu halaman seluruh method sakti, properti komponen, dan pola arsitektur penting yang paling sering digunakan selama praktikum GUI Swing. Simpan halaman ini sebagai contekan belajar Anda!
      </p>

      {tables_html}

      {nav_buttons('bab-14', 'Bab 14: Panduan Debugging & Error Populer', 'checklist', 'Checklist Kesiapan Jurnal')}
    </article>
    '''

def get_checklist():
    items_html = ""
    for idx, item in enumerate(CHECKLIST_ITEMS, 1):
        items_html += f'''
        <label style="display: flex; align-items: flex-start; gap: 0.85rem; padding: 0.85rem 1rem; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-sm); margin-bottom: 0.65rem; cursor: pointer; transition: background 0.15s;">
          <input type="checkbox" style="margin-top: 0.3rem; width: 18px; height: 18px; accent-color: var(--primary);">
          <span style="font-size: 0.92rem; color: var(--text-main); line-height: 1.5;">{item}</span>
        </label>
        '''

    return f'''
    <article class="chapter-article" id="checklist">
      <div class="chapter-badge">✅ Persiapan Mandiri</div>
      <h1 class="chapter-title">Checklist Kesiapan Jurnal Praktikum</h1>
      <p class="chapter-lead">
        Sebelum membuka lembar soal tugas jurnal, uji kesiapan pemahaman konsep Anda secara mandiri dengan mencentang daftar periksa di bawah ini.
      </p>

      <div class="callout callout-info">
        <div class="callout-header">📋 Panduan Self-Assessment</div>
        <p>
          Jika seluruh kotak di bawah ini sudah berhasil Anda centang dengan penuh keyakinan, Anda telah memiliki 100% bekal pengetahuan teknis yang dibutuhkan untuk menyelesaikan tugas jurnal dengan nilai maksimal!
        </p>
      </div>

      <div style="margin: 2rem 0;">
        {items_html}
      </div>

      {nav_buttons('cheatsheet', 'Cheat Sheet Ringkas', 'kuis', 'Kuis Interaktif (12 Soal)')}
    </article>
    '''

def get_kuis():
    questions_html = ""
    for q_idx, q in enumerate(QUIZ_QUESTIONS):
        opts_html = ""
        for o_idx, opt in enumerate(q["options"]):
            letter = chr(65 + o_idx) # A, B, C, D
            opts_html += f'''
            <div class="quiz-option-label" data-opt="{o_idx}">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; border-radius: 50%; background: var(--border-color); font-weight: 700; font-size: 0.78rem; flex-shrink: 0;">{letter}</span>
              <span>{opt}</span>
            </div>
            '''

        questions_html += f'''
        <div class="quiz-question-card" data-correct="{q["correct"]}">
          <div class="quiz-question-title">{q["question"]}</div>
          <div class="quiz-options">
            {opts_html}
          </div>
          <div class="quiz-explanation" data-explain="{q["explanation"]}"></div>
        </div>
        '''

    return f'''
    <article class="chapter-article" id="kuis">
      <div class="chapter-badge">🎯 Evaluasi Pemahaman</div>
      <h1 class="chapter-title">Kuis Pilihan Ganda Interaktif</h1>
      <p class="chapter-lead">
        Uji penguasaan Anda seputar konsep GUI Swing, siklus event, arsitektur modular, dan teknik clean code melalui 12 soal pilihan ganda di bawah ini. Jawaban Anda akan langsung dinilai beserta pembahasan lengkapnya!
      </p>

      <div class="quiz-container">
        {questions_html}

        <div class="quiz-result-banner">
          <div style="font-size: 1.1rem; font-weight: 700; color: var(--primary);">SKOR AKHIR ANDA</div>
          <div class="quiz-score-number">0 / 100</div>
          <p class="quiz-score-remark" style="font-weight: 600; color: var(--text-main); margin-bottom: 1.25rem;"></p>
          <button class="btn-reset-quiz swing-btn swing-btn-primary" type="button" style="padding: 0.6rem 1.5rem; cursor: pointer;">
            🔄 Ulangi Kuis
          </button>
        </div>
      </div>

      {nav_buttons('checklist', 'Checklist Kesiapan Jurnal', 'glosarium', 'Glosarium Istilah')}
    </article>
    '''

def get_glosarium():
    items_html = ""
    for item in GLOSSARY_ITEMS:
        items_html += f'''
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1rem 1.25rem; margin-bottom: 0.75rem;">
          <dt style="font-weight: 700; color: var(--primary); font-size: 1rem; margin-bottom: 0.25rem;">
            {item["term"]}
          </dt>
          <dd style="color: var(--text-main); font-size: 0.9rem; line-height: 1.5; margin-left: 0;">
            {item["def"]}
          </dd>
        </div>
        '''

    return f'''
    <article class="chapter-article" id="glosarium">
      <div class="chapter-badge">📖 Kamus Praktikum</div>
      <h1 class="chapter-title">Glosarium Istilah GUI Java Swing</h1>
      <p class="chapter-lead">
        Daftar istilah dan kosakata teknis penting yang wajib dipahami oleh mahasiswa saat mempelajari Graphical User Interface di ekosistem Java.
      </p>

      <dl style="margin: 2rem 0;">
        {items_html}
      </dl>

      {nav_buttons('kuis', 'Kuis Interaktif', 'referensi', 'Daftar Referensi')}
    </article>
    '''

def get_referensi():
    return f'''
    <article class="chapter-article" id="referensi">
      <div class="chapter-badge">🔗 Sumber Pustaka</div>
      <h1 class="chapter-title">Daftar Referensi & Dokumentasi Resmi</h1>
      <p class="chapter-lead">
        Bahan bacaan lanjutan, standar dokumentasi resmi Oracle, dan buku rujukan akademis Pemrograman Berorientasi Objek.
      </p>

      <div style="display: flex; flex-direction: column; gap: 1rem; margin: 2rem 0;">
        
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: var(--primary); font-size: 1.05rem;">
            1. Oracle Official Java Tutorials: Creating a GUI With Swing
          </h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 0.5rem;">
            Panduan komprehensif resmi dari Oracle mengenai hierarki komponen, arsitektur Event Dispatch Thread, dan layout manager standar.
          </p>
          <a href="https://docs.oracle.com/javase/tutorial/uiswing/" target="_blank" rel="noopener noreferrer" style="color: var(--primary-light); font-weight: 600; font-size: 0.88rem; text-decoration: none;">
            Buka Dokumentasi Oracle Swing &rarr;
          </a>
        </div>

        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: var(--primary); font-size: 1.05rem;">
            2. Java SE 17 & 21 API Specifications (Package javax.swing)
          </h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 0.5rem;">
            Dokumentasi referensi teknis method, field, dan interface dari kelas JFrame, JPanel, JButton, JCheckBox, dan CardLayout.
          </p>
          <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/package-summary.html" target="_blank" rel="noopener noreferrer" style="color: var(--primary-light); font-weight: 600; font-size: 0.88rem; text-decoration: none;">
            Buka Java SE API Docs &rarr;
          </a>
        </div>

        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem;">
          <h3 style="margin-top: 0; color: var(--primary); font-size: 1.05rem;">
            3. Deitel, P. & Deitel, H. — Java How to Program (Early Objects), 11th Edition
          </h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 0;">
            Buku referensi standar akademis bab "GUI Components: Part 1 & Part 2" yang membahas Event-Driven Architecture dan teknik Clean Code.
          </p>
        </div>

      </div>

      <div class="callout callout-tip">
        <div class="callout-header">🎓 Selamat Belajar & Selamat Praktikum!</div>
        <p>
          Anda telah menyelesaikan seluruh materi belajar Modul 3. Kini Anda telah siap menaklukkan tugas Jurnal Modul 3 secara mandiri dengan hasil terbaik. Sukses selalu untuk Anda!
        </p>
      </div>

      {nav_buttons('glosarium', 'Glosarium Istilah', 'beranda', 'Kembali ke Beranda')}
    </article>
    '''

print("chapters_appendix.py ready.")
