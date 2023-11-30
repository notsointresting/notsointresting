import requests
import json
import os

def get_news_data(api_key):
    # Fetch news data from the News API
    news_url = ('https://newsapi.org/v2/top-headlines?'
                'q=Artificial Intelligence&'
                f'apiKey={api_key}')

    news_response = requests.get(news_url)
    news_data = news_response.json()

    # Check if the request was successful
    if news_response.status_code == 200 and news_data['status'] == 'ok':
        articles = news_data['articles']
        return articles
    else:
        return None

if __name__ == '__main__':
    # Retrieve API key from environment variable
    api_key = os.environ.get('API_KEY')

    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")

    # Fetch news data
    news_data = get_news_data(api_key)

    if news_data:
        # Print or process news data as needed
        print(json.dumps(news_data, indent=2))
    else:
        print("Error fetching news data")
