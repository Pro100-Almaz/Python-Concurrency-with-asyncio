import requests

response = requests.get('https://www.example.com') # Веб-запрос ограничен производительностью ввода-вывода

items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items] # Обработка ответа ограничением быстродействием процессора

formatted_headers = '\n'.join(headers) # Конкатенация строк ограничена быстродействием процессора

with open('headers.txt', 'w') as file: # Запись на диск ограничена производительностью ввода-вывода
    file.write(formatted_headers)