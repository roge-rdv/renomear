import os

def renomear_midias(pasta, novo_nome):
    # Extensões comuns de mídia
    extensoes_midias = ['.jpg', '.jpeg', '.png', '.mp4', '.mov', '.avi', '.mp3', '.wav', '.webp', '.heic']
    arquivos = [f for f in os.listdir(pasta) if os.path.splitext(f)[1].lower() in extensoes_midias]
    
    # Ordenar para manter uma ordem fixa
    arquivos.sort()

    for i, arquivo in enumerate(arquivos, start=1):
        extensao = os.path.splitext(arquivo)[1]
        novo_nome_arquivo = f"{novo_nome}{i}{extensao}"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome_arquivo)
        
        # Renomear arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"{arquivo} renomeado para {novo_nome_arquivo}")

# Exemplo de uso
pasta = r'C:/'  # Substitua pelo caminho da sua pasta
novo_nome = "Tete"  # Nome base desejado para os arquivos
renomear_midias(pasta, novo_nome)
