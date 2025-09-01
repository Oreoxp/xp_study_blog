import os
import yaml

# --- 配置 ---
DOCS_DIR = 'docs'
DATA_DIR = '_data'
OUTPUT_FILE = os.path.join(DATA_DIR, 'navigation.yml')

def generate_nav_item(path, base_dir):
    """根据文件或目录路径递归生成导航项"""
    name = os.path.splitext(os.path.basename(path))[0].replace('-', ' ').replace('_', ' ').title()
    
    # 计算相对路径（相对于 docs 目录）
    relative_path = os.path.relpath(os.path.join(base_dir, path), DOCS_DIR).replace('\\', '/')
    
    # 如果是目录，则递归
    if os.path.isdir(os.path.join(base_dir, path)):
        children = []
        for item in sorted(os.listdir(os.path.join(base_dir, path))):
            if item.endswith('.md') or os.path.isdir(os.path.join(base_dir, path, item)):
                child_item = generate_nav_item(item, os.path.join(base_dir, path))
                if child_item:
                    children.append(child_item)
        
        # 如果目录下没有有效的子项，返回 None
        if not children:
            return None
        
        return {'title': name, 'children': children}
    
    # 如果是 Markdown 文件
    elif path.endswith('.md'):
        # 生成正确的 Jekyll URL
        # Jekyll 会在 _site/docs/ 下生成文件，所以 URL 需要包含 /docs/ 前缀
        url_path = '/docs/' + relative_path.replace('.md', '') + '/'
        return {'title': name, 'url': url_path}
    
    return None

def main():
    """主函数，生成导航数据文件"""
    print("🚀 开始自动生成导航...")

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    navigation_data = []
    for item in sorted(os.listdir(DOCS_DIR)):
        # 只处理 Markdown 文件和目录
        full_path = os.path.join(DOCS_DIR, item)
        if item.endswith('.md') or os.path.isdir(full_path):
            nav_item = generate_nav_item(item, DOCS_DIR)
            if nav_item:
                navigation_data.append(nav_item)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(navigation_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"✅ 导航数据生成完毕，已保存到 {OUTPUT_FILE}")
    print("📁 生成的导航结构：")
    print_nav_structure(navigation_data, 0)

def print_nav_structure(nav_items, level):
    """打印导航结构，用于调试"""
    indent = "  " * level
    for item in nav_items:
        if 'children' in item:
            print(f"{indent}📁 {item['title']}")
            print_nav_structure(item['children'], level + 1)
        else:
            print(f"{indent}📄 {item['title']} -> {item['url']}")

if __name__ == "__main__":
    main()