import re

"""
    Para testar as expressões regulares checar final do código.
"""
def Testar(expressao,lista): 
    # Função para testar a expressão regular imprimindo de forma organizada no terminal
    print("Expressão regular: ", expressao)
    for i in lista:
        res = re.fullmatch(expressao, i)
        if res == None:
            print(i,"=> cadeia recusada")
        else:
            print(i,"=> cadeia aceita")
        print()

def Arranjo(lis):
    # Função para utilizada na função de fazer lista de combinações possíveis da 2G
    lista = []
    for i in lis:
        lista.append(i)
        lista.append(i)
    for i,x in enumerate(lista):
        if i % 2 ==0:
            lista[i] += "H"
        else:
            lista[i] += "M"
    return lista

def CombinacaoG(x,y):
    # Função que retorna a lista propriamente dita
    listaI = ["H","M"]
    listaF = []
    aux = 2
    while(aux <= y):
        listaI = Arranjo(listaI)
        if aux >= x:
            listaF += listaI
        aux += 1
    return listaF

# Expressões regulares
reNome = re.compile(r"[A-Z][a-z]+ ([A-Z][a-z]+ )?[A-Z][a-z]+")
reEmail = re.compile(r"[a-z]+@[a-z]+((\.com\.br)|(\.br))")
reSenha = re.compile(r"(?=.*[A-Z])(?=.*[0-9])[A-z0-9]+")
reCPF = re.compile(r"([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}")
reTel = re.compile(r"((\([0-9]{2}\) 9[0-9]{4}-[0-9]{4})|(\([0-9]{2}\) 9[0-9]{4}[0-9]{4})|([0-9]{2} 9[0-9]{8}))")
reDataHorario = re.compile(r"[0-9]{2}/[0-9]{2}/[0-9]{4} [0-2][0-9]:[0-5][0-9]:[0-5][0-9]")
reNum = re.compile(r"[+ -]?[0-9]+(\.[0-9]+)?")
reA = re.compile(r"(HM|MH)((h*m+h*m+h*)+|(m*h+m*)+|h+mh+)")
reB = re.compile(r"(HM|MH)h*mh*(h*mh*mh*)*")
reC = re.compile(r"(MH|HM)m[h m]*h")
reD = re.compile(r"(MM|HH)(hm|mh)[h m]{2}[h m]*(hm|mh)")
reE = re.compile(r"(MM|HH)((hm)*|(mh)*)")
reF = re.compile(r"(MM|HH)(mm|hm|m)*h?")

