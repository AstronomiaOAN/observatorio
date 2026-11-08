(() => {
  'use strict';
  const hero = document.querySelector('.hero-slideshow');
  const button = document.querySelector('.motion-toggle');
  if (!hero || !button) return;
  const slides = [...hero.querySelectorAll('.hero-slide')];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const en = document.documentElement.lang === 'en';
  let paused = reduced.matches, timer = null, current = 0;
  function sync() {
    clearInterval(timer);
    document.body.classList.toggle('motion-paused', paused || document.hidden);
    button.setAttribute('aria-pressed', String(paused));
    button.textContent = paused ? (en ? 'Resume animation' : 'Reanudar animación') : (en ? 'Pause animation' : 'Pausar animación');
    if (paused || document.hidden) return;
    timer = setInterval(() => {
      let next = current;
      for (let offset = 1; offset < slides.length; offset++) {
        const candidate = (current + offset) % slides.length;
        if (slides[candidate].complete && slides[candidate].naturalWidth) { next = candidate; break; }
      }
      if (next === current) return;
      slides[current].classList.remove('is-active');
      slides[next].classList.add('is-active');
      current = next;
    }, 5000);
  }
  button.addEventListener('click', () => { paused = !paused; sync(); });
  reduced.addEventListener('change', () => { paused = reduced.matches; sync(); });
  document.addEventListener('visibilitychange', sync);
  sync();
})();
