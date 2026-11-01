'use strict';
(() => {
  const collection = 'compass';
  const docs = window.PARAMETRICALLY_STANDARDS.documents;
  document.querySelector('.nav-intro span').textContent = 'Yönetmelik • 9 ek';
  document.querySelector('.brand small').textContent = 'COMPASS · MEVZUAT';
  const byId = new Map(docs.map(doc => [doc.id, doc]));
  const $ = id => document.getElementById(id);
  const fold = text => text.toLocaleLowerCase('tr-TR').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i');
  const slug = text => fold(text).replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const node = (tag, text, className) => { const el = document.createElement(tag); if (text !== undefined) el.textContent = text; if (className) el.className = className; return el; };
  let current = null, headings = [], pdfMode = false, searchTimer;
  const pref = {get(key) { try { return localStorage.getItem('prm-library-' + key); } catch (_) { return null; } }, set(key, value) { try { localStorage.setItem('prm-library-' + key, value); } catch (_) { /* Optional preference storage. */ } }};
  let fontSize = Math.max(14, Math.min(23, Number(pref.get('font')) || 17));
  function applyFont() { document.documentElement.style.setProperty('--font', fontSize + 'px'); pref.set('font', fontSize); }
  document.documentElement.dataset.theme = pref.get('theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  applyFont();
  $('theme').addEventListener('click', () => { const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'; document.documentElement.dataset.theme = theme; pref.set('theme', theme); });
  $('smaller').addEventListener('click', () => { fontSize = Math.max(14, fontSize - 1); applyFont(); });
  $('larger').addEventListener('click', () => { fontSize = Math.min(23, fontSize + 1); applyFont(); });
  $('menu').addEventListener('click', () => { const open = document.body.classList.toggle('menu-open'); $('menu').setAttribute('aria-expanded', open); });

  function linkTo(doc, section = '', mode = '') {
    const params = new URLSearchParams({collection, doc}); if (section) params.set('section', section); if (mode) params.set('mode', mode);
    return '#' + params.toString();
  }
  let group = '';
  for (const doc of docs) {
    if (doc.group !== group) { group = doc.group; $('document-list').append(node('div', group, 'group-title')); }
    const link = node('a', doc.title, 'doc-link'); link.href = linkTo(doc.id); link.dataset.doc = doc.id;
    $('document-list').append(link);
  }

  function inline(el, text) {
    for (const token of text.split(/(!\[[^\]]*\]\(figures\/[a-z0-9-]+\.svg\)|`[^`]+`|\*\*[^*]+\*\*)/g)) {
      const graphic = /^!\[([^\]]*)\]\((figures\/[a-z0-9-]+\.svg)\)$/.exec(token);
      if (graphic) { const img = node('img'); img.src = graphic[2]; img.alt = graphic[1]; img.className = 'source-vector'; img.loading = 'lazy'; el.append(img); }
      else if (token.startsWith('`') && token.endsWith('`')) el.append(node('code', token.slice(1, -1)));
      else if (token.startsWith('**') && token.endsWith('**')) el.append(node('strong', token.slice(2, -2)));
      else el.append(document.createTextNode(token));
    }
  }
  function sourceTable(markup) {
    // Parse the deliberately tiny table dialect without browser HTML parsing:
    // unknown elements cannot fetch URLs, run handlers, or create host objects.
    const table = node('table'), stack = [table];
    const allowed = new Set(['caption','thead','tbody','tfoot','tr','th','td','br']);
    for (const token of markup.match(/<[^>]*>|[^<]+|</g) || []) {
      if (token.startsWith('<')) {
        const tag = /^<(\/?)([a-z]+)\b[^>]*>$/i.exec(token);
        if (!tag || !allowed.has(tag[2].toLowerCase())) continue;
        const name = tag[2].toLowerCase();
        if (tag[1]) {
          for (let i = stack.length - 1; i > 0; i--) { if (stack[i].tagName.toLowerCase() === name) { stack.length = i; break; } }
        } else {
          const child = node(name);
          if (name === 'td' || name === 'th') {
            for (const attr of ['rowspan','colspan']) { const m = new RegExp('\\b' + attr + '="([0-9]{1,3})"').exec(token); if (m && Number(m[1]) >= 1 && Number(m[1]) <= 128) child.setAttribute(attr, m[1]); }
          }
          stack[stack.length - 1].append(child); if (name !== 'br') stack.push(child);
        }
      } else if (token.trim()) {
        const value = token.replace(/&(amp|lt|gt|quot|#x27|#39);/g, (_, name) => ({amp:'&',lt:'<',gt:'>',quot:'"','#x27':"'",'#39':"'"}[name]));
        const span = node('span'); inline(span, value); stack[stack.length - 1].append(span);
      }
    }
    const wrap = node('div', undefined, 'table-scroll source-table'); wrap.append(table); return wrap;
  }
  function render(markdown) {
    const frag = document.createDocumentFragment(); const lines = markdown.split('\n'); headings = [];
    const used = new Map();
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i]; if (!line.trim()) continue;
      const heading = /^(#{1,3}) (.*)$/.exec(line);
      if (heading) {
        if (heading[1].length === 1) continue;
        const h = node('h' + heading[1].length, heading[2]); const base = slug(heading[2]) || 'bolum';
        const count = (used.get(base) || 0) + 1; used.set(base, count); h.id = base + (count > 1 ? '-' + count : '');
        headings.push({id: h.id, text: heading[2]}); frag.append(h); continue;
      }
      if (line.startsWith('```')) {
        const text = []; while (++i < lines.length && !lines[i].startsWith('```')) text.push(lines[i]);
        frag.append(node('pre', text.join('\n'))); continue;
      }
      if (line.startsWith('<table>')) {
        const table = [line]; while (++i < lines.length) { table.push(lines[i]); if (lines[i] === '</table>') break; }
        frag.append(sourceTable(table.join('\n'))); continue;
      }
      if (line.startsWith('|') && /^\|[\s:|\-]+\|$/.test(lines[i + 1] || '')) {
        const wrap = node('div', undefined, 'table-scroll'); const table = node('table'); const body = node('tbody');
        let header = true;
        while (i < lines.length && lines[i].startsWith('|')) {
          if (/^\|[\s:|\-]+\|$/.test(lines[i])) { i++; continue; }
          const row = node('tr');
          for (const cell of lines[i].slice(1, -1).split(/(?<!\\)\|/)) { const item = node(header ? 'th' : 'td'); inline(item, cell.trim().replace(/\\\|/g, '|')); row.append(item); }
          if (header) { const head = node('thead'); head.append(row); table.append(head); } else body.append(row);
          header = false; i++;
        }
        i--; table.append(body); wrap.append(table); frag.append(wrap); continue;
      }
      const el = node(line.startsWith('> ') ? 'blockquote' : 'p'); inline(el, line.startsWith('> ') ? line.slice(2) : line); frag.append(el);
    }
    $('content').replaceChildren(frag); $('toc').replaceChildren();
    for (const h of headings) { const a = node('a', h.text); a.href = linkTo(current.id, h.id); a.dataset.section = h.id; $('toc').append(a); }
  }
  function setMode(enabled, page) {
    pdfMode = !!enabled && !!current.first_page;
    $('pdf').hidden = !pdfMode; $('pdf-notice').hidden = !pdfMode; $('content').hidden = pdfMode;
    $('pdf-toggle').textContent = pdfMode ? 'Metni oku' : 'Kaynak PDF (arşiv)';
    if (pdfMode) $('pdf').src = 'sources/20260805-2-1.pdf#page=' + Math.max(current.first_page, Math.min(current.last_page, page || current.first_page));
    else { $('pdf').removeAttribute('src'); }
  }
  function navigate() {
    closeSearch();
    const p = new URLSearchParams(location.hash.slice(1)); const doc = byId.get(p.get('doc')) || docs[0];
    const changed = !current || current.id !== doc.id; current = doc;
    if (changed) {
      document.title = doc.title + ' · Parametrically Compass'; $('title').textContent = doc.title; $('status').textContent = doc.status;
      $('breadcrumb').textContent = 'Kütüphane / ' + doc.group; $('pdf-toggle').hidden = !doc.first_page;
      $('official').hidden = doc.group !== 'Parametrically Compass'; $('subtitle').textContent = doc.first_page ? 'Düzenlenebilir metin ve tablolar · OCR teyidi gerekli' : (doc.id === 'yonetmelik' ? '17 madde · 2 geçici madde · Yayımlanma nüshasından aktarım' : 'Kaynaklar, kullanım ve aktarım durumu');
      $('source-note').textContent = doc.first_page ? 'Tablo düzenini ve kodları özgün PDF’den teyit edin. Kütüphane içeriği, uygulamanın bu kuralların tamamını denetlediği anlamına gelmez.' : 'Yönetmelik kaynakları çevrimdışı kullanılabilir; içerik hukuki uygunluk onayı değildir.';
      render(doc.markdown);
      for (const a of document.querySelectorAll('.doc-link')) { if (a.dataset.doc === doc.id) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); }
    }
    const section = p.get('section') || ''; const resolved = (doc.legacy_sections || {})[section] || section;
    const target = headings.find(h => h.id === resolved);
    const legacyPage = /^pdf-sayfa-(\d+)$/.exec(section);
    const page = legacyPage ? Number(legacyPage[1]) : (doc.section_pages || {})[resolved];
    setMode(p.get('mode') === 'pdf', page || doc.first_page);
    for (const a of $('toc').children) { if (a.dataset.section === resolved) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); }
    if (!pdfMode && target) document.getElementById(target.id).scrollIntoView({block: 'start'});
    else if (changed) window.scrollTo(0, 0);
    document.body.classList.remove('menu-open'); $('menu').setAttribute('aria-expanded', 'false');
  }
  $('pdf-toggle').addEventListener('click', () => {
    const p = new URLSearchParams(location.hash.slice(1)); location.hash = linkTo(current.id, p.get('section') || '', pdfMode ? '' : 'pdf');
  });
  $('print').addEventListener('click', () => window.print());
  window.addEventListener('hashchange', navigate);

  const searchIndex = [];
  for (const doc of docs) {
    let section = ''; const used = new Map();
    for (const line of doc.markdown.split('\n')) {
      const heading = /^(#{2,3}) (.*)$/.exec(line);
      if (heading) { const base = slug(heading[2]) || 'bolum'; const count = (used.get(base) || 0) + 1; used.set(base, count); section = base + (count > 1 ? '-' + count : ''); }
      const plain = line.replace(/<br\s*\/?\s*>/gi, ' ').replace(/<[^>]*>/g, ' ').replace(/&(amp|lt|gt|quot|#x27|#39);/g, (_, name) => ({amp:'&',lt:'<',gt:'>',quot:'"','#x27':"'",'#39':"'"}[name]));
      if (plain.trim() && !line.startsWith('```')) searchIndex.push({doc, section, text: plain.replace(/^[#>| ]+/, ''), folded: fold(plain)});
    }
  }
  function closeSearch() { $('search-panel').hidden = true; }
  function search() {
    const query = fold($('search').value.trim()); $('search-results').replaceChildren();
    if (!query) { closeSearch(); return; }
    const words = query.split(/\s+/); const results = searchIndex.filter(item => words.every(word => item.folded.includes(word)));
    $('search-count').textContent = `${results.length} eşleşme · ${new Set(results.map(item => item.doc.id)).size} belge` + (results.length > 100 ? ' · İlk 100 gösteriliyor' : '');
    for (const result of results.slice(0, 100)) {
      const button = node('button', undefined, 'search-result'); button.append(node('strong', result.doc.title));
      const at = result.folded.indexOf(words[0]); const start = Math.max(0, at - 65); const excerpt = (start ? '…' : '') + result.text.slice(start, start + 230) + (result.text.length > start + 230 ? '…' : '');
      button.append(node('span', excerpt)); button.addEventListener('click', () => { location.hash = linkTo(result.doc.id, result.section); closeSearch(); setTimeout(() => { $('reading').focus({preventScroll: true}); }, 0); });
      $('search-results').append(button);
    }
    if (!results.length) $('search-results').append(node('p', 'Sonuç bulunamadı. Farklı bir terim veya kısa kod deneyin.', 'empty-search'));
    $('search-panel').hidden = false;
  }
  $('search').addEventListener('input', () => { clearTimeout(searchTimer); searchTimer = setTimeout(search, 140); });
  $('search').addEventListener('focus', () => { if ($('search').value.trim()) search(); });
  $('close-search').addEventListener('click', () => { $('search').focus(); closeSearch(); });
  document.addEventListener('keydown', event => {
    const editing = /^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName);
    if ((event.ctrlKey && event.key.toLowerCase() === 'k') || (event.key === '/' && !editing)) { event.preventDefault(); $('search').focus(); }
    if (event.key === 'Escape') { closeSearch(); document.body.classList.remove('menu-open'); $('menu').setAttribute('aria-expanded', 'false'); }
    if (event.key === 'ArrowDown' && document.activeElement === $('search') && !$('search-panel').hidden) { event.preventDefault(); const first = $('search-results').querySelector('button'); if (first) first.focus(); }
  });
  document.addEventListener('pointerdown', event => { if (!$('search-panel').contains(event.target) && !$('search').contains(event.target)) closeSearch(); });
  navigate();
})();
