from pathlib import Path
import json,csv,copy,hashlib,collections
src=Path('evaluations/assembled/inputs-full.json');base=json.loads(src.read_text());by={c['case_id']:c for c in base};cases=copy.deepcopy(base)
# Explicit synthetic current requests; source histories and catalogs remain unchanged.
variants={
'birthday_festive_greetings':[
('S1-001','生日当天客户主动说谢谢还记得生日，请简短回复祝福，不转入商品推荐。','谢谢你还记得我生日呀！'),
('S1-002','年末客户回复问候并提到希望新年能多休息，回复简洁祝愿，不安排未经请求的活动。','谢谢，今年忙了一年，希望明年能多休息一点。'),
('S1-003','新年客户主动祝福顾问，请自然回礼，避免虚构熟悉关系。','新年快乐，祝你工作顺利。'),
('S1-004','客户回复新年问候，强调今天陪家人；简短祝福，不加入邀约。','新年快乐！今天和家人在一起，晚点再聊。')],
'product_recommendation':[
('S2-001','优先比较给定款式重量与容量，客户预算上限明确。','通勤用，预算一万元以内。先把能选的款式和重量发我，我再看看。'),
('S2-001','客户电脑长宽明确但包的内部适配未必已验证；不可仅外尺寸保证。','我的电脑带套大概32×23厘米，我想要有拉链的，哪款更值得先看？'),
('S2-001','客户已说明暂不装电脑，围绕日常用品与既有审美提供选择。','这次不装电脑，只放手机、钱包和小雨伞，尽量轻一点。'),
('S2-002','旅行小皮具按具体收纳需求比较，不把收纳品说成可装全部物品。','主要收护照、登机牌和几张卡，不需要放电脑，最好容易拿取。'),
('S2-003','比较材料和结构，客户不需要工艺术语堆砌。','别讲太多专业名词，直接说这两款背起来和放东西有什么区别就好。'),
('S2-004','丝巾用途优先级明确，需要基于实际尺寸推荐。','主要系在包上，偶尔搭外套，不要为了两用选得太大。')],
'post_purchase_care':[
('S3-001','客户已看过图示仍卡住；提出下一步服务，不重复已完成说明。','图示看过了，还是不太顺手，我不敢用力，能帮我联系人看一下吗？'),
('S3-002','客户要求简明护理建议，不虚构专属保养方法。','我怕保养弄错，只告诉我最需要避免的事就好。'),
('S3-003','未有维修进展事实，回复追问并接手跟进，不保证工期。','下周要用这个钱包，有消息了吗？如果还没确定，也请直接告诉我。'),
('S3-004','强调暂时不用的存放需求，不借机推销。','最近先不用这只收纳包，想收起来一段时间，有什么需要注意的吗？')],
'reactivation':[
('S4-001','客户回应新增资料，先整合关键数据，不立即邀约。','可以，先发我尺寸和重量就好。'),
('S4-001','客户重新回应并说明依然出差多，聚焦电脑文件收纳。','我最近还是出差多，主要看电脑和文件放起来方便不方便。'),
('S4-001','客户对新资料感兴趣但当前不购买；提供服务不催单。','资料可以看看，不过近期先不买。'),
('S4-001','客户希望更休闲而非正式商务外观，使用已知设计事实。','之前那款太正式了，这次想看线条简单、不那么商务的。'),
('S4-001','客户没时间读长资料，压缩具体价值与可选下一步。','我这会儿没空看长介绍，你先把最主要的差别说一下。'),
('S4-001','客户询问资料是否是新品促销，明确为服务资料且品牌不打折。','你说的新资料，是又有新品或者促销了吗？'),
('S4-001','客户希望周末再看，尊重时机，不即时追问或编造预约。','这两天比较忙，周末我再看，你先发微信就行。')],
'event_invitation':[
('S5-001','客户要求先收电子邀请函，不索取邮寄地址。','先把电子邀请函发我看看吧。'),
('S5-002','客户希望专属时段；可协商但不直接确认未设时段。','我想安静一点看，专属时间能安排在下午吗？'),
('S5-003','客户有预订意向，区分登记需求与确认供货订单。','如果看到喜欢的下季款，可以先登记想要的颜色吗？'),
('S5-004','客户无法到店，提供已确认可分享介绍而非编造直播。','当天可能来不了，可以先发活动介绍给我吗？')],
'price_objection':[
('S6-001','客户质疑工艺与售价关系，区分已知结构差异与未知成本因果。','你说工艺不同，具体差在哪？是不是做起来更贵？'),
('S6-002','客户预算明确，提供在预算内的已知替代，不施压。','我预算最多一万元，12800那款就先不看了，有别的合适的吗？'),
('S6-003','客户明确不需要品牌故事，仅比较已知实用差异。','品牌故事就不用讲了，我想知道多花的钱对应哪些看得见的差别。'),
('S6-004','客户询问优惠与积分，活动规则未提供不能编造。','不打折的话，能用积分抵扣或者送点什么吗？')]
}
for typ,rows in variants.items():
 for n,(parent,goal,msg) in enumerate(rows,1):
  c=copy.deepcopy(by[parent]);c['case_id']=parent+'-V'+str(n);c['direction']='回复客户';c['task_goal']=goal;c['trigger']='合成情境变体：'+goal;c['current_client_message']={'message_id':c['case_id']+'-CURRENT','timestamp':c['as_of_datetime'],'sender':'client','text':msg}
  if typ=='reactivation':
   # Give the inbound reactivation follow-up an explicit preceding outreach in its own branch.
   c['conversation_history'].append({'message_id':c['case_id']+'-OUTREACH','timestamp':c['as_of_datetime'],'sender':'advisor','text':'陈先生，我们新增了通勤包尺寸、重量与收纳对照资料，想到您之前关注出差时电脑和文件的收纳，想发您参考。'})
   c['trigger']='重新激活对话的客户回应；新增对照资料契机保持不变。'
  c['dataset_provenance']={'parent_case':parent,'kind':'synthetic_counterfactual_branch','note':'独立假设分支，不写回客户真实历史或视为已发生事件'};cases.append(c)
