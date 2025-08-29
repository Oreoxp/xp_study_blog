#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试生成的文档URL是否正确
"""

import yaml
from pathlib import Path


def test_docs_urls():
    """测试文档URL格式"""
    print("🔍 测试文档URL格式...")

    # 读取生成的文档数据
    yaml_file = Path("_data/docs.yml")
    if not yaml_file.exists():
        print("❌ docs.yml 文件不存在")
        return False

    try:
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ 无法读取 docs.yml: {e}")
        return False

    # 检查URL格式
    expected_format = "/docs/文档名/"
    issues = []

    for category in data.get("categories", []):
        for doc in category.get("docs", []):
            url = doc.get("url", "")
            title = doc.get("title", "")

            # 检查URL格式
            if not url.startswith("/docs/"):
                issues.append(f"❌ {title}: URL格式错误，应该是 /docs/开头")
            elif not url.endswith("/"):
                issues.append(f"❌ {title}: URL应该以 / 结尾")
            elif url.count("/") != 3:  # /docs/文档名/
                issues.append(f"❌ {title}: URL格式应该是 {expected_format}")
            else:
                print(f"✅ {title}: {url}")

    if issues:
        print("\n⚠️  发现的问题:")
        for issue in issues:
            print(f"   {issue}")
        return False

    print("\n✅ 所有URL格式正确！")
    return True


def test_jekyll_compatibility():
    """测试Jekyll兼容性"""
    print("\n🔍 测试Jekyll兼容性...")

    # 检查必要的文件
    required_files = [
        "_layouts/docs_page.html",
        "_data/docs.yml",
        "_includes/dynamic_docs.html",
    ]

    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path} 存在")
        else:
            print(f"❌ {file_path} 不存在")
            return False

    # 检查Jekyll配置
    config_file = Path("_config.yml")
    if config_file.exists():
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config_content = f.read()

            required_configs = [
                "collections:",
                "docs:",
                "output: true",
                "permalink: /docs/:title/",
                'layout: "docs_page"',
            ]

            for config in required_configs:
                if config in config_content:
                    print(f"✅ Jekyll配置: {config}")
                else:
                    print(f"❌ Jekyll配置缺少: {config}")
                    return False
        except Exception as e:
            print(f"❌ 无法读取Jekyll配置: {e}")
            return False

    print("✅ Jekyll配置检查通过！")
    return True


def main():
    """主函数"""
    print("🧪 开始测试文档URL和Jekyll兼容性...\n")

    tests = [test_docs_urls, test_jekyll_compatibility]

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
        print("🎉 所有测试通过！文档系统应该能正常工作。")
        print("\n💡 下一步:")
        print("   1. 运行 'bundle exec jekyll serve' 启动本地服务器")
        print("   2. 访问 http://localhost:4000/xp_study_blog/")
        print("   3. 测试文档链接是否正常工作")
    else:
        print("❌ 部分测试失败，请检查上述问题。")

    return passed == total


if __name__ == "__main__":
    main()
