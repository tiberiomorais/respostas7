# 3. Classe Retangulo: Crie uma classe que modele um retangulo:
# A. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a
# escolher)
# B. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área
# e calcular Perímetro;
# C. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
# informe as medidades de um local. Depois, deve criar um objeto com as
# medidas e calcular a quantidade de pisos e de rodapés necessárias para
# o local.

class retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura= largura

    def mudar_comprimeno(self,comprimento):

