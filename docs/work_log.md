# Work Log

2026-11-09 最新完成：依据新话术Reference与人工review优化generation-v0.3提示，本地Qwen3:8b已完成50例150条原始回复，技术失败/重试0，累计78.9分钟。输入与CSV/原始响应一致性验证通过。旧六例及v0.2失败校准样本保留。结果：evaluations/test-set-50-v1/test-results-50.csv；完整证据：evaluations/runs/fifty-generation-v0.3-8k/。注意TC041联系限制遗漏等缺陷，不能当作可直接发送或质量通过。Judge/人工review、质量修订及三方案对比仍待完成。新合并Codex编写版Excel独立保留，不混入本批次。

2026-11-09（Codex自然话术交付归档）：按用户要求，将本聊天最终Excel更新到 `deliverables/clienteling-50-codex-final/`，新增描述、修订总结与可重复验证脚本。此前由Codex根据用户上传的50例及话术reference编写和复核，保留自然表达；复核修正10个输出单元，TC041因客户联系限制改为3条明确不发送的处理建议。技术核验覆盖双表50例、8列、源字段保全、JSON解析、历史对话和150输出一致性；未运行新Qwen或Judge，未记录为人工金标准或独立质量成绩。文件与本地模型批次分开归档。

2026-11-09：读取六场景新话术参考，以既有人工反馈解决冲突，新增生成提示与可恢复50例本地批量运行。v0.2生日抽查仍失败，保留bad case；v0.3追加场景末尾提醒及生日正例，正式批次全部重新运行，当前进行中。模型Qwen3:8b，8192上下文，思考关闭，温度0.4，固定seed42；不运行Judge。完整记录请求、响应、耗时、版本。

2026-11-09：生成50例输入与结果CSV（UTF-8 BOM、多行JSON单元格），附状态CSV和输入JSON；回读验证均50行，原实测仅6例，未伪造其他输出。未运行新模型或Judge。保留各分支source_case_id，避免将反事实分支当实际历史。

2026-11-09（六场景话术Reference）：新增完整 LIUXU CA 话术参考，覆盖生日/节日、个性化推荐、购后关怀、重新激活、活动邀请、价格异议；补充工具输入输出、分支、事实和隐私边界。入库前对齐 rules.md v0.3：节日不推断家庭结构、重新激活须有新增契机、品牌不打折且第三方积分与品牌定价分离。本次仅文档更新，未修改运行时提示或服务代码，未运行模型评测。

2026-11-09：保留用户定性review不造数字，Judge单独目录保存六次真实推理。S1/S4重点对照已完成；附模型原文、请求、耗时、提示快照与引用校验。发现漏判及误报，未按Judge意见自动改写。原18条生成JSON与原目录哈希一致。

2026-11-09：实际运行本地Qwen3:8b六场景，首轮生日212.4秒、购后149.1秒、重新激活221.7秒、邀请220.7秒、价格220.7秒；产品推荐首次302.5秒连接失败，改长连接处理后191.5秒完成。18条原文未改写，Judge按用户要求延后。新增本地运行命令及使用说明，14测试通过。

2026-11-09：采纳用户三项业务回复，新增虚构活动表并区分邀请/预约/预订意向/订单。重新组装21例，抽取六场景pilot输入。沿用讨论活动日期与地点，未擅自生成商品预览SKU、礼物或折扣。未运行模型。

2026-11-09：读取用户新参考资料，新增scripts/assemble-inputs.mjs，校验ID、交易映射、商品证据路径、重量比较和生日；组装原始聊天、CRM、当前消息、相关商品/活动，限制场景时间并隔离未来服务快照。修复生日为11月9日，15输入组装/9阻断；未擅自新增活动或营销契机，未运行新模型。13测试通过。

2026-11-09（客户模拟Agent落地）：新增本地两阶段工具（档案→场景/目录/历史），年龄与属相按日期计算；实际运行三次，保留类型失败、语义失败和待审核样本。修正商品ID补充事实引用校验并保存验证版本。最终样本仍有价格定位与CA表达缺陷，未作为合格测试数据。原P01–P06话术未改，网页未接入新工具。

2026-11-09：按用户review更新校准包v0.2。P01补CA/品牌身份、持续兴趣与自然沟通，删“不用回复”；P02新增明确虚构SKU事实、主动比较和可选下周预约。P03–P06话术未变。客户模拟Agent提示规范已准备但未接入/运行，六例年龄生日购物历史必填化，属相待校验；旧稿归档，等待用户继续review。

