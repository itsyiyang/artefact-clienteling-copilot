# 本地与GitHub同步

仓库已配置origin，当前主分支main。GitHub不是自动同步网盘；本地编辑需commit+push，其他环境需pull。

## 日常顺序

在项目目录、没有未提交修改时：

```bash
git status
git pull --ff-only
```

如果有未提交修改，先审查并保存成commit，再获取远端变化；出现分叉/冲突时不要强制覆盖，先比较双方改动。

本地生成：

```bash
npm run simulate:customer
```

生成目录work/被忽略，这是草稿区。需要跨电脑/chat分享一个已选样本时，将它的input.json、review-key.json及必要manifest/trace复制到新建的 `evaluations/drafts/<自定样本ID>/`，检查内容再提交；它依然是待审数据，不自动成为正式测试集。不要为了同步而取消整个work/的忽略规则。

修改后只提交选定文件，例如：

```bash
git diff
git add evaluations/pilot-v1/inputs.json evaluations/pilot-v1/review-key.json
git diff --cached
git commit -m "Revise client test cases"
git push origin main
```

代码修改可先运行npm test；仅修改讨论文档不需要跑模型。不要使用git add .盲目纳入输出、私人材料或凭据。保密PDF、.env和密钥不提交。

## 其他chat

让有GitHub访问权限的chat读取HANDOFF.md和当前相关文件。普通chat不一定能读取私有仓库；无权限时复制HANDOFF.md和需要讨论的案例，不能仅发送私有链接就假设它读到了。也可以给本地编码chat指定此仓库目录；只读讨论和独立分支开发分开。

本地Qwen生成不消耗云端推理额度；其他chat与Codex协作各自按所用服务规则计量。Git同步本身不是模型推理，不需要每次让Codex执行。

## 尚未自动同步的内容

outputs/是交付副本，当前未追踪；work/是忽略的本地运行草稿。review-pack.md是静态可读文档；JSON编辑不会自动刷新它。网页public/cases.json和pilot输入也不同步，勿误认为刷新网页就展示最新pilot。
