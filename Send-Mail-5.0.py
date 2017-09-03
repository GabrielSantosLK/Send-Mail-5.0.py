#!/usr/bin/env python 
# -*- coding: utf-8 -*-
print('\n © 2017 Copyright TODOS OS DIREITOS RESERVADOS POR LOOCK UNDERWOOD') 
import smtplib
import getpass
import time
print('''

 ███████╗███████╗███╗   ██╗██████╗               ███╗   ███╗ █████╗ ██╗██╗        ██████╗ ██╗   ██╗
 ██╔════╝██╔════╝████╗  ██║██╔══██╗              ████╗ ████║██╔══██╗██║██║        ██╔══██╗╚██╗ ██╔╝
 ███████╗█████╗  ██╔██╗ ██║██║  ██║    █████╗    ██╔████╔██║███████║██║██║        ██████╔╝ ╚████╔╝ 
 ╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ╚════╝    ██║╚██╔╝██║██╔══██║██║██║        ██╔═══╝   ╚██╔╝  
 ███████║███████╗██║ ╚████║██████╔╝              ██║ ╚═╝ ██║██║  ██║██║███████╗██╗██║        ██║   
 ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝               ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝        ╚═╝   


 :================================================================:
 :  -  SCRIPT DE ESTUDO BASICO EM PYTHON // BY: Loock Underwood   :
 :================================================================:
 :  - TAMO JUNTO ° DERICK SANTOS e ° FELIPE MANDIOCA              :
 :================================================================:                                                              
 :  - GRUPO : https://www.facebook.com/groups/fsocietybrasil/     :
 :================================================================:
 :  - MY GITHUB : https://github.com/LoockUnderwood               :
 :================================================================: ''')

time.sleep(2)

print('''
 \n OBS: - É NECESSÁRIO PERMITIR LOGUINS NO SEU GMAIL SEM SER PELO SITE.
 \n OBS: - CALMA, ISSO NÃO VAI VAZAR OS SEUS DADOS.

 \n [!]  - BASTA ACESSAR ESTE LINK E ATIVAR, DEPOIS DO PROCESSO PODES DESATIVAR.

 \n [!]  - LINK: myaccount.google.com/lesssecureapps ''')





#=================================================================================#
print('\n #============================================================================================#')
#=================================================================================#
print("\n\n [!]  - Olá! Vamos dar início ao processo?\n")


print('\n #============================================================================================#')
#=================================================================================#
de = input('\n [!]  - Digite o seu Email: ')

print('\n #============================================================================================#')
#=================================================================================#
sen = getpass.getpass('\n [!]  - Digite a sua Senha: ')

print('\n #============================================================================================#')
#=================================================================================#
para = input('\n [!]  - Digite o Email do Alvo: ')

print('\n #============================================================================================#')
#=================================================================================#
msg = input('\n [!]  - Digite a Mensagem: ')

print('\n #============================================================================================#')

#=================================================================================#

vezes = int(input('\n [!]  - Digite a quantidade de mensagens a serem enviadas: '))

print('\n #============================================================================================#')


#=================================================================================#

print('\n [!]  - ESPERE 4 SEGUNDOS POR FAVOR.')
time.sleep(4) 

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
x = 1
smtp.login(de, sen)

while x <= vezes:
     smtp.sendmail(de, para, msg)
     print("\n [!]  - [%d Enviado Sucefull!]" % x)
     x += 1

      



print('''
KKK     KKK   III    SSSSSS     SSSSSS
KKK    KKK    III   SSSSSSS    SSSSSSS
KKK  KKKK     III   SSS        SSS
KKKKKK        III   SSSSSS     SSSSSS
KKKKKK        III   SSSSSSS    SSSSSSS
KKK  KKKK     III       SSS        SSS
KKK    KKK    III   SSSSSSS    SSSSSSS
KKK     KKK   III   SSSSSSS    SSSSSSS''')


time.sleep(6)
#sleep 6 secs




    


  
