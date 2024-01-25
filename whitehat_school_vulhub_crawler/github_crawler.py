import requests
from bs4 import BeautifulSoup
import pandas as pd


def crawl_and_parse(url, max_pages=6):
    data = []

    for page in range(1, max_pages + 1):
        page_url = f"{url}?page={page}&q=is%3Apr+is%3Aopen"
        response = requests.get(page_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            pull_requests = soup.find_all(
                "a",
                class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title",
            )

            for pr in pull_requests:
                print(pr, "\n")
                data.append({"Title": pr.text.strip()})

        else:
            print(
                f"Failed to retrieve data from page {page}. Status code: {response.status_code}"
            )

    df = pd.DataFrame(data)
    df.to_csv("result.csv", index=False)
    print(df)


if __name__ == "__main__":
    github_url = "https://github.com/gunh0/whitehat-school-vulhub/pulls"
    crawl_and_parse(github_url, max_pages=10)
