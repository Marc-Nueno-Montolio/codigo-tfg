import json, requests

class apiClient():
    def __init__(self):
        self.base_url = 'http://127.0.0.1:5000'
        print(f"Created REST Client to {self.base_url}")
        
    def get_stock(self):
        url = f"{self.base_url}/stocks" 
        res = requests.get(url)
        stocks = res.json()
        # for stock in stocks:
        #     print(f"[Stock {stock['id']} => {stock['content']} - Pos: {stock['position']}]" )
        return stocks

if __name__ == '__main__':
    crud = apiClient()