
# cd = cedulas 
# total de cedulas
# opc = opcao de escolhas do user
# valor = escolhar do saldo deposito/saque 
###################################################


from ast import While
from imaplib import Int2AP
from importlib.resources import path
from pickle import TRUE
from secrets import choice
from time import sleep
from datetime import date , datetime
import os
import json

horaSaque = datetime.now().replace( microsecond=0)
timelog = str(horaSaque)

path = ".\dadoUser"
os.chdir(path)
with open("db.json", encoding='utf-8') as user_json:
    dados = json.load(user_json)


user = dados.get("clients").get("client").get("user")
key  = dados.get("clients").get("client").get("key")
total = dados.get("clients").get("client").get("total")


while (True):
    print('='*30)
    print('{:^30}'.format('Caixa Eletronico'))
    loginKey = int(input("Senha: "))
    print('='*30)
   
    if loginKey == key:   

            os.system('clear') or None
            print('='*30)
            print('{:^30}'.format('Caixa Eletronico'))
            print('{:^10}'.format('Bem vindo de volta Sr:'),user)
            print('='*30)

            print( "1 - Depositar saldo"  )
            print( "2 - Sacar saldo" )
            print( "3 - Saldo em carteira " )
            print( "4 - Sair" )
            opc = int(input("Qual é sua opçao: "))


            if opc == 1:

                os.system('clear') or None
                print('Qual valor de deposito?')
                print('1 - 100')
                print('2 - 50')
                print('3 - 20')
                print('4 - 10')
                print('5 - outro valor')
                deposito = int(input("Qual é o valor? R$ "))
                if deposito == 1:
                    total = total + 100
                elif deposito ==2:
                    total = total + 50
                elif deposito == 3:
                    total = total + 20
                elif deposito == 4:
                    total = total + 5
                elif deposito == 5:
                    outroValor = float(input("Qual o valor? "))
                    total = total + outroValor
                elif deposito >= 6:
                        print("Valor invalidore, por seguranca tente novamente")
                saldoFinal = total
                        
                        
                dict1 ={
                        "clients":{

                            "client": {
                                "user": user,
                                "key": key ,
                                "total": saldoFinal, 
                                "ultima movimentacao": timelog
                            }
                        }
                    }
                        
                arquivo = open("db.json", "w")  
                
                        
                json.dump(dict1, arquivo, indent = 6)  
                        
                arquivo.close()
                #
                dict1 ={ 
                        "dados": {
                                "saque": "False",
                                "deposito": "True",
                                "valor deposito": deposito,
                                "valor total em conta": total,
                                
                        },

                            "client": {
                                "Cliente": user,
                                "key": key,
                                "Hora saque": timelog
                            }
                    }
                        
                arquivo = open("ComprovantelogUserEntrada.json", "w")  
                        
                json.dump(dict1, arquivo, indent = 6)  
                        
                arquivo.close()

                #   
                logdeposito = str (input ('Imprimir o comprovante? (S/N) : '))
                if logdeposito =='s':
                    arquivo = open('ComprovanteDeposito.txt','w')
                    print('='*30)
                    arquivo.write('='*30)
                    arquivo.write('\n{:^30}'.format('COMPROVANTE'))
                    arquivo.write('\n-Deposito efetuado de R$/OPC{}'.format(deposito))
                    arquivo.write('\n-Total em conta R${}'.format(total))
                    arquivo.write('\n-Caixa Eletronico 24H\n')
                    arquivo.write('='*30)
                    print('='*30)
                    arquivo.close()
                    sleep(0.8)
                    print("COMPROVANTE GERADO")
                    print('Volte sempre')
                    sleep(1)
                    os.system('clear') or None    
                    os.sys.exit()

                elif  logdeposito == 'n' :
                    os.system('clear') or None

                    

            elif opc == 2:
                    os.system('clear') or None
                    
                    while(True):
                        try:
                            valor = int(input('Valor do saque R$: '))
                            break
                        except ValueError :                        
                            print("Saque de menors a R$10 ou quebrados nao sao permitidos!")
                    while True:
                        if(valor < 10):
                            print("Saque de menors a R$10 ou quebrados nao sao permitidos!")
                            break
                        else:
                            
                            sleep(0.8)
                            os.system('clear') or None
                    
                        if valor > total :
                            print("Saldo insuficiente para saque ")
                                
                        elif valor < total:

                            total = total - valor

                                                                

                                    #DADOS SALDOS DO USUARIO#
                            dict1 ={ 
                                    "dados": {
                                            "saque": "true",
                                            "deposito": "false",
                                            "valor saque": valor,
                                            "valor total em conta": total,
                                           
                                    },

                                        "client": {
                                            "Cliente": user,
                                            "key": key,
                                            "Hora saque": timelog
                                        }
                                }
                                    
                            arquivo = open("ComprovantelogUserSaida.json", "w")  
                                    
                            json.dump(dict1, arquivo, indent = 6)  
                                    
                            arquivo.close()
                            saldoFinal = total
                            
                            
                            dict1 ={
                                    "clients":{

                                        "client": {
                                            "user": user,
                                            "key": key ,
                                            "total": saldoFinal, 
                                            "ultima movimentacao": timelog
                                        }
                                    }
                                }
                                    
                            arquivo = open("db.json", "w")  
                                    
                            json.dump(dict1, arquivo, indent = 6)  
                                    
                            arquivo.close()


                        
                        print("Saque no valor de:", valor , "Efetuado com sucesso!")

                        #COMPROVATE #
                        logdeposito = str (input ('Imprimir o comprovante? (S/N) : '))
                        if logdeposito =='s':
                            arquivo = open('Comprovante.txt','w')
                            print('='*30)
                            arquivo.write('='*30)
                            arquivo.write('\n{:^30}'.format('COMPROVANTE'))
                            arquivo.write('\n-Saque total de R${}'.format(valor))
                            arquivo.write('\n-Caixa Eletronico 24H\n')
                            arquivo.write('\n='*30)
                            print('='*30)
                            arquivo.close()
                            sleep(0.8)
                            print("COMPROVANTE GERADO")
                            print('Volte sempre')
                            os.system('clear') or None 
                            break

                        elif logdeposito == 'n':
                            os.system('clear') or None
                            break


            elif opc == 3:
                    os.system('clear') or None    
                    
                    print('{:^30}'.format('Caixa Eletronico'))
                    print('{:^10}'.format('Saldo total: '), total)
                    print('{:^10}'.format('Consulta feito em: '), horaSaque)
                    logdeposito = str (input ('Imprimir o comprovante? (S/N) : '))
                    if logdeposito =='s':
                        arquivo = open('ComprovanteSaldo.txt','w')
                        print('='*30)
                        arquivo.write('='*30)
                        arquivo.write('\n{:^30}'.format('COMPROVANTE'))
                        arquivo.write('\n-Total em conta R${}'.format(total))
                        arquivo.write('\n-Caixa Eletronico 24H\n')
                        arquivo.write('='*30)
                        print('='*30)
                        arquivo.close()
                        sleep(0.8)
                        print("COMPROVANTE GERADO")
                        print('Volte sempre')
                        sleep(1)
                        os.system('clear') or None    
                    elif  logdeposito == 'n' :
                            os.system('clear') or None

            elif opc == 4:    
                    print("Finalizando servidor") 
                    sleep(0.8)
                    os.system('clear') or None    

                    os.sys.exit()
                
                
    else:
        print("Senha invalida, tente novamente em 2 segundos!")
        sleep(2)
        os.system('clear') or None

