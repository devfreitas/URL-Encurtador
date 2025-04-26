import requests
import os
os.system("cls")

print("----> ENCURTADOR DE URL <----\nDigite uma URL para ser encurtada!\nQuando digitado 0 ou qualquer outra texto, aplicação será encerrada!\n")

while True:
    url = input("Cole sua URL longa: ").strip()
    if url == '0':
        print("Até mais!")
        break
    if '.' not in url:
        print("Entrada inválida. Encerrando...")
        break
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    resposta = requests.get('https://tinyurl.com/api-create.php?url=' + url)

    print("\nURL encurtada:", resposta.text)
    print("-" * 50)
os.system("cls")