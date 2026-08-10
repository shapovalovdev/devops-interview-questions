(() => {
  const DEFAULT_TOTAL = 30;

  function seededRandom(seed) {
    let value = 2166136261;
    for (const character of String(seed)) value = Math.imul(value ^ character.charCodeAt(0), 16777619);
    return () => {
      value += 0x6D2B79F5;
      let result = Math.imul(value ^ value >>> 15, 1 | value);
      result ^= result + Math.imul(result ^ result >>> 7, 61 | result);
      return ((result ^ result >>> 14) >>> 0) / 4294967296;
    };
  }

  function shuffle(items, random) {
    const copy = [...items];
    for (let index = copy.length - 1; index > 0; index -= 1) {
      const swap = Math.floor(random() * (index + 1));
      [copy[index], copy[swap]] = [copy[swap], copy[index]];
    }
    return copy;
  }

  function balanceAllocations(themes, total) {
    const allocation = Object.fromEntries(themes.map((theme) => [theme, 0]));
    if (!themes.length || total < 1) return allocation;
    themes.forEach((theme, index) => { allocation[theme] = Math.floor(total / themes.length) + (index < total % themes.length ? 1 : 0); });
    return allocation;
  }

  function createSession(questions, themes, total, seed, requestedAllocations = {}) {
    const selected = [...new Set(themes)].filter(Boolean);
    const allocation = Object.values(requestedAllocations).reduce((sum, value) => sum + Number(value || 0), 0) === total
      ? requestedAllocations : balanceAllocations(selected, total);
    const random = seededRandom(seed);
    const picked = [];
    const used = new Set();
    selected.forEach((theme) => {
      shuffle(questions.filter((question) => question.theme === theme), random)
        .slice(0, allocation[theme] || 0)
        .forEach((question) => { if (!used.has(question.path)) { used.add(question.path); picked.push(question); } });
    });
    if (picked.length < total) {
      shuffle(questions.filter((question) => selected.includes(question.theme) && !used.has(question.path)), random)
        .slice(0, total - picked.length)
        .forEach((question) => picked.push(question));
    }
    return shuffle(picked, random).slice(0, total);
  }

  function writeState(state) {
    const params = new URLSearchParams({ themes: state.themes.join(','), total: String(state.total), seed: state.seed, index: String(state.index || 0) });
    const allocations = Object.entries(state.allocations || {}).filter(([theme]) => state.themes.includes(theme));
    if (allocations.length) params.set('allocations', allocations.map(([theme, count]) => `${theme}:${count}`).join(','));
    if (state.revealed) params.set('revealed', '1');
    return params.toString();
  }

  function readState(serialized) {
    const params = new URLSearchParams(String(serialized).replace(/^[?#]/, ''));
    const allocations = Object.fromEntries((params.get('allocations') || '').split(',').map((entry) => entry.split(':')).filter(([theme, count]) => theme && /^\d+$/.test(count)).map(([theme, count]) => [theme, Number(count)]));
    return {
      themes: (params.get('themes') || '').split(',').filter(Boolean),
      total: Math.max(1, Number(params.get('total')) || DEFAULT_TOTAL),
      seed: params.get('seed') || '',
      index: Math.max(0, Number(params.get('index')) || 0),
      revealed: params.get('revealed') === '1',
      allocations,
    };
  }

  window.InterviewSession = { balanceAllocations, createSession, readState, writeState };
  if (!document || !document.querySelector('#session-builder')) return;

  const data = window.questions;
  const themes = [...new Set(data.map((question) => question.theme))].sort();
  const builder = document.querySelector('#session-builder');
  const deck = document.querySelector('#interview-deck');
  const themeList = document.querySelector('#session-themes');
  const totalInput = document.querySelector('#session-total');
  let state = readState(location.search || location.hash);
  let session = [];

  const label = (value) => value.replaceAll('-', ' ');
  const newSeed = () => `${Date.now()}-${Math.random().toString(36).slice(2)}`;
  const selectedThemes = () => [...themeList.querySelectorAll('input[type="checkbox"]:checked')].map((input) => input.value);
  const allocationInputs = () => Object.fromEntries([...themeList.querySelectorAll('input[type="number"]')].map((input) => [input.dataset.theme, Number(input.value || 0)]));

  function renderThemeChooser() {
    const allocations = state.allocations;
    themeList.innerHTML = themes.map((theme) => `
      <label class="session-theme ${state.themes.includes(theme) ? 'selected' : ''}">
        <input type="checkbox" value="${theme}" ${state.themes.includes(theme) ? 'checked' : ''}>
        <span>${label(theme)}</span>
        <input aria-label="${label(theme)} allocation" data-theme="${theme}" type="number" min="0" max="100" value="${state.themes.includes(theme) ? allocations[theme] || 0 : 0}">
      </label>`).join('');
  }

  function updateUrl() { history.replaceState(null, '', `?${writeState(state)}`); }

  function renderDeck() {
    const question = session[state.index];
    if (!question) return;
    document.querySelector('#session-progress').textContent = `${state.index + 1} / ${session.length}`;
    document.querySelector('#session-theme').textContent = label(question.theme);
    document.querySelector('#session-question').textContent = question.title;
    const answer = document.querySelector('#session-answer');
    answer.hidden = !state.revealed;
    answer.innerHTML = `<p>Use the canonical field note to compare your answer with the answer guide and sources.</p><a href="${question.path}">Open canonical answer guide <b>→</b></a>`;
    document.querySelector('#previous-question').disabled = state.index === 0;
    document.querySelector('#next-question').disabled = state.index === session.length - 1;
    document.querySelector('#reveal-answer').textContent = state.revealed ? 'Answer revealed' : 'Reveal answer link';
    updateUrl();
  }

  function startSession() {
    const selected = selectedThemes();
    if (!selected.length) { document.querySelector('#session-message').textContent = 'Select at least one Theme to build a session.'; return; }
    const total = Math.max(1, Number(totalInput.value) || DEFAULT_TOTAL);
    const allocations = allocationInputs();
    const allocatedTotal = selected.reduce((sum, theme) => sum + (allocations[theme] || 0), 0);
    if (allocatedTotal !== total) { document.querySelector('#session-message').textContent = `Your selected Theme allocations total ${allocatedTotal}; they must total ${total}.`; return; }
    const unavailable = selected.find((theme) => (allocations[theme] || 0) > data.filter((question) => question.theme === theme).length);
    if (unavailable) { document.querySelector('#session-message').textContent = `${label(unavailable)} does not have enough unique Questions for that allocation.`; return; }
    state = { themes: selected, total, allocations, seed: newSeed(), index: 0, revealed: false };
    session = createSession(data, selected, total, state.seed, allocations);
    if (session.length !== total) { document.querySelector('#session-message').textContent = 'Those Themes do not contain enough unique Questions for that allocation.'; return; }
    builder.hidden = true; deck.hidden = false; renderDeck();
  }

  themeList.addEventListener('change', (event) => {
    if (event.target.type === 'checkbox') {
      state.themes = selectedThemes();
      state.allocations = balanceAllocations(state.themes, Number(totalInput.value) || DEFAULT_TOTAL);
      renderThemeChooser();
    } else {
      state.allocations = allocationInputs();
      updateUrl();
    }
  });
  totalInput.addEventListener('change', () => { state.total = Math.max(1, Number(totalInput.value) || DEFAULT_TOTAL); state.allocations = balanceAllocations(state.themes, state.total); renderThemeChooser(); });
  document.querySelector('#start-session').addEventListener('click', startSession);
  document.querySelector('#reveal-answer').addEventListener('click', () => { state.revealed = true; renderDeck(); });
  document.querySelector('#previous-question').addEventListener('click', () => { state.index -= 1; state.revealed = false; renderDeck(); });
  document.querySelector('#next-question').addEventListener('click', () => { state.index += 1; state.revealed = false; renderDeck(); });
  document.querySelector('#restart-session').addEventListener('click', () => { state.index = 0; state.revealed = false; renderDeck(); });
  document.querySelector('#edit-session').addEventListener('click', () => { builder.hidden = false; deck.hidden = true; });

  if (state.themes.length) {
    totalInput.value = state.total;
    state.allocations = Object.keys(state.allocations).length ? state.allocations : balanceAllocations(state.themes, state.total);
    renderThemeChooser();
    session = createSession(data, state.themes, state.total, state.seed);
    if (session.length === state.total) { builder.hidden = true; deck.hidden = false; state.index = Math.min(state.index, session.length - 1); renderDeck(); }
  } else {
    renderThemeChooser();
  }
})();
