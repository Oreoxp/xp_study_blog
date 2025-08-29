# 动态文档系统说明

## 概述

这个系统可以自动扫描 `_docs` 文件夹，生成动态的文档数据，让你的博客首页能够实时显示最新的文档信息，无需手动更新。

## 工作原理

1. **Python脚本** (`scripts/generate_docs_data.py`) 扫描 `_docs` 文件夹
2. **生成数据文件** 存储在 `_data/` 目录中
3. **Jekyll模板** 使用这些数据动态渲染页面
4. **GitHub Action** 在文档更新时自动运行脚本

## 文件结构

```
├── scripts/
│   └── generate_docs_data.py    # 文档扫描脚本
├── .github/workflows/
│   └── update-docs.yml          # GitHub Action工作流
├── _data/                       # 生成的数据文件（自动创建）
│   ├── docs.json               # JSON格式的文档数据
│   └── docs.yml                # YAML格式的文档数据
├── _includes/
│   └── dynamic_docs.html       # 动态HTML片段（自动生成）
└── requirements.txt             # Python依赖
```

## 使用方法

### 1. 添加新文档

只需要在 `_docs` 文件夹的相应分类目录下添加 `.md` 文件即可：

```bash
# 例如添加一个新的学习笔记
echo "# 新文档标题" > _docs/学习笔记/新文档.md
```

### 2. 文档格式

建议在文档开头添加 front matter 来提供更好的描述：

```markdown
---
title: 文档标题
description: 文档描述
date: 2024-01-20
tags: [标签1, 标签2]
---

文档内容...
```

### 3. 手动运行脚本

如果需要手动更新文档数据：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行脚本
python scripts/generate_docs_data.py
```

## GitHub Action 自动化

当你在 `_docs` 文件夹中添加、修改或删除文档时：

1. 提交并推送到 GitHub
2. GitHub Action 自动触发
3. 运行文档扫描脚本
4. 生成新的数据文件
5. 自动提交更新

## 配置说明

### Jekyll 配置

确保 `_config.yml` 中启用了数据文件支持：

```yaml
# 数据文件目录
data_dir: _data
```

### 首页模板

`index.html` 现在使用动态数据：

```liquid
{% if site.data.docs %}
  {% for category in site.data.docs.categories %}
    <!-- 动态渲染分类和文档 -->
  {% endfor %}
{% else %}
  <!-- 后备方案 -->
  {% include dynamic_docs.html %}
{% endif %}
```

## 故障排除

### 问题：脚本无法运行

- 检查 Python 版本（需要 3.6+）
- 安装依赖：`pip install -r requirements.txt`
- 确保 `_docs` 文件夹存在

### 问题：GitHub Action 失败

- 检查 `.github/workflows/update-docs.yml` 文件
- 查看 GitHub Actions 日志
- 确保仓库有适当的权限

### 问题：页面显示不正确

- 检查 `_data/docs.yml` 文件是否正确生成
- 验证 Jekyll 模板语法
- 清除 Jekyll 缓存：`jekyll clean`

## 扩展功能

### 添加新的文档属性

修改 `scripts/generate_docs_data.py` 中的 `extract_doc_info` 函数：

```python
def extract_doc_info(doc_file):
    # 添加新的属性
    doc_info = {
        # ... 现有属性
        "new_property": "新属性值"
    }
    # ... 提取逻辑
    return doc_info
```

### 自定义排序

修改 `scan_docs_directory` 函数中的排序逻辑：

```python
# 按文档数量排序
docs_data["categories"].sort(key=lambda x: x["doc_count"], reverse=True)
```

## 注意事项

1. **文件编码**：确保所有 `.md` 文件使用 UTF-8 编码
2. **文件名**：避免使用特殊字符，推荐使用英文或中文
3. **路径**：文档路径会自动生成，无需手动指定
4. **性能**：对于大量文档，脚本可能需要几秒钟运行

## 更新日志

- **v1.0.0**: 初始版本，支持基本的文档扫描和动态生成
- 支持 YAML front matter 解析
- 自动生成 JSON 和 YAML 数据文件
- GitHub Action 自动化工作流
