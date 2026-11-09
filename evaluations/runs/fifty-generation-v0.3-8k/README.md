# Qwen 50例实际生成结果（待评审）

已根据新话术参考和人工review调整批量提示，使用本地Ollama Qwen3:8b完成50例、150条实际回复。未使用云端推理，未混入项目Final Outputs Excel的候选。

- 六场景分布：生日/节日8、商品推荐10、购后关怀8、重新激活8、活动邀请8、价格异议8。
- 所有50例首次调用均返回三条非空候选；技术失败0，技术重试0。这个比例是结构完成率，不是质量通过率。
- 累计请求耗时 4736.176 秒（78.9分钟），单例中位数 86.5 秒，范围 42.0–199.4 秒。
- 最大输入加输出长度 4613 tokens，未触及8192上下文配置。未发现输出截断。
- 50行输入逐格不变，150条CSV正文与原始响应逐字一致；输入与提示哈希核对通过。
- 生成代码commit：51f5ec01664029d64d3fc96563220041315b88c3；提示版本：generation-v0.3。基础提示在prompts/generation-v0.2.md，v0.3场景末尾提醒在脚本及实际请求中。
- 模型参数：temperature=0.4，seed=42，think=false，num_ctx=8192，num_predict=1000。

## 查看与复跑

`test-results-50.csv`为所需八列，UTF-8 BOM编码；`test-inputs-50.csv`为单独输入；`run-status.csv`记录逐例耗时、状态和原始结果位置。

原始证据：[GitHub运行目录](https://github.com/itsyiyang/artefact-clienteling-copilot/tree/main/evaluations/runs/fifty-generation-v0.3-8k)。每例的request.json是实际请求，attempt-1.json包含原始响应、解析结果、耗时。manifest及输入/提示/参考/脚本快照均保存。

在仓库根目录运行`node scripts/run-fifty.mjs`可恢复同一批次，已完成案例会跳过；要生成新的实验，运行`node scripts/run-fifty.mjs evaluations/runs/my-new-run`。

## 质量边界与下一步

本轮未运行Judge，也未进行质量修订。仍有称呼、对话连续性、候选重复、泛泛表达或未经证实的推断。TC041尤其未遵守客户只接收工艺资料的限制，三条活动邀约均不可直接发送。参见运行目录的spotcheck-notes.md；validation.json中的机械线索不是完整Judge结果。

下一步先由用户review这150条原文，再校准Judge并作对照，不能把这次生成完成率写成质量通过率。50例包含相关客户分支，不是50个独立客户。旧六例CSV在evaluations/test-set-50-v1/baseline-six-before-v0.3保留，旧六例模型/Judge记录未改。批量提示已更新，网页运行时提示尚未切换；独立Planner、自动质量门与修订不在本轮实现范围。
