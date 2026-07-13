"""增长分析Agent — 监控和优化关键指标"""
import json
import logging
from typing import Optional
from datetime import datetime, timedelta

from ..core.config import get_settings

logger = logging.getLogger(__name__)


class GrowthAnalyzerAgent:
    """增长指标分析与优化建议引擎"""
    
    KEY_METRICS = ["retention", "conversion", "cac", "ltv", "mau", "nps"]
    
    async def analyze_metrics(self, metrics_data: list[dict]) -> dict:
        """分析指标数据，返回洞察和优化建议"""
        analysis = {
            "metrics_summary": {},
            "trends": {},
            "alerts": [],
            "recommendations": [],
            "analyzed_at": datetime.utcnow().isoformat(),
        }
        
        for metric in metrics_data:
            name = metric.get("metric_name", "")
            value = metric.get("value", 0)
            
            analysis["metrics_summary"][name] = {
                "current_value": value,
                "status": self._evaluate_metric(name, value),
                "benchmark": self._get_benchmark(name),
            }
            
            alert = self._check_alerts(name, value)
            if alert:
                analysis["alerts"].append(alert)
            
            rec = self._generate_recommendation(name, value)
            if rec:
                analysis["recommendations"].append(rec)
        
        return analysis
    
    def _evaluate_metric(self, name: str, value: float) -> str:
        """评估指标状态"""
        benchmarks = {
            "retention": {"good": 40, "bad": 20},
            "conversion": {"good": 5, "bad": 1},
            "cac": {"good": 15, "bad": 50},
            "ltv": {"good": 500, "bad": 100},
            "mau": {"good": 1000, "bad": 100},
            "nps": {"good": 50, "bad": 20},
        }
        
        bench = benchmarks.get(name, {"good": 50, "bad": 20})
        if name == "cac":  # Lower is better
            if value <= bench["good"]:
                return "excellent"
            elif value >= bench["bad"]:
                return "critical"
            return "needs_improvement"
        
        if value >= bench["good"]:
            return "excellent"
        elif value <= bench["bad"]:
            return "critical"
        return "needs_improvement"
    
    def _get_benchmark(self, name: str) -> float:
        """行业基准值"""
        benchmarks = {
            "retention": 40.0,   # Day-30 retention %
            "conversion": 5.0,   # Signup → Paid %
            "cac": 15.0,         # $
            "ltv": 500.0,        # $
            "mau": 1000.0,       # users
            "nps": 50.0,         # score
        }
        return benchmarks.get(name, 50.0)
    
    def _check_alerts(self, name: str, value: float) -> Optional[dict]:
        """检查是否需要告警"""
        alerts = {
            "retention": {"threshold": 20, "msg": f"Retention critically low at {value}%. Consider onboarding improvements."},
            "conversion": {"threshold": 1, "msg": f"Conversion rate below 1%. Review pricing page and checkout flow."},
            "cac": {"threshold": 50, "msg": f"CAC too high at ${value}. Optimize acquisition channels."},
            "nps": {"threshold": 20, "msg": f"NPS below 20. User satisfaction needs attention."},
        }
        
        if name in alerts:
            alert = alerts[name]
            if (name == "cac" and value >= alert["threshold"]) or \
               (name != "cac" and value <= alert["threshold"]):
                return {"metric": name, "value": value, "message": alert["msg"]}
        
        return None
    
    def _generate_recommendation(self, name: str, value: float) -> Optional[str]:
        """生成优化建议"""
        recommendations = {
            "retention": "Implement progressive onboarding with interactive tutorials. Add push notifications for re-engagement.",
            "conversion": "A/B test pricing pages. Add social proof (testimonials, user counts). Reduce form fields.",
            "cac": "Double down on organic channels (SEO, content). Build referral program. Optimize ad targeting.",
            "ltv": "Introduce tiered pricing. Add premium features. Implement usage-based upselling.",
            "mau": "Add daily value hooks. Build community features. Send weekly digest emails.",
            "nps": "Conduct user interviews. Fix top 3 pain points. Implement feedback loop.",
        }
        
        if name in recommendations:
            return recommendations[name]
        return None
    
    async def predict_churn(self, user_data: list[dict]) -> list[dict]:
        """预测用户流失风险"""
        # 简化版：基于活动模式的规则引擎
        at_risk = []
        for user in user_data:
            days_since_active = user.get("days_since_active", 999)
            if days_since_active > 14:
                at_risk.append({
                    "user_id": user.get("id"),
                    "risk_level": "high" if days_since_active > 30 else "medium",
                    "recommended_action": "Send win-back email with new feature highlights",
                })
        return at_risk
