traducoes={'brasil':'Feliz Natal!',
           'alemanha':'Frohliche Weihnachten!',
           'austria':'Frohe Weihnacht!',
           'coreia':'Chuk Sung Tan!',
           'espanha':'Feliz Navidad!',
           'grecia':'Kala Christougena!',
           'estados-unidos':'Merry Christmas!',
           'inglaterra':'Merry Christmas!',
           'australia':'Merry Christmas!',
           'portugal':'Feliz Natal!',
           'suecia':'God Jul!',
           'turquia':'Mutlu Noeller',
           'argentina':'Feliz Navidad!',
           'chile':'Feliz Navidad!',
           'mexico':'Feliz Navidad!',
           'antardida':'Merry Christmas!',
           'canada':'Merry Christmas!',
           'irlanda':'Nollaig Shona Dhuit!',
           'belgica':'Zalig Kerstfeest!',
           'italia':'Buon Natale!',
           'libia':'Buon Natale!',
           'siria':'Milad Mubarak!',
           'marrocos':'Milad Mubarak!',
           'japao':'Merii Kurisumasu!'}
while True:
    try:
        lang=input()
        aux=0
        for tag,i in traducoes.items():
            if lang==tag:
                aux+=1
                print(i)
        if aux!=1:
            print("--- NOT FOUND ---")
    except EOFError:
        break
