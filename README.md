# Security Documentation Automation Tool

## Overview

The Security Documentation Automation Tool automates the generation of security compliance documentation for AWS environments, based on CIS AWS Foundations Benchmark, NIST Cybersecurity Framework (CSF), and PCI DSS standards.

## Features

- Supports CIS, NIST CSF, and PCI DSS frameworks
- Scans AWS services like S3, IAM, EC2, and CloudTrail
- Generates reports in PDF or Markdown format

## Prerequisites

- Python 3.x
- AWS credentials (set as environment variables or provided at runtime)
- AWS IAM Permissions (minimal policy found in `policies/security_doc_tool_iam_policy.json`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nat20infosec/security-doc-tool.git
    cd security-doc-tool
    ```

2. Set up a virtual environment (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python aws_compliance.py --framework <cis|nist|pci> --output <pdf|markdown>