"""MVP生成Agent — 从机会到可运行项目"""
import json
import logging
from typing import Optional
from datetime import datetime

from ..core.config import get_settings

logger = logging.getLogger(__name__)


class MVPGeneratorAgent:
    """MVP代码生成引擎"""
    
    async def generate_mvp_plan(self, scored_opportunity: dict) -> dict:
        """生成完整的MVP方案"""
        plan = {
            "product_name": await self._generate_product_name(scored_opportunity),
            "brand_positioning": await self._generate_branding(scored_opportunity),
            "value_proposition": await self._generate_value_prop(scored_opportunity),
            "feature_list": self._generate_features(scored_opportunity),
            "user_journey": self._generate_user_journey(scored_opportunity),
            "tech_stack": ["Next.js 14", "React 18", "TailwindCSS", "FastAPI", "PostgreSQL", "Clerk", "Stripe"],
            "database_schema": await self._generate_db_schema(scored_opportunity),
            "api_design": await self._generate_api_design(scored_opportunity),
            "project_structure": self._generate_project_structure(),
            "estimated_build_time": "48 hours",
            "generated_at": datetime.utcnow().isoformat(),
        }
        return plan
    
    async def _generate_product_name(self, opp: dict) -> str:
        """生成产品名称"""
        try:
            from langchain_openai import ChatOpenAI
            llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
            prompt = f"""
            Generate ONE catchy product name for a startup solving this problem:
            Title: {opp.get('pain_point', {}).get('raw_title', 'unknown')}
            Category: {opp.get('pain_point', {}).get('category', 'general')}
            
            Requirements:
            - 2-3 syllables
            - Memorable and brandable
            - Available as .com (assume it is)
            - Not generic (no "BestTool" or "SuperApp")
            
            Return ONLY the name, nothing else.
            """
            response = llm.invoke(prompt)
            name = response.content.strip().strip('"').strip("'").split()[0]
            return name.title()
        except Exception:
            return "VentureForge"
    
    async def _generate_branding(self, opp: dict) -> dict:
        """生成品牌定位"""
        try:
            from langchain_openai import ChatOpenAI
            llm = ChatOpenAI(model="gpt-4o", temperature=0.5)
            prompt = f"""
            Create brand positioning for a startup solving: {opp.get('pain_point', {}).get('raw_title', '')}
            
            Return JSON only:
            {{
                "tagline": "<one sentence>",
                "positioning": "<how we differ>",
                "target_audience": "<who pays>",
                "tone": "<brand voice>"
            }}
            """
            response = llm.invoke(prompt)
            return json.loads(response.content)
        except Exception:
            return {
                "tagline": "Build startups faster with AI",
                "positioning": "End-to-end AI创业引擎",
                "target_audience": "Indie hackers & bootstrappers",
                "tone": "Direct, data-driven, builder-focused",
            }
    
    def _generate_features(self, opp: dict) -> list[dict]:
        """生成MVP功能列表（80/20原则）"""
        return [
            {"id": "F1", "name": "Market Scanner", "priority": "P0", "effort": "S", "description": "自动扫描多平台发现痛点"},
            {"id": "F2", "name": "Opportunity Scorer", "priority": "P0", "effort": "M", "description": "AI驱动的评分引擎"},
            {"id": "F3", "name": "MVP Generator", "priority": "P0", "effort": "L", "description": "自动生成项目代码骨架"},
            {"id": "F4", "name": "Dashboard", "priority": "P1", "effort": "M", "description": "增长指标追踪面板"},
            {"id": "F5", "name": "User Auth", "priority": "P0", "effort": "S", "description": "Clerk认证集成"},
            {"id": "F6", "name": "Subscription", "priority": "P1", "effort": "M", "description": "Stripe订阅管理"},
        ]
    
    def _generate_user_journey(self, opp: dict) -> list[dict]:
        """定义用户旅程"""
        return [
            {"step": 1, "action": "Sign up", "screen": "Login/Register", "goal": "Create account"},
            {"step": 2, "action": "Discover opportunities", "screen": "Discover Page", "goal": "Find validated ideas"},
            {"step": 3, "action": "Score top ideas", "screen": "Opportunity Detail", "goal": "Select best opportunity"},
            {"step": 4, "action": "Generate MVP plan", "screen": "MVP Plan", "goal": "Get full project blueprint"},
            {"step": 5, "action": "Review code", "screen": "Code Preview", "goal": "Understand generated architecture"},
            {"step": 6, "action": "Deploy", "screen": "Deployment", "goal": "Launch to production"},
        ]
    
    async def _generate_db_schema(self, opp: dict) -> dict:
        """生成数据库Schema"""
        return {
            "users": {
                "id": "UUID PK",
                "email": "VARCHAR UNIQUE",
                "plan": "ENUM(free, pro, enterprise)",
                "clerk_id": "VARCHAR UNIQUE",
                "created_at": "TIMESTAMP",
            },
            "opportunities": {
                "id": "UUID PK",
                "title": "VARCHAR",
                "total_score": "FLOAT",
                "status": "VARCHAR",
                "target_persona": "JSON",
            },
            "projects": {
                "id": "UUID PK",
                "user_id": "UUID FK",
                "opportunity_id": "UUID FK",
                "name": "VARCHAR",
                "status": "VARCHAR",
                "project_structure": "JSON",
            },
            "metrics": {
                "id": "UUID PK",
                "project_id": "UUID FK",
                "metric_name": "VARCHAR",
                "value": "FLOAT",
                "period_start": "TIMESTAMP",
            },
        }
    
    async def _generate_api_design(self, opp: dict) -> dict:
        """生成API设计"""
        return {
            "routes": [
                {"method": "GET", "path": "/api/v1/opportunities", "desc": "List scored opportunities"},
                {"method": "POST", "path": "/api/v1/scanner/run", "desc": "Trigger market scan"},
                {"method": "GET", "path": "/api/v1/opportunities/{id}", "desc": "Opportunity detail"},
                {"method": "POST", "path": "/api/v1/projects/generate", "desc": "Generate MVP plan"},
                {"method": "GET", "path": "/api/v1/projects/{id}", "desc": "Project detail"},
                {"method": "POST", "path": "/api/v1/metrics", "desc": "Record metric"},
                {"method": "GET", "path": "/api/v1/dashboard/stats", "desc": "Dashboard statistics"},
            ],
            "auth": "Clerk JWT middleware",
            "rate_limit": "100 req/min (pro), 20 req/min (free)",
        }
    
    def _generate_project_structure(self) -> dict:
        """生成标准项目结构"""
        return {
            "frontend": {
                "src/app": ["page.tsx", "layout.tsx", "globals.css"],
                "src/components/ui": ["button.tsx", "card.tsx", "input.tsx"],
                "src/lib": ["utils.ts", "api-client.ts"],
            },
            "backend": {
                "app/main.py": "FastAPI entrypoint",
                "app/routers/": ["opportunities.py", "projects.py", "auth.py"],
                "app/services/": ["scanner.py", "scorer.py", "generator.py"],
                "app/models/": ["user.py", "opportunity.py", "project.py"],
                "app/core/": ["config.py", "database.py"],
            },
            "infra": {
                "Dockerfile": "Multi-stage build",
                "docker-compose.yml": "PostgreSQL + Backend + Frontend",
                ".github/workflows/ci.yml": "Test + Build + Deploy",
            },
        }
