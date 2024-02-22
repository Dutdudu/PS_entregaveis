class Drone():
    def __init__(self,num_mot,qtd_cam,ano,nome,cor):
        self.num_mot = num_mot
        self.qtd_cam = qtd_cam
        self.ano = ano
        self.nome = nome
        self.cor = cor

    def exibir_indv(self):
        print('Drone individual: ')
        print('------------------------------------')
        print(f'Nome: {self.nome}')
        print(f'Numero de motores: {self.num_mot}')
        print(f'Quantidade de cameras: {self.qtd_cam}')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        print("-----------------------------------------------")

class Frota():
    def __init__(self):
        self.frota = []

    def add_drone(self,drone):
        self.frota.append(drone)

    def exibir_todos(self):
        print('Lista de drones: ')
        print('---------------------------------------')
        for drone in self.frota:
            print(drone.nome)
        print("-----------------------------------------------")

    def rank_por_ano(self)  :
        print('Rank por ano: ')
        print("-----------------------------------------------")
        sorted_drones = sorted(self.frota, key=lambda x: x.ano)
        for i, drone in enumerate(sorted_drones, start=1):
            print(f"{i}. {drone.nome}")
        print("-----------------------------------------------")


drone1 = Drone(3,4,2018,"Rei dos céus","azul")    
drone2 = Drone(5,1,2020,"Tempestade","verde")    
drone3 = Drone(1,2,2017,"Peixe aéreo","vermelho")    
frota = Frota()
frota.add_drone(drone1)
frota.add_drone(drone2)
frota.add_drone(drone3)

drone1.exibir_indv()

frota.exibir_todos()    
frota.rank_por_ano()    