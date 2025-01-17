from bs4 import BeautifulSoup
import requests
import json

def get_soup(url, headers):
    """Fetches the page content and returns a BeautifulSoup object."""
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_attributes(page_soup, element):
    """Extracts text from a specified element."""
    try:
        return page_soup.select(element)[0].get_text(strip=True)
    except (IndexError, AttributeError):
        return "NA"

def get_attribute_list(page_soup, element):
    """Extracts a list of texts from specified elements."""
    try:
        attr_list = page_soup.select(element)
        return [link.get_text(strip=True) for link in attr_list]
    except (IndexError, AttributeError):
        return []

def get_script_attribute(page_soup, element):
    """Extracts a JSON-based attribute from a script tag."""
    try:
        script_tag = page_soup.find('script', type='application/ld+json')
        json_data = json.loads(script_tag.string)
        return json_data.get(element, "NA")
    except (IndexError, AttributeError):
        return "NA"