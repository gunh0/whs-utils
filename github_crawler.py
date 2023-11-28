import requests
from bs4 import BeautifulSoup
import pandas as pd


def crawl_and_parse(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        pull_requests = soup.find_all(
            "div", class_="flex-auto min-width-0 p-2 pr-3 pr-md-2"
        )

        data = []

        for pr in pull_requests:
            title = pr.find("a", class_="Link--primary")["title"]
            number = pr.find("span", class_="opened-by").text.split("#")[1].split()[0]
            opened_by = pr.find("a", class_="Link--muted").text.strip()
            opened_at = pr.find("relative-time")["datetime"]

            data.append(
                {
                    "Number": number,
                    "Title": title,
                    "Opened By": opened_by,
                    "Opened At": opened_at,
                }
            )

        df = pd.DataFrame(data)
        print(df)

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


if __name__ == "__main__":
    github_url = "https://github.com/gunh0/whitehat-school-vulhub/pulls"
    crawl_and_parse(github_url)
