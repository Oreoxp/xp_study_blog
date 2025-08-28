---
layout: post
title: "使用Jekyll和GitHub Pages搭建个人博客"
date: 2024-01-16
categories: [技术, 教程]
tags: [Jekyll, GitHub Pages, 博客搭建, 静态网站]
author: XP
excerpt: "详细介绍了如何使用Jekyll静态网站生成器和GitHub Pages免费托管服务来搭建个人博客，包括环境配置、主题定制和部署流程。"
---

# 使用Jekyll和GitHub Pages搭建个人博客

在上一篇文章中，我介绍了创建这个博客的初衷。今天，我想详细分享一下我是如何使用Jekyll和GitHub Pages来搭建这个博客的。

## 为什么选择Jekyll + GitHub Pages？

在开始搭建之前，我对比了多种博客解决方案：

### 静态网站生成器对比
- **Jekyll**: Ruby生态，GitHub原生支持，社区成熟
- **Hugo**: Go语言，构建速度快，但学习成本较高
- **Hexo**: Node.js生态，适合前端开发者
- **Next.js**: React框架，功能强大但相对复杂

### 托管平台对比
- **GitHub Pages**: 免费，与Git集成好，自动部署
- **Netlify**: 功能丰富，但免费版有限制
- **Vercel**: 适合前端项目，但主要面向React/Vue
- **自建服务器**: 完全控制，但需要维护成本

最终选择Jekyll + GitHub Pages的原因：
1. **免费且稳定** - GitHub Pages提供免费托管
2. **简单易用** - Jekyll语法简单，学习成本低
3. **社区支持** - 有丰富的主题和插件
4. **版本控制** - 与Git完美集成
5. **自动部署** - 推送代码即可自动更新

## 环境准备

### 1. 安装Ruby和Jekyll

首先需要安装Ruby环境：

```bash
# macOS (使用Homebrew)
brew install ruby

# 或者使用rbenv管理Ruby版本
brew install rbenv
rbenv install 3.2.0
rbenv global 3.2.0
```

安装Jekyll：

```bash
gem install jekyll bundler
```

### 2. 创建Jekyll项目

```bash
# 创建新的Jekyll站点
jekyll new my-blog
cd my-blog

# 或者从现有项目初始化
bundle init
```

### 3. 配置Gemfile

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3.0"
gem "jekyll-feed", "~> 0.17"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-sitemap", "~> 1.4"

# Windows和JRuby不支持
platforms :mingw, :x64_mingw, :mswin, :jruby do
  exclude_comments = true
end

gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "webrick", "~> 1.7"
```

## 项目结构

一个标准的Jekyll项目结构如下：

```
my-blog/
├── _config.yml          # 配置文件
├── _layouts/            # 布局模板
│   ├── default.html
│   ├── post.html
│   └── page.html
├── _includes/           # 可重用的HTML片段
├── _posts/              # 博客文章
├── _pages/              # 静态页面
├── assets/              # 静态资源
│   ├── css/
│   ├── js/
│   └── images/
├── index.html           # 首页
└── Gemfile              # Ruby依赖
```

## 配置文件详解

`_config.yml`是Jekyll的核心配置文件：

```yaml
# 基本信息
title: XP的学习博客
description: 记录学习笔记、技术分享和个人思考
author: XP
email: your-email@example.com
url: "https://duxinpei.github.io/xp_study_blog"
baseurl: "/xp_study_blog"

# 构建设置
markdown: kramdown
highlighter: rouge
permalink: /:year/:month/:day/:title/

# 插件
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap

# 默认值
defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
      author: "XP"
```

## 主题定制

### 1. 创建布局文件

`_layouts/default.html` - 主布局：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} - {{ site.title }}{% else %}{{ site.title }}{% endif %}</title>
    <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
</head>
<body>
    <nav class="navbar">
        <!-- 导航栏内容 -->
    </nav>
    
    <main class="main-content">
        {{ content }}
    </main>
    
    <footer class="footer">
        <!-- 页脚内容 -->
    </footer>
</body>
</html>
```

### 2. 样式设计

使用现代CSS特性创建响应式设计：

```css
:root {
    --primary-color: #3b82f6;
    --text-primary: #1e293b;
    --bg-primary: #ffffff;
    /* 更多CSS变量 */
}

/* 响应式设计 */
@media (max-width: 768px) {
    .container {
        padding: 0 1rem;
    }
}
```

## 本地开发

### 启动本地服务器

```bash
# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 或者使用实时重载
bundle exec jekyll serve --livereload
```

访问 `http://localhost:4000` 查看效果。

### 常用命令

```bash
# 构建静态文件
bundle exec jekyll build

# 清理构建文件
bundle exec jekyll clean

# 草稿模式
bundle exec jekyll serve --drafts
```

## 部署到GitHub Pages

### 1. 创建GitHub仓库

在GitHub上创建一个名为 `username.github.io` 的仓库（username是你的GitHub用户名）。

### 2. 推送代码

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/username.github.io.git
git push -u origin main
```

### 3. 配置GitHub Pages

在仓库设置中：
1. 进入 "Settings" → "Pages"
2. Source选择 "Deploy from a branch"
3. Branch选择 "main"，文件夹选择 "/ (root)"
4. 点击 "Save"

### 4. 自定义域名（可选）

如果你有自己的域名：
1. 在域名提供商处添加CNAME记录
2. 在仓库根目录创建 `CNAME` 文件，内容为你的域名
3. 在GitHub Pages设置中启用自定义域名

## 优化建议

### 1. SEO优化

```html
<!-- 在head中添加 -->
<meta name="description" content="{{ page.description | default: site.description }}">
<meta name="keywords" content="{{ page.tags | join: ', ' }}">
<link rel="canonical" href="{{ site.url }}{{ page.url }}">
```

### 2. 性能优化

- 压缩CSS和JavaScript
- 优化图片大小
- 使用CDN加载字体和图标
- 启用Gzip压缩

### 3. 用户体验

- 添加搜索功能
- 实现标签和分类页面
- 添加评论系统（如Disqus）
- 实现RSS订阅

## 常见问题

### 1. 构建失败

检查：
- Ruby版本是否兼容
- 依赖是否正确安装
- 配置文件语法是否正确

### 2. 样式不生效

确保：
- CSS文件路径正确
- 文件已正确提交到GitHub
- 缓存已清理

### 3. 图片不显示

检查：
- 图片路径是否正确
- 文件名是否包含特殊字符
- 文件大小是否超过限制

## 总结

使用Jekyll和GitHub Pages搭建博客是一个很好的选择，特别是对于程序员来说。它提供了：

- **完全控制** - 可以自定义所有细节
- **版本控制** - 所有更改都有历史记录
- **免费托管** - GitHub Pages提供免费服务
- **学习价值** - 可以学习静态网站生成和部署

虽然初期配置可能需要一些时间，但一旦搭建完成，维护和更新就变得非常简单。

希望这篇文章对想要搭建个人博客的朋友有所帮助！如果你有任何问题，欢迎在评论区讨论。

---

*下一篇我将分享如何为博客添加更多功能，比如搜索、评论系统等。*