assert len(cases)==50
order=['birthday_festive_greetings','product_recommendation','post_purchase_care','reactivation','event_invitation','price_objection'];cases.sort(key=lambda x:(order.index(x['scenario']),x['case_id']))
out=Path('evaluations/test-set-50-v1');out.mkdir(exist_ok=True)
headers=['Case ID','Scenario','Client Information','Conversation history','Product information'];rows=[];status=[]
for n,c in enumerate(cases,1):
 old=c['case_id'];c['source_case_id']=old;c['case_id']=f'TC{n:03}'
 ci={'as_of_datetime':c['as_of_datetime'],'direction':c['direction'],'trigger':c['trigger'],'task_goal':c['task_goal'],'client':c['client_information']}
 hist={'historical_messages':c['conversation_history'],'current_client_message':c['current_client_message']}
 prod={'products':c['product_information'],'events':c['event_information'],'comparison_evidence':c['comparison_evidence'],'policy':c['policy'],'warnings':c['warnings']}
 row=[c['case_id'],c['scenario']]+[json.dumps(x,ensure_ascii=False,indent=2) for x in [ci,hist,prod]]
 path=Path('evaluations/runs/pilot-six-review')/(old+'.generate.json');outputs=['','',''];run=None
 if path.exists():
  r=json.loads(path.read_text());outputs=[x['text'] for x in r['parsed']['candidates']];run=str(path)
 rows.append(row+outputs);status.append({'Case ID':c['case_id'],'Source Case ID':old,'Status':'generated_pending_quality_revision' if run else 'not_run','Output source':run or '', 'Branch':c.get('dataset_provenance',{}).get('kind','source_scenario')})
for name,hs,rs in [('test-inputs-50.csv',headers,[r[:5] for r in rows]),('test-results-50.csv',headers+['Output 1','Output 2','Output 3'],rows)]:
 with (out/name).open('w',encoding='utf-8-sig',newline='') as f:w=csv.writer(f);w.writerow(hs);w.writerows(rs)
 with (out/name).open(encoding='utf-8-sig',newline='') as f:assert len(list(csv.DictReader(f)))==50
with (out/'run-status.csv').open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(status[0]));w.writeheader();w.writerows(status)
(out/'inputs.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2))
(out/'manifest.json').write_text(json.dumps({'status':'draft_50_inputs_6_generated_44_not_run','counts':dict(collections.Counter(c['scenario'] for c in cases)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'notes':['21 existing assembled scenarios +29 explicit synthetic variants','Reactivation has 1 outbound and7 inbound follow-ups from same client; not8 independent clients','Same client branches belong to same eval partition','Original six outputs contain known defects, not revised or declared good']},ensure_ascii=False,indent=2))
print(json.dumps({'cases':len(cases),'generated':sum(bool(r[5]) for r in rows),'counts':dict(collections.Counter(c['scenario'] for c in cases))},ensure_ascii=False))
