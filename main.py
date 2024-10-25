from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
@app.head("/")
def read_root():
    return {"Hello": "World"}

@app.get("/scrape/{option}")
def scrape_page(option: str):
    base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    url = f"{base_url}?opcao={option}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrando todas as tabelas
    tables = soup.find_all('table')
    if not tables:
        return {"error": "No tables found"}

    # Extraindo os dados de todas as tabelas
    table_data = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            table_data.append(cols)
    
    return {"table_data": table_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
