# 项目接手入口

最后更新：2026-11-09。私有仓库：https://github.com/itsyiyang/artefact-clienteling-copilot

## 目标与当前事实

Artefact Luxury Clienteling Copilot Challenge：输入客户/场景/聊天/相关商品，输出三条有不同沟通策略的中文微信候选，CA最终决定采用和发送。虚构品牌留序LIUXU；本品牌不打折，常规护理/维修联络/预约默认可提供。题目PDF保密，不提交。截止目标曾设为11月9日22点（上海时间），交付状态以task.md为准，勿假定已完成。

本地网页+Node服务+Ollama Qwen3:8b，零云端推理预算。`npm start` 后访问 http://127.0.0.1:3210 。当前Demo理解/规划/生成仍合并一次调用；Judge及一次Edit由按钮触发。独立策略规划、自动质量门与有限重试是已确认设计，尚未完整落地。网页美化最后。

## 主要编辑入口

- evaluations/pilot-v1/inputs.json：P01–P06客户/历史/事实。Codex拟写，P01/P02按用户review修改；其余参考话术待review。
- evaluations/pilot-v1/review-key.json：独立评审依据/参考策略，不提供给生成器。
- evaluations/pilot-v1/review-pack.md：可读快照，与JSON不自动同步；JSON为数据编辑入口。
- public/cases.json：网页旧种子，与上述pilot不是自动联动。
- scripts/customer-agent.mjs：本地两阶段合成数据工具。
- prompts/customer-simulation-agent.md：客户模拟规范。
- evaluations/pilot-v1/customer-agent-config.json：默认单例生成配置。
- rules.md、task.md、docs/decisions/、evaluations/methodology/：业务规则、进度、决策和评估方案。

## 用户最新反馈

客户姓名、年龄、生日、购物历史必填；职业/兴趣等完整度可不同。年龄/属相依出生日期计算，属相按农历年界，不推断性格。
CA应专业、主动、自然，整合确定商品信息，不能只说“帮您确认”。陶艺等兴趣要持续记录，并保留联系范围。生日自然说明品牌/CA身份，不写“不用回复”。客户本周无暇可先微信提供完整资料，并可选邀请下周，不推断必然成交。新增商品事实要显式加入虚构目录，不能无据编造。

六案例先审核输入与成功条件，再实际生成、用户先评、对照Judge、按分歧修订。可以同Qwen独立调用作内部Judge，是否换模型由人工校准决定；不能只用自评分证明效果。底线、价值、单条/整组质量都必须满足。正常展示通过候选，重试耗尽允许明确标记的失败草稿；不能绕过拒绝。正式50例未完成。

## 运行与证据

`npm test`；`npm run simulate:customer`；自定义：`node scripts/customer-agent.mjs <config.json> [profile.json]`。
新样本保存在work/customer-agent/<ID>/，默认不进Git。输入/评审答案隔离；保留trace与manifest，不把生成内容当人工金标准。
三次客户模拟实测记录在evaluations/customer-agent-trials/：有格式失败、语义失败和待审样本，最新仍有价格定位/CA表达问题。不要冒称数据生成已验收。下一步可先冻结虚构商品价格带、改善历史表达。

## 协作纪律

先读git status与本文件；不覆盖用户未提交修改。其他chat只讨论时，给出文件名、case_id和明确建议，不声称已改仓库。并行改代码使用独立分支/工作副本，不在同一目录相互切换分支。启动前拉取，完成后审查差异、提交、推送；未追踪/忽略文件不会同步。具体步骤见docs/local-github-workflow.md。
