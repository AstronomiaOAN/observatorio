(() => {
 const en = document.documentElement.lang === 'en';
 const normalize = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
 const form = document.querySelector('#publication-form');
 if (form) {
  const query = document.querySelector('#publication-search');
  const year = document.querySelector('#publication-year');
  const kind = document.querySelector('#publication-kind');
  const cards = [...document.querySelectorAll('[data-publication]')];
  const update = () => {
   const terms = normalize(query.value.trim()).split(/\s+/).filter(Boolean);
   let count = 0;
   cards.forEach(card => {
    const visible = terms.every(t => normalize(card.textContent).includes(t)) && (year.value === 'all' || card.dataset.year === year.value) && (kind.value === 'all' || card.dataset.kind === kind.value);
    card.hidden = !visible; count += Number(visible);
   });
   document.querySelectorAll('[data-publication-year]').forEach(group => {group.hidden = ![...group.querySelectorAll('[data-publication]')].some(card => !card.hidden);});
   document.querySelector('#publication-count').textContent = `${count} ${en ? 'of' : 'de'} ${cards.length} ${en ? 'publications' : 'publicaciones'}`;
   document.querySelector('#publication-empty').hidden = count !== 0;
  };
  form.addEventListener('input', update); form.addEventListener('change', update);
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('reset', () => setTimeout(update, 0)); update();
 }
 document.querySelectorAll('.load-playlist').forEach(button => button.addEventListener('click', () => {
  const box = button.closest('[data-playlist]');
  if (!/^https?:$/.test(location.protocol)) {
   const msg = document.createElement('p');msg.textContent = en ? 'Open the season on YouTube using the link below, or serve this website over HTTP to use the player.' : 'Abre la temporada en YouTube con el enlace inferior, o usa la versión web para reproducirla aquí.';box.replaceChildren(msg);return;
  }
  const frame = document.createElement('iframe');
  frame.src = `https://www.youtube-nocookie.com/embed/videoseries?list=${encodeURIComponent(box.dataset.playlist)}`;
  frame.title = en ? 'Navegando por el Cosmos playlist' : 'Lista de Navegando por el Cosmos';
  frame.referrerPolicy = 'strict-origin-when-cross-origin';frame.allow = 'encrypted-media; picture-in-picture; fullscreen';frame.allowFullscreen = true;
  box.replaceChildren(frame);
 }));
})();
