from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape/{option}")
def scrape_page(option: str):
    base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    url = f"{base_url}?opcao={option}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    paragraphs = [p.text for p in soup.find_all('p')]
    return {"paragraphs": paragraphs}

# Run the app only if this file is executed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
