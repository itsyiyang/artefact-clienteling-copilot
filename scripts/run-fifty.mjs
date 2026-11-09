import http from 'node:http';
import {readFile,writeFile,mkdir,access} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const dir=process.argv[2]||'evaluations/runs/fifty-generation-v0.3';
const sha=x=>createHash('sha256').update(x).digest('hex');
const exists=async p=>{try{await access(p);return true;}catch{return false;}};
const chat=body=>new Promise((resolve,reject)=>{const req=http.request('http://127.0.0.1:11434/api/chat',{method:'POST',headers:{'Content-Type':'application/json'}},res=>{let s='';res.on('data',x=>s+=x);res.on('end',()=>{try{const o=JSON.parse(s);if(res.statusCode!==200)throw Error(s);resolve(o);}catch(e){reject(e);}});res.on('error',reject);});const t=setTimeout(()=>req.destroy(Error('600s inference timeout')),600000);req.on('close',()=>clearTimeout(t));req.on('error',reject);req.end(JSON.stringify(body));});
await mkdir(dir,{recursive:true});
let manifest;
if(await exists(dir+'/manifest.json'))manifest=JSON.parse(await readFile(dir+'/manifest.json','utf8'));
else{
 const input=await readFile('evaluations/test-set-50-v1/inputs.json','utf8'),prompt=await readFile('prompts/generation-v0.2.md','utf8'),reference=await readFile('docs/clienteling_messaging_reference.md','utf8');
 const tags=await(await fetch('http://127.0.0.1:11434/api/tags')).json();
 manifest={created_at:new Date().toISOString(),model:'qwen3:8b',model_metadata:tags.models.find(x=>x.name==='qwen3:8b'),code_commit:execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim(),prompt_version:'generation-v0.3',prompt_sha256:sha(prompt),input_sha256:sha(input),reference_sha256:sha(reference),pipeline:'Single local generation call with implicit strategy planning; no independent planner, Judge or revisions',input_transform:'Only product claim_evidence omitted as redundant provenance; all history and other facts retained',status:'running',records:[]};
 await writeFile(dir+'/inputs.json',input);await writeFile(dir+'/generation-prompt.md',prompt);await writeFile(dir+'/reference-snapshot.md',reference);await writeFile(dir+'/runner-snapshot.mjs',await readFile(new URL(import.meta.url),'utf8'));
}
const cases=JSON.parse(await readFile(dir+'/inputs.json','utf8')),prompt=await readFile(dir+'/generation-prompt.md','utf8');
const quote=x=>'"'+String(x??'').replaceAll('"','""')+'"';
async function checkpoint(){
 await writeFile(dir+'/manifest.json',JSON.stringify(manifest,null,2));
 const rows=[['Case ID','Scenario','Client Information','Conversation history','Product information','Output 1','Output 2','Output 3']],statuses=[['Case ID','Source Case ID','Status','Elapsed seconds','Attempts','Prompt version','Raw result']];
 for(const c of cases){const rec=manifest.records.find(r=>r.case_id===c.case_id);let outputs=[];if(rec?.status==='generated_pending_review')outputs=JSON.parse(await readFile(dir+'/'+rec.result_file,'utf8')).parsed.candidates.map(x=>x.text);
 rows.push([c.case_id,c.scenario,JSON.stringify({as_of_datetime:c.as_of_datetime,direction:c.direction,trigger:c.trigger,task_goal:c.task_goal,client:c.client_information},null,2),JSON.stringify({historical_messages:c.conversation_history,current_client_message:c.current_client_message},null,2),JSON.stringify({products:c.product_information,events:c.event_information,comparison_evidence:c.comparison_evidence,policy:c.policy,warnings:c.warnings},null,2),...Array.from({length:3},(_,i)=>outputs[i]||'')]);
 statuses.push([c.case_id,c.source_case_id,rec?.status||'not_run',rec?rec.elapsed_ms/1000:'',rec?.attempts||0,manifest.prompt_version,rec?.result_file||'']);}
 for(const [name,table] of [['test-results-50.csv',rows],['run-status.csv',statuses]])await writeFile(dir+'/'+name,'\uFEFF'+table.map(r=>r.map(quote).join(',')).join('\r\n')+'\r\n');
}
await checkpoint();
for(const c of cases.filter(c=>!process.env.CASE_IDS||process.env.CASE_IDS.split(',').includes(c.case_id))){if(manifest.records.some(r=>r.case_id===c.case_id&&r.status==='generated_pending_review'))continue;
 const input=structuredClone(c);input.product_information=input.product_information.map(({claim_evidence,...rest})=>rest);
 let total=0;
 for(let attempt=1;attempt<=2;attempt++){
 const file=`${c.case_id}.attempt-${attempt}.json`;if(await exists(dir+'/'+file))continue;
 const reminders={birthday_festive_greetings:'本例只祝福，不提任何商品、方巾、丝巾、包装、系法、购物记录！历史用于识别称呼和联系限制，不能用购物细节凑个性化。三条分别重在日常安好、未来心愿、感谢陪伴与LIUXU理念。不要表情。正例风格：许女士，生日快乐。我是LIUXU的客户顾问，愿您新的一岁从容自在，所愿皆有回响。另一个方向：许女士，感谢您一直以来对LIUXU的喜爱，愿新的一岁留白有意，自有天地。仅学习表达，客户称呼/节日/是否需要介绍按本例事实调整。',reactivation:'必须直接给出新资料的具体帮助，能用输入中的尺寸重量对比就给出；不能三条都只有“有资料，可以发您”。这是服务资料更新，不等于新品。客户已回复则回答其最新问题。',price_objection:'称呼必须用历史确认的姓氏+女士/先生，不可全名。只用已知事实解释价值，不推断成本或耐用性。'};
 const userContent=JSON.stringify(input)+'\n以上是资料，以下是本次写作要求：'+(reminders[c.scenario]||'优先回答当前客户消息，用已知具体事实提供帮助，遵守客户历史限制。')+'\n三条必须有不同信息重点，不得重复同一段；每条至多一个行动邀请。只返回candidates三项，每项approach和text。';
 const request={model:manifest.model,stream:false,think:false,format:'json',keep_alive:'30m',options:{temperature:0.4,num_ctx:16384,num_predict:1000,seed:42},messages:[{role:'system',content:prompt},{role:'user',content:userContent}]};
 const started=Date.now(),record={case_id:c.case_id,attempt,started_at:new Date().toISOString(),request};
 await writeFile(dir+`/${c.case_id}.attempt-${attempt}.request.json`,JSON.stringify(request,null,2));
 try{record.raw=await chat(request);record.parsed=JSON.parse(record.raw.message.content);if(record.raw.done_reason==='length'||record.parsed.candidates?.length!==3||record.parsed.candidates.some(x=>typeof x.text!=='string'||!x.text.trim()))throw Error('Incomplete three-candidate JSON');record.status='generated_pending_review';}catch(e){record.status='technical_failure';record.error=e.message;}
 record.elapsed_ms=Date.now()-started;total+=record.elapsed_ms;delete record.request;
 await writeFile(dir+'/'+file,JSON.stringify(record,null,2));
 manifest.records=manifest.records.filter(x=>x.case_id!==c.case_id);manifest.records.push({case_id:c.case_id,status:record.status,elapsed_ms:total,attempts:attempt,result_file:file,error:record.error});await checkpoint();console.log(c.case_id,record.status,Math.round(record.elapsed_ms/1000)+'s',manifest.records.filter(x=>x.status==='generated_pending_review').length+'/50');if(record.status==='generated_pending_review')break;
 }
}
manifest.finished_at=new Date().toISOString();manifest.status=manifest.records.filter(x=>x.status==='generated_pending_review').length===50?'generation_complete_pending_review':'finished_with_technical_failures';await checkpoint();console.log(manifest.status);
