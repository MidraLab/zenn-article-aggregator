import requests
from datetime import datetime


class ZennScraper:
    def __init__(self, url):
        """
        ZennScraperクラスのコンストラクタ。
        指定したURLを初期化し、空の記事リストを作成する。

        Args:
            url (str): スクレイピングするZennのURL。
        """
        self.url = url
        self.articles = []

    def get_midra_lab_articles(self, usernames):
        base_url = "https://zenn.dev/api/articles"

        for username in usernames:
            response = requests.get(base_url, params={'username': username, 'order': 'latest'})
            if response.status_code == 200:
                data = response.json()
                for article in data["articles"]:
                    # 'publication'が存在し、その'name'が'midra_lab'であるか確認
                    if article.get("publication") and article["publication"].get("name") == "midra_lab":

                        # 日付の解析とフォーマット
                        published_at = article.get("published_at")
                        if published_at:
                            date_obj = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S.%f%z')
                            formatted_date = date_obj.strftime('%Y-%m-%d')
                        article_info = {
                            'title': article["title"],
                            'name': article["user"]["username"],
                            'url': f"https://zenn.dev{article['path']}",
                            'created_at': formatted_date
                        }
                        self.articles.append(article_info)

    def is_articles_empty(self):
        """
        記事リストが空かどうかを確認する。

        Returns:
            bool: リストが空の場合はTrue、それ以外の場合はFalse。
        """
        return len(self.articles) == 0
