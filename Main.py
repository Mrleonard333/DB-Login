from os import system
from time import sleep
import mysql.connector

TF = False

IDs = 0
Username = str()
Password = str()

# v Vai se conectar com o DataBase
conection = mysql.connector.connect(
    host='Host', 
    user='User', 
    password=r'Senha', 
    database='Database'
)
cursor = conection.cursor()

print('[Fundacao_Crypto] - [DB_Login]\n')
sleep(0.5)
SL = str(input('[S/N] Ja possui uma conta?: '))

# v Se não possui uma conta
if SL.upper() == 'S':
    cursor.execute('SELECT * FROM logs')
        # ^ Irá guardar todas as informações da tabela de logs

    Username = str(input('\nInsira o seu usuario: '))
    Password = str(input('Insira sua senha: '))
    Acount = f'{Username} {Password}'

                # v Vai separar os dados do database em uma lista
    for L in cursor.fetchall():
        Logs = f'{L[1]} {L[2]}' # < Vai pegar o usuario e senha
        
        if Acount == Logs: # < Se for igual ao usuario e senha colocadas
            TF = True
            print('\n[Processo de login feito com sucesso]')
            break
    
    if TF != True:
        print('[*Usuario não encontrado*]')
        cursor.close()
        conection.close()
        exit()

# v Se possui uma conta
if SL.upper() == 'N':
    cursor.execute('SELECT * FROM logs')

    Username = str(input('\nInsira o seu usuario: '))
    Password = str(input('Insira sua senha: '))

    for L in cursor.fetchall():
        Logs = f'{L[1]}' # < Vai pegar o usuario
        IDs += 1

        if Username == Logs: # < Se for igual ao usuario colocado
            TF = True
            print('\n[*Usuario já existe*]')
            cursor.close()
            conection.close()
            exit()

    if TF != True:
        IDs += 1
        cursor.execute(f'INSERT INTO logs (idlogs, username, password) VALUES ({IDs}, "{Username}", "{Password}")')
        # ^ Vai registrar a conta no database
        conection.commit()
        # ^ Irá salvar as alterações
        print('\n[Usuario cadastrado]')

sleep(0.5)
system('cls')

print(f'[Fundacao_Crypto] - [{Username}]\n')
sleep(0.5)
print('[1] Reescrever a senha')
sleep(0.5)
print('[2] Deletar o usuario')
sleep(0.5)
print('[3] Terminate')
sleep(0.5)
OT = int(input('\nQual operacao sera feita?: '))

# v Se for Reescrever a senha
if OT == 1:
    NewPassword = str(input('\nInsira sua nova senha: '))

    # v Vai mudar a senha antiga para a nova onde o usuario sejá igual ao do tester
    cursor.execute(f'UPDATE logs SET password = "{NewPassword}" WHERE username = "{Username}"')
    conection.commit()
    print('[Senha Modificada]')

# v Se for Deletar a conta
if OT == 2:
    try:
        # v Delete em logs, onde o username for igual ao username do tester
        cursor.execute(f'DELETE FROM logs WHERE username = "{Username}"')
        conection.commit()
        sleep(0.5)
        print('[Usuario Deletado]')
    except:
        sleep(0.5)
        print('[*Houve um erro*]')

cursor.close() # < Vai fechar o cursor
conection.close() # < Vai fechar a conexão do DataBase