#!/usr/bin/env python3
"""Initialize a domain-neutral survey workspace. Empty inventories are explicitly draft, never completed reviews."""
from pathlib import Path
import argparse,json,re

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--domain-id',required=True)
    p.add_argument('--name',required=True)
    p.add_argument('--scope',required=True)
    a=p.parse_args()
    if not re.fullmatch(r'[a-z][a-z0-9-]{0,63}',a.domain_id):p.error('domain-id must use lowercase letters, digits and hyphens')
    root=a.output.resolve()
    if root.exists() and any(root.iterdir()):p.error('output must be new or empty; existing surveys are resumed, never reset')
    root.mkdir(parents=True,exist_ok=True)
    def write(name,obj):
        dest=root/name;dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    adapter={'schema_version':'survey-domain-adapter-v1','domain_id':a.domain_id,'name':a.name,
      'operational_definition':a.scope,'scope':{'inclusions':[],'exclusions':[],'search_cutoff':None,'search_sources':[],
      'completion_unit':'versioned work family with role-specific evidence decisions'},
      'roles':{'method':['problem','inputs_outputs','mechanism','assumptions','evaluation_protocol','limits'],
      'benchmark':['task_unit','data_split','metric','selection','validity_limits'],
      'theory':['definitions','assumptions','statement','proof_scope','limits'],
      'survey_background':['coverage','definitions','organization','relevance','limits']},
      'comparison_axes':[],'relation_vocabulary':{'extends':'requires evidence from both endpoints',
      'compares_with':'requires explicit shared axes; does not imply a shared evaluation protocol',
      'contrasts_with':'curator comparison must be labeled; does not imply ancestry'},
      'reader_profiles':[],'reader_questions':[],
      'budget':{'source_read_limit':None,'model_token_limit':None,'review_mode':'targeted_self_review'},
      'publication':{'status':'local_draft','audience':None,'source_quote_export':'excluded_by_default'}}
    write('method/domain_adapter.json',adapter)
    for name in ['works','sources','evidence','configurations','claims','relations','frontiers','assignments']:
        dest=root/'catalog'/(name+'.jsonl');dest.parent.mkdir(exist_ok=True);dest.write_bytes(b'')
    for name in ['branches','modules','questions','reader_profiles']:write('catalog/'+name+'.json',[])
    write('catalog/dependency_index.json',{'claim_consumers':{},'work_family_consumers':{},'configuration_consumers':{}})
    write('catalog/domain.json',{'domain_id':a.domain_id,'name':a.name,'release_version':'0.1.0-draft',
        'operational_definition':a.scope,'completion_scope':'unfrozen','data_sources':[],'views':[]})
    write('work/run_state.json',{'status':'scope_definition_required','accepted_work_ids':[],
        'pending_scope_fields':['inclusions','exclusions','search_cutoff','search_sources','comparison_axes','reader_questions'],
        'completed_primary_reviews':0,'next_action':'Complete the domain adapter before locking the corpus.'})
    for folder in ['papers','indexes']: (root/folder).mkdir(exist_ok=True)
    print(json.dumps({'output':str(root),'status':'draft_initialized','completed_primary_reviews':0,
        'next_action':'Complete method/domain_adapter.json; then use the Skill to curate real sources.'},ensure_ascii=True))

if __name__=='__main__':main()
