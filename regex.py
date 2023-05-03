import re

""" Para executar o programa, use a função fullmatch, que recebe a expressão regular e 
    uma string.
    Resolução da primeira questão.
"""


reNome = re.compile(r"[A-Z][a-z]+ ([A-Z][a-z]+ )?[A-Z][a-z]+")

reEmail = re.compile(
    r"[A-Z0-9]*[a-z]+[A-z0-9]*@[A-Z0-9]*[a-z]+[A-z0-9]*((\.com\.br)|(\.br))")

reSenhas = re.compile(r"[A-z0-9]{8}")

reCPF = re.compile(r"([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}")

reTel = re.compile(
    r"((\([0-9]{2}\) 9[0-9]{4}-[0-9]{4})|(\([0-9]{2}\) 9[0-9]{4}[0-9]{4})|([0-9]{2} 9[0-9]{8}))")

reDataHorario = re.compile(
    r"[0-9]{2}/[0-9]{2}/[0-9]{4} [0-2][0-9]:[0-5][0-9]:[0-5][0-9]")

reNum = re.compile(r"[+ -]?[0-9]+(\.[0-9]+)?")

print(re.fullmatch(reNome,"Arthur Guimaraes Elleres"))

""" Resolução da segunda questão. """



reB = re.compile(r"(HM|MH)h*mh*(h*mh*mh*)*")

reC = re.compile(r"(MH|HM)m[h m]*h")

reD = re.compile(r"(MM|HH)(hm|mh)[h m]{2}[h m]*(hm|mh)")

reE = re.compile(r"(MM|HH)(hm)|(mh)")

reF = re.compile(r"(MM|HH)(mm|hm|m)*(h|mh)?")

reG = re.compile(r"(M|H)+(h|m)*(m|mh|mhh)|\\s|h|hh")
