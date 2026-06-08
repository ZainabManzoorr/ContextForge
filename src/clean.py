# preprocessing/clean_text.py
import re

def clean_text(text: str) -> str:
    

    # Step 1: normalize case
    text = text.lower()

    # Step 2: remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Step 3: remove HTML tags (important for scraped data)
    text = re.sub(r'<.*?>', '', text)

    # Step 4: remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    # Step 5: remove common web noise
    text = re.sub(
        r'click here|subscribe|copyright|all rights reserved|privacy policy',
        '',
        text
    )

    # Step 6: remove special junk characters (optional cleanup)
    text = re.sub(r'[^\w\s\.\,\!\?\-\']', '', text)

    return text.strip()