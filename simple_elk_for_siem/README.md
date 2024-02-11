# Simple ELK Stack for SIEM (Docker Compose)

This Docker Compose file, named `docker-compose.yml`, serves as a utility for setting up a simple ELK stack for SIEM purposes.

### Overview

This `docker-compose.yml`` file is used to set up a simple ELK (Elasticsearch, Logstash, Kibana) stack for Security Information and Event Management (SIEM) purposes. This configuration provides an effective solution for security log analysis, real-time data monitoring, and visualization.

### Components

`Elasticsearch` : A distributed search engine for data storage and retrieval.
`Kibana` : A web interface for data visualization and dashboarding.
`Logstash` : A data processing pipeline that ingests data from various sources and transforms it.
`Metricbeat` : A lightweight shipper for collecting metrics from your systems and services.
`Filebeat` : A lightweight shipper for forwarding and centralizing log data.
`Fleet Server` : Manages Elastic Agents centrally.

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
