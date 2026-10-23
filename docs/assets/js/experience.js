/* Continuous presentation navigation. Reading scroll is never intercepted. */
(()=>{'use strict';
const body=document.body,$=s=>document.querySelector(s),nav=$('#pageNav'),toggle=$('#menuToggle'),mobile=matchMedia('(max-width:1170px)'),motion=matchMedia('(prefers-reduced-motion: reduce)');
function close(focus=false){nav?.classList.remove('is-open');toggle?.setAttribute('aria-expanded','false');if(focus)toggle?.focus()}
toggle?.addEventListener('click',()=>{const open=nav.classList.toggle('is-open');toggle.setAttribute('aria-expanded',String(open));if(open)nav.querySelector('.is-current')?.focus()});
nav?.addEventListener('click',e=>{if(e.target.closest('a'))close()});document.addEventListener('click',e=>{if(!e.target.closest('.p-masthead'))close()});addEventListener('keydown',e=>{if(e.key==='Escape')close(true)});mobile.addEventListener('change',()=>close());
const sections=[...document.querySelectorAll('main>.p-section')],links=[...document.querySelectorAll('.p-nav-link')];let tick=false;
const language=$('#languageSwitch');const languageBase=language?new URL(language.href):null;
function update(){if(sections.length){let current=sections[0].id;for(const section of sections){if(section.getBoundingClientRect().top<=170)current=section.id}links.forEach(a=>{const active=a.dataset.section===current;a.classList.toggle('is-current',active);if(active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')});if(languageBase){const u=new URL(languageBase);u.hash=current;language.href=u.href}}tick=false}
addEventListener('scroll',()=>{if(!tick){requestAnimationFrame(update);tick=true}},{passive:true});update();
// Reveal panels only once; UI changes use a short transition, not perpetual motion.
if(!motion.matches&&'IntersectionObserver'in window){const io=new IntersectionObserver(xs=>xs.forEach(x=>{if(x.isIntersecting){x.target.classList.add('p-arrived');io.unobserve(x.target)}}),{threshold:.12});document.querySelectorAll('.p-release-story,.p-architecture-stage').forEach(el=>io.observe(el))}
motion.addEventListener('change',e=>{body.classList.toggle('p-reduced',e.matches);if($('#heroMotion'))$('#heroMotion').disabled=e.matches;const loop=$('#caseAutoplay');if(e.matches&&loop?.getAttribute('aria-pressed')==='true')loop.click();if(loop)loop.disabled=e.matches;if(e.matches)document.querySelectorAll('.p-reveal').forEach(x=>x.classList.add('is-visible'))});
const hero=$('#heroMotion');hero?.addEventListener('click',()=>{const paused=$('.p-cover').classList.toggle('is-paused');hero.setAttribute('aria-pressed',String(paused));hero.textContent=body.dataset.lang==='en'?(paused?'▷ Play motion':'Ⅱ Pause motion'):(paused?'▷ 播放动态':'Ⅱ 暂停动态')});if(hero&&motion.matches)hero.disabled=true;
const loop=$('#caseAutoplay');if(loop&&motion.matches){loop.disabled=true;loop.title=body.dataset.lang==='en'?'Reduced-motion preference is enabled':'已启用减少动态效果'}
})();

if('IntersectionObserver'in window&&document.querySelector('.p-cover-media')){new IntersectionObserver(xs=>{document.querySelector('.p-cover-media').style.animationPlayState=xs[0].isIntersecting&&!document.querySelector('.p-cover').classList.contains('is-paused')?'running':'paused'}).observe(document.querySelector('.p-cover'))}
