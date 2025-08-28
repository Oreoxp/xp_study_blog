# 使用说明

## 🎯 快速开始

### 1. 环境准备

确保你的系统已安装以下软件：

- **Ruby** (2.6.0+)
- **Git**
- **文本编辑器** (推荐VS Code)

### 2. 本地开发

```bash
# 克隆项目
git clone https://github.com/duxinpei/xp_study_blog.git
cd xp_study_blog

# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

### 3. 部署到GitHub Pages

```bash
# 使用部署脚本（推荐）
./deploy.sh

# 或手动部署
git add .
git commit -m "Update blog"
git push origin main
```

## 📝 写作指南

### 创建新文章

1. 在 `_posts/` 目录下创建新的Markdown文件
2. 文件名格式：`YYYY-MM-DD-title.md`
3. 添加前置数据：

```yaml
---
layout: post
title: "文章标题"
date: 2024-01-15
categories: [分类]
tags: [标签1, 标签2]
author: XP
excerpt: "文章摘要"
---
```

### 创建新页面

1. 在 `_pages/` 目录下创建Markdown文件
2. 添加前置数据：

```yaml
---
layout: page
title: 页面标题
description: 页面描述
permalink: /your-page/
---
```

### Markdown语法

支持标准Markdown语法：

```markdown
# 一级标题
## 二级标题

**粗体文字**
*斜体文字*

[链接文字](URL)

![图片描述](图片URL)

`行内代码`

```javascript
// 代码块
function hello() {
    console.log("Hello!");
}
```

> 引用文字

- 列表项1
- 列表项2
```

## 🎨 自定义主题

### 修改颜色

编辑 `assets/css/main.css` 中的CSS变量：

```css
:root {
    --primary-color: #3b82f6;    /* 主色调 */
    --text-primary: #1e293b;     /* 文字颜色 */
    --bg-primary: #ffffff;       /* 背景色 */
}
```

### 修改网站信息

编辑 `_config.yml`：

```yaml
title: 你的博客标题
description: 博客描述
author: 你的名字
email: your-email@example.com
url: "https://your-username.github.io/your-repo"
baseurl: "/your-repo"
```

### 修改导航菜单

```yaml
navigation:
  - title: 首页
    url: /
  - title: 博客
    url: /blog/
  - title: 关于
    url: /about/
```

## 🔧 常用命令

```bash
# 本地开发
bundle exec jekyll serve          # 启动服务器
bundle exec jekyll serve --livereload  # 实时重载
bundle exec jekyll serve --drafts # 包含草稿

# 构建
bundle exec jekyll build          # 构建静态文件
bundle exec jekyll clean          # 清理构建文件

# 部署
./deploy.sh                       # 快速部署
git push origin main              # 手动推送
```

## 📁 文件结构说明

```
xp_study_blog/
├── _config.yml          # 配置文件
├── _layouts/            # 布局模板
│   ├── default.html     # 默认布局
│   ├── post.html        # 文章布局
│   └── page.html        # 页面布局
├── _posts/              # 博客文章
├── _pages/              # 静态页面
├── assets/              # 静态资源
│   ├── css/main.css     # 主样式文件
│   ├── js/main.js       # 主脚本文件
│   └── images/          # 图片资源
├── index.html           # 首页
├── Gemfile              # Ruby依赖
├── deploy.sh            # 部署脚本
└── README.md            # 项目说明
```

## 🚨 常见问题

### Q: 本地服务器启动失败
A: 检查Ruby版本和依赖安装：
```bash
ruby --version
bundle install
```

### Q: 样式不生效
A: 检查CSS文件路径和缓存：
```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

### Q: GitHub Pages部署失败
A: 检查仓库设置和分支名称：
- 确保仓库名为 `username.github.io` 或已启用Pages功能
- 确保分支名为 `main` 或 `master`

### Q: 图片不显示
A: 检查图片路径和文件名：
- 使用相对路径：`/assets/images/your-image.jpg`
- 避免文件名包含特殊字符

## 📞 获取帮助

- 查看 [README.md](README.md) 获取详细文档
- 提交 [Issue](https://github.com/duxinpei/xp_study_blog/issues) 报告问题
- 发送邮件到 your-email@example.com

## 🎉 下一步

- 添加更多文章
- 自定义主题颜色
- 添加评论系统
- 配置自定义域名
- 添加分析工具

祝你使用愉快！🎊
