import requests
from bs4 import BeautifulSoup

file_name = input("Enter file name: ")

url = 'https://pyobfuscate.com/pyd'
with open(f'./{file_name}', 'r', encoding='utf-8') as file:
    file_content = file.read()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://pyobfuscate.com/'
}
response = requests.post(url, data={"pyinput": file_content}, headers=headers)
if response.status_code == 200:
    print("Request successful!")

    soup = BeautifulSoup(response.content, 'html.parser')
    textarea = soup.find('textarea', {'id': 'sourceCode2'})
    with open("output.py", 'w', encoding='utf-8') as file:
        file.write(textarea.text)

    print("File successfully pyobfuscated as output.py!")
else:
    print("Error!")
input("Press Enter to close...")
