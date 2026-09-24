'use strict';
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});document.addEventListener('keydown',ev=>{if(ev.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus()}})}
const page=location.pathname.split('/').pop()||'index.html';
document.querySelectorAll('#navigation a').forEach(a=>{if(a.getAttribute('href')===page)a.setAttribute('aria-current','page')});
const search=document.querySelector('#media-search');
const filters=[...document.querySelectorAll('[data-filter]')];
const items=[...document.querySelectorAll('[data-media]')];
let selected='todos';
function normalize(value){return value.toLocaleLowerCase('es').normalize('NFD').replace(/[\u0300-\u036f]/g,'')}
function applyFilters(){const query=normalize(search?.value||'');let count=0;items.forEach(item=>{const show=(selected==='todos'||item.dataset.media===selected)&&normalize(item.textContent).includes(query);item.hidden=!show;if(show)count++});const status=document.querySelector('#media-count');if(status)status.textContent=document.documentElement.lang==='en'?`${count} resource${count===1?'':'s'}`:`${count} recurso${count===1?'':'s'}`;const empty=document.querySelector('.empty');if(empty)empty.style.display=count?'none':'block'}
filters.forEach(button=>button.addEventListener('click',()=>{selected=button.dataset.filter;filters.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));applyFilters()}));
if(search)search.addEventListener('input',applyFilters);
if(items.length)applyFilters();
if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('reveal');observer.unobserve(entry.target)}}),{threshold:.12});document.querySelectorAll('.section-heading,.image-card,.friends-banner').forEach(el=>observer.observe(el))}
const isEnglish=document.documentElement.lang==='en';
// Switching language preserves the section hash without changing external links.
document.querySelectorAll('.language-switch a').forEach(a=>{if(location.hash)a.href+=location.hash});
document.querySelectorAll('.utility-nav>a').forEach(a=>{if(a.getAttribute('href')===page)a.setAttribute('aria-current','page')});
const talkSearch=document.querySelector('#talk-search');
const talkCards=[...document.querySelectorAll('[data-talk]')];
const yearButtons=[...document.querySelectorAll('[data-year-filter]')];
let talkYear='all';
function filterTalks(){const q=normalize(talkSearch?.value||'');let count=0;talkCards.forEach(card=>{const show=(talkYear==='all'||card.dataset.year===talkYear)&&normalize(card.textContent).includes(q);card.hidden=!show;if(show)count++});const status=document.querySelector('#talk-count');if(status)status.textContent=isEnglish?`${count} talk${count===1?'':'s'}`:`${count} conferencia${count===1?'':'s'}`;const empty=document.querySelector('#talk-empty');if(empty)empty.hidden=count>0;}
yearButtons.forEach(button=>button.addEventListener('click',()=>{talkYear=button.dataset.yearFilter;yearButtons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));filterTalks()}));
if(talkSearch){talkSearch.addEventListener('input',filterTalks);filterTalks()}
// YouTube needs an HTTP Referer. A file:// page cannot supply one.
document.querySelectorAll('iframe[data-youtube-src]').forEach(frame=>{
 if(location.protocol==='https:'||location.protocol==='http:'){
  frame.referrerPolicy='strict-origin-when-cross-origin';
  frame.src=frame.dataset.youtubeSrc;
 }else{
  const box=document.createElement('div');box.className='video-local-message';
  const message=document.createElement('p');
  message.textContent=isEnglish?'To play this tour within the page, open the online version. YouTube cannot identify a page opened directly from a local file.':'Para reproducir el recorrido dentro de la página, abre la versión web. YouTube no puede identificar una página abierta directamente desde un archivo local.';
  const online=document.createElement('a');online.className='button';online.href='https://observatorio-nacional-colombia.savory-brush-1142.chatgpt.site/'+(isEnglish?'en/':'')+'patrimonio.html';online.target='_blank';online.rel='noopener';online.textContent=isEnglish?'Open online tour ↗':'Abrir recorrido en la web ↗';
  const direct=document.createElement('a');direct.href='https://www.youtube.com/watch?v=9gAK0wLzbLM';direct.target='_blank';direct.rel='noopener';direct.textContent=isEnglish?'Watch on YouTube ↗':'Ver en YouTube ↗';
  box.append(message,online,direct);frame.replaceWith(box);
 }
});
