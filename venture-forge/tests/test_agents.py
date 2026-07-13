"""Test suite for AI Agents"""
import pytest
import json
from unittest.mock import AsyncMock, patch, MagicMock


class TestMarketScannerAgent:
    """测试市场扫描Agent"""

    def setup_method(self):
        from backend.app.agents.market_scanner import MarketScannerAgent
        self.agent = MarketScannerAgent()

    @pytest.mark.asyncio
    async def test_scan_reddit_basic(self):
        """测试Reddit扫描基本功能"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "children": [
                    {
                        "data": {
                            "title": "Why doesn't anyone build a good AI tool for this?",
                            "score": 850,
                            "num_comments": 120,
                            "permalink": "/r/startups/test",
                        }
                    },
                    {
                        "data": {
                            "title": "This is so frustrating to deal with manually",
                            "score": 320,
                            "num_comments": 45,
                            "permalink": "/r/SaaS/test",
                        }
                    },
                ]
            }
        }

        with patch("httpx.AsyncClient") as MockClient:
            mock_client = AsyncMock()
            mock_client.get = AsyncMock(return_value=mock_response)
            MockClient.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            MockClient.return_value.__aexit__ = AsyncMock(return_value=None)

            results = await self.agent._scan_reddit()
            assert len(results) >= 1
            assert any(r["platform"] == "reddit" for r in results)

    def test_rule_based_extract(self):
        """测试基于规则的痛点提取"""
        finding = {
            "title": "Why doesn't anyone build a good AI tool for this?",
            "platform": "reddit",
            "signal_strength": 4.5,
        }
        result = self.agent._rule_based_extract(finding)
        assert result is not None
        assert result["raw_title"] == finding["title"]
        assert result["platform"] == "reddit"

    def test_categorize_dev_tool(self):
        """测试分类 - 开发者工具"""
        cat = self.agent._categorize("best developer tool alternatives")
        assert cat == "dev tool"

    def test_categorize_time_saver(self):
        """测试分类 - 节省时间"""
        cat = self.agent._categorize("manual tedious process takes too long")
        assert cat == "time saver"

    def test_categorize_cost_reduction(self):
        """测试分类 - 降低成本"""
        cat = self.agent._categorize("too expensive budget constraints")
        assert cat == "cost reduction"

    def test_categorize_default(self):
        """测试默认分类"""
        cat = self.agent._categorize("some random feedback about products")
        assert cat == "general"

    def test_simulate_product_hunt(self):
        """测试Product Hunt模拟数据"""
        results = self.agent._simulate_product_hunt()
        assert isinstance(results, list)
        assert len(results) >= 2
        assert all(r["platform"] == "producthunt" for r in results)


class TestOpportunityScorerAgent:
    """测试机会评分Agent"""

    def setup_method(self):
        from backend.app.agents.opportunity_scorer import OpportunityScorerAgent
        self.agent = OpportunityScorerAgent()

    def test_weights_defined(self):
        """测试权重定义"""
        total = sum(self.agent.WEIGHTS.values())
        assert abs(total - 1.0) < 0.01

    def test_filter_high_value(self):
        """测试高分筛选"""
        opportunities = [
            {"total_score": 92, "title": "High value"},
            {"total_score": 75, "title": "Low value"},
            {"total_score": 88, "title": "Also high"},
        ]
        filtered = self.agent.filter_high_value(opportunities, threshold=80)
        assert len(filtered) == 2
        assert all(op["total_score"] >= 80 for op in filtered)

    def test_rule_based_score_structure(self):
        """测试规则评分结构"""
        pain_point = {
            "raw_title": "Test pain point",
            "signal": 4,
            "category": "dev tool",
        }
        score = self.agent._rule_based_score(pain_point)
        assert "market_size" in score
        assert "competition" in score
        assert "dev_difficulty" in score
        assert "ai_replaceability" in score
        assert "profitability" in score


class TestMVPGeneratorAgent:
    """测试MVP生成Agent"""

    def setup_method(self):
        from backend.app.agents.mvp_generator import MVPGeneratorAgent
        self.agent = MVPGeneratorAgent()

    def test_generate_features(self):
        """测试MVP功能列表生成"""
        opp = {"pain_point": {"raw_title": "Test"}}
        features = self.agent._generate_features(opp)
        assert isinstance(features, list)
        assert len(features) >= 4
        assert all("priority" in f for f in features)
        assert all("effort" in f for f in features)

    def test_generate_user_journey(self):
        """测试用户旅程生成"""
        opp = {"pain_point": {"raw_title": "Test"}}
        journey = self.agent._generate_user_journey(opp)
        assert isinstance(journey, list)
        assert len(journey) >= 4
        assert all("step" in j for j in journey)
        assert all("action" in j for j in journey)

    def test_generate_project_structure(self):
        """测试项目结构生成"""
        structure = self.agent._generate_project_structure()
        assert "frontend" in structure
        assert "backend" in structure
        assert "infra" in structure

    def test_database_schema_structure(self):
        """测试数据库Schema结构"""
        schema = self.agent._generate_db_schema({"pain_point": {}})
        assert "users" in schema
        assert "opportunities" in schema
        assert "projects" in schema
        assert "metrics" in schema

    def test_api_design_structure(self):
        """测试API设计结构"""
        api = self.agent._generate_api_design({"pain_point": {}})
        assert "routes" in api
        assert "auth" in api
        assert "rate_limit" in api


class TestGrowthAnalyzerAgent:
    """测试增长分析Agent"""

    def setup_method(self):
        from backend.app.agents.growth_analyzer import GrowthAnalyzerAgent
        self.agent = GrowthAnalyzerAgent()

    def test_evaluate_metric_excellent(self):
        """测试优秀指标评估"""
        status = self.agent._evaluate_metric("retention", 50)
        assert status == "excellent"

    def test_evaluate_metric_critical(self):
        """测试危险指标评估"""
        status = self.agent._evaluate_metric("retention", 10)
        assert status == "critical"

    def test_evaluate_metric_needs_improvement(self):
        """测试需改进指标评估"""
        status = self.agent._evaluate_metric("retention", 30)
        assert status == "needs_improvement"

    def test_get_benchmark(self):
        """测试基准值获取"""
        assert self.agent._get_benchmark("retention") == 40.0
        assert self.agent._get_benchmark("conversion") == 5.0
        assert self.agent._get_benchmark("cac") == 15.0

    def test_check_alerts_retention_low(self):
        """测试告警 - 低留存"""
        alert = self.agent._check_alerts("retention", 15)
        assert alert is not None
        assert "Retention" in alert["message"]

    def test_check_alerts_no_alert(self):
        """测试无告警"""
        alert = self.agent._check_alerts("retention", 50)
        assert alert is None

    def test_check_alerts_cac_high(self):
        """测试告警 - 高CAC"""
        alert = self.agent._check_alerts("cac", 60)
        assert alert is not None

    def test_predict_churn(self):
        """测试流失预测"""
        users = [
            {"id": "u1", "days_since_active": 5},
            {"id": "u2", "days_since_active": 20},
            {"id": "u3", "days_since_active": 45},
        ]
        at_risk = self.agent.predict_churn(users)
        assert len(at_risk) == 2  # u2 and u3
        assert at_risk[1]["risk_level"] == "high"

    def test_recommendations_exist(self):
        """测试建议存在"""
        rec = self.agent._generate_recommendation("retention", 25)
        assert rec is not None
        assert len(rec) > 10
