import re

email1 = "Meu numero é 91234-5678"
email2 = "99876-5432 é meu celular"

padrao = "[0-9]{5}-[0-9]{4}"

retorno1 = re.search(padrao, email1)
print(retorno1.group())
retorno2 = re.search(padrao, email2)
print(retorno2.group())