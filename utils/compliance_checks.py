# CIS Control 1.1 - Ensure MFA is enabled for all IAM users
def check_iam_mfa_enabled(iam_client):
    results = []
    users = iam_client.list_users()

    for user in users['Users']:
        user_name = user['UserName']
        mfa_devices = iam_client.list_mfa_devices(UserName=user_name)
        if not mfa_devices['MFADevices']:
            results.append({
                'control': 'CIS 1.1',
                'resource': f'IAM User {user_name}',
                'status': 'Fail',
                'detail': 'MFA not enabled'
            })
        else:
            results.append({
                'control': 'CIS 1.1',
                'resource': f'IAM User {user_name}',
                'status': 'Pass',
                'detail': 'MFA enabled'
            })
    return results

# NIST CSF Control - Identify IAM roles following least privilege principles
def check_iam_least_privilege(iam_client):
    results = []
    roles = iam_client.list_roles()

    for role in roles['Roles']:
        role_name = role['RoleName']
        policies = iam_client.list_attached_role_policies(RoleName=role_name)
        for policy in policies['AttachedPolicies']:
            policy_arn = policy['PolicyArn']
            document = iam_client.get_policy(PolicyArn=policy_arn)
            if '*' in document['PolicyVersion']['Document']['Statement'][0]['Action']:
                results.append({
                    'control': 'NIST ID.AM-2',
                    'resource': f'IAM Role {role_name}',
                    'status': 'Fail',
                    'detail': 'Overly permissive policy'
                })
            else:
                results.append({
                    'control': 'NIST ID.AM-2',
                    'resource': f'IAM Role {role_name}',
                    'status': 'Pass',
                    'detail': 'Least privilege policy'
                })
    return results

# CIS Control 3.1 - Ensure no S3 buckets allow public access
def check_s3_public_access(s3_client):
    results = []
    buckets = s3_client.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        acl = s3_client.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            if 'URI' in grant['Grantee'] and 'AllUsers' in grant['Grantee']['URI']:
                results.append({
                    'control': 'CIS 3.1',
                    'resource': f'S3 Bucket {bucket_name}',
                    'status': 'Fail',
                    'detail': 'Publicly accessible'
                })
            else:
                results.append({
                    'control': 'CIS 3.1',
                    'resource': f'S3 Bucket {bucket_name}',
                    'status': 'Pass',
                    'detail': 'Not publicly accessible'
                })
    return results

# PCI DSS Control 1.1 - Ensure firewall and router configurations restrict traffic from untrusted networks
def check_firewall_rules(ec2_client):
    results = []
    security_groups = ec2_client.describe_security_groups()

    for sg in security_groups['SecurityGroups']:
        sg_name = sg['GroupName']
        for rule in sg['IpPermissions']:
            for ip_range in rule.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    results.append({
                        'control': 'PCI DSS 1.1',
                        'resource': f'Security Group {sg_name}',
                        'status': 'Fail',
                        'detail': f'Open to 0.0.0.0/0 for {rule["IpProtocol"]} on port {rule.get("FromPort")}'
                    })
                else:
                    results.append({
                        'control': 'PCI DSS 1.1',
                        'resource': f'Security Group {sg_name}',
                        'status': 'Pass',
                        'detail': 'Restricted access'
                    })
    return results

# PCI DSS Control 6.1 - Ensure Security Groups do not allow unrestricted access
def check_security_groups(ec2_client):
    results = []
    security_groups = ec2_client.describe_security_groups()

    for sg in security_groups['SecurityGroups']:
        sg_name = sg['GroupName']
        for rule in sg['IpPermissions']:
            for ip_range in rule.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    results.append({
                        'control': 'PCI DSS 6.1',
                        'resource': f'Security Group {sg_name}',
                        'status': 'Fail',
                        'detail': f'Open to 0.0.0.0/0 for {rule["IpProtocol"]} on port {rule.get("FromPort")}'
                    })
                else:
                    results.append({
                        'control': 'PCI DSS 6.1',
                        'resource': f'Security Group {sg_name}',
                        'status': 'Pass',
                        'detail': 'Restricted access'
                    })
    return results

# CIS Control 4.1 - Ensure EBS volumes are encrypted
def check_ebs_encryption(ec2_client):
    results = []
    volumes = ec2_client.describe_volumes()

    for volume in volumes['Volumes']:
        if not volume.get('Encrypted', False):
            results.append({
                'control': 'CIS 4.1',
                'resource': f'EBS Volume {volume["VolumeId"]}',
                'status': 'Fail',
                'detail': 'EBS volume is not encrypted'
            })
        else:
            results.append({
                'control': 'CIS 4.1',
                'resource': f'EBS Volume {volume["VolumeId"]}',
                'status': 'Pass',
                'detail': 'EBS volume is encrypted'
            })
    return results

# NIST CSF Control - Ensure CloudTrail is enabled
def check_cloudtrail_enabled(cloudtrail_client):
    results = []
    trails = cloudtrail_client.describe_trails()

    if not trails['trailList']:
        results.append({
            'control': 'NIST DE.CM-1',
            'resource': 'CloudTrail',
            'status': 'Fail',
            'detail': 'CloudTrail is not enabled in any region'
        })
    else:
        for trail in trails['trailList']:
            trail_name = trail['Name']
            results.append({
                'control': 'NIST DE.CM-1',
                'resource': f'CloudTrail {trail_name}',
                'status': 'Pass',
                'detail': 'CloudTrail is enabled'
            })
    return results