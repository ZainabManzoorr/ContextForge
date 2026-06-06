from scraper import scrape_url,save_text
from urls import DEV_URLS,ML_URLS,GENERAL_URLS

def process_urls(urls,folder):
  for url in urls:
    print(f"Scraping: {url}")
    text = scrape_url(url)
    filename = url.replace("https://","").replace("/","_") + ".txt"
    save_text(text,folder,filename)

#DEV KB
process_urls(DEV_URLS,"data/dev")

#ML KB
process_urls(ML_URLS,"data/ml")

#General KB
process_urls(GENERAL_URLS,"data/general")