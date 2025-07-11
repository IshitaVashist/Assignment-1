from typing import List
import requests

# Base URLs for PubMed E-utilities API
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_paper_ids(query: str, retmax: int = 50) -> List[str]:
    """
    Fetch paper IDs from PubMed based on a search query.
    
    Args:
        query (str): The search term to look up in PubMed.
        retmax (int): Maximum number of results to retrieve.

    Returns:
        List[str]: List of PubMed article IDs.
    """
    params = {
        "db": "pubmed",        # database: PubMed
        "term": query,         # your search query
        "retmode": "json",     # response format
        "retmax": retmax       # max number of IDs to return
    }

    response = requests.get(ESEARCH_URL, params=params)
    response.raise_for_status()  # Raise an error if the request failed

    data = response.json()
    return data['esearchresult']['idlist']  # list of article IDs

def fetch_paper_details(ids: List[str]) -> str:
    """
    Fetch detailed information about papers from PubMed using paper IDs.

    Args:
        ids (List[str]): List of PubMed article IDs.

    Returns:
        str: XML data of article details.
    """
    id_string = ",".join(ids)  # convert list of IDs to comma-separated string

    params = {
        "db": "pubmed",
        "id": id_string,
        "retmode": "xml"
    }

    response = requests.get(EFETCH_URL, params=params)
    response.raise_for_status()

    return response.text  # XML data
