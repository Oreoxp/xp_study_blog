#!/bin/bash

# XP的学习博客 - 部署脚本
# 使用方法: ./deploy.sh

echo "🚀 开始部署XP的学习博客..."

# 检查是否在正确的目录
if [ ! -f "_config.yml" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 检查Git是否已初始化
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
fi

# 添加所有文件到Git
echo "📝 添加文件到Git..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Update blog content - $(date '+%Y-%m-%d %H:%M:%S')"

# 检查远程仓库
if ! git remote | grep -q origin; then
    echo "🔗 请先添加远程仓库:"
    echo "   git remote add origin https://github.com/duxinpei/xp_study_blog.git"
    echo "   或者修改_config.yml中的url和baseurl配置"
    exit 1
fi

# 推送到GitHub
echo "⬆️  推送到GitHub..."
git push origin main

echo "✅ 部署完成！"
echo "🌐 你的博客将在几分钟后可用:"
echo "   https://duxinpei.github.io/xp_study_blog"
echo ""
echo "📝 提示:"
echo "   - 确保GitHub仓库已启用Pages功能"
echo "   - 第一次部署可能需要等待几分钟"
echo "   - 可以在仓库设置中查看部署状态"
