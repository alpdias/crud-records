import os
import pymysql
from time import sleep
from datetime import date

numeroID = int(input('ID: '))
empresa = str(input('Empresa: '))
cnpj = str(input('CNPJ: '))
tributacao = str(input('Tributação: '))
email = str(input('E-mail: '))
telefone = str(input('Telefone: '))
endereco = str(input('Endereço: '))
situacao = str(input('Situação: '))
