# As-Is Process: Manual Invoice Processing

## Overview
This document outlines the current manual process for handling vendor invoices. The process involves receiving invoices via email, manually extracting data, validating against purchase orders, and entering data into the ERP system.

## Process Details

### 1. Inbound Receipt
- **Role:** Accounts Payable (AP) Clerk
- **Description:** Invoices are received via a shared email inbox (`invoices@company.com`) as PDF or Excel attachments.
- **Volume:** ~500 invoices per week.
- **Pain Point:** High volume leads to overlooked emails and delayed processing.

### 2. Data Extraction
- **Role:** AP Clerk
- **Description:** Clerk opens each email, downloads the attachment, and manually reads key fields (Invoice Number, Date, Vendor Name, Total Amount, Line Items).
- **Time:** Approx. 5-7 minutes per invoice.
- **Error Rate:** ~5% due to manual keying errors.

### 3. Validation
- **Role:** AP Specialist
- **Description:** Extracted data is cross-referenced with the Purchase Order (PO) in the legacy ERP system.
- **Checks:**
    - Vendor exists in master data.
    - PO number matches.
    - Status is "Open".
    - Line item totals match.
- **Bottleneck:** Validation requires switching between multiple screens and systems.

### 4. Data Entry
- **Role:** AP Clerk
- **Description:** Validated data is manually typed into the SAP/ERP finance module.
- **Action:** Clerk fills out 15+ fields in the transaction form and hits "Post".

### 5. Archiving
- **Role:** AP Clerk
- **Description:** The email attachment is saved to a network drive in a generic "Processed" folder.
- **Issue:** Poor organization makes retrieval difficult during audits.

## Swimlane Diagram (Text Representation)

| Role | Activity |
|------|----------|
| **Vendor** | Sends Invoice via Email |
| **Email Server** | Receives Email -> Stores in Inbox |
| **AP Clerk** | Checks Inbox -> Downloads Attachment -> Reads Data -> Enters Data in ERP -> Archives File |
| **AP Specialist** | Validates Non-PO Invoices (Exception Handling) |
| **ERP System** | Validates PO -> Posts Transaction -> Generates Payment Schedule |

## Metrics (Current State)
- **Average Handling Time (AHT):** 12 minutes per invoice.
- **Full-Time Equivalent (FTE):** 3 full-time employees dedicated to this process.
- **Cost per Invoice:** ~$8.50.
- **SLA Compliance:** 85% (target is 98%).
