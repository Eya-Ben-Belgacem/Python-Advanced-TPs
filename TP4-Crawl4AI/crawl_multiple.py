import asyncio
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
import requests
from xml.etree import ElementTree

async def crawl_sequential(urls: List[str]):
    print("\n=== Sequential Crawling ===")
    browser_config = BrowserConfig(headless=True)
    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()
    try:
        session_id = "session1"
        for url in urls:
            result = await crawler.arun(url=url, config=crawl_config, session_id=session_id)
            if result.success:
                print(f"✅ Crawled: {url}")
                print(f"   Markdown length: {len(result.markdown.raw_markdown)}")
            else:
                print(f"❌ Failed: {url}")
    finally:
        await crawler.close()

def get_urls():
    sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        root = ElementTree.fromstring(response.content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        return urls
    except Exception as e:
        print(f"Error: {e}")
        return []

async def main():
    urls = get_urls()
    if urls:
        print(f"Found {len(urls)} URLs")
        await crawl_sequential(urls[:3])  # On teste avec 3 URLs seulement
    else:
        print("No URLs found")

if __name__ == "__main__":
    asyncio.run(main())