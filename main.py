from bs4 import BeautifulSoup
import requests

html_text = requests.get("http://scstrade.com/FIPILIPI.aspx").text
print(html_text)
