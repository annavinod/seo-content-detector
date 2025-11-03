import re
import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (LeadWalnut Assignment)"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            return res.text
    except Exception:
        pass
    return ""

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "Untitled"
    for s in soup(["script", "style", "noscript"]):
        s.decompose()
    text = " ".join(p.get_text() for p in soup.find_all(["p", "article", "main"]))
    text = re.sub(r"\s+", " ", text).strip()
    return title, text
