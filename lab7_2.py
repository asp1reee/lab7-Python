import requests


def fetch_news(
    api_key, query="автомобили", from_date="2025-02-19",
    sort_by="publishedAt", page_size=5
):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "sortBy": sort_by,
        "pageSize": page_size,
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return None


def display_news(news_data):
    if news_data and "articles" in news_data:
        for article in news_data["articles"]:
            print("\n=== Новость ===")
            print(f"Источник: {article['source']['name']}")
            print(f"Автор: {article.get('author', 'Не указан')}")
            print(f"Заголовок: {article['title']}")
            print(f"Описание: {article.get('description', 'Нет описания')}")
            print(f"Ссылка: {article['url']}")
            print(f"Дата публикации: {article['publishedAt']}")
    else:
        print("Нет данных для отображения.")


if __name__ == "__main__":
    api_key = "5ab1e3a8bcc1445b85db36226c5ea467"
    news = fetch_news(api_key)
    display_news(news)
