# Discovery 参考答案
Problem: 内部团队需要反复人工核对资料和摘录验房信息；没有统一状态与审核证据。
As-Is: Coordinator 收件/核对 → Listing Agent 手工读 PDF → Marketing 起草 → Broker 审批；邮件/共享盘/CRM 交接。
To-Be: 内部 case workspace → 确定性 checklist → Agent 提取引用与草稿 → Broker 审批/退回；状态、版本、来源统一。
P0: 缺件识别、inspection review、listing package、broker approval。P1: 获授权市场报告/CMA 辅助、内部 timeline。P2: 内部 offer comparison、周报。排除卖方门户、自动发送/发布、维修义务判断、自动定价。
Pilot: 4 周 10 case；8 日、5 次为假设基线，先实测；示例目标收齐中位≤6日、沟通减少25%、关键引用≥95%、关键缺件漏检<5%（小样本须报告分母，不能推断生产可靠性），越权 0 容忍。
Owner: Broker; FDE 与运营共同建立数据记录、人工标注、回归测试。未确认：真实 API/权限、清单适用规则、样本代表性。
