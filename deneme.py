name=input("name:")
print(f"hello {name}")
hak=10
kelime="can"
list=[]
for x in kelime:
    list.append("-")



while hak > 0:
    for index,_ in enumerate(range(len(kelime))):
        print(list[index])


    tahmin=input("tahmininiz: ")
    if tahmin in kelime:
        index=kelime.index(tahmin)
        list[index]=tahmin

        print(list)

        if "".join(list)==kelime:
            print("tebrikler") 
            break
    elif tahmin not in kelime and hak>0:
        hak-=1
        print(f"yanlış bildiniz hak sayınız {hak}")
    else:
        print("öldünüz") 
                      