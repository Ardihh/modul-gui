# -*- coding: utf-8 -*-
import html

def get_code(path):
    with open(path, 'r', encoding='utf-8') as f:
        return html.escape(f.read())

def code_box(rel_path, file_title):
    escaped_code = get_code(rel_path)
    return f'''
    <div class="code-wrapper">
      <div class="code-header">
        <span class="file-name">📄 {file_title}</span>
        <button class="copy-btn" type="button">Salin Kode</button>
      </div>
      <pre><code class="language-java">{escaped_code}</code></pre>
    </div>
    '''

def nav_buttons(prev_id, prev_title, next_id, next_title):
    html_out = '<div class="chapter-nav-buttons">'
    if prev_id:
        html_out += f'''
        <a href="#{prev_id}" class="btn-nav-chapter btn-nav-prev">
          <span class="nav-dir">← Sebelumnya</span>
          <span class="nav-title">{prev_title}</span>
        </a>
        '''
    else:
        html_out += '<div></div>'
    
    if next_id:
        html_out += f'''
        <a href="#{next_id}" class="btn-nav-chapter btn-nav-next">
          <span class="nav-dir">Berikutnya →</span>
          <span class="nav-title">{next_title}</span>
        </a>
        '''
    html_out += '</div>'
    return html_out
