---
layout: page
title: 分类
permalink: /categories/
---

<div class="categories-page">
  <h1>内容分类</h1>

  <!-- 文章分类 -->
  <section class="posts-section">
    <h2>📝 文章分类</h2>
    {% assign all_categories = "" | split: "" %}
    {% for post in site.posts %}
      {% for category in post.categories %}
        {% unless all_categories contains category %}
          {% assign all_categories = all_categories | push: category %}
        {% endunless %}
      {% endfor %}
    {% endfor %}
    
    {% assign sorted_categories = all_categories | sort %}
    
    {% if sorted_categories.size > 0 %}
      <div class="categories-list">
        {% for category_name in sorted_categories %}
          {% assign category_posts = site.posts | where_exp: "post", "post.categories contains category_name" %}
          <div class="category-item posts-category">
            <div class="category-header">
              <h3 class="category-title">
                <a href="#{{ category_name | slugify }}">{{ category_name }}</a>
                <span class="post-count">({{ category_posts.size }} 篇文章)</span>
              </h3>
            </div>
            
            <div class="category-posts">
              {% for post in category_posts %}
                <div class="post-item">
                  <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
                  <a href="{{ post.url }}" class="post-title">{{ post.title }}</a>
                </div>
              {% endfor %}
            </div>
          </div>
        {% endfor %}
      </div>
    {% else %}
      <p class="no-content">暂无分类文章</p>
    {% endif %}
  </section>
</div>

<style>
.categories-page {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem 0;
}

.categories-page h1 {
  color: var(--text-primary);
  margin-bottom: 2rem;
  text-align: center;
  font-size: 2.5rem;
}

.categories-page h2 {
  color: var(--text-primary);
  margin: 3rem 0 2rem 0;
  font-size: 1.8rem;
  border-bottom: 3px solid var(--primary-color);
  padding-bottom: 0.5rem;
}

.docs-section {
  margin-bottom: 4rem;
}

.categories-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.category-item {
  background: var(--bg-secondary);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  border-left: 4px solid var(--primary-color);
}

.category-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.docs-category {
  border-left-color: #10b981;
}

.posts-category {
  border-left-color: #3b82f6;
}

.category-header {
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.category-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.category-title a {
  color: inherit;
  text-decoration: none;
  font-weight: 600;
}

.category-title a:hover {
  text-decoration: underline;
}

.post-count {
  font-size: 0.9rem;
  color: var(--text-secondary);
  font-weight: normal;
}

.category-posts {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.post-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--border-color);
}

.post-item:last-child {
  border-bottom: none;
}

.post-item.more {
  font-style: italic;
}

.post-date {
  font-size: 0.85rem;
  color: var(--text-secondary);
  min-width: 80px;
}

.post-title {
  color: var(--text-primary);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.post-title:hover {
  color: var(--primary-color);
}

.no-content {
  text-align: center;
  color: var(--text-secondary);
  font-style: italic;
  padding: 2rem;
  background: var(--bg-secondary);
  border-radius: 8px;
}

@media (max-width: 768px) {
  .categories-page {
    padding: 1rem;
  }
  
  .categories-page h1 {
    font-size: 2rem;
  }
  
  .categories-page h2 {
    font-size: 1.5rem;
  }
  
  .category-item {
    padding: 1rem;
  }
  
  .category-title {
    font-size: 1.25rem;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
  }
  
  .post-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
  }
  
  .post-date {
    min-width: auto;
  }
}
</style>
