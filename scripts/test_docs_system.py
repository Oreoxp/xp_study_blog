#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试动态文档系统
验证生成的数据文件和HTML片段是否正确
"""

import json
import yaml
from pathlib import Path


def test_data_files():
    """测试数据文件是否正确生成"""
    print("🔍 测试数据文件...")

    # 检查 _data 目录
    data_dir = Path("_data")
    if not data_dir.exists():
        print("❌ _data 目录不存在")
        return False

    # 检查 JSON 文件
    json_file = data_dir / "docs.json"
    if not json_file.exists():
        print("❌ docs.json 文件不存在")
        return False

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        print("✅ docs.json 文件读取成功")
    except Exception as e:
        print(f"❌ 无法读取 docs.json: {e}")
        return False

    # 检查 YAML 文件
    yaml_file = data_dir / "docs.yml"
    if not yaml_file.exists():
        print("❌ docs.yml 文件不存在")
        return False

    try:
        with open(yaml_file, "r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        print("✅ docs.yml 文件读取成功")
    except Exception as e:
        print(f"❌ 无法读取 docs.yml: {e}")
        return False

    # 验证数据结构
    required_keys = ["categories", "total_docs", "last_updated", "generated_by"]
    for key in required_keys:
        if key not in yaml_data:
            print(f"❌ 缺少必需的键: {key}")
            return False

    print(f"✅ 数据结构验证通过")
    print(f"   - 分类数量: {len(yaml_data['categories'])}")
    print(f"   - 文档总数: {yaml_data['total_docs']}")

    return True


def test_html_fragment():
    """测试HTML片段是否正确生成"""
    print("\n🔍 测试HTML片段...")

    html_file = Path("_includes/dynamic_docs.html")
    if not html_file.exists():
        print("❌ dynamic_docs.html 文件不存在")
        return False

    try:
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        # 检查是否包含必要的HTML元素
        required_elements = [
            "docs-category-card",
            "docs-category-header",
            "docs-list",
            "doc-item",
        ]

        for element in required_elements:
            if element not in html_content:
                print(f"❌ HTML中缺少元素: {element}")
                return False

        print("✅ HTML片段验证通过")
        return True

    except Exception as e:
        print(f"❌ 无法读取HTML文件: {e}")
        return False


def test_docs_directory():
    """测试文档目录结构"""
    print("\n🔍 测试文档目录结构...")

    docs_dir = Path("_docs")
    if not docs_dir.exists():
        print("❌ _docs 目录不存在")
        return False

    categories = []
    total_files = 0

    for item in docs_dir.iterdir():
        if item.is_dir():
            category_name = item.name
            md_files = list(item.glob("*.md"))
            categories.append((category_name, len(md_files)))
            total_files += len(md_files)

    print(f"✅ 文档目录结构验证通过")
    print(f"   - 分类数量: {len(categories)}")
    print(f"   - 文档总数: {total_files}")

    for category, count in categories:
        print(f"   - {category}: {count} 个文档")

    return True


def main():
    """主测试函数"""
    print("🧪 开始测试动态文档系统...\n")

    tests = [test_data_files, test_html_fragment, test_docs_directory]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ 测试失败: {e}")

    print(f"\n📊 测试结果: {passed}/{total} 通过")

    if passed == total:
        print("🎉 所有测试通过！动态文档系统工作正常。")
        return True
    else:
        print("⚠️  部分测试失败，请检查系统配置。")
        return False


if __name__ == "__main__":
    main()
