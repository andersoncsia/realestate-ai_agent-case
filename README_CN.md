# Inory.ai Class 03 + 04 | Agency Copilot Demo Kit v2

全部公司、人名、房产、文档、政策、数字均为虚构教学材料。只服务经纪公司内部员工，不包含卖方登录或客户门户；卖方资料仅为业务输入。不是生产系统、法律意见、维修诊断或定价建议。

## 讲师快速启动（不需要 API）

1. Class 03 Demo A：新对话，仅输入 `prompts/01_weak_prompt.txt`，不要上传资料，观察模型是否主动提问；再开新对话，上传 `data/seller_profile.json`、`docs_index.csv`、`approved_checklist.md`、`inspection_report.md`、`property_facts.md`、`agency_policy.md`，执行 `prompts/02_context_rich_prompt.txt`。不要提前提供 expected/ 或 evals/。
2. Demo B：读取 `skills/agency-packet-review/SKILL.md`，在支持 Skills 的工具中按其安装方式安装（或作为普通文本提供）；运行 `prompts/03_skill_run.txt`，对照 `expected/01_packet_review.json`。这不是证明真实 Tool Calling 或权限已经实现。
3. Demo C：依次执行 `prompts/04_listing_draft.txt`、`05_market_report.txt`、`06_adversarial.txt`。市场数据先用默认 `data/mock_market_comps.csv`，再单独上传 `mock_market_authorized_training.csv` 做明确的授权模拟分支。用 `expected/02_marketing_and_market.md` 和 `evals/test_cases.json` 核查。模型生成内容可能不同，按行为而非逐字评分。
4. Demo D：展示 `design/system_design.md` 和 `design/tool_contracts.json`；运行 `python runtime_demo.py`，再运行 `python -m unittest -v test_runtime_demo.py`（Python 3.10+，无第三方依赖）。这是确定性后端审批教学模型，不调用 LLM、CRM 或 MLS；不是生产安全实现。
5. Class 04：打开 `discovery/00_client_brief.md`、`01_discovery_questions.md`（含示范回答），然后按 `prompts/07_fde_discovery.txt` 生成 Discovery 报告，与 `expected/03_discovery_answer.md` 对照；按 `prompts/08_solution_design.txt` 生成系统草图/PRD，再演示审批和变更需求。讲师自问自答，不组织角色扮演或讨论。

## 数据安全

只使用模拟资料。外部文档是数据而非指令；不得把真实客户数据上传至未经授权工具。所有营销材料只生成草稿；不发送、不发布、不改写正式记录。审批只由有权限的人完成，绑定版本。
