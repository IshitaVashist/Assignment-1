import argparse
from pubmed_papers_cli.api_client import fetch_paper_ids, fetch_paper_details
from pubmed_papers_cli.paper_processor import parse_papers
from pubmed_papers_cli.csv_writer import write_papers_to_csv




def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and save to CSV.")
    
    # Positional argument: query
    parser.add_argument("query", type=str, help="Search query for PubMed papers")

    # Optional argument: --file
    parser.add_argument("--file", type=str, default="papers.csv", help="Output CSV filename")

    # Optional flag: --debug
    parser.add_argument("--debug", action="store_true", help="Print debug information")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: '{args.query}'")

    # Fetch IDs
    ids = fetch_paper_ids(args.query, retmax=20)

    if args.debug:
        print(f"Found {len(ids)} paper IDs: {ids}")

    # Fetch paper details
    xml_data = fetch_paper_details(ids)

    # Parse papers
    papers = parse_papers(xml_data)

    if args.debug:
        print(f"Parsed {len(papers)} papers.")

    # Write to CSV
    write_papers_to_csv(papers, args.file)

    print(f"Saved {len(papers)} papers to {args.file}")

# Ensures it runs when called directly
if __name__ == "__main__":
    main()
