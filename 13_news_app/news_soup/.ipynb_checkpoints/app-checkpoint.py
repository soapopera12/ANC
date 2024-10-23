from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def fetch_headlines():
    urls = { "https://indianexpress.com/",
           "https://www.thehindu.com/",
           "https://www.indiatoday.in/",
           "https://www.ndtv.com/"
          }

    headlines = []
    
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Adjust the selector based on the website's structure

        headlines.append(url)

        header_tag = { "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            }

        for tag in header_tag:
            for item in soup.find_all(tag):
                text = item.get_text(strip=True)
                if len(text) > 30:
                    if re.match(r'^[A-Za-z0-9\s.,\'"()-]*$', text):
                        headlines.append(text)
            
        # for item in soup.find_all('h1'):
        #     headlines.append(item.get_text(strip=True))
        
        # for item in soup.find_all('h2'):
        #     headlines.append(item.get_text(strip=True))
            
        # for item in soup.find_all('h3'):
        #     headlines.append(item.get_text(strip=True))
    
        # for item in soup.find_all('h4'):
        #     headlines.append(item.get_text(strip=True))
    
        # for item in soup.find_all('h5'):
        #     headlines.append(item.get_text(strip=True))
        
    return headlines

@app.route('/')
def home():
    headlines = fetch_headlines()
    
    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
