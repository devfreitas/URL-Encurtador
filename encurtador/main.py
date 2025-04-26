import requests

def encurtar_com_tinyurl(url_longa):
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={url_longa}")
        return response.text if response.status_code == 200 else f"Erro: {response.status_code}"
    except Exception as e:
        return f"Erro ao encurtar: {str(e)}"

def verificar_url(url):
    """Verifica se a URL parece válida"""
    return url.startswith(('http://', 'https://'))

def main():
    print("=== Encurtador de URL usando TinyURL ===")
    
    while True:
        print("\n1. Encurtar URL")
        print("2. Sair")
        
        opcao = input("Escolha uma opção (1/2): ").strip()
        
        if opcao == "1":
            url_original = input("\nDigite a URL que deseja encurtar: ").strip()
            
            if not verificar_url(url_original):
                print("URL inválida. Deve começar com http:// ou https://")
                continue
                
            url_curta = encurtar_com_tinyurl(url_original)
            
            if url_curta.startswith("http"):
                print(f"\n✅ URL encurtada com sucesso!")
                print(f"Original: {url_original}")
                print(f"Encurtada: {url_curta}")
            else:
                print(f"\n❌ {url_curta}")
                
        elif opcao == "2":
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida. Digite 1 ou 2.")

if __name__ == "__main__":
    main()