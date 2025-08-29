#!/bin/bash
# 快速更新文档数据脚本

echo "🚀 快速更新文档数据..."

# 检查虚拟环境是否存在
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📚 安装依赖..."
pip install -q PyYAML

# 运行文档生成脚本
echo "📝 生成文档数据..."
python scripts/generate_docs_data.py

# 显示更新结果
echo ""
echo "📊 更新完成！"
echo "   - 数据文件: _data/docs.yml, _data/docs.json"
echo "   - HTML片段: _includes/dynamic_docs.html"
echo ""
echo "💡 提示: 现在可以提交这些文件到GitHub了！"
echo "   git add _data/ _includes/dynamic_docs.html"
echo "   git commit -m '更新文档数据'"
echo "   git push"
