texto = input("Digite o texto a ser codificado: ")
dicionario = {
'a':'01','b':'02','c':'03','d':'04','e':'05','f':'06','g':'07','h':'08','i':'09','j':'10','k':'11','l':'12','m':'13',
'n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
}
lista_dict = []
for i in texto:
    i = i.lower()

    lista_dict.append(dicionario[i])
x =  " ".join(lista_dict)
print(" ".join(lista_dict))