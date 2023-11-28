import requests
from bs4 import BeautifulSoup
import pandas as pd


def crawl_and_parse(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        pull_requests = soup.find_all(
            "a",
            class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title",
        )

        data = []

        for pr in pull_requests:
            print(pr, "\n")
            data.append({"Title": pr.text.strip()})

        df = pd.DataFrame(data)
        print(df)

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


if __name__ == "__main__":
    github_url = "https://github.com/gunh0/whitehat-school-vulhub/pulls"
    crawl_and_parse(github_url)
