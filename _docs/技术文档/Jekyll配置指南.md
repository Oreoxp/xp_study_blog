---
layout: docs_page
title: Jekyll配置指南
category: 技术文档
description: Jekyll静态站点生成器的配置和使用指南
date: 2024-01-01
---

# Jekyll配置指南

## 基本配置

### _config.yml 文件结构
```yaml
# 站点信息
title: "我的博客"
description: "个人技术博客"
author: "作者名"
email: "email@example.com"

# URL配置
url: "https://yourdomain.com"
baseurl: "/blog"

# 构建配置
markdown: kramdown
highlighter: rouge
permalink: /:year/:month/:day/:title/

# 插件配置
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap
```

## 目录结构

```
your-blog/
├── _config.yml          # 配置文件
├── _posts/              # 博客文章
├── _pages/              # 页面文件
├── _layouts/            # 布局模板
├── _includes/           # 包含文件
├── _sass/               # Sass样式
├── assets/              # 静态资源
│   ├── css/
│   ├── js/
│   └── images/
└── _site/               # 生成的静态文件
```

## 文章格式

### Front Matter
```yaml
---
layout: post
title: "文章标题"
date: 2024-01-20 10:00:00 +0800
categories: [技术, 教程]
tags: [jekyll, 博客]
author: 作者名
---
```

### 支持的变量
- `layout`: 布局模板
- `title`: 文章标题
- `date`: 发布日期
- `categories`: 分类（数组）
- `tags`: 标签（数组）
- `author`: 作者
- `comments`: 是否启用评论
- `published`: 是否发布

## 布局系统

### 默认布局
```html
<!DOCTYPE html>
<html>
<head>
    <title>页面标题 - 站点标题</title>
</head>
<body>
    <header>
        <!-- 页面头部 -->
    </header>
    
    <main>
        页面内容
    </main>
    
    <footer>
        <!-- 页面底部 -->
    </footer>
</body>
</html>
```

### 文章布局
```html
---
layout: default
---
<article class="post">
    <header>
        <h1>文章标题</h1>
        <time>发布日期</time>
    </header>
    
    <div class="content">
        文章内容
    </div>
    
    <footer>
        <div class="categories">
            分类: 技术, 教程
        </div>
        <div class="tags">
            标签: jekyll, 博客
        </div>
    </footer>
</article>
```

## 数据文件

### _data 目录
```
_data/
├── authors.yml
├── navigation.yml
└── settings.yml
```

### 使用数据文件
```yaml
# _data/navigation.yml
main:
  - title: 首页
    url: /
  - title: 博客
    url: /blog/
  - title: 关于
    url: /about/
```

```html
<!-- 在模板中使用 -->
<nav>
    <a href="/">首页</a>
    <a href="/blog/">博客</a>
    <a href="/about/">关于</a>
</nav>
```

## 插件配置

### 常用插件

#### jekyll-feed
```yaml
# _config.yml
plugins:
  - jekyll-feed

# 生成RSS订阅
feed:
  path: feed.xml
```

#### jekyll-seo-tag
```yaml
# _config.yml
plugins:
  - jekyll-seo-tag

# SEO配置
title: "我的博客"
description: "个人技术博客"
author: "作者名"
```

#### jekyll-sitemap
```yaml
# _config.yml
plugins:
  - jekyll-sitemap

# 站点地图配置
sitemap:
  exclude: ['/admin/']
  include: ['/important-page/']
```

## 主题定制

### 自定义CSS
```scss
// _sass/_variables.scss
$primary-color: #007acc;
$font-family: 'Helvetica Neue', Arial, sans-serif;
$max-width: 1200px;
```

```scss
// _sass/main.scss
@import 'variables';

body {
    font-family: $font-family;
    color: #333;
}

.container {
    max-width: $max-width;
    margin: 0 auto;
    padding: 0 20px;
}
```

### 响应式设计
```scss
// 移动端优先
.container {
    width: 100%;
    padding: 0 15px;
}

// 平板
@media (min-width: 768px) {
    .container {
        max-width: 750px;
    }
}

// 桌面
@media (min-width: 992px) {
    .container {
        max-width: 970px;
    }
}
```

## 部署配置

### GitHub Pages
```yaml
# _config.yml
url: "https://username.github.io"
baseurl: "/repository-name"
```

### 自定义域名
```yaml
# _config.yml
url: "https://yourdomain.com"
baseurl: ""
```

### 部署脚本
```bash
#!/bin/bash
# deploy.sh

# 构建站点
bundle exec jekyll build

# 部署到服务器
rsync -avz _site/ user@server:/path/to/web/root/
```

## 性能优化

### 图片优化
```html
<!-- 使用WebP格式 -->
<picture>
    <source srcset="image.webp" type="image/webp">
    <img src="image.jpg" alt="描述">
</picture>
```

### 代码高亮
```yaml
# _config.yml
highlighter: rouge
markdown: kramdown
kramdown:
  syntax_highlighter: rouge
  syntax_highlighter_opts:
    block:
      line_numbers: false
```

### 缓存优化
```html
<!-- 添加缓存头 -->
<meta http-equiv="Cache-Control" content="max-age=31536000">
```

## 调试技巧

### 本地开发
```bash
# 启动开发服务器
bundle exec jekyll serve --livereload

# 增量构建
bundle exec jekyll serve --incremental

# 详细输出
bundle exec jekyll serve --verbose
```

### 调试信息
```liquid
<!-- 在模板中输出调试信息 -->
<pre>站点信息</pre>
<pre>页面信息</pre>
```

## 常见问题

### 1. 文章不显示
- 检查文件名格式：`YYYY-MM-DD-title.md`
- 确认Front Matter格式正确
- 检查`published`字段是否为`true`

### 2. 样式不生效
- 确认CSS文件路径正确
- 检查`_config.yml`中的样式配置
- 清除浏览器缓存

### 3. 插件不工作
- 确认插件已添加到`Gemfile`
- 运行`bundle install`
- 检查`_config.yml`中的插件配置

---

*最后更新: 2024-01-20*
