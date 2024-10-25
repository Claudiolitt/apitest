from fastapi import FastAPI

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
    
    paragraphs = [p.text for p in soup.find_all('p')]
    return {"paragraphs": paragraphs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

