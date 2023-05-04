import re

""" 
    Todas as questões serão executadas no arquivo teste.py com uma lista de expressões.
    Para executar o programa, use a função fullmatch, que recebe a expressão regular e 
    uma string.
    Resolução da primeira questão.
"""

reNome = re.compile(r"[A-Z][a-z]+ ([A-Z][a-z]+ )?[A-Z][a-z]+")

reEmail = re.compile(r"[a-z]+@[a-z]+((\.com\.br)|(\.br))")

reSenha = re.compile(r"(?=.*[A-Z])(?=.*[0-9])[A-z0-9]+")

reCPF = re.compile(r"([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}")

reTel = re.compile(r"((\([0-9]{2}\) 9[0-9]{4}-[0-9]{4})|(\([0-9]{2}\) 9[0-9]{4}[0-9]{4})|([0-9]{2} 9[0-9]{8}))")

reDataHorario = re.compile(r"[0-9]{2}/[0-9]{2}/[0-9]{4} [0-2][0-9]:[0-5][0-9]:[0-5][0-9]")

reNum = re.compile(r"[+ -]?[0-9]+(\.[0-9]+)?")

""" Resolução da segunda questão. """

reA = re.compile(r"(HM|MH)((h*m+h*m+h*)+|(m*h+m*)+|h+mh+)")

reB = re.compile(r"(HM|MH)h*mh*(h*mh*mh*)*")

reC = re.compile(r"(MH|HM)m[h m]*h")

reD = re.compile(r"(MM|HH)(hm|mh)[h m]{2}[h m]*(hm|mh)")

reE = re.compile(r"(MM|HH)((hm)*|(mh)*)")

reF = re.compile(r"(MM|HH)(mm|hm|m)*h?")

# reG está na página de testes apenas já que sua formação depende 
# de algumas funções para funcionar de forma correta :)
