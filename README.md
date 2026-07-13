# Aether — 极简 WordPress 主题

> 零干扰设计 · Tailwind CSS v4 · htmx · 极致精简

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0.html)
[![WordPress](https://img.shields.io/badge/WordPress-6.0+-5393fe)](https://wordpress.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-v4-38bdf8)](https://tailwindcss.com/)

## ✨ 特性

| 特性 | 说明 |
|------|------|
| **Tailwind CSS v4** | 通过 CDN 自动加载，无需构建步骤 |
| **htmx** | 声明式 AJAX、WebSocket、SSE 交互 |
| **零干扰设计** | 移除所有 WordPress 默认输出（emoji、RSS、oEmbed、DNS 预取等） |
| **SEO 友好** | 自定义 meta title/description/canonical URL + Open Graph + Twitter Card |
| **响应式布局** | max-w-4xl 居中布局，移动端自适应 |
| **自动更新** | 内置主题更新器，支持远程版本检查 |
| **极致轻量** | 核心代码不到 900 行，无冗余依赖 |

## 📦 安装

### 方法一：后台上传

1. 下载 `zerowp-theme-x.y.z.zip`
2. WordPress 后台 → 外观 → 主题 → 添加新主题 → 上传主题
3. 启用主题

### 方法二：FTP 上传

将 `zerowp/` 文件夹上传到 `wp-content/themes/`，然后在后台启用。

## ⚙️ 配置

### 菜单

外观 → 菜单 → 分配到"Primary Menu"位置

### 首页设置

设置 → 阅读 → 首页显示 → 选择文章列表或静态页面

### 自动更新

主题内置更新器，默认检查 `aetherwp.dev` API。如需禁用：

```php
// wp-config.php
define('AETHER_DISABLE_UPDATE_CHECKS', true);
```

## 🛠 开发

```bash
# 仅构建 ZIP（不上传）
chmod +x only-build.sh
./only-build.sh
```

## 📄 文件结构

```
zerowp/
├── style.css              # 主题元数据
├── functions.php          # 核心功能
├── header.php             # 页头 + Tailwind CDN + SEO
├── footer.php             # 页脚
├── index.php              # 主循环
├── single.php             # 单篇文章
├── page.php               # 页面
├── page-landing.php       # 着陆页模板
├── search.php             # 搜索结果
├── comments.php           # 评论
├── 404.php                # 404 页面
├── screenshot.png         # 主题预览图 (1200×900)
├── assets/js/htmx.min.js  # htmx 运行时
└── inc/theme-updater.php  # 自动更新器
```

## 🎨 设计理念

Aether 遵循 **"内容优先"** 的设计哲学：

1. **移除一切干扰** — 无 emoji 脚本、无 RSS、无 oEmbed、无 DNS 预取
2. **最小化 CSS** — 只保留 Tailwind Typography 的微调
3. **最简化 body class** — 只保留必要的页面类型标识
4. **干净的 HTML** — 语义化标签，无障碍友好

## 📝 License

GPL v2 or later

## 🔗 相关链接

- [主题主页](https://aetherwp.dev)
- [GitHub 仓库](https://github.com/your-username/aether-theme)
- [WordPress.org 主题目录](https://wordpress.org/themes/aether/)
