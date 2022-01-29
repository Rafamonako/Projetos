class Primos:
    def __init__(self, num):
        self.Num = num

    def verificar_primo(self):
        self.NonPrimo = False
        for i in range(2, self.Num):
            if (self.Num % i) == 0:
                self.NonPrimo = True

            return self.NonPrimo

    def mostrar_primo(self):
        self.verificar_primo()
        while self.Num < 0:
            print('Por favor, insira um número maior do que 0!')
            self.Num = int(input("Insira o número aqui: "))
        if self.Num == 0:
            print('O número', self.Num, 'é neutro!')
        elif self.NonPrimo:
            print('O número', self.Num, 'não é primo!')
        else:
            print('O número', self.Num, 'é primo!')


Num = int(input('Insira o número aqui: '))
ver_primo = Primos(Num)
ver_primo.mostrar_primo()
