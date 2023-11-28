# WhiteHat School Utilities

**Latest Checked: November 2023**

Essential utilities for mentors conducting classes in the WhiteHat School education program.

<br/>

## Overview

This Python script, named `github_crawler.py`, serves as a utility for crawling and parsing information from the GitHub repository of WhiteHat School's Vulhub project. The script extracts data about open Pull Requests, specifically focusing on the titles of these requests.

The goal is to collect the list of 'Pull Requests' from the repository 'https://github.com/gunh0/whitehat-school-vulhub' and identify names using regular expressions.

Set up a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

-   On Windows:

```bash
.\venv\Scripts\activate
```

-   On macOS/Linux:

```bash
source venv/bin/activate
```

Install required libraries from the requirements.txt file:

```bash
pip install -r requirements.txt
```

-   Ensure that you have the required Python libraries installed in your virtual environment before running the script.
-   The script's latest update was in November 2023.

Feel free to use, modify, and enhance this utility according to your needs.
