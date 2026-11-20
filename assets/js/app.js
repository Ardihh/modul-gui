/**
 * MODUL 3 GUI JAVA SWING - JAVASCRIPT ENGINE
 * Penulis: Tim Asisten PBO Teknik Informatika UNRAM
 */

(function () {
  'use strict';

  // State
  let currentChapter = 'beranda';

  // Search Data Index
  const searchIndex = [
    { id: 'beranda', title: 'Beranda & Pengantar Modul 3', snippet: 'Peta konsep, prasyarat OOP, cara belajar Swing efektif.' },
    { id: 'bab-1', title: 'Bab 1: Pengantar GUI & Event-Driven', snippet: 'AWT vs Swing, konsep komponen & container, alur event-driven vs prosedural.' },
    { id: 'bab-2', title: 'Bab 2: Jendela Pertama dengan JFrame', snippet: 'setTitle, setSize, setDefaultCloseOperation, setLocationRelativeTo, setResizable, extends JFrame.' },
    { id: 'bab-3', title: 'Bab 3: Container Fleksibel dengan JPanel', snippet: 'Custom panel extends JPanel, passing referensi frame di constructor, komunikasi modular.' },
    { id: 'bab-4', title: 'Bab 4: Komponen Dasar (JLabel, JButton, JCheckBox)', snippet: 'Properti font, warna, perataan horizontal, teks dan ikon.' },
    { id: 'bab-5', title: 'Bab 5: Menangani Gambar dengan ImageIcon', snippet: 'Path relatif assets/, resize getScaledInstance, jebakan path file hilang di Swing.' },
    { id: 'bab-6', title: 'Bab 6: Menguasai Layout Manager', snippet: 'BorderLayout, GridLayout, FlowLayout, dan teknik nested layout panel di dalam panel.' },
    { id: 'bab-7', title: 'Bab 7: Navigasi Halaman dengan CardLayout', snippet: 'Sistem kartu bertumpuk, add kartu, cardLayout.show, beralih antar-halaman.' },
    { id: 'bab-8', title: 'Bab 8: Kerapian Tampilan dengan Border', snippet: 'BorderFactory, createEmptyBorder (padding), createLineBorder, compound border.' },
    { id: 'bab-9a', title: 'Bab 09A: Fondasi Event Handling & 4 Gaya Listener', snippet: 'Model Event, Analogi Bel Pintu, Interface OOP, 4 Gaya Penulisan, getSource vs getActionCommand.' },
    { id: 'bab-9b', title: 'Bab 09B: Katalog Lengkap Interface Listener & Adapter', snippet: 'ItemListener, MouseListener, KeyListener, FocusListener, DocumentListener, ChangeListener, ListSelectionListener, WindowListener, Adapter Classes.' },
    { id: 'bab-9c', title: 'Bab 09C: Event Playground Interaktif & 3 Mini-Proyek', snippet: 'Simulator Event Real-Time, Urutan Pemanggilan Event, 3 Mini-Proyek Kasir Bertingkat (Level 1, 2, 3), Latihan Mandiri.' },
    { id: 'bab-10', title: 'Bab 10: Dialog Pop-Up dengan JOptionPane', snippet: 'showMessageDialog, tipe pesan informasi, peringatan, error, custom icon dialog.' },
    { id: 'bab-11', title: 'Bab 11: Clean Code & Arsitektur GUI', snippet: 'Komponen sebagai field, inisialisasi bertahap, modular method, kelas Theme terpusat.' },
    { id: 'bab-12', title: 'Bab 12: Pola Perhitungan Harga & Format Rupiah', snippet: 'Base price + add-on dinamis, format mata uang rupiah, reset form ke kondisi default.' },
    { id: 'bab-13', title: 'Bab 13: Membaca UML Class Diagram GUI', snippet: 'Menerjemahkan atribut, method, visibility (+, -), inheritance, dan asosiasi ke Java.' },
    { id: 'bab-14', title: 'Bab 14: Panduan Debugging & Error Populer', snippet: 'Mengatasi NullPointerException, layout gepeng/berantakan, tombol tidak merespon, gambar hilang.' },
    { id: 'cheatsheet', title: 'Cheat Sheet Ringkas Java Swing', snippet: 'Tabel referensi cepat method sakti JFrame, JPanel, Komponen, dan Layout.' },
    { id: 'checklist', title: 'Checklist Kesiapan Jurnal Praktikum', snippet: 'Daftar periksa mandiri sebelum mengerjakan tugas jurnal praktikum.' },
    { id: 'kuis', title: 'Kuis Pilihan Ganda Interaktif', snippet: '12 soal evaluasi pemahaman GUI Swing dengan skor otomatis dan pembahasan.' },
    { id: 'glosarium', title: 'Glosarium Istilah GUI Swing', snippet: 'Kamus definisi istilah penting: EDT, LayoutManager, Listener, Container, dsb.' },
    { id: 'referensi', title: 'Daftar Referensi & Sumber Belajar', snippet: 'Dokumentasi resmi Oracle Java Swing Tutorials dan buku acuan.' }
  ];

  // DOM Elements
  const themeToggleBtn = document.getElementById('theme-toggle');
  const sidebar = document.getElementById('site-sidebar');
  const sidebarToggleBtn = document.getElementById('sidebar-toggle');
  const readingProgressBar = document.getElementById('reading-progress');
  const searchTriggerBtn = document.getElementById('search-trigger');
  const searchModal = document.getElementById('search-modal');
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');

  // ==========================================
  // 1. Dark Mode Engine
  // ==========================================
  function initTheme() {
    let savedTheme = 'light';
    try {
      savedTheme = localStorage.getItem('pbo_gui_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    } catch (e) {
      console.warn('localStorage not accessible for theme', e);
    }
    applyTheme(savedTheme);
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    if (themeToggleBtn) {
      themeToggleBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
      themeToggleBtn.setAttribute('title', theme === 'dark' ? 'Beralih ke Mode Terang' : 'Beralih ke Mode Gelap');
    }
    try {
      localStorage.setItem('pbo_gui_theme', theme);
    } catch (e) {}
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      applyTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  // ==========================================
  // 2. Hash Router
  // ==========================================
  function navigateToHash() {
    let hash = window.location.hash.replace('#', '').trim();
    if (!hash) hash = 'beranda';

    const targetArticle = document.getElementById(hash);
    if (!targetArticle) {
      hash = 'beranda';
    }

    // Toggle active article
    document.querySelectorAll('.chapter-article').forEach(art => {
      art.classList.remove('active');
    });
    const activeArt = document.getElementById(hash);
    if (activeArt) {
      activeArt.classList.add('active');
    }

    // Update active nav-link
    document.querySelectorAll('.nav-link').forEach(link => {
      const linkHash = link.getAttribute('href').replace('#', '');
      if (linkHash === hash) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    currentChapter = hash;

    // Scroll to top of content
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Close mobile sidebar if open
    if (sidebar && sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
    }

    // Update document title
    const activeLink = document.querySelector(`.nav-link[href="#${hash}"]`);
    if (activeLink) {
      document.title = activeLink.innerText.trim() + ' | Modul 3 PBO GUI Swing';
    } else {
      document.title = 'Modul 3 GUI Java Swing - Pemrograman Berorientasi Objek';
    }

    // Highlight code blocks with Prism
    if (window.Prism) {
      setTimeout(() => Prism.highlightAll(), 50);
    }
  }

  window.addEventListener('hashchange', navigateToHash);

  // ==========================================
  // 3. Reading Progress
  // ==========================================
  window.addEventListener('scroll', () => {
    if (!readingProgressBar) return;
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    readingProgressBar.style.width = scrolled + '%';
  });

  // ==========================================
  // 4. Sidebar Mobile Toggle
  // ==========================================
  if (sidebarToggleBtn && sidebar) {
    sidebarToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      sidebar.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && e.target !== sidebarToggleBtn) {
        sidebar.classList.remove('open');
      }
    });
  }

  // ==========================================
  // 5. Copy Code Blocks
  // ==========================================
  function setupCopyButtons() {
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const codeWrapper = btn.closest('.code-wrapper');
        if (!codeWrapper) return;
        const codeEl = codeWrapper.querySelector('code');
        if (!codeEl) return;

        const textToCopy = codeEl.innerText;
        navigator.clipboard.writeText(textToCopy).then(() => {
          const originalHTML = btn.innerHTML;
          btn.innerHTML = '<span>Tersalin! ✓</span>';
          btn.style.backgroundColor = '#22c55e';
          btn.style.color = '#ffffff';
          setTimeout(() => {
            btn.innerHTML = originalHTML;
            btn.style.backgroundColor = '';
            btn.style.color = '';
          }, 2000);
        }).catch(err => {
          console.error('Gagal menyalin kode:', err);
        });
      });
    });
  }

  // ==========================================
  // 6. Client-Side Search
  // ==========================================
  function openSearch() {
    if (!searchModal) return;
    searchModal.classList.add('open');
    if (searchInput) {
      searchInput.value = '';
      renderSearchResults('');
      setTimeout(() => searchInput.focus(), 50);
    }
  }

  function closeSearch() {
    if (searchModal) {
      searchModal.classList.remove('open');
    }
  }

  function renderSearchResults(keyword) {
    if (!searchResults) return;
    const cleanKeyword = keyword.toLowerCase().trim();
    if (!cleanKeyword) {
      searchResults.innerHTML = '<li style="padding: 1.5rem; text-align: center; color: var(--text-muted);">Ketik kata kunci untuk mencari bab, konsep, atau komponen...</li>';
      return;
    }

    const filtered = searchIndex.filter(item =>
      item.title.toLowerCase().includes(cleanKeyword) ||
      item.snippet.toLowerCase().includes(cleanKeyword)
    );

    if (filtered.length === 0) {
      searchResults.innerHTML = `<li style="padding: 1.5rem; text-align: center; color: var(--text-muted);">Tidak ditemukan hasil untuk "${keyword}"</li>`;
      return;
    }

    searchResults.innerHTML = filtered.map(item => `
      <li class="search-item" data-hash="${item.id}">
        <div class="search-item-title">${item.title}</div>
        <div class="search-item-snippet">${item.snippet}</div>
      </li>
    `).join('');

    searchResults.querySelectorAll('.search-item').forEach(item => {
      item.addEventListener('click', () => {
        const targetHash = item.getAttribute('data-hash');
        window.location.hash = targetHash;
        closeSearch();
      });
    });
  }

  if (searchTriggerBtn) {
    searchTriggerBtn.addEventListener('click', openSearch);
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      renderSearchResults(e.target.value);
    });
  }

  if (searchModal) {
    searchModal.addEventListener('click', (e) => {
      if (e.target === searchModal) {
        closeSearch();
      }
    });
  }

  // Keyboard shortcut: Ctrl+K or / or Escape
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSearch();
    } else if (e.key === '/' && document.activeElement !== searchInput && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      e.preventDefault();
      openSearch();
    } else if (e.key === 'Escape') {
      closeSearch();
    }
  });

  // ==========================================
  // 7. Interactive Quiz Engine
  // ==========================================
  function setupQuiz() {
    const quizContainers = document.querySelectorAll('.quiz-container');
    quizContainers.forEach(container => {
      const questionCards = container.querySelectorAll('.quiz-question-card');
      const resultBanner = container.querySelector('.quiz-result-banner');
      const scoreNumberEl = container.querySelector('.quiz-score-number');
      const scoreRemarkEl = container.querySelector('.quiz-score-remark');
      const btnResetQuiz = container.querySelector('.btn-reset-quiz');

      let userAnswers = {};

      questionCards.forEach((card, qIndex) => {
        const options = card.querySelectorAll('.quiz-option-label');
        const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
        const explanationEl = card.querySelector('.quiz-explanation');

        options.forEach((opt, optIndex) => {
          opt.addEventListener('click', () => {
            if (userAnswers[qIndex] !== undefined) return; // already answered

            userAnswers[qIndex] = optIndex;

            // Highlight choice
            if (optIndex === correctIndex) {
              opt.classList.add('correct');
              if (explanationEl) {
                explanationEl.style.display = 'block';
                explanationEl.style.backgroundColor = 'var(--callout-tip-bg)';
                explanationEl.style.color = 'var(--callout-tip-text)';
                explanationEl.style.border = '1px solid var(--callout-tip-border)';
                explanationEl.innerHTML = '<strong>Jawaban Tepat! ✓</strong> ' + (explanationEl.getAttribute('data-explain') || '');
              }
            } else {
              opt.classList.add('incorrect');
              // Highlight the correct one too
              options[correctIndex].classList.add('correct');
              if (explanationEl) {
                explanationEl.style.display = 'block';
                explanationEl.style.backgroundColor = 'var(--callout-warn-bg)';
                explanationEl.style.color = 'var(--callout-warn-text)';
                explanationEl.style.border = '1px solid var(--callout-warn-border)';
                explanationEl.innerHTML = '<strong>Kurang Tepat. ✕</strong> ' + (explanationEl.getAttribute('data-explain') || '');
              }
            }

            // Check if all answered
            if (Object.keys(userAnswers).length === questionCards.length) {
              let score = 0;
              questionCards.forEach((c, idx) => {
                if (userAnswers[idx] === parseInt(c.getAttribute('data-correct'), 10)) {
                  score++;
                }
              });

              const total = questionCards.length;
              const percentage = Math.round((score / total) * 100);

              if (resultBanner && scoreNumberEl) {
                resultBanner.style.display = 'block';
                scoreNumberEl.innerText = `${percentage} / 100`;

                let remark = '';
                if (percentage >= 85) {
                  remark = '🎉 Luar Biasa! Pemahaman Anda tentang GUI Swing sangat kuat dan siap menaklukkan Jurnal Modul 3!';
                } else if (percentage >= 65) {
                  remark = '👍 Bagus! Anda sudah memahami sebagian besar konsep. Silakan baca ulang bab yang penjelasannya belum Anda kuasai.';
                } else {
                  remark = '📚 Masih perlu latihan lagi. Coba ulas kembali contoh-contoh kode pada Bab 2 hingga Bab 11, lalu coba kuis ini kembali.';
                }
                if (scoreRemarkEl) scoreRemarkEl.innerText = remark;
              }
            }
          });
        });
      });

      if (btnResetQuiz) {
        btnResetQuiz.addEventListener('click', () => {
          userAnswers = {};
          questionCards.forEach(card => {
            const options = card.querySelectorAll('.quiz-option-label');
            options.forEach(opt => {
              opt.classList.remove('correct', 'incorrect');
            });
            const exp = card.querySelector('.quiz-explanation');
            if (exp) exp.style.display = 'none';
          });
          if (resultBanner) resultBanner.style.display = 'none';
        });
      }
    });
  }

  // ==========================================
  // 8. Event Playground Simulator Engine
  // ==========================================
  function setupEventPlayground() {
    const consoleLog = document.getElementById('console-log-content');
    const btnClear = document.getElementById('btn-clear-sim-log');
    const simBtn = document.getElementById('sim-btn');
    const simArea = document.getElementById('sim-area');
    const simInput = document.getElementById('sim-input');
    const javaCodeView = document.getElementById('playground-java-code');

    if (!consoleLog) return;

    function addLog(eventName, detailText) {
      const now = new Date();
      const timeStr = now.toTimeString().split(' ')[0] + '.' + String(now.getMilliseconds()).padStart(3, '0');

      const logRow = document.createElement('div');
      logRow.className = 'log-item';
      logRow.innerHTML = `
        <span class="log-time">[${timeStr}]</span>
        <span class="log-event-name">${eventName}</span>
        <span class="log-event-detail">&rarr; ${detailText}</span>
      `;
      consoleLog.appendChild(logRow);
      consoleLog.scrollTop = consoleLog.scrollHeight;
    }

    function flashBadge(badgeId) {
      const el = document.getElementById(badgeId);
      if (el) {
        el.classList.add('fired');
        setTimeout(() => el.classList.remove('fired'), 400);
      }
    }

    if (btnClear) {
      btnClear.addEventListener('click', () => {
        consoleLog.innerHTML = '<div style="color: #64748b; font-style: italic;">Log konsol dibersihkan. Lakukan aksi pada tombol, kanvas, atau input teks di sebelah kiri...</div>';
      });
    }

    // --- Sim Button Interactions ---
    if (simBtn) {
      simBtn.addEventListener('mousedown', (e) => {
        addLog('mousePressed', `MouseEvent (source=JButton, button=${e.button + 1}, x=${e.offsetX}, y=${e.offsetY})`);
        flashBadge('seq-mp');
      });

      simBtn.addEventListener('mouseup', (e) => {
        addLog('mouseReleased', `MouseEvent (source=JButton, button=${e.button + 1}, x=${e.offsetX}, y=${e.offsetY})`);
        flashBadge('seq-mr');
      });

      simBtn.addEventListener('click', (e) => {
        addLog('mouseClicked', `MouseEvent (clickCount=1, x=${e.offsetX}, y=${e.offsetY})`);
        flashBadge('seq-mc');
        setTimeout(() => {
          addLog('actionPerformed', `ActionEvent (source=JButton, cmd="PESAN_ESPRESSO", id=ACTION_PERFORMED)`);
          flashBadge('seq-ap');
        }, 60);

        if (javaCodeView) {
          javaCodeView.textContent =
`// Siklus pemanggilan saat JButton diklik:
btnPesan.addMouseListener(new MouseAdapter() {
    public void mousePressed(MouseEvent e)  { /* 1. mousePressed */ }
    public void mouseReleased(MouseEvent e) { /* 2. mouseReleased */ }
    public void mouseClicked(MouseEvent e)  { /* 3. mouseClicked */ }
});

// Listener Utama Aksi Tombol (dipicu setelah klik tuntas):
btnPesan.addActionListener(e -> {
    // 4. actionPerformed
    System.out.println("Aksi dijalankan: " + e.getActionCommand());
});`;
          if (window.Prism) Prism.highlightElement(javaCodeView);
        }
      });
    }

    // --- Sim Area Interactions ---
    if (simArea) {
      simArea.addEventListener('mouseenter', (e) => {
        simArea.classList.add('area-hover');
        addLog('mouseEntered', `MouseEvent (kursor masuk ke JPanel, x=${e.offsetX}, y=${e.offsetY})`);
        flashBadge('seq-me');
      });

      simArea.addEventListener('mouseleave', () => {
        simArea.classList.remove('area-hover');
        addLog('mouseExited', `MouseEvent (kursor meninggalkan area JPanel)`);
        flashBadge('seq-mx');
      });

      let moveThrottle = false;
      simArea.addEventListener('mousemove', (e) => {
        if (moveThrottle) return;
        moveThrottle = true;
        setTimeout(() => { moveThrottle = false; }, 100);
        addLog('mouseMoved', `MouseMotion (x=${e.offsetX}, y=${e.offsetY})`);
      });
    }

    // --- Sim Input Interactions ---
    if (simInput) {
      simInput.addEventListener('focus', () => {
        addLog('focusGained', 'FocusEvent (JTextField menerima fokus kursor)');
      });

      simInput.addEventListener('blur', () => {
        addLog('focusLost', 'FocusEvent (Kursor meninggalkan JTextField)');
      });

      simInput.addEventListener('keydown', (e) => {
        addLog('keyPressed', `KeyEvent (keyCode=${e.keyCode}, key="${e.key}")`);
        flashBadge('seq-kp');
      });

      simInput.addEventListener('keypress', (e) => {
        addLog('keyTyped', `KeyEvent (keyChar='${e.key}', code=VK_UNDEFINED)`);
        flashBadge('seq-kt');
      });

      simInput.addEventListener('keyup', (e) => {
        addLog('keyReleased', `KeyEvent (keyCode=${e.keyCode}, key="${e.key}")`);
        flashBadge('seq-kr');
      });

      simInput.addEventListener('input', (e) => {
        addLog('DocumentListener', `DocumentEvent (insert/remove: teks sekarang="${simInput.value}")`);
        flashBadge('seq-doc');

        if (javaCodeView) {
          javaCodeView.textContent =
`// Memantau pengetikan teks secara real-time:
textField.addKeyListener(new KeyAdapter() {
    public void keyPressed(KeyEvent e)  { /* 1. keyPressed */ }
    public void keyTyped(KeyEvent e)    { /* 2. keyTyped */ }
    public void keyReleased(KeyEvent e) { /* 3. keyReleased */ }
});

textField.getDocument().addDocumentListener(new DocumentListener() {
    public void insertUpdate(DocumentEvent e) { /* Perubahan isi teks */ }
    public void removeUpdate(DocumentEvent e) { /* Penghapusan karakter */ }
    public void changedUpdate(DocumentEvent e) { /* Format styling */ }
});`;
          if (window.Prism) Prism.highlightElement(javaCodeView);
        }
      });
    }
  }

  // ==========================================
  // Initialization
  // ==========================================
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    navigateToHash();
    setupCopyButtons();
    setupQuiz();
    setupEventPlayground();
  });

})();
