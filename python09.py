class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: \t\t', self.marca, '\nModelo: \t', self.modelo, '\nEn Marcha: \t',
              self.enmarcha, '\nAcelerando: ', self.acelera, '\nFrenando: \t', self.frena)


class Moto(Vehiculos):
    hcaballito = ''

    def caballito(self):
        self.hcaballito = 'Voy haciendo un caballito'

    def estado(self):
        print('Marca: \t\t', self.marca, '\nModelo: \t', self.modelo, '\nEn Marcha: \t',
              self.enmarcha, '\nAcelerando: ', self.acelera, '\nFrenando: \t', self.frena,
              '\nCaballito: \t', self.hcaballito, )


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'

    def estado(self):
        print('Marca: \t\t', self.marca, '\nModelo: \t', self.modelo, '\nEn Marcha: \t',
              self.enmarcha, '\nAcelerando: ', self.acelera, '\nFrenando: \t', self.frena,
              '\nCarga: \t\t', self.cargado, )


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True


class BicicletaElectrica(VElectricos, Vehiculos):
    pass


miMoto = Moto('Honda', 'CBR',)
miMoto.caballito()
miMoto.estado()

print('------------------------------- A continuación creamos el segundo objeto --------------------------------------')

miFurgoneta = Furgoneta('Hyundai', 'H1')
miFurgoneta.arrancar()
miFurgoneta.carga(True)
miFurgoneta.estado()

print('------------------------------- A continuación creamos el segundo objeto --------------------------------------')

miBici = BicicletaElectrica('Orbea', 'Xsa')
miBici.estado()