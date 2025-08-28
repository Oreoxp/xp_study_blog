module Jekyll
  class DocsGenerator < Generator
    safe true
    priority :normal

    def generate(site)
      docs_dir = File.join(site.source, '_docs')
      return unless Dir.exist?(docs_dir)

      # 遍历_docs目录下的所有文件夹
      Dir.foreach(docs_dir) do |category|
        next if category == '.' || category == '..'
        
        category_path = File.join(docs_dir, category)
        next unless Dir.exist?(category_path)

        # 为每个分类创建页面
        create_category_page(site, category)
      end
    end

    private

    def create_category_page(site, category)
      # 创建分类页面
      category_page = PageWithoutAFile.new(site, site.source, '_docs', "#{category}/index.html")
      category_page.data = {
        'layout' => 'docs_category',
        'title' => category,
        'category' => category,
        'permalink' => "/docs/#{category}/"
      }
      category_page.content = generate_category_content(site, category)
      site.pages << category_page
    end

    def generate_category_content(site, category)
      category_path = File.join(site.source, '_docs', category)
      docs = []
      
      Dir.foreach(category_path) do |file|
        next if file == '.' || file == '..'
        next unless file.end_with?('.md')
        
        file_path = File.join(category_path, file)
        content = File.read(file_path)
        
        # 解析标题
        title = file.gsub('.md', '').gsub('-', ' ').capitalize
        if content.start_with?('# ')
          title = content.lines.first.gsub('# ', '').strip
        end
        
        docs << {
          'title' => title,
          'filename' => file,
          'url' => "/docs/#{category}/#{file.gsub('.md', '')}/"
        }
      end
      
      # 生成分类页面内容
      content = "# #{category}\n\n"
      content += "本分类包含以下文档：\n\n"
      
      docs.each do |doc|
        content += "- [#{doc['title']}](#{doc['url']})\n"
      end
      
      content
    end
  end

  class DocsData < Liquid::Tag
    def initialize(tag_name, text, tokens)
      super
      @text = text.strip
    end

    def render(context)
      site = context.registers[:site]
      docs_dir = File.join(site.source, '_docs')
      return '' unless Dir.exist?(docs_dir)

      categories = []
      
      Dir.foreach(docs_dir) do |category|
        next if category == '.' || category == '..'
        
        category_path = File.join(docs_dir, category)
        next unless Dir.exist?(category_path)

        docs = []
        Dir.foreach(category_path) do |file|
          next if file == '.' || file == '..'
          next unless file.end_with?('.md')
          
          file_path = File.join(category_path, file)
          content = File.read(file_path)
          
          # 解析标题
          title = file.gsub('.md', '').gsub('-', ' ').capitalize
          if content.start_with?('# ')
            title = content.lines.first.gsub('# ', '').strip
          end
          
          docs << {
            'title' => title,
            'filename' => file,
            'url' => "/docs/#{category}/#{file.gsub('.md', '')}/"
          }
        end
        
        categories << {
          'name' => category,
          'docs' => docs,
          'count' => docs.length
        }
      end
      
      categories.to_json
    end
  end
end

Liquid::Template.register_tag('docs_data', Jekyll::DocsData)
