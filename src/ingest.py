import os

def load_kb_files(kb_path):
    documents = []

    for file in os.listdir(kb_path):
        if file.endswith(".txt"):
            with open(os.path.join(kb_path, file), "r", encoding="utf-8") as f:
                documents.append({
                    "text": f.read(),
                    "source": file
                })

    return documents