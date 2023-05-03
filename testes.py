import re

"""
    Para testar as expressões regulares checar final do código.
"""


reNome = re.compile(r"[A-Z][a-z]+ ([A-Z][a-z]+ )?[A-Z][a-z]+")
reEmail = re.compile(r"[a-z]+@[a-z]+((\.com\.br)|(\.br))")
reSenha = re.compile(r"(?=.*[A-Z])(?=.*[0-9])[A-z0-9]+")

listaNome = ['Agnes Karimy Da Silva Maia',
'Alexandre Rogerio Andrade Moraes', 
'Allan Marcelo Trindade De Amorim' ,
'Amanda Leite De Alcantara',
'Andreya Cristina Bentes De Paiva', 
'Antonio Henrique De Assis De Matos' ,
'Arthur Duarte Montoril',
'Arthur Guimaraes Elleres' ,
'Arthur Henrique Azevedo Pimentel' ,
'Braz Gabriel Silva De Souza' ,
'Brendo Vieira De Freitas' ,
'Caio Julio Santos Da Silva' ,
'Carlos Eduardo Alvares Branco' ,
'Cristiano Da Silva Monteiro' ,
'Daniel Diniz Da Silva' ,
'Davi Brasil Franco' ,
'Davison Logan Dos Santos Cardoso' ,
'Deyvid Da Silva Lima' ,
'Elton Santos Torres' ,
'Gabriel Da Silva Pereira ',
'Gabriel Sodre Do Amaral' ,
'Isabel Dos Reis Camarao' ,
'Joao De Deus Da Conceicao Dias Neto',
'Joao Thalis Silveira Bezerra' ,
'Joao Vitor Yokoyama Nobayashi' ,
'Jose Gabriel Silva Pereira' ,
'Livia Emanuelle Carrera Soares Da Silva' ,
'Luan Matheus Silva Farias' ,
'Luan Sousa De Souza' ,
'Lucas Correa Magno' ,
'Luis Felipe Fernandes Cardoso' ,
'Luiz Antonio Lima De Freitas Leite' ,
'Luiz Sergio Samico Maciel Filho' ,
'Maria Heloisa Pinheiro Silva' ,
'Mario Roberto Lima Pinto' ,
'Mario Roberto Lima Pinto' ,
'Maverick Rescem Mescouto De Moraes' ,
'Max Jose Lobato Pantoja Junior' ,
'Nina Niwa Shibata' ,
'Pedro Miranda Duarte De Castro' ,
'Rafael Araujo Tenorio' ,
'Ramon Henrique Pereira Neves' ,
'Thiago Correa De Castro' ,
'Thyago Ronald Santos Da Silva' ,
'Tiago Oliveira Da Silva' ,
'Victor Hugo Goncalves De Oliveira' ,
'Wesley Pontes Barbosa' ,
'Yuri Gabriel Cardoso Delgado' ,
'Yuri Gabriel Menezes Ferreira' ,
'Yuri Luiz Silva Do Nascimento',
]

listaEmail = [
'agneskarimymaia@gmail.com',
'alexandre.moraes@icen.ufpa.br',
'allan.amorim@icen.ufpa.br',
'amanda.leite.a@gmail.com',
'andreya.paiva@icen.ufpa.br',
'henrickmatos17@gmail.com',
'amontoril1@gmail.com',
'arthur.elleres@itec.ufpa.br',
'azevedoarthur001@gmail.com',
'brazsdsgabriel@gmail.com',
'brendofreitasvieira@gmail.com',
'caiojuliosilv@gmail.com',
'carlos.branco@icen.ufpa.br',
'crismonteiro673@gmail.com',
'danieldinizbelem@gmail.com', 
'davifranco04@gmail.com',
'logancardoso4@gmail.com', 
'deyvid.baby@gmail.com',
'elton.torres@icen.ufpa.br',
'gabriel.pereira@icen.ufpa.br',
'gabrielsodredocs@gmail.com',
'isabel.camarao@icen.ufpa.br', 
'netodiasj1234@gmail.com',
'joao.silveira.bezerra@icen.ufpa.br',
'joaovitoryoko@gmail.com',
'josegab12@outlook.com',
'lixipluv@gmail.com',
'luan.farias_bvs@outlook.com',
'luansousa894@gmail.com',
'lucascorreamagno@gmail.com',
'luisfelipefcardoso@gmail.com',
'luiz_fleite@outlook.com',
'luiz.filho@icen.ufpa.br',
'mariahelloisa971@gmail.com',
'mrlimaroberto@gmail.com',
'mbastos95@gmail.com',
'maveri.rescem@gmail.com',
'max.junior@icen.ufpa.br',
'nina.shibata@gmail.com',
'pedro7mirand@gmail.com',
'rafael.tenorio@icen.ufpa.br',
'ramonhenrique27r@gmail.com',
'thiago.correa@icen.ufpa.br',
'thyagoronald8@gmail.com',
'tiagoliveira003@gmail.com',
'victorhhugo128@gmail.com',
'wesleypontes50879@gmail.com',
'yuri.0n333@gmail.com',
'ferreirayuri0901@gmail.com',
'luizyuri57@gmail.com',
]

listaSenha = [
    'JHKHJsdfdf9',
    'sdfsdfsdsf',
    'asdasd4425H',
    'asdasdadsDFDF555',
    'batatinha1213',
    'Batatinha1213',
    '554654asdasdKLJK',
    'asdas2421423dasFDFFF',
    'at45645689yutljjDGHyutyu',
    'batata13',
    'Pedro123',
    'asdasH21',
    'asasJ54a',
    'asd4sJja',
    'sdfsSfk5',
    'asdasdav',
    '45454545',
    'JJKJKJFK',
    'asdasdiwer9',
    'tiago666',
    'Tiago666',
    'ada12345',
]

#Nome
""" print("Expressão regular: ", "[A-Z][a-z]+ ([A-Z][a-z]+ )?[A-Z][a-z]+")
for i in listaNome:
    res = re.fullmatch(reNome, i)
    if res == None:
        print(i,"=> cadeia recusada")
    else:
        print(i,"=> cadeia aceita")
    print()
 """


#Senha
""" print("Expressão regular: ", "(?=.*[A-Z])(?=.*[0-9])[A-z0-9]+")
for i in listaSenha:
    res = re.fullmatch(reSenha, i)
    if res == None:
        print(i,"=> cadeia recusada")
    else:
        print(i,"=> cadeia aceita")
    print()
 """

#Email
""" print("Expressão regular: ", "[a-z]+@[a-z]+((\.com\.br)|(\.br))")
for i in listaEmail:
    res = re.fullmatch(reEmail, i)
    if res == None:
        print(i,"=> cadeia recusada")
    else:
        print(i,"=> cadeia aceita")
    print() """


#Para testar, remova do comentário o bloco de código da expressão regular a ser testada.
