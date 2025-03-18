import requests
from bs4 import BeautifulSoup

def dynamic_learning(data_sources):
    """
    Dynamically scrape and return data from given URLs.

    Args:
        data_sources (dict): A dictionary with keys as data types and values as URLs.

    Returns:
        dict: A knowledge base with scraped data.
    """
    knowledge_base = {}

    for key, link in data_sources.items():
        try:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                
                # Simple text extraction logic (customize as needed)
                text_content = " ".join([p.get_text() for p in soup.find_all('p')])
                
                # Store in knowledge base
                knowledge_base[key] = text_content.strip() or "No data found on the page."
            else:
                knowledge_base[key] = "Failed to fetch data."
        
        except Exception as e:
            knowledge_base[key] = f"Error while scraping: {str(e)}"

    return knowledge_base
