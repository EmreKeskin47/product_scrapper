from flask import Flask, request
from flask_cors import CORS
from routes.amazon import AmazonProductScrapper   

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/product_scrapper/amazon', methods=['GET'])
def getProductFromURL():
        url = request.args.get('url', default = "", type = str)
        return AmazonProductScrapper(url)
    
@app.route('/', methods=['GET'])
def home():
        return "<h1>Amazon Product Scrapper API</h1><p>This site is a prototype API for an Amazon Product Scrapper.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)