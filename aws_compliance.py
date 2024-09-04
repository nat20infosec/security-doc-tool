import argparse
import boto3
from utils.compliance_checks import (
    check_iam_mfa_enabled,
    check_iam_least_privilege,
    check_s3_public_access,
    check_ebs_encryption,
    check_cloudtrail_enabled,
    check_firewall_rules,
    check_security_groups
)
from utils.report_generator import generate_pdf_report, generate_markdown_report

# Function to set up AWS credentials using boto3 Session
def setup_aws_session():
    print("AWS credentials not configured. Please enter your AWS credentials.")
    aws_access_key = input("Enter AWS Access Key ID: ")
    aws_secret_key = input("Enter AWS Secret Access Key: ")
    aws_region = input("Enter AWS Region (default: us-east-1): ") or 'us-east-1'

    # Create a boto3 session with the input credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )
    return session

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='AWS Security Documentation Automation Tool')
    parser.add_argument('-f', '--framework', choices=['cis', 'nist', 'pci'], help='Compliance framework: cis, nist, pci', required=True)
    parser.add_argument('-o', '--output', choices=['pdf', 'markdown'], help='Output format: pdf or markdown', required=True)
    args = parser.parse_args()

    # Set up AWS session and boto3 clients
    session = boto3.Session()
    iam_client = session.client('iam')
    s3_client = session.client('s3')
    ec2_client = session.client('ec2')
    cloudtrail_client = session.client('cloudtrail')

    # Run compliance checks based on the selected framework
    results = []
    if args.framework == 'cis':
        print("Running CIS compliance checks...\n")
        results.extend(check_iam_mfa_enabled(iam_client))
        results.extend(check_s3_public_access(s3_client))
        results.extend(check_ebs_encryption(ec2_client))
        results.extend(check_security_groups(ec2_client))
        results.extend(check_cloudtrail_enabled(cloudtrail_client))
    elif args.framework == 'nist':
        print("Running NIST CSF compliance checks...\n")
        results.extend(check_iam_least_privilege(iam_client))
        results.extend(check_cloudtrail_enabled(cloudtrail_client))
    elif args.framework == 'pci':
        print("Running PCI DSS compliance checks...\n")
        results.extend(check_firewall_rules(ec2_client))
        results.extend(check_security_groups(ec2_client))

    # Output results in the chosen format
    if args.output == 'pdf':
        generate_pdf_report(results, args.framework)
    elif args.output == 'markdown':
        generate_markdown_report(results, args.framework)

if __name__ == "__main__":
    main()