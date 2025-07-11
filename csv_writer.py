from typing import List, Dict
import csv

def write_papers_to_csv(papers: List[Dict], filename: str) -> None:
    """
    Writes the list of paper details to a CSV file.

    Args:
        papers (List[Dict]): List of paper detail dictionaries.
        filename (str): Path to the output CSV file.
    """
    fieldnames = [
        "pubmed_id",
        "title",
        "publication_date",
        "authors",
        "company_affiliations",
        "corresponding_author_email"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # write column headers

        for paper in papers:
            # Convert authors and company affiliations lists into comma-separated strings
            paper["authors"] = ", ".join(paper.get("authors", []))
            paper["company_affiliations"] = ", ".join(paper.get("company_affiliations", []))

            writer.writerow(paper)
