from concurrent.futures import ThreadPoolExecutor
from notion_client import Client


class NotionManager:
    def __init__(self, api_key, database_id):
        """
        Notion APIのクライアントを初期化し、データベースIDを設定する。
        """
        self.notion = Client(auth=api_key)
        self.database_id = database_id

    def add_article(self, title, url, name, date):
        """
        新しい記事をNotionデータベースに追加する。
        """
        new_page = {
            "Title": {"title": [{"text": {"content": title}}]},
            "Link": {"url": url},
            "Author": {"rich_text": [{"text": {"content": name}}]},
            "Date": {"date": {"start": date}}
        }
        self.notion.pages.create(parent={"database_id": self.database_id}, properties=new_page)

    def get_tags_and_remove_default_tag(self, tags) -> list:
        """
        提供されたタグのリストからデフォルトのタグ（`tech`, `idea`）を除外し、
        Notionに適合する形式のリストを返す。
        """
        notion_tags = []
        for tag in tags:
            if tag not in ["tech", "idea"]:
                notion_tags.append({"name": tag})
        return notion_tags

    def delete_page(self, page_id):
        """
        指定された`page_id`のページをNotionデータベースから削除（アーカイブ）する。
        """
        self.notion.pages.update(page_id=page_id, archived=True)

    def delete_all_pages(self):
        """
        データベース内の全ページを削除する。`ThreadPoolExecutor`を使用して並列削除を行う。
        """
        pages = self.notion.databases.query(database_id=self.database_id)
        with ThreadPoolExecutor() as executor:
            [executor.submit(self.delete_page, page['id']) for page in pages['results']]
