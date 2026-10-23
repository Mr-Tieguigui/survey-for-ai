(()=>{'use strict';const prefix=document.body.dataset.prefix||'./',$=s=>document.querySelector(s),E=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
try{if(localStorage.getItem('rsi-theme')==='light')document.body.classList.add('theme-light')}catch{}
$('#themeToggle').onclick=()=>{document.body.classList.toggle('theme-light');try{localStorage.setItem('rsi-theme',document.body.classList.contains('theme-light')?'light':'dark')}catch{}};
$('#menuToggle').onclick=()=>{const open=$('.navlinks').classList.toggle('mobile-open');$('#menuToggle').setAttribute('aria-expanded',String(open))};
if(document.body.dataset.page==='home'){const s=document.createElement('script');s.src=prefix+'assets/js/home.js';document.body.appendChild(s)}
if(document.body.dataset.page!=='explore')return;
const L=window.RSI_LIBRARY,xs=L.cards;$('#exploreRole').innerHTML+=[...new Map(xs.map(x=>[x.role,x.role_label])).entries()].map(([k,v])=>`<option value="${E(k)}">${E(v)}</option>`).join('');$('#exploreBranch').innerHTML+=L.branches.map(x=>`<option value="${E(x.id)}">${E(x.name)}</option>`).join('');
let count=24;const corpus=new Map(xs.map(x=>[x.work_family_id,JSON.stringify([x.title,x.summary,x.claims,x.reviews]).toLowerCase()]));
function draw(reset=true){if(reset)count=24;const q=$('#exploreSearch').value.toLowerCase().trim(),role=$('#exploreRole').value,branch=$('#exploreBranch').value,pass=$('#onlyPassages').checked;
const matches=xs.filter(x=>(!q||corpus.get(x.work_family_id).includes(q))&&(!role||x.role===role)&&(!branch||x.branch_id===branch)&&(!pass||x.primary_passages>0));$('#exploreCount').textContent=`${matches.length} / 808 篇 · 展示 ${Math.min(matches.length,count)} 篇`;
$('#exploreRows').innerHTML=matches.slice(0,count).map(x=>`<a class="paper-row" href="${prefix}${E(x.article)}"><span class="paper-year">${E(x.year||'—')}</span><div><b>${E(x.title)}</b><p>${E(x.summary)}</p></div><div class="paper-status"><span>${E(x.role_label)}</span><span>${x.primary_passages} 段已存正文</span><span>${x.claim_count} 条主张 · ${x.config_count} 个配置</span></div><span>↗</span></a>`).join('')||'<p class="empty">未找到记录。请更换关键词或筛选条件。</p>';$('#exploreMore').hidden=count>=matches.length}
$('#exploreSearch').oninput=()=>draw();$('#exploreRole').onchange=()=>draw();$('#exploreBranch').onchange=()=>draw();$('#onlyPassages').onchange=()=>draw();$('#exploreMore').onclick=()=>{count+=24;draw(false)};
const params=new URLSearchParams(location.search);if(params.has('q'))$('#exploreSearch').value=params.get('q');if(params.has('branch'))$('#exploreBranch').value=params.get('branch');draw();
})();
