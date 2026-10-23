"""Read-only compact review views; never changes evidence or completion counts."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
read = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
ap = argparse.ArgumentParser(description=__doc__)
sub = ap.add_subparsers(dest='mode', required=True)
st = sub.add_parser('status'); st.add_argument('root', type=Path)
bu = sub.add_parser('bundle'); bu.add_argument('batch', type=Path)
bu.add_argument('--start', type=int, default=0)
bu.add_argument('--limit', type=int, default=6)
bu.add_argument('--provenance', action='store_true', help='Include cache/hash/URL metadata; omitted from ordinary reading to avoid repeated context.')
args = ap.parse_args()
if args.mode == 'status':
    w = args.root / 'work'; s = read(w / 'stage2_run_state.json')
    p = read(w / 'stage2_570_progress.json')
    print(json.dumps(dict(status=s['status'], release=s['current_release'],
        completed=p['completed_count'], target=p['target_count'],
        remaining=p['target_count']-p['completed_count'], held=p['held_primary_source_count'],
        current_batch=s.get('current_batch'), assignments=s.get('work_assignments', [])[-2:]), ensure_ascii=False))
else:
    b = args.batch; packets = read(b / 'review_packets.json')
    manifest = read(b / 'freeze_manifest.json')['files']
    for n in ['roles.json', 'review_packets.json']:
        assert sha(b / n) == manifest[n]['sha256'], 'Stale frozen input: '+n
    rows = [p for p in packets['review_packets'] if p.get('counts_as_completed')]
    print(json.dumps(dict(batch=str(b), batch_sha=sha(b/'roles.json'),
        reviewed_by_this_view=False, available=len(rows), counts=packets.get('completion_counts')), ensure_ascii=False))
    for p in rows[args.start:args.start+args.limit]:
        print(json.dumps({k:p.get(k) for k in ['work_family_id','role_review_id','title',
            'primary_version','actual_source_heading','actual_research_type','scope_disposition','claim','limits']}, ensure_ascii=False))
        seen = set()
        for kind in ['protocol_packets','limit_packets','conflict_packets']:
            blocks=p.get(kind) or ([p['limit_packet']] if kind=='limit_packets' and p.get('limit_packet') else [])
            for q in blocks:
                key=(q['cache_path'],q['locator'])
                if key in seen: continue
                seen.add(key)
                keys=['locator','render_path','render_sha256']
                if args.provenance: keys+=['url','version','cache_path','sha256']
                out={k:q.get(k) for k in keys if q.get(k) is not None}
                out['kind']=kind
                out['text']='\n'.join(x['text'] for x in q.get('excerpt_lines',[]))
                print(json.dumps(out, ensure_ascii=False))
