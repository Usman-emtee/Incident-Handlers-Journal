# Incident-Handlers-Journal# Incident Handler’s Journal

## Overview
This repository presents an incident handler’s journal from a cybersecurity training course, documenting hands-on exercises in incident detection and response. As an aspiring security analyst, I analyzed ransomware and malicious file incidents, used tools like Wireshark, tcpdump, and VirusTotal, and applied NIST CSF principles. Python scripts summarize incident data, reflecting my skills in problem-solving and protecting organizations from digital threats, with a focus on web-related incidents like phishing.

## Objectives
- Document and analyze cybersecurity incidents from a course journal.
- Use tools (Wireshark, tcpdump, VirusTotal) to investigate network traffic and threats.
- Summarize findings with Python and propose NIST CSF-aligned mitigations.

## Tools Used
- **Framework**: NIST CSF (Respond/Recover functions).
- **Tools**: Wireshark, tcpdump (network analysis), VirusTotal (threat investigation).
- **Analysis**: Python (pandas, matplotlib) for incident summarization.
- **Documentation**: PDF journal, Markdown, screenshots.

## Repository Structure
- `incident_journal.pdf`: Journal documenting ransomware, network analysis, and file hash investigations.
- `scripts/`: Python script for incident analysis.
- `data/`: CSV file with summarized incidents.
- `docs/`: Analysis and reflections.

## Key Findings
- **Ransomware Incident**: Phishing-based attack on a healthcare company, mitigated by system shutdown (NIST CSF RS.CO-2).
- **Malicious File**: Email attachment with malicious hash detected at a financial company, analyzed via VirusTotal.
- **Network Analysis**: Captured and analyzed traffic using Wireshark and tcpdump, identifying potential threats.
- **Recommendations**:
  - Enhance email filtering to block phishing.
  - Train employees on recognizing malicious attachments.
  - Deploy IDS/IPS for real-time monitoring.

## Usage
1. Clone the repository: `git clone https://github.com/usman-emtee/Incident-Handlers-Journal.git`
2. Review the journal in `incident_journal.pdf`.
3. Run the script: `python scripts/incident_parser.py` to analyze incidents.
4. View evidence in `evidence/` and data in `data/incident_summary.csv`.

## Example Script
```python
import pandas as pd
import matplotlib.pyplot as plt

def parse_incident_journal(file_path):
    df = pd.read_csv(file_path)
    summary = df.groupby(['incident_type', 'severity']).size().unstack(fill_value=0)
    summary.plot(kind='bar', stacked=True)
    plt.savefig('evidence/incident_chart.png')
    return df

journal_path = 'data/incidents.csv'
incidents = parse_incident_journal(journal_path)
```

## Disclaimer
This journal is based on a fictional training scenario. Always obtain permission before analyzing real systems.

## Contact
- GitHub: [usman-emtee](https://github.com/usman-emtee)
- LinkedIn: [usman-mt](https://linkedin.com/in/usman-mt)
- Email: usmanemtee@gmail.com
