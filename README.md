# NIST 800-53 Control Mapper (GovTech)

## 📌 Overview
A machine-readable mapping tool designed to translate **NIST SP 800-53 Rev. 5** controls into actionable requirements for GovTech startups pursuing **CJIS** or **TX-RAMP** authorization.

## 🎯 Purpose
Government control frameworks are often distributed as dense PDFs. This repository attempts to convert those requirements into:
1.  **JSON Data:** For ingestion into GRC tools (Vanta, Drata, Hyperproof).
2.  **CLI Lookup Tool:** For engineering teams to quickly check requirements without reading a 500-page policy.

## 📂 Repository Contents

| Component | File | Description |
| :--- | :--- | :--- |
| **Data Source** | [`/data/nist_cjis_mapping.json`](data/nist_cjis_mapping.json) | The structured JSON database mapping NIST Controls (e.g., `AC-2`) to CJIS Policy 5.9.2 and TX-RAMP Levels. |
| **CLI Tool** | [`/tools/lookup_control.py`](tools/lookup_control.py) | A Python script allowing developers to query requirements via command line. |

## 🚀 Usage

**Look up a specific control:**
```bash
# Returns CJIS and TX-RAMP requirements for Account Management
python tools/lookup_control.py --id AC-2
