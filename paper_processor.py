from typing import List, Dict
import xml.etree.ElementTree as ET

def parse_papers(xml_data: str) -> List[Dict]:
    """
    Parses the XML data for PubMed papers and extracts relevant fields.

    Args:
        xml_data (str): XML string containing paper details.

    Returns:
        List[Dict]: List of paper details as dictionaries.
    """
    papers = []

    root = ET.fromstring(xml_data)  # parse the XML string

    for article in root.findall(".//PubmedArticle"):
        paper_info = {}

        # PubMed ID
        pmid = article.findtext(".//PMID")
        paper_info["pubmed_id"] = pmid

        # Article Title
        title = article.findtext(".//ArticleTitle")
        paper_info["title"] = title

        # Publication Date
        pub_date_elem = article.find(".//PubDate")
        if pub_date_elem is not None:
            year = pub_date_elem.findtext("Year")
            month = pub_date_elem.findtext("Month")
            day = pub_date_elem.findtext("Day")
            pub_date = f"{year or ''}-{month or ''}-{day or ''}"
        else:
            pub_date = "Unknown"
        paper_info["publication_date"] = pub_date

        # Author names and affiliations
        authors = []
        company_affiliations = []
        corresponding_email = None

        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName") or ""
            fore_name = author.findtext("ForeName") or ""
            full_name = f"{fore_name} {last_name}".strip()
            authors.append(full_name)

            for aff in author.findall(".//AffiliationInfo/Affiliation"):
                aff_text = aff.text or ""
                # Detect companies based on simple heuristics
                if any(company_term in aff_text for company_term in ["Inc", "Ltd", "Corporation", "Corp", "LLC"]):
                    company_affiliations.append(aff_text)
                # Detect emails (simple pattern)
                if "@" in aff_text and not corresponding_email:
                    corresponding_email = aff_text.split()[-1]  # pick last word assuming it's the email

        paper_info["authors"] = authors
        paper_info["company_affiliations"] = company_affiliations
        paper_info["corresponding_author_email"] = corresponding_email

        papers.append(paper_info)

    return papers
