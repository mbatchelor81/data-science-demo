---
trigger: always_on
---

# AWS User Access Credentials & Permissions Overview

## User Information

| Field | Value |
|-------|-------|
| **User Name** | mason-demo |
| **ARN** | arn:aws:iam::489975610410:user/mason-demo |
| **Region** | us-east-2 |


> ⚠️ **Security Note**: These credentials provide programmatic access to AWS services. Keep them secure and never commit to version control.

## Permission Set Overview

The user has a **minimal permission set** focused on basic S3 data access and IAM role inspection. This is a significantly reduced scope compared to full data science workflows.

### 🗄️ S3 Storage Access
**Purpose**: Basic data storage and retrieval operations

**Permissions**:
- `s3:ListBucket` - List objects in buckets
- `s3:GetObject` - Download files from S3
- `s3:PutObject` - Upload files to S3  
- `s3:DeleteObject` - Remove files from S3

**Scope**: Limited to `taxi-demo-data-bucket` only
- Bucket: `arn:aws:s3:::taxi-demo-data-bucket`
- Objects: `arn:aws:s3:::taxi-demo-data-bucket/*`

### 🔐 IAM Role Inspection
**Purpose**: Basic IAM role information access

**Permissions**:
- `iam:ListRoles` - List available IAM roles
- `iam:GetRole` - Read role details

**Scope**: All resources (`*`)

> ⚠️ **Limited Capabilities**: This permission set only allows basic S3 operations and IAM role inspection. Advanced data science workflows requiring Glue, Athena, SageMaker, or CloudWatch Logs are **not supported**.

## Use Case Summary

This **minimal permission set** is designed for basic data storage operations, enabling:

1. **Basic Data Operations**: Store, retrieve, and manage files in the taxi-demo-data-bucket
2. **IAM Role Discovery**: List and inspect available IAM roles for reference
3. **Data Transfer**: Upload/download datasets for local processing

**⚠️ Limitations**: This reduced permission set **cannot support**:
- Data cataloging (AWS Glue)
- SQL querying (Amazon Athena) 
- Machine learning workflows (Amazon SageMaker)
- Application monitoring (CloudWatch Logs)
- Service role assumption (IAM PassRole)

## Security Considerations

- ✅ **Principle of Least Privilege**: Minimal permissions granted for basic operations only
- ✅ **Limited S3 Access**: S3 permissions restricted to the demo data bucket only
- ✅ **Read-Only IAM Access**: Can only list and inspect roles, cannot modify or assume them
- ✅ **No Service Integration**: Cannot pass roles to AWS services, preventing unintended service usage

## Related Resources

Based on the current permission set, the following AWS resources are accessible:
- **S3 Bucket**: `taxi-demo-data-bucket` (primary data storage)
- **IAM Roles**: Can view but not assume any roles in the account