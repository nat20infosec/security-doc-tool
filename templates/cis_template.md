# CIS AWS Foundations Benchmark Compliance Report

This report provides the current compliance status of your AWS environment based on the CIS AWS Foundations Benchmark.

---

## Control: CIS 1.1 - Ensure MFA is enabled for all IAM users

- **Resource:** {{iam_mfa_resource}}
- **Status:** {{iam_mfa_status}}
- **Detail:** {{iam_mfa_detail}}

---

## Control: CIS 2.1 - Ensure CloudTrail is enabled in all regions

- **Resource:** {{cloudtrail_resource}}
- **Status:** {{cloudtrail_status}}
- **Detail:** {{cloudtrail_detail}}

---

## Control: CIS 3.1 - Ensure no S3 buckets allow public access

- **Resource:** {{s3_resource_name}}
- **Status:** {{s3_status}}
- **Detail:** {{s3_detail}}

---

## Control: CIS 3.2 - Ensure CloudTrail logs are encrypted at rest

- **Resource:** {{cloudtrail_s3_encryption_resource}}
- **Status:** {{cloudtrail_s3_encryption_status}}
- **Detail:** {{cloudtrail_s3_encryption_detail}}

---

## Control: CIS 4.1 - Ensure EBS volumes are encrypted

- **Resource:** {{ebs_resource_name}}
- **Status:** {{ebs_status}}
- **Detail:** {{ebs_detail}}

---

## Control: CIS 5.1 - Ensure security groups do not allow unrestricted access

- **Resource:** {{sg_resource_name}}
- **Status:** {{sg_status}}
- **Detail:** {{sg_detail}}

---

## Summary:

This report outlines the results of each CIS control check for your AWS environment. Make sure to address any failed controls to ensure compliance with the CIS benchmark.