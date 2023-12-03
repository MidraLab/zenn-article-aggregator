import asyncio
from dotenv import load_dotenv
import os
import sys

from zenn_scraper import ZennScraper
from notion_manager import NotionManager


async def main():
    load_dotenv()

    notion_api_key = os.environ["MIDRA_LAB_NOTION_API"]
    notion_database_id = os.environ["NOTION_DATABASE_ID"]
    print(f"{notion_api_key}, {notion_database_id}")
    # TODO: 使用者によって変更する
    usernames = ["keisuke114", "ayousanz"]

    publication_url = "https://zenn.dev/p/midra_lab"

    zenn_scraper = ZennScraper(publication_url)
    zenn_scraper.get_midra_lab_articles(usernames)

    if zenn_scraper.is_articles_empty():
        print("記事がありません。")
        sys.exit()

    notion_manager = NotionManager(notion_api_key, notion_database_id)
    notion_manager.delete_all_pages()

    for article in zenn_scraper.articles:
        notion_manager.add_article(article['title'], article['url'], article['name'], article['created_at'])


# 非同期イベントループを使用してmain関数を実行
asyncio.run(main())
