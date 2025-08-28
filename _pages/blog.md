---
layout: page
title: 博客文章
description: 所有博客文章列表
permalink: /blog/
---

# 博客文章

这里是我所有的博客文章，按时间倒序排列。

{% for post in site.posts %}
<article class="blog-post-item">
    <h2 class="post-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h2>
    <div class="post-meta">
        <span class="post-date">
            <i class="far fa-calendar-alt"></i>
            {{ post.date | date: "%Y年%m月%d日" }}
        </span>
        {% if post.categories %}
        <span class="post-categories">
            <i class="far fa-folder"></i>
            {% for category in post.categories %}
            <a href="{{ '/categories/' | relative_url }}#{{ category | slugify }}">{{ category }}</a>
            {% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </span>
        {% endif %}
        {% if post.tags %}
        <span class="post-tags">
            <i class="fas fa-tags"></i>
            {% for tag in post.tags %}
            <a href="{{ '/tags/' | relative_url }}#{{ tag | slugify }}">{{ tag }}</a>
            {% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </span>
        {% endif %}
    </div>
    <div class="post-excerpt">
        {% if post.excerpt %}
        {{ post.excerpt }}
        {% else %}
        {{ post.content | strip_html | truncatewords: 50 }}
        {% endif %}
    </div>
    <a href="{{ post.url | relative_url }}" class="read-more">阅读全文 →</a>
</article>
{% endfor %}

{% if site.posts.size == 0 %}
<div class="no-posts">
    <h3>暂无文章</h3>
    <p>我正在准备第一篇文章，敬请期待！</p>
</div>
{% endif %}
