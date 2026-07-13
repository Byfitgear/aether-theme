# Aether — 极简 WordPress 主题

> 零干扰设计 · Tailwind CSS v4 · htmx · 极致精简

## ✨ 特性

- **Tailwind CSS v4** — 通过 CDN 自动加载，无需构建步骤
- **htmx** — 声明式 AJAX、WebSocket、SSE 交互
- **极致精简** — 移除所有 WordPress 默认输出（emoji、RSS、oEmbed、DNS 预取等）
- **SEO 友好** — 自定义 meta title/description/canonical URL
- **响应式布局** — max-w-4xl 居中布局，移动端自适应
- **自动更新** — 内置主题更新器，支持远程版本检查
- **开发模式** — 快速迭代，5 分钟级更新检测

## 📦 安装

1. 下载 `zerowp-theme-x.y.z.zip`
2. WordPress 后台 → 外观 → 主题 → 添加新主题 → 上传主题
3. 启用主题

或者通过 FTP 上传 `zerowp/` 到 `wp-content/themes/`

## ⚙️ 配置

### 菜单

外观 → 菜单 → 分配到"Primary Menu"位置

### 首页设置

设置 → 阅读 → 首页显示 → 选择文章列表或静态页面

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
├── header.php             # 页头 + Tailwind CDN
├── footer.php             # 页脚
├── index.php              # 主循环
├── single.php             # 单篇文章
├── page.php               # 页面
├── page-landing.php       # 着陆页模板
├── search.php             # 搜索结果
├── comments.php           # 评论
├── 404.php                # 404 页面
├── dev-config.php         # 开发模式配置
├── only-build.sh          # 构建脚本
├── screenshot.png         # 主题预览图
├── assets/js/htmx.min.js  # htmx 运行时
└── inc/theme-updater.php  # 自动更新器
```

## 📝 License

GPL v2 or later
