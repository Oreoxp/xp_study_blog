---
layout: page
title: 标签
description: 按标签浏览所有文章
permalink: /tags/
---

# 标签

按标签浏览所有文章：

{% assign tags = site.tags | sort %}
{% for tag in tags %}
<section class="tag-section">
    <h2 id="{{ tag[0] | slugify }}" class="tag-title">
        <i class="fas fa-tag"></i>
        {{ tag[0] }}
        <span class="tag-count">({{ tag[1].size }})</span>
    </h2>
    <div class="tag-posts">
        {% for post in tag[1] %}
        <article class="tag-post-item">
            <h3 class="post-title">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            <div class="post-meta">
                <span class="post-date">
                    <i class="far fa-calendar-alt"></i>
                    {{ post.date | date: "%Y年%m月%d日" }}
                </span>
            </div>
            <div class="post-excerpt">
                {% if post.excerpt %}
                {{ post.excerpt }}
                {% else %}
                {{ post.content | strip_html | truncatewords: 30 }}
                {% endif %}
            </div>
        </article>
        {% endfor %}
    </div>
</section>
{% endfor %}

{% if site.tags.size == 0 %}
<div class="no-tags">
    <h3>暂无标签</h3>
    <p>文章还没有添加标签，敬请期待！</p>
</div>
{% endif %}
