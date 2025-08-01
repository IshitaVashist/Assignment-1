from pubmed_papers_cli.api_client import fetch_paper_ids, fetch_paper_details
from pubmed_papers_cli.paper_processor import parse_papers
from pubmed_papers_cli.csv_writer import write_papers_to_csv




# Fetch paper IDs
ids = fetch_paper_ids("covid 19", retmax=5)
xml_data = fetch_paper_details(ids)

# Parse papers{}
papers = parse_papers(xml_data)

# Write to CSV
write_papers_to_csv(papers, "papers_output.csv")
print("CSV file created successfully.")
