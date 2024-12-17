import requests
# https://drive.apluseducation.lk/pdf/pdf/PDF/AJ/2025/MS/{i}.pdf

def scrape_pages():
        url = f"https://drive.apluseducation.lk/pdf/pdf/PDF/AJ/2025/paper marking/"
        response = requests.get(url, verify=False)

        # Save the content to a file
        with open(f"ms00/", "wb") as file:
            file.write(response.content)
            file.close()
        print(f"File downloaded")

        # Sleep for a random interval between 2 and 60 seconds
        # time.sleep(random.randint(2, 5))
