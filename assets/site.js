(() => {
  const data = window.questions;
  const search = document.querySelector('#search');
  const filters = document.querySelector('#filters');
  const certificationFilters = document.querySelector('#certification-filters');
  const grid = document.querySelector('#question-grid');
  const resultLine = document.querySelector('#result-line');
  const themes = [...new Set(data.map((question) => question.theme))];
  const certifications = window.certifications || [];
  const mustKnowFilter = document.querySelector('#must-know-filter');
  // A learning path is ordered data, so it is rendered as a sequence rather
  // than folded into the filtered grid: the position of a step is the point.
  const learningPaths = window.learningPaths || [];
  // A study order is the same idea inside one Theme: rendered beside the grid
  // as a collapsed panel, because the grid stays the Theme view's subject.
  const studyOrders = window.studyOrders || [];
  const studyOrderView = document.querySelector('#study-order');
  // A lab is practice data attached to a Theme: the whole catalog gets its
  // own view, while a single Theme gets a collapsed strip beside the grid.
  const labs = window.labs || [];
  const labsView = document.querySelector('#labs-view');
  const themeLabsView = document.querySelector('#theme-labs');
  const pathFilters = document.querySelector('#path-filters');
  const pathView = document.querySelector('#path-view');
  const questionZone = document.querySelector('#question-zone');
  // Exactly one selection is active at a time. That was always true -- every
  // handler reset the other four by hand -- but it was enforced by convention
  // across five variables rather than by construction, so nothing stopped a
  // path and the Labs view being on at once. The URL layer already said it
  // properly: setHash() has only ever written a single key.
  //
  //   { kind: 'all' }
  //   { kind: 'theme',         theme }
  //   { kind: 'certification', tag }
  //   { kind: 'collection',    collection }
  //   { kind: 'path',          slug }
  //   { kind: 'labs' }
  let view = { kind: 'all' };

  //: The Theme in view, or null when the selection is not a Theme. The study
  //: order and the per-Theme lab strip both belong to a Theme and to nothing
  //: else, so they ask this rather than comparing against an 'all' sentinel.
  const selectedTheme = () => (view.kind === 'theme' ? view.theme : null);

  document.querySelector('#question-count').textContent = data.length;
  document.querySelector('#theme-count').textContent = themes.length;

  const label = (value) => value.replaceAll('-', ' ');
  const escapeHtml = (value) => value.replace(/[&<>'"]/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[char]);

  function renderFilters() {
    filters.innerHTML = ['all', ...themes].map((theme) => `
      <button class="filter ${view.kind === 'theme' ? (theme === view.theme ? 'active' : '') : (theme === 'all' ? 'active' : '')}" type="button" data-theme="${theme}">
        ${theme === 'all' ? 'all themes' : label(theme)}
      </button>`).join('');
  }

  function renderCertificationFilters() {
    certificationFilters.innerHTML = `
      <p class="filter-heading">Certification tracks <span>${certifications.length}</span></p>
      <div class="filter-buttons">
        ${certifications.map((certification) => `
          <button class="filter certification-filter ${view.kind === 'certification' && certification.tag === view.tag ? 'active' : ''}" type="button" data-certificate="${certification.tag}" aria-pressed="${view.kind === 'certification' && certification.tag === view.tag}">
            ${certification.tag.toUpperCase()}
          </button>`).join('')}
      </div>`;
  }

  function renderPathFilters() {
    if (!learningPaths.length) return;
    pathFilters.innerHTML = `
      <p class="filter-heading">Learning paths <span>${learningPaths.length}</span></p>
      <div class="filter-buttons">
        ${learningPaths.map((path) => `
          <button class="filter path-filter ${view.kind === 'path' && path.slug === view.slug ? 'active' : ''}" type="button" data-path="${path.slug}" aria-pressed="${view.kind === 'path' && path.slug === view.slug}">
            ${escapeHtml(path.title)} <span class="filter-count">${path.steps.length}</span>
          </button>`).join('')}
      </div>`;
  }

  //: One view, one hash key. The parameter names are the published URL surface
  //: -- shared links carry them -- so they stay exactly as they were.
  const HASH_KEY = { theme: 'theme', certification: 'certificate', collection: 'collection', path: 'path' };

  function setHash() {
    const params = new URLSearchParams();
    if (view.kind === 'theme') params.set(HASH_KEY.theme, view.theme);
    if (view.kind === 'certification') params.set(HASH_KEY.certification, view.tag);
    if (view.kind === 'collection') params.set(HASH_KEY.collection, view.collection);
    if (view.kind === 'path') params.set(HASH_KEY.path, view.slug);
    if (view.kind === 'labs') params.set('labs', '');
    const hash = params.toString().replace(/labs=$/, 'labs');
    history.pushState(null, '', hash ? `#${hash}` : `${location.pathname}${location.search}`);
  }

  //: Read the hash into a view, keeping the first key that names something
  //: real. An unknown Theme or a retired path slug falls through to 'all'
  //: rather than producing a view that renders nothing.
  function readHash() {
    const params = new URLSearchParams(location.hash.slice(1));
    const theme = params.get(HASH_KEY.theme);
    const certification = params.get(HASH_KEY.certification);
    const collection = params.get(HASH_KEY.collection);
    const path = params.get(HASH_KEY.path);

    if (params.has('labs')) view = { kind: 'labs' };
    else if (themes.includes(theme)) view = { kind: 'theme', theme };
    else if (certifications.some((item) => item.tag === certification)) view = { kind: 'certification', tag: certification };
    else if (collection === 'must-know') view = { kind: 'collection', collection };
    else if (learningPaths.some((item) => item.slug === path)) view = { kind: 'path', slug: path };
    else view = { kind: 'all' };

    mustKnowFilter.setAttribute('aria-pressed', String(view.kind === 'collection'));
    mustKnowFilter.classList.toggle('active', view.kind === 'collection');
  }

  function renderPath() {
    // Three regions, one selection: each is visible exactly when the view is
    // its own kind. No expression combines a path with a labs flag any more,
    // because no state exists in which both are set.
    const path = view.kind === 'path' ? learningPaths.find((item) => item.slug === view.slug) : undefined;
    questionZone.hidden = view.kind === 'path' || view.kind === 'labs';
    pathView.hidden = !path;
    if (!path) {
      pathView.innerHTML = '';
      return;
    }
    const prerequisites = path.prerequisites
      .map((slug) => learningPaths.find((item) => item.slug === slug))
      .filter(Boolean);
    pathView.innerHTML = `
      <header class="path-header">
        <p class="eyebrow">LEARNING PATH / ${path.steps.length} STEPS IN ORDER</p>
        <h2>${escapeHtml(path.title)}</h2>
        <p class="path-audience">${escapeHtml(path.audience)}</p>
        <p class="path-prerequisites">${prerequisites.length
          ? `Complete first: ${prerequisites.map((item) => `<a href="#path=${item.slug}">${escapeHtml(item.title)}</a>`).join(', ')}`
          : 'No prerequisite path — start here.'}</p>
        <a class="path-exit" href="#">Back to the full database <b>→</b></a>
      </header>
      <ol class="path-steps">
        ${path.steps.map((step, index) => `
          <li class="path-step">
            <p class="step-index">${String(index + 1).padStart(2, '0')}</p>
            <div class="step-body">
              <p class="card-top"><span>${label(step.theme)}</span><span>${step.difficulty}</span></p>
              <h3><a href="${step.href}">${escapeHtml(step.title)}</a></h3>
              <p class="step-why">${escapeHtml(step.why)}</p>
            </div>
          </li>`).join('')}
      </ol>`;
  }

  function renderStudyOrder() {
    const order = studyOrders.find((item) => item.theme === selectedTheme());
    if (!order) {
      studyOrderView.hidden = true;
      studyOrderView.innerHTML = '';
      return;
    }
    studyOrderView.hidden = false;
    studyOrderView.innerHTML = `
      <details class="study-order-panel">
        <summary>Suggested study order <span class="study-order-count">${order.steps.length} steps in order</span><span class="study-order-toggle" aria-hidden="true"></span></summary>
        <div class="study-order-body">
          <p class="study-order-note">${escapeHtml(order.note)}</p>
          <ol class="path-steps">
            ${order.steps.map((step, index) => `
              <li class="path-step">
                <p class="step-index">${String(index + 1).padStart(2, '0')}</p>
                <div class="step-body">
                  <p class="card-top"><span>${step.difficulty}</span></p>
                  <h3><a href="${step.href}">${escapeHtml(step.title)}</a></h3>
                  <p class="step-why">${escapeHtml(step.why)}</p>
                </div>
              </li>`).join('')}
          </ol>
        </div>
      </details>`;
  }

  function renderThemeLabs() {
    const themeLabs = labs.filter((lab) => lab.theme === selectedTheme());
    if (!themeLabs.length) {
      themeLabsView.hidden = true;
      themeLabsView.innerHTML = '';
      return;
    }
    themeLabsView.hidden = false;
    themeLabsView.innerHTML = `
      <details class="study-order-panel">
        <summary>Hands-on labs <span class="study-order-count">${themeLabs.length} lab${themeLabs.length === 1 ? '' : 's'}</span><span class="study-order-toggle" aria-hidden="true"></span></summary>
        <div class="study-order-body">
          <ol class="path-steps">
            ${themeLabs.map((lab, index) => `
              <li class="path-step">
                <p class="step-index">${String(index + 1).padStart(2, '0')}</p>
                <div class="step-body">
                  <p class="card-top"><span>${label(lab.theme)}</span><span>${lab.difficulty}</span></p>
                  <h3><a href="${lab.questionHref}">${escapeHtml(lab.title)}</a></h3>
                  <p class="step-why">${escapeHtml(lab.why)}</p>
                </div>
              </li>`).join('')}
          </ol>
        </div>
      </details>`;
  }

  function renderLabs() {
    labsView.hidden = view.kind !== 'labs';
    if (view.kind !== 'labs') {
      labsView.innerHTML = '';
      return;
    }
    // window.labs arrives sorted by theme then slug, so grouping while
    // iterating keeps both the theme sections and the cards deterministic.
    const groups = [];
    labs.forEach((lab) => {
      const group = groups[groups.length - 1];
      if (group && group.theme === lab.theme) group.labs.push(lab);
      else groups.push({ theme: lab.theme, labs: [lab] });
    });
    labsView.innerHTML = `
      <header class="path-header">
        <p class="eyebrow">HANDS-ON LABS / ${labs.length} LABS IN ${groups.length} THEMES</p>
        <h2>Hands-on labs.</h2>
        <p class="path-audience">Practice first: every lab is a guided exercise tied to the interview question it prepares you for, grouped by Theme.</p>
        <a class="path-exit" href="#">Back to the full database <b>→</b></a>
      </header>
      ${groups.map((group) => `
        <section class="lab-theme-group" data-theme="${group.theme}">
          <p class="filter-heading">${label(group.theme)} <span>${group.labs.length}</span></p>
          <div class="lab-grid">
            ${group.labs.map((lab) => `
              <article class="lab-card">
                <p class="card-top"><span>${label(lab.theme)}</span><span>${lab.difficulty}</span></p>
                <h3>${escapeHtml(lab.title)}</h3>
                <div class="tags">${lab.tags.map((tag) => `<span>#${tag}</span>`).join('')}</div>
                <p class="step-why">${escapeHtml(lab.why)}</p>
                <a href="${lab.questionHref}">${escapeHtml(lab.questionTitle)} <b>→</b></a>
              </article>`).join('')}
          </div>
        </section>`).join('')}`;
  }

  function render() {
    renderFilters();
    renderCertificationFilters();
    renderPathFilters();
    renderStudyOrder();
    renderThemeLabs();
    renderQuestions();
    renderPath();
    renderLabs();
  }

  //: Which Questions the current view admits. 'path' and 'labs' never reach
  //: here -- their regions replace the grid rather than filter it.
  function matchesView(question) {
    switch (view.kind) {
      case 'theme': return question.theme === view.theme;
      case 'certification': return question.tags.includes(view.tag);
      case 'collection': return question.tags.includes(view.collection);
      default: return true;
    }
  }

  function renderQuestions() {
    const query = search.value.trim().toLowerCase();
    const shown = data.filter((question) => {
      const text = [question.title, question.theme, question.type, ...question.tags].join(' ').toLowerCase();
      return matchesView(question) && text.includes(query);
    });
    resultLine.textContent = `${shown.length.toString().padStart(2, '0')} RECORD${shown.length === 1 ? '' : 'S'} FOUND`;
    grid.innerHTML = shown.length ? shown.map((question, index) => `
      <article class="question-card" style="--delay: ${index * 45}ms">
        <div class="card-top"><span>${label(question.theme)}</span><span>${question.difficulty}</span></div>
        <h2>${escapeHtml(question.title)}</h2>
        <div class="tags">${question.tags.slice(0, 3).map((tag) => `<span>#${tag}</span>`).join('')}</div>
        <a href="${question.path}" aria-label="Open ${escapeHtml(question.title)}">Read the field note <b>→</b></a>
      </article>`).join('') : '<p class="empty">No record matches this search. Try a broader term.</p>';
  }

  filters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-theme]');
    if (!button) return;
    view = button.dataset.theme === 'all' ? { kind: 'all' } : { kind: 'theme', theme: button.dataset.theme };
    setHash();
    render();
  });
  certificationFilters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-certificate]');
    if (!button) return;
    view = { kind: 'certification', tag: button.dataset.certificate };
    setHash();
    render();
  });
  pathFilters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-path]');
    if (!button) return;
    const same = view.kind === 'path' && view.slug === button.dataset.path;
    view = same ? { kind: 'all' } : { kind: 'path', slug: button.dataset.path };
    setHash();
    render();
  });
  mustKnowFilter.addEventListener('click', () => {
    view = view.kind === 'collection' ? { kind: 'all' } : { kind: 'collection', collection: 'must-know' };
    setHash();
    render();
  });
  window.addEventListener('hashchange', () => {
    readHash();
    render();
  });
  search.addEventListener('input', renderQuestions);
  readHash();
  render();
})();