# Listas de palavras para testar
listaNome = [
'Agnes Karimy Da Silva Maia',
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
listaCPF = [
"023.123.123-12",
"023-123.123.123",
"12.234.521-12",
"123.1.2.12-12",
"12312312311-12",
"abb.cac.aaa-ad",
"...-",
"123.456.789-12",
"567.234.111.12",
"555-555-555.12",
"000.000.000-00",
"123,456,789-12",
"@@@.@@@.@@@-@@",
"tes.tef.unc-io",
"soc.orr.ore-gi",
"b12.123.144-12",
"001.234.567-89",
    "002.345.678-90",
    "003.456.789-01",
"004.567.890-12",
"005.678.901-23",
"006.789.012-34",
"007.890.123-45",
"008.901.234-56",
"009.012.345-67",
"010.123.456-78",
"011.234.567-89",
"012.345.678-90",
"013.456.789-01",
"014.567.890-12",
"015.678.901-23",
"016.789.012-34",
"017.890.123-45",
"018.901.234-56",
"019.012.345-67",
"020.123.456-78",
"021.234.567-89",
"022.345.678-90",
"023.456.789-01",
"024.567.890-12",
"025.678.901-23",
"026.789.012-34",
"027.890.123-45",
"028.901.234-56",
"029.012.345-67",
"030.123.456-78",
"031.234.567-89",
"032.345.678-90",
"033.456.789-01",
"034.567.890-12",
"035.678.901-23",
"036.789.012-34",
"037.890.123-45",
"038.901.234-56",
"039.012.345-67",
"040.123.456-78",
"041.234.567-89",
"042.345.678-90",
"043.456.789-01",
"044.567.890-12",
"045.678.901-23",
"046.789.012-34",
"047.890.123-45",
"048.901.234-56",
"049.012.345-67",
"050.123.456-78",
"frasealeatoria",
"123456789",
"11.111.111/0001-01",
"22.222.222/0001-02",
"33.333.333/0001-03",
"44.444.444/0001-04",
"55.555.555/0001-05",
"66.666.666/0001-06",
"77.777.777/0001-07",
"88.888.888/0001-08",
"99.999.999/0001-09",
"00.000.000/0001-10",
"12.345-6",
"23-456.7",
"34.5678-",
"4567.-89",
"5-6789.0",
"6.7890-1",
"78901.-2",
"8-90123.4",
"9.01234-5",
"0.12345-6",
"11.111.111/0001-11",
"22.222.222/0001-12",
"33.333.333/0001-13",
"44.444.444/0001-14",
"55.555.555/0001-15",
]
listaTel = [
'(11) 93577-3929',
'(85) 97071-8702',
'(16) 99156-2881',
'(43) 98301-7459',
'(62) 98879-7994',
'(91) 95691-7905',
'(28) 96422-3786',
'(79) 93649-4475',
'(21) 95672-8266',
'(98) 98161-4495',
'(11) 94887-7285',
'(85) 96987-7758',
'(16) 94752-3042',
'(43) 99153-9107',
'(62) 93549-5717',
'(91) 94701-8348',
'(28) 95870-8642',
'(79) 95696-4702',
'(21) 97936-7117',
'(98) 97484-9711',
'(61) 983148921',
'(82) 992928634',
'(11) 978755428',
'(31) 981996344',
'(27) 985508503',
'(79) 985247854',
'(84) 981307091',
'(21) 985974459',
'(47) 989487753',
'(16) 983163252',
'(61) 982112363',
'(82) 991869655',
'(11) 982656661',
'(31) 988210347',
'(27) 984458915',
'(79) 985843327',
'(84) 981244145',
'(21) 986191310',
'(47) 985304692',
'(16) 988778901',
'50 997105678',
'63 992007154',
'82 988708400',
'71 998478551',
'47 987260791',
'61 997903182',
'32 989392065',
'89 998239123',
'19 990742445',
'60 995452939',
'15 997267057',
'28 997021885',
'64 989455832',
'68 995013740',
'20 996958440',
'17 994645725',
'66 999372700',
'80 991934550',
'83 999651171',
'18 997332594'
"(91) 992961708",
"(12)12345-9123",
"91 99999-9999",
"122 91234-1234",
"9 1912341234",
"92  912341234",
"91   912341234",
"91912341234",
"9112341234",
"(91 ) 91234-1234",
"(9 1) 91234-1234",
"( 91) 91234-1234",
" 91) 91234-1234",
" (91) 91234-1234",
"91 999999999",
"(912) 91234-1234",
"(9999) 912341234",
"(91) 92131-1231",
"(91) 921311231",
"91 912341234",
"00 900000000",
"xx 9xxxxxxxx",
"(xx) 9xxxxxxxx",
"(xx) 9xxxx-xxxx",
"xx 999990999",
"@@ 9@@@@@@@@",
"12 890312341",
"123 123412344",
"zz 9zzzz9zzz",
"12 987654321",
'923406788',
'3549470218',
'46701348012',
'887622674',
'2001141812',
'158084934',
'773880686',
'7543268023',
'6674319830',
'1006265297',
'6140583425',
'818811386',
'4917207886',
'4370032248',
'827223248',
'9010551967',
'7824339474',
'3041242777',
'2209723908',
'556632147',
'7498736206',
'2809661362',
'619417885',
'7752986896',
'9051650074'
]
listaDataHorario = []
listaNum = []
listaA = [
'HMhmm', 
'MHmm',
'HMmh',
'HMh', 
'HMhmhhhhh',
'HMmmmhm',
'MHhhh',
'HMhmhmh',
'HMmhm', 
'MHhmh', 
'MHhhhmmmhhmmh', 
'HMmmm', 
'HMhmmmh', 
'MHhhmh', 
'HMhhmhh',
'Hhmh', 
'mmHM', 
'HMm', 
'HHmh', 
'HMMhmm', 
'Mhmmh', 
'HmmhHmM', 
'mhhMmh', 
'HMh', 
'MHm', 
'MMm', 
'HMmmh', 
'MHHmm', 
'HMhMm', 
'hMmm'
]
listaB = [
'HMm', 
'HMhm', 
'MHmmmh', 
'HMmhhhh', 
'MHmhmmh', 
'HMhmhhmhmh', 
'MHhmhhmhmh', 
'HMhmh', 
'HMmmm', 
'HMmh', 
'MHmmmmm', 
'HMhmhmm', 
'MHmmmhmm', 
'MHmmmmmmm', 
'MHhmhhhhh', 
'MHhmhmhmhmhm',
'HMmm', 
'HMh', 
'MHmmmhm', 
'HMmmhhhh', 
'MHmmhmmh', 
'HMhmmhhmhmh', 
'MHhmmhhmhmh', 
'HMmhmh', 
'HMmmmm', 
'HMmmh', 
'MHmmmmmm', 
'HMhmmhmm', 
'MHmmmmhmm', 
'MHmmmmmmmm', 
'MHhmhmhhhh', 
'MHhmhmmhmhmhm']
listaC = []
listaD = [
"HHmhmmmmmmmhm",
"MMhmhhhhhhhhhmh",
"HHHMmmmmmmhm",
"HMmmmmmmhhhhm",
"hMHmmmmmhhhmm",
"HHhmMMMMMhM",
"MMmhmmmmmmmmhm",
"MMhmhm",
"HHhmmhm",
"MMmhhm",
"HMmhmh",
"HMmmmHH",
"HHmmmhhmh",
"MMhmhmmmh",
"HHmhmmmmhm",
"HHmhmmmmmhm",
"MMhhhhhmmh",
"HHmmmmhhhhmmm",
"HHHHHH",
"HHmhhhhHmh",
"MMmhmmmhm",
"MMhmhmhm",
"HHmhmmmhh",
"HHmhmhmhmhmhmhmhm",
"Hhmmmhmmhm",
"hhhmmmhmhmmmh",
"hmmhmmmhmmmmhh",
"HHmmmHHHmmmh",
"hhHMMMMhhmmh",
"hhHHmmmmhhm",
"MMhmhmmmhmhmmhm",
"mmhmmmmhmmhm",
"hmmhmhmmhmh",
"HHhmmmmmhmhmhmhmhm",
"MMhhhmhmhmmmhm",
"HHmhmmhmh",
"MMhhmhmhmhHHmm",
"MMhhmhmhhmh",
"mhmhmMHMHMHM",
"HHmmhmmhmhh",
"mhmhmhm",
"HHhmmhmh",
"HHHHHHHHHHH",
"MMMMMMMMM",
"HmhmhHmmh",
"HHMmhh",
"HmhmhmhmHMHM",
"HMHMHMHMH",
"HMmmm hmmhm",
"HHmhmhmmhmh",
"MMHhmhmhmhmh",
"MMHMHHmhmhmh",
"mmmHHMhmmh",
"HMmmhmmh",
"HMHMhmhmmh",
"mmmHmmmh",
"mmhmhmhmhm",
"HHmmhm",
"HHmmmhmmhmhm",
"HHmmmhmhmhmh",
"HHmhmhmhmhm",
"MMhmhmhmhm",
"MMhmhmhmhm"
]
listaE = [
'MMhmhmhmhmhmmmh','MH', 'MHmhmhmhmh', 'HHmhmhmhmh', 'MMMhmhmmmhmhmmhmh', 'HHhmhmhmhm', 'HMHMMHMhm', 'MMhmhmhmmmhHMmh', 'HHhmh','MMHMH', 'mmhmhmmmh', 'HHmhmhmhm', 
'h', 'MMmhmhmhh', 'mmmhmhmh', 'HHmhmhmhmh', 'MMhmhmmmh', 'MMhmhmhm', 'HHhmhmhmhmhmhm', 'HHmh', 'MMmh', 'MMhm', 'MMhmhmhmhm', 'H', 'M', 'HHMmhhmhmMMHMH', 'MMhmmmhmhm', 'HHmhmhmh',
'HMhmhmhm', 'MH', 'MHMHmhmhhmh', 'HMmhmhmmm', 'MHmhmmhmhmh', 'HMmhmhmmmmmmh', 'MMmmmmmm', 'Hmmhmmm', 'HHmmhmmmhhhhh', 'MMmhmmh', 'Hhmh', 'HHmhmhmh', 'HHmmMMMhmhmhMM', 'HmMmmHM', 
'MMmhmhmhm', 'MhmmH', 'HHmhmhmhm', 'HmmH', 'HmhmH', 'MMmhmhm', 'Mhmmhmhmhmhmhmhmh', 'HmmhmhmMmh', 'MhmhmhmMHMHmh', 'MMmmhmhm', 'HHmhmhmhmhmh', 'MMhmmhm', 'HHmhmhmhmhh', 'HHmhmhmmhmh',
'HHmhhmhm','MMhmhmhmh', 'Mhmhm', 'MHMHMMHM', 'MMHMmmhm', 'mhmhmhmmhMHMH', 'HHmmhmhm', 'HHmhmh', 'MMhmhmhmhmhm', 'HHmhmhmmmmhmhm', 'HHmhmhmhmh', 'MHMhmhm', 'MMHmhmhmhMHMHmhmhm',
'HHmhmhhm', 'MHMHmmhmhmMHMH', 'HHMHmhmhmh', 'HHmhmhmhm', 'HHmhmhmhmh', 'hhmhmh', 'mhmhmh', 'HmhmhmmhMMHMHM', 'MHMHmmhmmh', 'HHmhmhmhmhmhmhmhmh', 'HHmhmhm', 'HHmhmhhmHHMH','MHhm', 'M'
'MHMHMHMHMMHM', 'MHmh', 'hhMh', 'MHmhmhmhmh', 'MMmhmh', 'MMhmhm', 'MMhmhmhmhmMMHhmhm', 'MMhmhmMMHMHMH', 'mmhmhmMMHmhm', 'mhmh', 'mmmhmhmMhmhm', 'MMhmhmmhmhmhmhm', 'MMMhmHHHm', 'MM',
'HHHHHHHHH', 'MMMMMMMM', 'MMHmhmhmhm', 'MMMHMHMMHmhmhmhmmmhm', 'MhhMMHmhm', 'Mhmhmhmm', 'MMHmhmhmhhhhmhmhhh', 'MMHmmhmmmmmhmmhhhhhh', 'MMhmmmhmmmhmmh', 'HHHHmmmhhhhhhhmmhhh', 'HHmh',
'HHmmhhmhhh', 'HHmhmhmhmhhhhmmmmm', 'HHmhmhmhmhmh', 'MMhmhmmmmhmmhhhhmmh', 'HHmhmhmmhMHMHmhmmmh','HHMmhmhhh', 'HMhmhmmmhMHMH', 'HHMhmhmmhm', 'MMhmhmhmhm', 'HHmhmh', 'HHHHHmhmhmhhm']
listaF = [
'MMhmhmhmhmhmmmhh','MH', 'MHmhmhmhmhhhhh', 'HHmhmhmmmmhhmh', 'MMMhmhmhhhh', 'HHhmhmhmmhmhhhm', 'HMHMMHMhhhm', 'MMhmhmhmmmhHMmhh', 'HHhmhhh','MMHMhH', 'mmhmhhmmmh', 'HHmhmhmhm', 
'h', 'MMmhmhmhh', 'mmmhmhmh', 'HHmhmhmhmh', 'MMhmhmmmh', 'MMhmhmhm', 'HHhmhmhmhmhmhm', 'HHmh', 'MMmh', 'MMhm', 'MMhmhmhmhm', 'H', 'M', 'HHMmhhmhmMMHMH', 'MMhmmmhmhm', 'HHmhmhmh',
'HMhmhmhm', 'MH', 'MHMHmhmhhmh', 'HMmhmhmmm', 'MHmhmmhmhmh', 'HMmhmhmhhh', 'MMmmmmmmhhh', 'Hmmhhhmmm', 'HHmmhmmmhh', 'MMmhmmhh', 'Hhmh', 'HHmhmhmhhhh', 'HHmmMMMhmhhhmhMM', 'HmMmmHM', 
'MMmhmhmhm', 'MhmmH', 'HHmhmhmhm', 'HmmH', 'HmhmH', 'MMmhmhmhh', 'Mhmmhmhmhmhmhmhmh', 'HmmhmhmMmh', 'MhmhmhmMHMHmh', 'MMmmhmhm', 'HHmhmhmhmhmh', 'MMhmmhm', 'HHmhmhhmhmhh', 'HHmhmhmmhmh',
'HHmhhmhm','MMhmhmhmh', 'Mhmhm', 'MHMHMMHM', 'MMHMmmhm', 'mhmhmhmmhMHMH', 'HHmmhmhm', 'HHmhmh', 'MMhmhmhmhmhm', 'HHmhmhmmmmhmhm', 'HHmhmhmhmh', 'MHMhmhm', 'MMHmhmhmhmhhh', 'MMHhh'
'HHmhmhhm', 'MHMHmmhmhmMHMH', 'HHMHmhmhmh', 'HHmhmhmhm', 'HHmhmhmhmh', 'hhmhmh', 'mhmhmh', 'HmhmhmmhMMHMHM', 'MHMHmmhmmh', 'HHmhmhmhmhmhmhmhmh', 'HHmhmhm', 'HHmhmhhmHHMH','MHhm', 'M'
'MHMHMHMHMMHM', 'MHmh', 'hhMh', 'MHmhmhmhmh', 'MMmhmh', 'MMhmhm', 'MMhmhmhmhmMMHhmhm', 'MMhmhmMMHMHMH', 'mmhmhmMMHmhm', 'mhmh', 'mmmhmhmMhmhm', 'MMhmhmmhmhmhmhm', 'MMMhmHHHm', 'MM',
'HHHHHHHHH', 'MMMMMMMM', 'MMHmhmhmhm', 'MMMHMHMMHmhmhmhmmmhm', 'MhhMMHmhm', 'Mhmhmhmm', 'MMHmhmhmhhhhmhmhhh', 'MMHmmhmmmmmhmmhhhhhh', 'MMhmmmhmmmhmmh', 'HHHHmmmhhhhhhhmmhhh', 'HHmh',
'HHmmhhmhhh', 'HHmhmhmhmhhhhmmmmm', 'HHmhmhmhmhmh', 'MMhmhmmmmhmmhhhhmmh', 'HHmhmhmmhMHMHmhmmmh','HHMmhmhhh', 'HMhmhmmmhMHMH', 'HHMhmhmmhm', 'MMhmhmhmhm', 'HHmhmh', 'HHHHHmhmhmhhm',
'MMmhhhmhhhmhmhmhmhh', 'MMhhmhmmmhmhmhhh', 'MMhh', 'MM', 'HH', 'MMhmhmhhmhhhmh', 'HHhhmh', 'HHmhmhhhh', 'MmMHMHM', 'HHmhmhh', 'mMMhmmmhhhm', 'MMhmhhhmhh', 'hhhmhm', 'HHmmMhhh',
'MMMHmhhhhmhhh', 'MMhhmhhhhmh', 'MhhmmMMH', 'MMhhhhmhmhh', 'MMMhmhmh', 'HHmhmmmmhmhhhm', 'MMhmhhmmhmmm', 'MMhmmmm', 'HHmhmhhhm', 'MHmhmhmmmh', 'MMHMhhmhh', 'MMMHhhmmhh', 'mMMHMhm'
'MMHmhhhmhhmh', 'MMHmhhhhmhh', 'MHhhhhhmhh', 'MMHmhmmmmhMHMHmm', 'MMHmmhmhmmhmM', 'MMHmhmmh', 'mmhhmMHMMH', 'MMHMHmmhmmhmh' , 'mhmhmmMH' , 'MMHmmhm', 'hmMMHmh', 'MMMHmhmmhmh','MMhh']
listaG = [
"MMMh",
"HHm",
"HHmmmmmmmhhh",
"MMhhmhmhmhhhhmmhh",
"HHHHHHHHHHHHHHHHmhhmhmmm",
"HHHHHHHMMMMMMHHHHHmhmmhmmhhhh",
"HMmmmmhmhmhmhmhmh",
"HMH",
"HMHMHMHMMHmmmmmmmmmmm",
"H",
"HMmmmhmMhmMHMHMHM",
"MHMMHHMHMHMMHmmmmmhhhh",
"HHMHMMHHMMmmmmhmhmhmhm",
"HMHMHMHMHMmmmhmhmhmhm",
"HMHMHMHMHMmhmhmhmhh",
"HMHMHMHMMMMMHmhmmhhmhmh",
"HMHMHMHMHmhmhmhmhm",
"HMHMHMHMHMHhhhhhhhhh",
"HMMHMMMMMHHmmmmmmmmmhh",
"MHMMHmmhmhmhmhhmm",
"MMMMMHHHmmmhmhmh",
"MMMMMhmhmmhmh",
"MMMMMhhhhhhhhhm",
"MMMMMMMMhhh",
"MMMMMhmhmhmhmh",
"MMMMMMMMhhhmhmhmh",
"HHHHHHHHmmmmmhhhhhhm",
"HHHHHHmmmmmmmhm",
"HHHmmmmmmhmhmhhh",
"HHHHHHH",
"MMMMMMMMMMMM",
"HMhhhhhhm",
"MMMHmhmhmhmhmhmhh",
"MMMMHHHmmhmmhhm",
"MHMHMHMHHM",
"MMMHMHMHMHMHM",
"HMMHMHMHMHmmmmmhh",
"MMMMMMMHHHMmmhhh",
"MHMHMHMHMHMHMhmhhh",
"MMMMMMMMHhhhmmhm",
"MHMHMHMHMMHmmhmhmhm",
"HHHHHHMmmhmhmh",
"HMHMHMHMhmhmhmh",
"HHHHHmmmmmmmhhh",
"HMHHMmhmmhmhmhmhM",
"HHHHHHHHHHHHHHHHH",
"MMMMMMMMMMMMM",
"M",
"MHMmhmhmhmhm",
"MhmhmhmMHMhmh",
"MHmhmhmhmhmMHMm",
"HMMHMHMhhhmh",
"HMHMHMHMHmhmhmhm",
"HMHhmmhhmhmmmmh",
"HHMHMMHHMHMHMmhmmm",
"HMhmhmmhmmhhm",
"HMMMMMMHhmhmhmhmmh",
"MMHHHMMmmmmm",
"MMMMMhhhmhmhmhm",
"MHMMHMHmhmhmhmhmh",
"MHGMHMHMHMhmmmmh",
"HMHMHMhmmhmh",
"HMMMMMHmhmhmh",
"MHMHMMHMmmmmmh",
"HMMHMHMmmmh",
"HMMMMHHHmmmmhm",
"HMHMMMHMmmhhhhmm",
"HMMMMHMHHHHHMmm",
"HMMMMHMHMHMHHmmhhh",
"HMHMMHHmmhmhmhmhm",
"HMHMHHMMmmmhmhmhmh",
"HMHMhmhmmh",
"HMMMMHMHMMHmmmm",
"HMMMMHHMmhhmhmhhm",
"HMMHMHMmmhmhmhh",
"HMHmhmhmhh",
"MHMhmhmmmhh",
"HHmhmhmhmmhmh",
"HMmmhmhmmhm",
"HhHmmm",
"HHHmhmhmhh",
"MMhmhmhmmh",
"HHmmhmh",
"HMhmhmh",
"HHHmmmmhmhmh",
"MMmmmmmhhh",
"Hmmhmhmhmhh",
"HHHmmhmhmhmhh",
"HHHmmhmhmhmh",
"MMMhmhmhmh",
"HMHMhmmhmh",
]

#Para testar, remova do comentário o jogo da velha antes da função testar

#Nome
#Testar(reNome,listaNome)

#Senha
#Testar(reSenha,listaSenha)

#Email
#Testar(reEmail,listaEmail)

#CPF
#Testar(reCPF,listaCPF)

#Telefone
#Testar(reTel,listaTel)

#Data e Horario
#Testar(reDataHorario,listaDataHorario)

#Número com sinal
#Testar(reNum,listaNum)

#2A
#Testar(reA,listaA)

#2B
#Testar(reB,listaB)

#2C
#Testar(reC,listaC)

#2D
#Testar(reD,listaD)

#2E
#Testar(reE,listaE)

#2F
#Testar(reF,listaF)

#2G REMOVER TUDO ABAIXO DE DENTRO DO COMENTARIO E EXECUTAR PARA PODER TESTAR :)
""" x = int(input("Digite o valor mínimo: "))
y = int(input("Digite o valor máximo: "))

comb = CombinacaoG(x,y)
inicio = ""
for i in comb:
    inicio =inicio+ i + "|" 

inicio = inicio[:-1]
reG = re.compile(f"({inicio})[h m]*(?<!hhh)")
Testar(reG,listaG) """

#Para testar, remova do comentário o jogo da velha antes da função testar




