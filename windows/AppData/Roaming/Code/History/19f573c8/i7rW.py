import requests
from bs4 import BeautifulSoup
import os

def download_pdfs(url):
  """Downloads all PDFs from the given URL."""

  # Create a directory to store the PDFs
  os.makedirs('pdfs', exist_ok=True)

  # Get the HTML content of the page
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all the links to PDFs on the page
  pdf_links = []
  for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith('.pdf'):
      pdf_links.append(href)

  # Download each PDF
  for pdf_link in pdf_links:
    pdf_url = url + pdf_link
    pdf_filename = pdf_link.split('/')[-1]
    pdf_path = os.path.join('pdfs', pdf_filename)

    response = requests.get(pdf_url)
    with open(pdf_path, 'wb') as f:
      f.write(response.content)

    print(f'Downloaded {pdf_filename}')

if __name__ == '__main__':
  url = 'https://drive.apluseducation.lk/pdf/pdf/PDF/AJ/2025/paper marking/'
  download_pdfs(url)