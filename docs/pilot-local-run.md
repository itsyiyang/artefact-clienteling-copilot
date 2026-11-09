# 本地六场景运行

开启Ollama，在项目目录执行 `npm run pilot:generate`。每次创建新的evaluations/runs/pilot-时间目录，不覆盖前次。当前生成采用一次调用输出理解/策略/候选，尚非独立规划编排；不自动Judge，不自动修订。

结果：review.md为六例三候选阅读版；inputs.json为完整原始输入；各S*.generate.json包含模型原始返回、解析结果、耗时和错误；各request.json为实际模型请求。manifest.json保存模型digest/量化、Git版本、输入和规则哈希、状态；prompt及rules快照同目录。调用中会精简重复商品claim_evidence，保留商品事实和比较证据；实际请求可复核。

先人工review，之后执行 `node scripts/run-pilot.mjs judge evaluations/runs/你的运行目录`。同目录的S*.judge.json保存评估原文，judge-prompt.txt保存评分规则。Judge仍是本地Qwen独立调用，不作为人工真值。命令只有明确指定judge才运行。

生成新批次前确认没有其他本地推理任务，以免互相等待。每场景最多等待10分钟，失败保留不自动重试；不得把失败当零分或把手写话术补作模型输出。git add选定运行目录、提交、推送即可共享（全部虚构数据）。这些运行可供review，不等于已完成50例。

本批六例合并review目录：evaluations/runs/pilot-six-review。它是5个首轮成功与1个补跑的阅读集合，不是独立运行。人工review之后可对该目录执行judge命令，生成每例独立评估；首轮技术失败仍在原目录。