2026-11-09（六例校准包）：用户批准先审核案例、再生成、人工先评、对照Judge、按分歧校准的闭环。Codex拟写六组丰富输入、18条待审参考消息、证据/成功失败条件；生成输入与评审答案分文件，人工表留空。完成结构和日期检查，未运行Qwen，未把参考组声明为Good。更新同模型Judge决策：可以保留内部Qwen，以人工验证其可靠性。

2026-11-09（Methodology草案）：按用户反馈补充三道质量门、丰富客户/历史证据结构、50例交叉分布与三方案实验协议。用户要求正式生成与Judge分模型，提供人工建议校准；参考Anthropic评估方法、Promptfoo rubric与Ollama官方资料，Gemma3:4b仅作待测候选。无新模型下载、代码修改或正式测试；草案待业务review。

2026-11-09（Workflow v0.2共识）：用户确认单条与三候选整体检查、独立evaluation、CA互动方向，并修正为重试耗尽后可展示失败结果。记录明确标记的例外展示，保留失败草稿和完整修订链；独立规划和有限内部修正待实现。新增ADR-013、同步设计/评估/task；本次只更新文档，未修改代码或运行新模型实验。

2026-11-09（Prototype v0.1）：用户授权本地搭建，确认Ollama内qwen3:8b Q4_K_M已安装。建立原生Node服务与CA工作台、六虚构种子、生成/Judge/一次Edit、导出；结构校验测试通过。浏览器已检查本地模型状态、表单与布局；真实产品推荐小样已完成生成、Judge v0.2复测、一次Edit及重新评测；记录见evaluations/samples/local-product-review.json。生成耗时133.363秒，修订前后差异评分均2/5，流程可运行但质量待人工校准。3项结构校验测试通过。设计使用frontend-design指导墨蓝/银灰/绿色消息卡与克制排版。尚未进行正式50例或人工评分校准。

2026-11-09（Demo与范围扩展）：用户确认沟通方向、客户显式限制、三产品线、不打折与第三方积分区分、一次Edit、用户先审小样、DeepSeek/Qwen方向，并要求网页前后端Demo。阅读Promptfoo仓库与官方llm-rubric说明，记录T17–T20及R16–18。只变更规划文档，无模型运行或实现；截图待归档。

2026-11-09（规则v0.2）：用户指出旧S04暗示延误售后、不专业，确认新增及时性和新契机检查，并确认常规CA服务协助默认可提供。更新R02，新增R14–15，修订S04并保留否定原因；增加权限字段缺失时不误拦截的对比检查。工具：本聊天与Git文档；未运行Judge，截图待归档。

2026-11-09（规则整理）：根据用户确认的品牌、服务姿态与CRM范围边界，建立rules.md R01–R13及Judge检查点；人工编写六场景正反例与反事实检查；核对task.md完成证据。输出均为讨论文档，未运行Judge，未生成正式50例。业务评审和聊天截图待归档；参考截图不视为开云官方规则。

2026-11-09：直接读取保密题目PDF两页，对照A–E及ground rules，新增task.md执行计划讨论稿。用户确认22:00前完成材料供review、皮具品类但品牌定位重议、Judge四项逻辑职责先人工校准；Agent数量待定。使用PDF文本提取与本聊天，截图尚待归档。本次仅规划文档，无产品实现。

This log distinguishes reconstructed discussion history from primary evidence. Chat screenshots and source materials are not yet archived in this repository.

| Date | Step | Work performed | Output | Tool / evidence status |
|---|---:|---|---|---|
| 2026-11-08 | 01 | Analyzed the challenge and working delivery scope | Requirements summary and confidentiality boundary | Reconstructed from prior AI discussion; official PDF excluded |
| 2026-11-08 | 02 | Developed Luxury Clienteling business principles | Relationship-first and grounding principles | Reconstructed from prior AI discussion |
| 2026-11-08 | 03 | Compared direct generation with explicit strategy | Explicit strategy selected | Reconstructed from prior AI discussion |
| 2026-11-08 | 04 | Defined Client Understanding | Scenario-aware design; fact/inference/unknown separation | Reconstructed from prior AI discussion |
| 2026-11-08 | 05 | Defined Communication Planning | Shared objective plus three Dynamic Approaches | Reconstructed from prior AI discussion |
| 2026-11-08 | 06 | Established project tracking | Private GitHub repository, ADR log, work log, tracker, and open questions | Repository history |
| 2026-11-08 | 07 | Brand Identity & Policy | Not started; next discussion | Pending |

## Logging rule going forward

For each important discussion or experiment, record the input/version, action, output, conclusion, unresolved issues, tool/model where relevant, and an evidence reference. Git history supports traceability but does not replace any required AI-chat screenshots.
