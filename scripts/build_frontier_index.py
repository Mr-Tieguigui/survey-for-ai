"""Build/check bilingual frontier directories from scope proposals. No network or model calls."""
from pathlib import Path
import argparse,json,re
R=Path(__file__).resolve().parents[1];F=R/'frontiers'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def clean(s):return str(s).replace('|',' / ').replace('\n',' ')
def render():
 registry=load(F/'registry.json');directions=[];seen=set();outputs={}
 for item in registry['directions']:
  path=(F/item['scope_path']).resolve()
  assert path.is_relative_to(F.resolve()) and path.name=='scope.json',item
  scope=load(path);ident=scope['domain_id']
  assert re.fullmatch(r'[a-z][a-z0-9-]{0,63}',ident) and ident==item['id'] and path.parent.name==ident
  assert ident not in seen;seen.add(ident)
  assert scope['status'] in registry['states']
  assert all(isinstance(scope[k],int) and scope[k]>=0 for k in ['completed_primary_reviews','admitted_claims'])
  assert all(set(scope[k])=={'en','zh'} for k in ['name','focus','reader_questions','comparison_axes'])
  assert all(len(scope[k]['en'])==len(scope[k]['zh']) for k in ['reader_questions','comparison_axes'])
  if scope['status']=='proposed':assert scope['completed_primary_reviews']==scope['admitted_claims']==0
  for source in scope['seed_sources']:
   assert source['url'].startswith('https://') and source['permission']=='navigation_only' and not source['primary_body_reviewed']
  directions.append(scope)
 def table(lang,prefix):
  zh=lang=='zh';header='| 编号 | 候选方向 | 核心研究问题 | 状态 | 文件夹 |\n|---|---|---|---|---|\n' if zh else '| ID | Proposed survey | Research question | Status | Directory |\n|---|---|---|---|---|\n'
  labels={'proposed':('待启动','Proposed'),'scoped':('范围已定','Scoped'),'curating':('证据整理中','Curating'),'synthesizing':('综合中','Synthesizing'),'ready':('按声明范围就绪','Ready within declared scope')}
  for i,s in enumerate(directions,1):
   status=labels[s['status']][0 if zh else 1];header+=f'| F{i:02} | {clean(s["name"][lang])} | {clean(s["focus"][lang])} | ○ {status} | [{s["domain_id"]}]({prefix}{s["domain_id"]}/) |\n'
  return header+('| ＋ | **你的领域** | 提出范围与读者问题 | 开放补充 | [_template]('+prefix+'_template/) |\n' if zh else '| ＋ | **Your domain** | Define the scope and reader questions | Open slot | [_template]('+prefix+'_template/) |\n')
 for lang,filename in [('en','README.md'),('zh','README_CN.md')]:
  title='前沿 Survey · 开放方向目录' if lang=='zh' else 'Frontier Surveys · Open Direction Directory'
  intro=('这些是待认领的研究提案，不是已完成的 Survey。RSI 仍为现有实例，且独立管理其固定语料。提案中的链接仅有发现导航权限；候选目录不增加 RSI 的收录量。' if lang=='zh' else 'These are unassigned research proposals, not completed surveys. RSI remains the worked example with its own fixed corpus. Discovery links carry navigation permission only; this directory does not enlarge RSI membership.')
  steps=('1. 选择候选方向；或复制 `_template/` 到新 ID 的目录。\n2. 编辑该目录的 `scope.json`：名称、问题、比较轴、一手发现入口及责任人。\n3. 在 `registry.json` 的 `directions` 中登记 ID 和相对范围文件路径。\n4. 执行下方构建与检查命令，自动同步本目录及项目主 README 的中英文表格。\n5. 按[主 README 的步骤](../README_CN.md#为其他领域构建-survey)，将实际研究初始化到该方向的 `survey/` 子目录。\n6. 完成相应阶段后再修改状态；`ready` 仅指声明范围的验收，并保留证据深度与例外。' if lang=='zh' else '1. Choose a direction, or copy `_template/` to a new domain-ID folder.\n2. Edit its `scope.json`: name, questions, comparison axes, first-party entry points and maintainer.\n3. Register the ID and relative scope path in `registry.json` under `directions`.\n4. Run the commands below to synchronize this index and both project README tables.\n5. Follow the [project onboarding](../README.md#build-a-survey-in-another-domain) to initialize actual research inside the direction\'s `survey/` child.\n6. Change status only after the corresponding work exists. `ready` refers to the declared scope and retains evidence-depth and exception disclosures.')
  outputs[F/filename]=f'# {title}\n\n[English](README.md) · [简体中文](README_CN.md) · [Registry](registry.json)\n\n{intro}\n\n'+table(lang,'')+'\n## '+('如何补充' if lang=='zh' else 'How to contribute')+'\n\n'+steps+'\n\n```bash\npython scripts/build_frontier_index.py\npython scripts/build_frontier_index.py --check\n```\n\n'+('命令在仓库根目录执行，无需模型或网络。`registry.json` 只登记目录，各方向的 `scope.json` 是提案内容的维护源；README 为生成视图。不要在提案中计入未做的正文审查。' if lang=='zh' else 'Run from the repository root, without a model or network. `registry.json` registers locations; each `scope.json` owns the proposal content. README files are generated views. Never count unread sources as primary reviews.')+'\n'
  p=R/filename;s=p.read_text(encoding='utf-8');pattern=r'<!-- frontier-directory:start -->.*?<!-- frontier-directory:end -->'
  assert len(re.findall(pattern,s,re.S))==1,filename
  outputs[p]=re.sub(pattern,'<!-- frontier-directory:start -->\n'+table(lang,'frontiers/')+'<!-- frontier-directory:end -->',s,flags=re.S)
 for s in directions+[load(F/'_template/scope.json')]:
  template=s['domain_id']=='your-domain';folder=F/('_template' if template else s['domain_id'])
  sources='\n'.join(f'- [{x["label"]}]({x["url"]}) — checked {x["checked_on"]}; discovery/navigation only, not primary-body review.' for x in s['seed_sources']) or '- Add a first-party discovery entry with its URL and check date. / 填写一手发现入口、URL 与核对日期。'
  owner=s['maintainer'] or 'Unassigned / 待认领'
  outputs[folder/'README.md']=f'''# {s['name']['en']} / {s['name']['zh']}

[All directions / 全部方向](../README.md) · [中文目录](../README_CN.md) · [Machine-readable scope / 范围文件](scope.json)

> Proposal only / 方向提案。The README is generated from `scope.json`; maintain research records in `survey/` once initialized. / 本页由范围文件生成，实际研究启动后写入 `survey/`。

| Field / 字段 | Value / 当前值 |
|---|---|
| Status / 状态 | `{s['status']}` |
| Maintainer / 责任人 | {owner} |
| Primary reviews / 已完成原文审查 | {s['completed_primary_reviews']} |
| Admitted claims / 准入主张 | {s['admitted_claims']} |
| Scope lock / 范围锁 | {s['scope_lock'] or 'Not set / 未设置'} |
| Search cutoff / 检索截止 | {s['search_cutoff'] or 'Not set / 未设置'} |

## Proposed research question / 候选研究问题

{s['focus']['en']}

{s['focus']['zh']}

## Reader questions / 读者问题

'''+('\n'.join('- '+a+' / '+b for a,b in zip(s['reader_questions']['en'],s['reader_questions']['zh'])) or '- Define the reader questions. / 填写读者问题。')+'''

## Comparison axes / 比较维度

'''+('\n'.join('- '+a+' / '+b for a,b in zip(s['comparison_axes']['en'],s['comparison_axes']['zh'])) or '- Define role-appropriate comparison axes. / 填写对应角色的比较维度。')+f'''

## Discovery entries / 一手发现入口

{sources}

These mutable project pages are navigation seeds, not a frozen bibliography or technical citation evidence. Resolve exact paper identities, source versions and body locators during curation. / 动态项目页是发现种子，不是已固定书目或技术引用依据；正式整理时再确认论文身份、版本和正文定位。

## Start / 启动

Use the [project onboarding](../../README.md#build-a-survey-in-another-domain) / [中文步骤](../../README_CN.md#为其他领域构建-survey). Replace the example ID and output with this direction. A new or empty `survey/` child can be initialized; keep the proposal parent intact. / 替换示例 ID 与输出位置，在全新或空白的 `survey/` 子目录初始化，保留父目录提案。

`proposed → scoped → curating → synthesizing → ready` describes work status, not an automatic evidence upgrade. / 状态变化不自动提升证据权限。
'''
 return outputs,len(directions)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();out,count=render()
 stale=[str(f.relative_to(R)) for f,text in out.items() if not f.exists() or f.read_text(encoding='utf-8')!=text]
 if a.check:
  print(json.dumps({'status':'pass' if not stale else 'fail','directions':count,'open_template':True,'stale_files':stale}));raise SystemExit(bool(stale))
 for f,text in out.items():f.write_text(text,encoding='utf-8',newline='\n')
 print(json.dumps({'status':'built','directions':count,'generated_files':len(out),'model_calls':0,'network_calls':0}))
if __name__=='__main__':main()
