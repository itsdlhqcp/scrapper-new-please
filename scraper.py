from newsplease import NewsPlease

def main():
    urls = [
        'https://www.bbc.com/news/articles/ckgzez7mwl4o',
        'https://inshorts.com/news'
    ]

    articles = NewsPlease.from_urls(urls)

    for url, article in articles.items():
        if article:
            print(f"URL: {url}")
            print(f"Title: {article.title}")
            print(f"Authors: {article.authors}")
            print(f"Publish Date: {article.date_publish}")
            print(f"Text (first 200 chars): {article.maintext[:200]}...")
            print("-" * 30)
        else:
            print(f"Could not extract article from: {url}")
            print("-" * 30)

if __name__ == "__main__":
    main()
