from pubmed_papers_cli.api_client import fetch_paper_details
from pubmed_papers_cli.api_client import fetch_paper_ids



ids = fetch_paper_ids("covid 19", retmax=5)
print(ids)

xml_data = fetch_paper_details(ids)
print(xml_data[:1000])
