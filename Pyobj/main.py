from modules.restaurentes import Restaurante

def main():
    restaurante1 = Restaurante("Holy molly", "Sorvete")
    restaurante2 = Restaurante("carnudos bar", "Churrasco")
    restaurante3 = Restaurante("Berniggas bar", "Leite")

    restaurante2.receber_avaliacao('João',  3)
    restaurante2.receber_avaliacao('Arthur', 5)
    restaurante2.receber_avaliacao('Daniel', 1)
    restaurante2.receber_avaliacao('Rafael', 4)
    Restaurante.listar_elementos()

if __name__ == '__main__':
    main()