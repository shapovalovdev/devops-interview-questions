(() => {
  const data = window.questions;
  const search = document.querySelector('#search');
  const filters = document.querySelector('#filters');
  const grid = document.querySelector('#question-grid');
  const resultLine = document.querySelector('#result-line');
  const themes = [...new Set(data.map((question) => question.theme))];
  let activeTheme = 'all';

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

  function renderQuestions() {
    const query = search.value.trim().toLowerCase();
    const shown = data.filter((question) => {
      const text = [question.title, question.theme, question.type, ...question.tags].join(' ').toLowerCase();
      return (activeTheme === 'all' || question.theme === activeTheme) && text.includes(query);
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
    renderFilters();
    renderQuestions();
  });
  search.addEventListener('input', renderQuestions);
  renderFilters();
  renderQuestions();
})();
