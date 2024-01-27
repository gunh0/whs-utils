# WhiteHat School Utilities

**Latest Checked: November 2023**

Essential utilities for mentors conducting classes in the WhiteHat School education program.

<br/>

## WhiteHat School's Simple ELK Stack for SIEM (Docker Compose)

This Docker Compose file, named `docker-compose.yml`, serves as a utility for setting up a simple ELK stack for SIEM purposes.

### Overview

This `docker-compose.yml`` file is used to set up a simple ELK (Elasticsearch, Logstash, Kibana) stack for Security Information and Event Management (SIEM) purposes. This configuration provides an effective solution for security log analysis, real-time data monitoring, and visualization.

### Components

Elasticsearch : A distributed search engine for data storage and retrieval.
Kibana: A web interface for data visualization and dashboarding.
Logstash : A data processing pipeline that ingests data from various sources and transforms it.
Metricbeat : A lightweight shipper for collecting metrics from your systems and services.
Filebeat : A lightweight shipper for forwarding and centralizing log data.
Fleet Server: Manages Elastic Agents centrally.

### Usage

Create a .env file and set the necessary environment variables (ELASTIC_PASSWORD, KIBANA_PASSWORD, etc.).
Start the stack using Docker Compose:

```bash
docker-compose up -d
```

Access the Elasticsearch cluster through Kibana and manage configurations for Logstash, Metricbeat, Filebeat, etc.

### Notes

-   This stack is suitable for development and testing purposes. Additional security and performance optimizations may be required for production environments.
-   Ports for Elasticsearch and Kibana can be configured in the `.env` file.
-   Fleet Server can be used for central management of Elastic Agents.

<br/>

## WhiteHat School's Vulhub GitHub Crawler

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
