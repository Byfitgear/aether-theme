#!/bin/bash

# Aether Theme 本地仅构建脚本（不上传）

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 开始仅构建 Aether 主题...${NC}"

# 获取主题版本
cd "$(dirname "$0")"
VERSION=$(grep "Version:" aether-theme/zerowp/style.css | head -1 | sed 's/Version: //' | tr -d ' ')
if [ -z "$VERSION" ]; then
  echo -e "${RED}❌ 未能从 style.css 获取版本号${NC}"
  exit 1
fi
echo -e "${YELLOW}📦 主题版本: $VERSION${NC}"

# Tailwind CLI 路径（优先本地安装，其次系统路径）
TAILWIND_CMD=""
if [ -f "aether-theme/zerowp/node_modules/.bin/tailwindcss" ]; then
  TAILWIND_CMD="aether-theme/zerowp/node_modules/.bin/tailwindcss"
elif command -v npx &>/dev/null; then
  TAILWIND_CMD="npx @tailwindcss/cli"
else
  echo -e "${YELLOW}⏭️  跳过 CSS 构建（未找到 Tailwind CLI）${NC}"
fi

# 构建 CSS（Tailwind CSS v4）
if [ -n "$TAILWIND_CMD" ] && [ -f "aether-theme/zerowp/assets/css/input.css" ]; then
  echo -e "${YELLOW}🎨 构建 Tailwind CSS v4...${NC}"
  cd aether-theme/zerowp
  if [[ "$TAILWIND_CMD" == *"npx"* ]]; then
    $TAILWIND_CMD -i assets/css/input.css -o assets/css/output.css --minify 2>/dev/null
  else
    $TAILWIND_CMD -i assets/css/input.css -o assets/css/output.css --minify 2>/dev/null
  fi
  cd ../..
  echo -e "${GREEN}✅ CSS 构建完成${NC}"
else
  echo -e "${YELLOW}⏭️  跳过 CSS 构建（未找到 input.css）${NC}"
fi

# 创建临时目录
TEMP_DIR="/tmp/aether-build-$$"
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

# 复制主题文件，排除不需要的文件
rsync -av \
  --exclude='.git' \
  --exclude='.github' \
  --exclude='node_modules' \
  --exclude='dist' \
  --exclude='.gitignore' \
  --exclude='.gitattributes' \
  --exclude='package.json' \
  --exclude='package-lock.json' \
  --exclude='README.md' \
  --exclude='build-and-upload.sh' \
  --exclude='only-build.sh' \
  --exclude='.env' \
  --exclude='.claude' \
  --exclude='.wrangler' \
  --exclude='*.zip' \
  --exclude='dev-config.php' \
  --exclude='tailwind.config.js' \
  --exclude='input.css' \
  . "$TEMP_DIR/zerowp/"

# 创建 ZIP 文件
cd "$TEMP_DIR"
zip -r "$OLDPWD/aether-theme/zerowp-theme-$VERSION.zip" zerowp/ >/dev/null
cd "$OLDPWD"

# 验证 ZIP 文件
if [ -f "aether-theme/zerowp-theme-$VERSION.zip" ]; then
  echo -e "${GREEN}✅ ZIP 文件创建成功:${NC}"
  ls -lh "aether-theme/zerowp-theme-$VERSION.zip"
else
  echo -e "${RED}❌ ZIP 文件创建失败${NC}"
  exit 1
fi

# 清理临时目录
rm -rf "$TEMP_DIR"

echo -e "${GREEN}✨ 构建完成! 输出: aether-theme/zerowp-theme-$VERSION.zip${NC}"
