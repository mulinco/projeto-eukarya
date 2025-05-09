import os

generos = [
    "Acanthamoeba", "Agaricus", "Aegagropila", "Amoeba", "Amphimedon", "Aplanochytrium", "Arabidopsis",
    "Bigelowiella", "Blastocystis", "Capsaspora", "Chlamydomonas", "Chondrus", "Corallochytrium",
    "Cryptomonas", "Cyanidioschyzon", "Dictyostelium", "Ectocarpus", "Entamoeba", "Euplotes", "Guillardia",
    "Homo", "Hydra", "Leishmania", "Malawimonas", "Monosiga", "Naegleria", "Ochromonas", "Oryza",
    "Paramecium", "Physarum", "Physcomitrella", "Polysphondylium", "Rhodelphis", "Saccharomyces",
    "Salpingoeca", "Spizellomyces", "Thalassiosira", "Thecamonas", "Trimastix", "Trichomonas",
    "Trypanosoma", "Volvox"
]


pasta = "C:/Users/mulin/OneDrive/Documentos/eukarya"

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.startswith("LUCAdup_aln_") and nome_arquivo.endswith(".fasta"):
        caminho_entrada = os.path.join(pasta, nome_arquivo)
        nome_saida = nome_arquivo.replace(".fasta", "_euka.fasta")
        caminho_saida = os.path.join(pasta, nome_saida)

        with open(caminho_entrada, "r") as infile, open(caminho_saida, "w") as outfile:
            for linha in infile:
                if linha.startswith(">"):
                    linha_sem_maior = linha[1:].strip()
                    genero = linha_sem_maior.split("_", 1)[0]
                    if genero in generos:
                        nova_linha = f">Eukarya_{linha_sem_maior}\n"
                        outfile.write(nova_linha)
                    else:
                        outfile.write(">" + linha_sem_maior + "\n")
                else:
                    outfile.write(linha)

print("Todos os arquivos foram processados com sucesso!")
print("Verifique os arquivos de saída na pasta especificada.")