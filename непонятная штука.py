import math 
def perevod(a,b):
    if b== "байт":
        a=a*2**3
    elif b== "килобайт":
        a=a*2**13
    elif b== "мегабайт":
        a=a*2**23
    elif b== "гигабайт":
        a=a*2**33
    return a 
def it(N):
    T = int(math.log2(2*N-1))
    return T
def inform():
    N ="1 - Мощность алфавита(N), "
    K ="2 - колво символов в тексте(K), "
    I ="3 - инф объём текста(I), "
    i ="0 - инф  символа(i), "
    print("что нужно найти? (",i,N,K,I,")")
    G=input("Введите нужную цифру: ")
    if G=="0":
        N=(input("Введите N \n"))
        K=int(input("Введите K \n"))
        I,V=int(input("Введите I \n")),input("""бит/байт/килобайт/
                                             мегабайт/гигабайт?\n""")
        if N=="":
            print(K*perevod(I,V))
        else: 
            print(it(int(N)))
    if G=="1":
        i=int(input("i-?\n"))
        print(2**i)
    if G=="3":
        K=int(input("K-?\n"))
        N=int(input("N-?\n"))
        i,V=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
             I=it(N)*K
        else:
            I=perevod(int(i),V)*K
        print(I)
    if G=="2":
        I,V1=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        i,V2=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        if i=="":
            K=perevod(I,V1)/it(N)
        else:
            K=perevod(I,V1)/perevod(int(i),V2)
        print(K)
def zvuk():
    N ="0 - количество уровней сигнала(N), "
    D ="1 - количество символов в тексте(D), "
    V ="2 - объём звуковоо файла(V), "
    i ="3 - глубина звука(i), "
    T ="4 - длительность звукового файла"
    print("Что нужно найти? (",N,D,V,i,T,")")
    G=input()
    if G=="0":
        i,b=int(input("i-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        print(2**perevod(i,b))
def isobr():
    print("isobr")
print("Какой тип задачи нужно решить? (звук, информация, изображение)")
A=input()
if A=="звук":
    zvuk()
if A=="информация":
    inform()
if A=="изображение":
    isobr()
