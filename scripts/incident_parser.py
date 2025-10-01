import pandas as pd
import matplotlib.pyplot as plt

def parse_incident_journal(file_path):
    """Parse incident journal data (CSV extracted from PDF) and summarize findings."""
    try:
        df = pd.read_csv(file_path)
        
        # Summarize incidents by type and severity
        summary = df.groupby(['incident_type', 'severity']).size().unstack(fill_value=0)
        print("Incident Summary by Type and Severity:")
        print(summary)
        
        # Save summary to CSV
        summary.to_csv('data/incident_summary.csv')
        
        # Visualize incidents
        summary.plot(kind='bar', stacked=True, color=['#ff9999', '#66b3ff'])
        plt.title('Incidents by Type and Severity')
        plt.xlabel('Incident Type')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('evidence/incident_chart.png')
        plt.close()
        
        return df
    except Exception as e:
        print(f"Error parsing journal: {str(e)}")
        return None

def main():
    journal_path = 'data/incidents.csv'
    incidents = parse_incident_journal(journal_path)
    if incidents is not None:
        print("\nSample Incidents:")
        print(incidents.head())

if __name__ == "__main__":
    main()