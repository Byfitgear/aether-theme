=== Aether ===
Contributors: byfitgear
Tags: one-column, custom-menu, custom-logo, editor-style, translation-ready, block-patterns, dark-mode
Requires at least: 6.0
Tested up to: 6.5
Requires PHP: 7.4
Stable tag: 1.2.0
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

极简 WordPress 主题，集成 Tailwind CSS v4 + htmx，零干扰设计。

== Description ==

Aether 是一个极简主义 WordPress 主题，专注于内容本身。通过移除所有不必要的默认输出，提供干净、快速的阅读体验。

**核心特性:**

* **Tailwind CSS v4** — 本地构建或 CDN 自动加载
* **htmx** — 声明式 AJAX、WebSocket、SSE 交互
* **暗色模式** — 跟随系统偏好或手动切换，localStorage 持久化
* **自定义 Logo** — 后台一键上传站点图标
* **极致精简** — 移除所有 WordPress 默认输出（emoji、RSS、oEmbed、DNS 预取等）
* **SEO 友好** — 自定义 meta title/description/canonical URL + Open Graph + Twitter Card
* **响应式布局** — max-w-4xl 居中布局，移动端自适应
* **自动更新** — 内置主题更新器，支持远程版本检查
* **文章导航** — 上一篇/下一篇 + 阅读时间估算

== Installation ==

1. 上传 `zerowp` 文件夹到 `/wp-content/themes/` 目录
2. 在 WordPress 后台「外观」→「主题」中启用
3. 配置菜单（外观 → 菜单 → Primary Menu）

== Changelog ==

= 1.2.0 =
* 新增: 暗色模式（跟随系统偏好 + 手动切换）
* 新增: 自定义 Logo 支持
* 新增: 文章导航（上一篇/下一篇 + 阅读时间估算）
* 新增: 改进搜索表单样式
* 新增: RSS Feed 链接
* 优化: Tailwind CSS v4 本地构建支持
* 优化: 全页面暗色适配

= 1.1.0 =
* 新增: Open Graph + Twitter Card SEO 标签
* 新增: 专业级主题预览图 (1200×900)
* 新增: 着陆页模板（无页眉页脚）
* 修复: 清理重复的 WordPress 默认样式移除逻辑
* 修复: 评论模板安全加固
* 优化: functions.php 精简 60+ 行冗余代码

= 1.0.0 =
* 初始发布

== Upgrade Notice ==

= 1.2.0 =
新增暗色模式、自定义 Logo 和文章导航，建议升级。

= 1.1.0 =
新增 SEO 标签和着陆页模板，建议升级。
