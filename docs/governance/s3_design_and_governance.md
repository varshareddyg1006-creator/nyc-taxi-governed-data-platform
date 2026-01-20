# S3 Design & Governance – Day 2

## Bucket Strategy
- Single bucket used as a data lake
- Logical separation using prefixes instead of multiple buckets

## Prefixes
- landing-raw: raw ingested data
- validated: quality-checked data
- curated: analytics-ready data
- master: MDM golden records
- dq-results: data quality outputs
- audit: lineage and execution logs

## Metadata Strategy
- Technical metadata: schema via Glue Catalog
- Business metadata: owner, steward, classification
- Operational metadata: quality rules, lineage

## Security
- Bucket versioning enabled
- Server-side encryption (SSE-S3)
- Public access blocked
- IAM-based access via AWS CloudShell

