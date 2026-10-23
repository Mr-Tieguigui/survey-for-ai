/* Chapter navigation and progressive motion; ordinary links remain the baseline. */
(()=>{'use strict';
const $=s=>document.querySelector(s),body=document.body,en=body.dataset.lang==='en',t=(zh,eng)=>en?eng:zh;
const media=matchMedia('(prefers-reduced-motion: reduce)'),fine=matchMedia('(hover:hover) and (pointer:fine)');
const rail=$('#chapterRail'),menu=$('#menuToggle'),option=$('#chapterScroll'),isArchive=body.dataset.archive==='true';
const links=[...document.querySelectorAll('[data-chapter]')],index=links.findIndex(a=>a.classList.contains('is-current'));
let reduced=media.matches,enabled=!isArchive,busy=false,lastY=scrollY,boundaryAt=0,edge='',energy=0,lastWheel=0,armed=false;
const setting='survey-chapter-scroll';
try{enabled=enabled&&localStorage.getItem(setting)!=='off'}catch{}
if(option){option.checked=enabled;option.disabled=isArchive;option.addEventListener('change',()=>{enabled=option.checked;reset();try{localStorage.setItem(setting,enabled?'on':'off')}catch{}})}
const mobile=matchMedia('(max-width:900px)');function syncRail(){rail.inert=mobile.matches&&!body.classList.contains('p-rail-open')}mobile.addEventListener('change',()=>{body.classList.remove('p-rail-open');menu?.setAttribute('aria-expanded','false');syncRail()});syncRail();
function toggleRail(open){body.classList.toggle('p-rail-open',open);menu?.setAttribute('aria-expanded',String(open));syncRail();if(open)rail.querySelector('[aria-current]')?.focus({preventScroll:true});else menu?.focus({preventScroll:true})}
menu?.addEventListener('click',()=>toggleRail(!body.classList.contains('p-rail-open')));
$('#railBackdrop')?.addEventListener('click',()=>toggleRail(false));
addEventListener('keydown',e=>{if(e.key==='Escape'&&body.classList.contains('p-rail-open'))toggleRail(false);if(e.key==='Tab'&&body.classList.contains('p-rail-open')){const nodes=[menu,...rail.querySelectorAll('a,input:not(:disabled)')],first=nodes[0],last=nodes.at(-1);if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}}});
function reset(){energy=0;armed=false;boundaryAt=performance.now();$('#chapterToast')?.classList.remove('is-visible')}
function boundary(){const max=Math.max(0,document.documentElement.scrollHeight-innerHeight);return scrollY>=max-3?'bottom':scrollY<=2?'top':''}
function progress(){const max=document.documentElement.scrollHeight-innerHeight,p=max>0?Math.min(1,Math.max(0,scrollY/max)):1;body.style.setProperty('--chapter-progress',p);const now=boundary();if(now!==edge){edge=now;reset()}lastY=scrollY}
addEventListener('scroll',progress,{passive:true});progress();
function go(a,direction,fromScroll=false){if(!a||busy)return;busy=true;body.dataset.travel=direction;try{sessionStorage.setItem('survey-travel',JSON.stringify({path:new URL(a.href).pathname,direction,end:fromScroll&&direction==='previous',time:Date.now()}))}catch{}body.classList.add('p-leaving');location.assign(a.href)}
// Only intercept unmodified same-origin chapter clicks. New tabs, downloads and anchors stay native.
document.querySelectorAll('.p-chapter-link,.p-adjacent').forEach(a=>a.addEventListener('click',e=>{if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||a.getAttribute('aria-current')==='page')return;e.preventDefault();go(a,a.dataset.direction==='previous'||links.indexOf(a)>=0&&links.indexOf(a)<index?'previous':'next')}));
try{const travel=JSON.parse(sessionStorage.getItem('survey-travel')||'null');sessionStorage.removeItem('survey-travel');if(travel&&travel.path===location.pathname&&Date.now()-travel.time<10000){body.dataset.travel=travel.direction;body.classList.add('p-entering');setTimeout(()=>body.classList.remove('p-entering'),650);if(travel.end&&!location.hash)requestAnimationFrame(()=>scrollTo({top:document.documentElement.scrollHeight,behavior:'instant'}))}}catch{}
addEventListener('pageshow',()=>{busy=false;body.classList.remove('p-leaving');progress()});
const nested='input,textarea,select,pre,[contenteditable],.p-rail,.p-masthead,.p-table-scroll,.p-network,.p-branch-list,.p-stage-list,.p-question-list,.p-tabs';
function attempt(direction,delta,gap){if(!enabled||busy||body.classList.contains('p-rail-open')||isArchive)return;
 const wanted=direction==='next'?'bottom':'top',next=links[index+(direction==='next'?1:-1)];if(!next||boundary()!==wanted){reset();return}
 // A fresh gesture after a pause is required: inertia from reading never changes a chapter.
 if(performance.now()-boundaryAt<650)return;
 if(!armed){if(gap<180)return;armed=true;energy=0}
 energy+=Math.min(Math.abs(delta),80);const toast=$('#chapterToast');toast.textContent=t('继续滚动进入','Keep scrolling for')+' '+next.textContent.replace('↗','').trim();toast.classList.add('is-visible');
 if(energy>=150)go(next,direction,true)
}
addEventListener('wheel',e=>{const now=performance.now(),gap=now-lastWheel;lastWheel=now;if(e.ctrlKey||Math.abs(e.deltaX)>Math.abs(e.deltaY)||e.target.closest(nested))return;const amount=e.deltaY*(e.deltaMode===1?16:e.deltaMode===2?innerHeight:1);attempt(amount>0?'next':'previous',amount,gap)},{passive:true});
let touch=null;
addEventListener('touchstart',e=>{if(e.touches.length!==1||e.target.closest(nested)){touch=null;return}touch={y:e.touches[0].clientY,x:e.touches[0].clientX,edge:boundary(),at:performance.now()}},{passive:true});
addEventListener('touchend',e=>{if(!touch||!enabled||isArchive||busy||body.classList.contains('p-rail-open'))return;const dy=touch.y-e.changedTouches[0].clientY,dx=touch.x-e.changedTouches[0].clientX,direction=dy>0?'next':'previous',wanted=dy>0?'bottom':'top';if(touch.edge===wanted&&boundary()===wanted&&Math.abs(dy)>120&&Math.abs(dy)>Math.abs(dx)*1.5&&touch.at-boundaryAt>650)go(links[index+(dy>0?1:-1)],direction,true);touch=null},{passive:true});
// Subtle pointer light and elevation. No continuous JavaScript animation loop.
const surfaces='.p-hero-figure,.p-code-panel,.p-case-protocol,.p-archive-brief,.p-resource-grid>a,.p-adjacent,.p-home-strip>div,.p-example-door';
document.addEventListener('pointermove',e=>{if(reduced||!fine.matches)return;const card=e.target.closest(surfaces);if(!card)return;const r=card.getBoundingClientRect();card.style.setProperty('--light-x',`${(e.clientX-r.left)/r.width*100}%`);card.style.setProperty('--light-y',`${(e.clientY-r.top)/r.height*100}%`)},{passive:true});
function revealChildren(){if(reduced||!('IntersectionObserver'in window))return;const observer=new IntersectionObserver(xs=>xs.forEach(x=>{if(x.isIntersecting){x.target.classList.add('p-arrived');observer.unobserve(x.target)}}),{threshold:.05});document.querySelectorAll('.p-home-strip>*,.p-resource-grid>a,.p-module-routes>a,.p-stats>div,.p-adjacent').forEach((el,i)=>{el.classList.add('p-stagger');el.style.setProperty('--delay',`${Math.min(i%6*65,260)}ms`);observer.observe(el)})}
revealChildren();
media.addEventListener('change',e=>{reduced=e.matches;body.classList.toggle('p-reduced',reduced);if(reduced){document.querySelectorAll('.p-reveal,.p-stagger').forEach(el=>el.classList.add('is-visible','p-arrived'));$('.p-hero-figure')?.style.removeProperty('transform')}});
})();
