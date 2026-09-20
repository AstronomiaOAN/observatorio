'use strict';
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});document.addEventListener('keydown',ev=>{if(ev.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus()}})}
const page=location.pathname.split('/').pop()||'index.html';
document.querySelectorAll('nav a').forEach(a=>{if(a.getAttribute('href')===page)a.setAttribute('aria-current','page')});
const search=document.querySelector('#media-search');
const filters=[...document.querySelectorAll('[data-filter]')];
const items=[...document.querySelectorAll('[data-media]')];
let selected='todos';
function normalize(value){return value.toLocaleLowerCase('es').normalize('NFD').replace(/[\u0300-\u036f]/g,'')}
function applyFilters(){const query=normalize(search?.value||'');let count=0;items.forEach(item=>{const show=(selected==='todos'||item.dataset.media===selected)&&normalize(item.textContent).includes(query);item.hidden=!show;if(show)count++});const status=document.querySelector('#media-count');if(status)status.textContent=`${count} recurso${count===1?'':'s'}`;const empty=document.querySelector('.empty');if(empty)empty.style.display=count?'none':'block'}
filters.forEach(button=>button.addEventListener('click',()=>{selected=button.dataset.filter;filters.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));applyFilters()}));
if(search)search.addEventListener('input',applyFilters);
if(items.length)applyFilters();
if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('reveal');observer.unobserve(entry.target)}}),{threshold:.12});document.querySelectorAll('.section-heading,.image-card,.friends-banner').forEach(el=>observer.observe(el))}
