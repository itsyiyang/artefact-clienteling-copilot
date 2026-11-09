"""Audit saved local generation artifacts; does not edit model outputs or judge quality."""
import csv, json, hashlib, statistics, sys
from pathlib import Path

run = Path(sys.argv[1] if len(sys.argv)>1 else 'evaluations/runs/fifty-generation-v0.3-8k')
manifest = json.loads((run/'manifest.json').read_text())
inputs = json.loads((run/'inputs.json').read_text())
with (run/'test-results-50.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
with Path('evaluations/test-set-50-v1/test-inputs-50.csv').open(encoding='utf-8-sig', newline='') as f:
    original = list(csv.DictReader(f))
assert len(rows)==len(inputs)==len(original)==50
assert len({r['Case ID'] for r in rows})==50
assert hashlib.sha256((run/'inputs.json').read_bytes()).hexdigest()==manifest['input_sha256']
assert hashlib.sha256((run/'generation-prompt.md').read_bytes()).hexdigest()==manifest['prompt_sha256']
for row,old in zip(rows,original):
    assert all(row[k]==v for k,v in old.items()), row['Case ID']+' input changed'
durations=[]; token_totals=[]; observations=[]; complete=0
for row,c in zip(rows,inputs):
    records=[r for r in manifest['records'] if r['case_id']==c['case_id']]
    if not records or records[0]['status']!='generated_pending_review':
        assert all(not row[f'Output {i}'] for i in (1,2,3))
        continue
    record=records[0]; raw=json.loads((run/record['result_file']).read_text())
    assert len(raw['parsed']['candidates'])==3
    texts=[x['text'] for x in raw['parsed']['candidates']]
    assert texts==[row[f'Output {i}'] for i in (1,2,3)]
    assert all(t.strip() for t in texts)
    assert raw['raw']['done_reason']!='length'
    token_totals.append(raw['raw']['prompt_eval_count']+raw['raw']['eval_count'])
    durations.append(record['elapsed_ms']/1000);complete+=1
    name=c['client_information']['identity']['name']
    for i,t in enumerate(texts,1):
        flags=[]
        if name in t: flags.append('full_name_present_check_salutation')
        if any(w in t for w in ['不用回复','不必回复','不用特意回复','不必特意回复']): flags.append('discourages_reply')
        if c['scenario']=='birthday_festive_greetings' and any(w in t for w in ['丝巾','方巾','包装','系法']): flags.append('birthday_shopping_detail')
        if t in texts[:i-1]: flags.append('exact_duplicate')
        if flags: observations.append({'case_id':c['case_id'],'candidate':i,'flags':flags,'text':t})
result={'completed_cases':complete,'nonempty_outputs':complete*3,'expected_cases':50,'inputs_unchanged':True,'csv_matches_raw':True,'prompt_and_input_hashes_match':True,'context_max_used_tokens':max(token_totals,default=0),'latency_seconds':{'sum':sum(durations),'median':statistics.median(durations) if durations else None,'min':min(durations,default=0),'max':max(durations,default=0)},'mechanical_review_hints':observations,'quality_status':'not_evaluated; hints are not Judge verdicts','all_50_complete':complete==50}
(run/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
