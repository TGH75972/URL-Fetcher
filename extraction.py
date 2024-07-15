import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"http error occurred :/ : {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"connection error occurred :/ : {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"a timeout error occurred :/ : {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred :/ : {req_err}")
    return None

def save_to_file(content, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content saved to {filename}")
    except IOError as e:
        print(f"Error :/ saving content to file: {e}")

def extract_title(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        return title
    except Exception as e:
        print(f"Error parsing HTML content :/ : {e}")
        return 'No title found'

def main():
    url = input("Enter the URL to fetch: ")
    content = fetch_url(url)
    if content:
        print("Content fetched successfully.\n")
        
        title = extract_title(content)
        print(f"Page Title: {title}\n")
        
        save_option = input("Do you want to save the content to a text file maybe? (yes/no): ").strip().lower()
        if save_option == 'yes':
            filename = input("Enter the filename: ")
            save_to_file(content, filename)
        else:
            print("Content not saved.")
    else:
        print("Failed to fetch content :/ .")

if __name__ == "__main__":
    main()
