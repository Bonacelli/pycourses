from ExtratorArgumentosUrl import ExtratoArgumentosUrl

'''
cotacao = f'BRDT3 = {20,12}\nITSA4 = {8,50}'
print(cotacao)

index = cotacao.find("ITSA4")
print(index)
cotacao_ITSA4 = cotacao[index:]
print(cotacao_ITSA4)
'''

url = "https://twitter.com/home"
argumento = ExtratoArgumentosUrl(url)
print(argumento)

