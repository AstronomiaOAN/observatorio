(() => {
 const form = document.querySelector('.alumni-filters');
 if (!form) return;
 const search = document.querySelector('#alumni-search');
 const program = document.querySelector('#alumni-program');
 const year = document.querySelector('#alumni-year');
 const cards = [...document.querySelectorAll('.alumni-card')];
 const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
 const update = () => {
  const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
  let count = 0;
  cards.forEach(card => {
   const text = normalize(card.dataset.search);
   const visible = terms.every(term => text.includes(term)) && (program.value === 'all' || card.dataset.program === program.value) && (year.value === 'all' || card.dataset.year === year.value);
   card.hidden = !visible;
   count += Number(visible);
  });
  document.querySelectorAll('.alumni-year').forEach(group => { group.hidden = ![...group.querySelectorAll('.alumni-card')].some(card => !card.hidden); });
  const en = document.documentElement.lang === 'en';
  document.querySelector('#alumni-count').textContent = `${count} ${en ? 'of 117 records' : 'de 117 registros'}`;
  document.querySelector('#alumni-empty').hidden = count !== 0;
 };
 form.addEventListener('input', update);
 form.addEventListener('change', update);
 form.addEventListener('submit', event => event.preventDefault());
 form.addEventListener('reset', () => setTimeout(update, 0));
 update();
})();
