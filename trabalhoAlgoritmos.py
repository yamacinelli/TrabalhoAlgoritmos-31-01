import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host = "localhost", user = "yamacinelli", password = "765589", database = "cadastro")
    print('Conectado ao banco de dados!')
    cursor = db_connection.cursor()                  # CRIAÇÃO DO CURSOR LOGO NO INÍCIO PARA NÃO HAVER DUPLICAÇÕES

                                                                     #Criando o menu
    if(db_connection.is_connected):
        menu = True                       # VARIÁVEL CONTADORA PARA O LAÇO while DO MENU
        while(menu == True):
            print("=-"*20, "CADASTRO DE CLIENTES", "=-" * 20)
            print("""Menu\n
            Inserir[1]
            Editar[2]
            Excluir[3]
            Sair[4]""")
            opcao = int(input("Digite a opção: "))
            contadora_opcao1 = True               # VARIÁVEL CONTADORA, RESPONSÁVEL POR DAR INÍCIO OU FIM À REPETIÇÃO
            while (contadora_opcao1 == True):
                if (opcao == 4):
                    break
                if (opcao == 1):
                    nome = input("Nome do cliente: ")
                    cpf = str(input("CPF: "))
                    endereco = input("Endereço: ").strip()
                    numero_casa = input("Número: ")
                    cidade = input("Cidade: ")
                    estado = input("Estado: ")
                    pais = (input("País: "))
                                                                        # Inserindo os dados informados
                    adicionar = ("insert into pessoas"
                    "(nome, cpf, endereco, numero_casa, cidade, estado, pais)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                    dados_cliente = (nome, cpf, endereco, numero_casa, cidade, estado, pais )
                    cursor.execute(adicionar, dados_cliente)
                    db_connection.commit()                 # PROPRIEDADE QUE GRAVARÁ OS VALORES EXECUTADOS NO DB
                    print(f"\n{'='*15} Adicionado {cursor.rowcount} cadastro(s) ao Banco de Dados {'='*15}\n")         # ESTA PROPRIEDADE RETORNARÁ O Nº DE LINHAS QUE FORAM ADICIONADAS AO DB

                    outro = input(f"| REALIZAR OUTRO CADASTRO? [S/N] |\n")
                    outro = outro.upper()
                    if(outro == 'S'):
                        contadora_opcao1 = True
                    else:
                        contadora_opcao1 = False
                if(opcao == 2):
                    consulta = ("SELECT id, nome, cpf, endereco, numero_casa, cidade, estado, pais FROM pessoas;")
                    cursor.execute(consulta)
                    for (id, nome, cpf, endereco, numero_casa, cidade, estado, pais) in cursor:
                        print(f"| ID: {id} | NOME: {nome} | CPF: {cpf} | ENDEREÇO: {endereco} | Nº: {numero_casa} | CIDADE: {cidade} | ESTADO: {estado} | PAÍS: {pais} |")
                    break

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome do usuário ou senha incorretos")
    else:
        print(error)
        db_connection.close()               # CONEXÃO É INTERROMPIDA EM CASO DE ERRO