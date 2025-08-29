#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档数据生成脚本
自动扫描_docs文件夹结构，生成分类和文档统计信息
"""

import os
import json
import yaml
from pathlib import Path
from datetime import datetime


def scan_docs_directory(docs_path="_docs"):
    """
    扫描文档目录，生成分类和文档信息

    Args:
        docs_path (str): 文档目录路径

    Returns:
        dict: 包含分类和文档信息的字典
    """
    docs_data = {
        "categories": [],
        "total_docs": 0,
        "last_updated": datetime.now().isoformat(),
        "generated_by": "generate_docs_data.py",
    }

    docs_path = Path(docs_path)
    if not docs_path.exists():
        print(f"警告: 文档目录 {docs_path} 不存在")
        return docs_data

    # 遍历文档目录
    for category_dir in docs_path.iterdir():
        if category_dir.is_dir():
            category_name = category_dir.name
            category_info = {
                "name": category_name,
                "path": str(category_dir.relative_to(docs_path)),
                "docs": [],
                "doc_count": 0,
            }

            # 扫描该分类下的所有文档
            for doc_file in category_dir.glob("*.md"):
                if doc_file.is_file():
                    # 读取文档的front matter
                    doc_info = extract_doc_info(doc_file)
                    category_info["docs"].append(doc_info)
                    category_info["doc_count"] += 1
                    docs_data["total_docs"] += 1

            # 按文档数量排序
            category_info["docs"].sort(key=lambda x: x.get("title", ""))
            docs_data["categories"].append(category_info)

    # 按分类名称排序
    docs_data["categories"].sort(key=lambda x: x["name"])

    return docs_data


def extract_doc_info(doc_file):
    """
    从Markdown文件中提取文档信息

    Args:
        doc_file (Path): 文档文件路径

    Returns:
        dict: 文档信息字典
    """
    doc_info = {
        "filename": doc_file.stem,
        "title": doc_file.stem,
        "description": "",
        "path": str(doc_file.relative_to(Path("_docs"))),
        "url": f"/docs/{doc_file.stem}/",
    }

    try:
        with open(doc_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 尝试提取front matter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                front_matter = parts[1].strip()
                try:
                    # 解析YAML front matter
                    metadata = yaml.safe_load(front_matter)
                    if metadata:
                        doc_info["title"] = metadata.get("title", doc_file.stem)
                        doc_info["description"] = metadata.get("description", "")
                        # 确保日期是字符串格式
                        date_value = metadata.get("date", "")
                        if date_value:
                            if hasattr(date_value, "isoformat"):
                                doc_info["date"] = date_value.isoformat()
                            else:
                                doc_info["date"] = str(date_value)
                        else:
                            doc_info["date"] = ""
                        doc_info["tags"] = metadata.get("tags", [])
                except yaml.YAMLError:
                    pass
    except Exception as e:
        print(f"警告: 无法读取文件 {doc_file}: {e}")

    return doc_info


def generate_jekyll_data(docs_data, output_dir="_data"):
    """
    生成Jekyll数据文件

    Args:
        docs_data (dict): 文档数据
        output_dir (str): 输出目录
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # 生成JSON格式的数据文件
    json_file = output_path / "docs.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(docs_data, f, ensure_ascii=False, indent=2)

    # 生成YAML格式的数据文件（Jekyll更常用）
    yaml_file = output_path / "docs.yml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(
            docs_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
        )

    print(f"✅ 已生成数据文件:")
    print(f"   - {json_file}")
    print(f"   - {yaml_file}")


def generate_dynamic_index(docs_data, output_file="_includes/dynamic_docs.html"):
    """
    生成动态的文档HTML片段

    Args:
        docs_data (dict): 文档数据
        output_file (str): 输出文件路径
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    html_content = []
    html_content.append("<!-- 动态生成的文档内容 - 由generate_docs_data.py自动生成 -->")
    html_content.append("<!-- 最后更新: {} -->".format(docs_data["last_updated"]))
    html_content.append("")

    for category in docs_data["categories"]:
        html_content.append('<div class="docs-category-card">')
        html_content.append('    <div class="docs-category-header">')
        html_content.append(f'        <h3>{category["name"]}</h3>')
        html_content.append(
            f'        <span class="docs-count">{category["doc_count"]} 个文档</span>'
        )
        html_content.append("    </div>")
        html_content.append('    <div class="docs-list">')

        for doc in category["docs"]:
            html_content.append(f'        <a href="{doc["url"]}" class="doc-item">')
            html_content.append(
                f'            <span class="doc-title">{doc["title"]}</span>'
            )
            if doc["description"]:
                html_content.append(
                    f'            <span class="doc-description">{doc["description"]}</span>'
                )
            else:
                html_content.append(
                    f'            <span class="doc-description">{doc["title"]}相关文档</span>'
                )
            html_content.append("        </a>")

        html_content.append("    </div>")
        html_content.append('    <div class="docs-category-footer">')
        html_content.append(
            f'        <a href="/docs/{category["path"]}/" class="btn btn-outline">查看全部</a>'
        )
        html_content.append("    </div>")
        html_content.append("</div>")
        html_content.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))

    print(f"✅ 已生成动态HTML文件: {output_path}")


def main():
    """主函数"""
    print("🚀 开始扫描文档目录...")

    # 扫描文档目录
    docs_data = scan_docs_directory()

    print(f"📊 扫描完成:")
    print(f"   - 发现 {len(docs_data['categories'])} 个分类")
    print(f"   - 总计 {docs_data['total_docs']} 个文档")

    for category in docs_data["categories"]:
        print(f"   - {category['name']}: {category['doc_count']} 个文档")

    # 生成Jekyll数据文件
    generate_jekyll_data(docs_data)

    # 生成动态HTML片段
    generate_dynamic_index(docs_data)

    print("🎉 文档数据生成完成！")


if __name__ == "__main__":
    main()
