# PCI DSS Compliance Report

This report provides the current compliance status of your AWS environment based on the PCI DSS standards.

---

## Control: PCI DSS 1.1 - Ensure firewall and router configurations restrict traffic from untrusted networks

- **Resource:** {{firewall_resource_name}}
- **Status:** {{firewall_status}}
- **Detail:** {{firewall_detail}}

---

## Control: PCI DSS 3.2 - Ensure cardholder data is not stored unless absolutely necessary

- **Resource:** {{data_storage_resource_name}}
- **Status:** {{data_storage_status}}
- **Detail:** {{data_storage_detail}}

---

## Control: PCI DSS 6.1 - Ensure Security Groups do not allow unrestricted access

- **Resource:** {{sg_resource_name}}
- **Status:** {{sg_status}}
- **Detail:** {{sg_detail}}

---

## Control: PCI DSS 10.5 - Ensure CloudTrail is enabled for logging

- **Resource:** {{cloudtrail_resource_name}}
- **Status:** {{cloudtrail_status}}
- **Detail:** {{cloudtrail_detail}}

---

## Control: PCI DSS 12.1 - Ensure an incident response plan is in place

- **Resource:** {{incident_response_name}}
- **Status:** {{incident_response_status}}
- **Detail:** {{incident_response_detail}}

---

## Summary:

Ensure that any failed controls listed in this report are addressed to maintain compliance with the PCI DSS standards and protect sensitive cardholder data.