from flask import Flask, render_template
import requests

app = Flask(__name__)
#383854ce4abc4475b5e34098b15327da
@app.route('/')
def index():
    # Replace 'YOUR_API_KEY' with your actual API key
    url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=383854ce4abc4475b5e34098b15327da'
    response = requests.get(url)
    
    news_data = response.json()
    
    articles = news_data['articles'] if news_data['status'] == 'ok' else []
    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
