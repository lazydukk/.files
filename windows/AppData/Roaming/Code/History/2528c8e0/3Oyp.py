import re
from urllib import response
import requests
from bs4 import BeautifulSoup
import os

def scrape_pdf(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')

    pdf_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.pdf'):
             pdf_links.append(href)


    for pdf_link in pdf_links:
        pdf_url = url + pdf_link
        pdf_filename = pdf_link.split('/')[-1]
        print(pdf_filename)
        pdf_path = os.path.join('pdfs', pdf_filename)

        response = requests.get(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(response.content)

    print(f'Downloaded {pdf_filename}')

if __name__ == '__main__':
  url = "https://drive.apluseducation.lk/pdf/pdf/PDF/AJ/2025/paper&20marking"
  scrape_pdf(url)