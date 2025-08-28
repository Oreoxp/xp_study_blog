# XP的学习博客

一个使用Jekyll和GitHub Pages构建的现代化个人博客。

## 🌟 特性

- **响应式设计** - 在所有设备上都有完美的显示效果
- **现代化UI** - 使用CSS变量和现代CSS特性
- **快速加载** - 优化的资源加载和缓存策略
- **SEO友好** - 针对搜索引擎进行了优化
- **易于维护** - 清晰的代码结构和文档
- **免费托管** - 使用GitHub Pages免费托管

## 🚀 快速开始

### 环境要求

- Ruby 2.6.0 或更高版本
- Jekyll 4.0 或更高版本
- Git

### 本地开发

1. **克隆仓库**
   ```bash
   git clone https://github.com/duxinpei/xp_study_blog.git
   cd xp_study_blog
   ```

2. **安装依赖**
   ```bash
   bundle install
   ```

3. **启动本地服务器**
   ```bash
   bundle exec jekyll serve
   ```

4. **访问网站**
   打开浏览器访问 `http://localhost:4000`

### 部署到GitHub Pages

1. **推送代码到GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **配置GitHub Pages**
   - 进入仓库设置 → Pages
   - Source选择 "Deploy from a branch"
   - Branch选择 "main"
   - 点击 "Save"

3. **访问你的博客**
   访问 `https://duxinpei.github.io/xp_study_blog`

## 📁 项目结构

```
xp_study_blog/
├── _config.yml          # Jekyll配置文件
├── _layouts/            # 布局模板
│   ├── default.html     # 默认布局
│   ├── post.html        # 文章布局
│   └── page.html        # 页面布局
├── _includes/           # 可重用的HTML片段
├── _posts/              # 博客文章
├── _pages/              # 静态页面
├── assets/              # 静态资源
│   ├── css/             # 样式文件
│   ├── js/              # JavaScript文件
│   └── images/          # 图片资源
├── index.html           # 首页
├── Gemfile              # Ruby依赖
└── README.md            # 项目说明
```

## 🎨 自定义主题

### 修改颜色主题

在 `assets/css/main.css` 中修改CSS变量：

```css
:root {
    --primary-color: #3b82f6;    /* 主色调 */
    --text-primary: #1e293b;     /* 主要文字颜色 */
    --bg-primary: #ffffff;       /* 背景色 */
    /* 更多颜色变量... */
}
```

### 添加新页面

1. 在 `_pages/` 目录下创建新的Markdown文件
2. 添加YAML前置数据：

```yaml
---
layout: page
title: 页面标题
description: 页面描述
permalink: /your-page/
---
```

### 发布新文章

1. 在 `_posts/` 目录下创建新的Markdown文件
2. 文件名格式：`YYYY-MM-DD-title.md`
3. 添加YAML前置数据：

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

## 🔧 配置说明

### 基本信息配置

在 `_config.yml` 中修改：

```yaml
title: XP的学习博客
description: 记录学习笔记、技术分享和个人思考
author: XP
email: your-email@example.com
url: "https://duxinpei.github.io/xp_study_blog"
baseurl: "/xp_study_blog"
```

### 导航菜单配置

```yaml
navigation:
  - title: 首页
    url: /
  - title: 博客
    url: /blog/
  - title: 关于
    url: /about/
```

### 社交媒体链接

```yaml
social:
  github: duxinpei
  twitter: your-twitter
  linkedin: your-linkedin
  email: your-email@example.com
```

## 📝 写作指南

### Markdown语法

博客支持标准Markdown语法，包括：

- **标题**: `# 一级标题`, `## 二级标题`
- **强调**: `**粗体**`, `*斜体*`
- **链接**: `[链接文字](URL)`
- **图片**: `![alt文字](图片URL)`
- **代码**: `` `行内代码` ``
- **代码块**: ``` ```代码块```

### 代码高亮

支持多种编程语言的语法高亮：

```javascript
// JavaScript代码示例
function hello() {
    console.log("Hello, World!");
}
```

```python
# Python代码示例
def hello():
    print("Hello, World!")
```

## 🎯 功能特性

### 已实现功能

- ✅ 响应式导航栏
- ✅ 文章列表和详情页
- ✅ 分类和标签系统
- ✅ 搜索功能（基础）
- ✅ 代码高亮
- ✅ 社交分享
- ✅ RSS订阅
- ✅ 返回顶部按钮
- ✅ 移动端适配

### 计划功能

- 🔄 评论系统
- 🔄 深色模式
- 🔄 全文搜索
- 🔄 文章目录
- 🔄 阅读时间估算
- 🔄 多语言支持

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

### 提交Issue

1. 检查是否已有相关Issue
2. 创建新的Issue，详细描述问题或建议
3. 添加适当的标签

### 提交Pull Request

1. Fork这个仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个Pull Request

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Jekyll](https://jekyllrb.com/) - 静态网站生成器
- [GitHub Pages](https://pages.github.com/) - 免费托管服务
- [Font Awesome](https://fontawesome.com/) - 图标库
- [Google Fonts](https://fonts.google.com/) - 字体服务

## 📞 联系方式

- **GitHub**: [duxinpei](https://github.com/duxinpei)
- **邮箱**: your-email@example.com
- **博客**: [https://duxinpei.github.io/xp_study_blog](https://duxinpei.github.io/xp_study_blog)

---

如果这个项目对你有帮助，请给它一个⭐️！
