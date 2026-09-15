from modules.Conta import Livro

def main():
    livro1 = Livro("Kagurabachi", "gege akutami", "2023")
    livro2 = Livro("JoJo", "goku", "2000")
    livro3 = Livro("chainsaw man", "Bernardo", "2023")

    livro1.emprestar()
    livros2023 = Livro.livros_publicados(2023)
    for livro in livros2023:
        print(livro.disponibilidade)

if __name__ == '__main__':
    main()