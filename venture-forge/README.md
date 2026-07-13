# VentureForge — AI创业引擎

从市场发现 → 产品验证 → MVP开发 → 上线增长的完整创业操作系统。

## 架构

```
├── frontend/          # Next.js + React + TailwindCSS
│   ├── app/           # App Router
│   ├── components/    # UI组件
│   └── lib/           # 工具函数
├── backend/           # FastAPI + PostgreSQL
│   ├── routers/       # API路由
│   ├── services/      # 业务逻辑
│   ├── models/        # SQLAlchemy模型
│   └── agents/        # AI创业Agent
├── tests/             # 全栈测试
└── docs/              # 文档
```

## 快速启动

```bash
# 后端
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload

# 前端
cd frontend && npm install && npm run dev
```

## 技术栈

- **Frontend**: Next.js 14, React 18, TailwindCSS, shadcn/ui
- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Database**: PostgreSQL 16
- **AI**: OpenAI GPT-4o, LangChain
- **Auth**: Clerk
- **Payments**: Stripe
- **Deploy**: Docker + Vercel
