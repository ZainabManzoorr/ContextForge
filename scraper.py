import requests
from bs4 import BeautifulSoup


def clean_text(text):
  lines = text.split("\n")
  
  cleaned = []
  for line in lines:
    line = line.strip()
    
    # remove empty lines only (keep meaningful short text too)
    if not line:
      continue

    # remove navigation noise
    if line in ["Navigation", "index", "modules", "next", "previous"]:
      continue
    
    
    cleaned.append(line)
  return "\n".join(cleaned)

def scrape_url(url):
  response = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})
  soup = BeautifulSoup(response.text, 'lxml')
  
  main = soup.find("main") or soup.find("article") or soup.body
  text = main.get_text(separator="\n")
  cleaned_text = clean_text(text)
  return cleaned_text

import os
def save_text(text,folder,filename):
  os.makedirs(folder, exist_ok=True)
  
  path = os.path.join(folder,filename)
  with open(path,'w',encoding="utf-8") as f:
    f.write(text)
    
  print(f"Saved: {path}")