# NYC Taxi Governed Data Platform

## Project Overview
This project demonstrates an end-to-end data engineering platform built on AWS using
NYC Yellow Taxi trip data. The focus is on **data governance, MDM, data quality, and analytics-ready modeling**.

The platform simulates a real enterprise data lake with controlled ingestion,
quality gates, master data management, and dimensional modeling.

---

## Business Use Case
Enable reliable analytics on NYC taxi trips by:
- Governing location and vendor master data
- Preventing bad-quality data from reaching analytics
- Providing trusted, query-optimized datasets for reporting

---

## Architecture
See detailed architecture diagram:
- `docs/architecture/architecture.mmd`

Core components:
- Amazon S3 (data lake zones)
- AWS Glue (catalog + crawlers)
- Amazon Athena (SQL analytics)
- Data Quality validation layer
- Master Data Management (MDM)
- Step Functions orchestration (design)

