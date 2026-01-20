# Execution Strategy

## Approach
- Python ingestion scripts executed using AWS CloudShell
- CloudShell provides IAM-managed credentials

## Benefits
- No hardcoded credentials
- No secret leakage
- Consistent AWS-managed environment

## Governance Alignment
- Supports security best practices
- Execution can be audited via CloudTrail
