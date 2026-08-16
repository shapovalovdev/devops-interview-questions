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
  const pathFilters = document.querySelector('#path-filters');
  const pathView = document.querySelector('#path-view');
  const questionZone = document.querySelector('#question-zone');
  let activeTheme = 'all';
  let activeCertification = 'all';
  let activeCollection = 'all';
  let activePath = 'all';

  document.querySelector('#question-count').textContent = data.length;
  document.querySelector('#theme-count').textContent = themes.length;

  const label = (value) => value.replaceAll('-', ' ');
  const escapeHtml = (value) => value.replace(/[&<>'"]/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[char]);

  function renderFilters() {
    filters.innerHTML = ['all', ...themes].map((theme) => `
      <button class="filter ${theme === activeTheme ? 'active' : ''}" type="button" data-theme="${theme}">
        ${theme === 'all' ? 'all themes' : label(theme)}
      </button>`).join('');
  }

  function renderCertificationFilters() {
    certificationFilters.innerHTML = `
      <p class="filter-heading">Certification tracks <span>${certifications.length}</span></p>
      <div class="filter-buttons">
        ${certifications.map((certification) => `
          <button class="filter certification-filter ${certification.tag === activeCertification ? 'active' : ''}" type="button" data-certificate="${certification.tag}" aria-pressed="${certification.tag === activeCertification}">
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
          <button class="filter path-filter ${path.slug === activePath ? 'active' : ''}" type="button" data-path="${path.slug}" aria-pressed="${path.slug === activePath}">
            ${escapeHtml(path.title)} <span class="filter-count">${path.steps.length}</span>
          </button>`).join('')}
      </div>`;
  }

  function setHash(key, value) {
    const params = new URLSearchParams();
    if (key === 'theme' && value !== 'all') params.set('theme', value);
    if (key === 'certificate' && value !== 'all') params.set('certificate', value);
    if (key === 'collection' && value !== 'all') params.set('collection', value);
    if (key === 'path' && value !== 'all') params.set('path', value);
    const hash = params.toString();
    history.pushState(null, '', hash ? `#${hash}` : `${location.pathname}${location.search}`);
  }

  function readHash() {
    const params = new URLSearchParams(location.hash.slice(1));
    const theme = params.get('theme');
    const certification = params.get('certificate');
    const collection = params.get('collection');
    const path = params.get('path');
    activeTheme = themes.includes(theme) ? theme : 'all';
    activeCertification = certifications.some((item) => item.tag === certification) ? certification : 'all';
    activeCollection = collection === 'must-know' ? collection : 'all';
    activePath = learningPaths.some((item) => item.slug === path) ? path : 'all';
    mustKnowFilter.setAttribute('aria-pressed', String(activeCollection === 'must-know'));
    mustKnowFilter.classList.toggle('active', activeCollection === 'must-know');
  }

  function renderPath() {
    const path = learningPaths.find((item) => item.slug === activePath);
    questionZone.hidden = Boolean(path);
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
    const order = studyOrders.find((item) => item.theme === activeTheme);
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

  function render() {
    renderFilters();
    renderCertificationFilters();
    renderPathFilters();
    renderStudyOrder();
    renderQuestions();
    renderPath();
  }

  function renderQuestions() {
    const query = search.value.trim().toLowerCase();
    const shown = data.filter((question) => {
      const text = [question.title, question.theme, question.type, ...question.tags].join(' ').toLowerCase();
      return (activeTheme === 'all' || question.theme === activeTheme)
        && (activeCertification === 'all' || question.tags.includes(activeCertification))
        && (activeCollection === 'all' || question.tags.includes(activeCollection))
        && text.includes(query);
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
    activeTheme = button.dataset.theme;
    activeCertification = 'all';
    activeCollection = 'all';
    activePath = 'all';
    setHash('theme', activeTheme);
    render();
  });
  certificationFilters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-certificate]');
    if (!button) return;
    activeCertification = button.dataset.certificate;
    activeTheme = 'all';
    activeCollection = 'all';
    activePath = 'all';
    setHash('certificate', activeCertification);
    render();
  });
  pathFilters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-path]');
    if (!button) return;
    activePath = activePath === button.dataset.path ? 'all' : button.dataset.path;
    activeTheme = 'all'; activeCertification = 'all'; activeCollection = 'all';
    setHash('path', activePath);
    render();
  });
  mustKnowFilter.addEventListener('click', () => {
    activeCollection = activeCollection === 'must-know' ? 'all' : 'must-know';
    activeTheme = 'all'; activeCertification = 'all'; activePath = 'all';
    setHash('collection', activeCollection);
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
