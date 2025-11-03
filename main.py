def gravarArquivo():
    try:
        f = open(professor.txt, mode="w", encoding="utf-8")
        f.write("nome,cpf,matricula\n")
        f.write("João Silva,12345678900,2023001\n")
        f.write("Maria Oliveira,98765432100,2023002\n")
    except
        print("Erro ao gravar o arquivo.")
    finally:
        print("Arquivo fechado com sucesso")
        f.close()