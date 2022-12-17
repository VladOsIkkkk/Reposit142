def f():
    def fb():
        X = int(1)
        Y = int(1)
        Z = int()
        p = int(input("введите p (2<p<10) :"))
        print(p,"-ичная таблица умножения")
        for X in range(1,p):
            z=[]
            for Y in range(1,p):
                Z = (X * Y // p)*10 + (X * Y)%p
                z.append(Z)
            print(z)
    def fc():
        p = int(input("введите основание системы, p = "))

        Np = int(input(f"Исходное число N{p} = "))

        k = int(1)

        N10 = int(0)
        while not Np==0:
            N10 = N10 + (Np % 10) * k
            k = k * p
            Np = Np // 10
        print("N10 = ", N10)
    def fd():
        N10 = int(input("N10 ="))
        p = int(input("p ="))
        k = 1
        Np = 0
        while N10 != 0:
            Np = Np + (N10 % p) * k
            k = k * 10
            N10= N10 // p
        print(f"N{p} ={Np}")
    def fe():
        a='0123456789'
        nums=list(a)
        print(nums)
        b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
        hem=b.split()
        print(hem)
        for i in range(len(hem)):
            hem[i]=int(hem[i])
        print(hem)
        def distance(x,y):
            k=7
            for i in range(7):
                if x%10==y%10:
                    k=k-1
                x=x//10
                y=y//10
            return k
        cod=int(input("код"))
        min=distance(cod,hem[0])
        imin=0
        for i in range(10):
            D=distance(cod,hem[i])
            if D
        if min==0:
            print(f"код верный: символ {nums[imin]}")
        elif min==1:
            print(f"код исправлен: символ {nums[imin]}")
        else:print("Код неверный")

        def ff():
            morse_dic = {
                'а' : '.-',
                'б' : '-...',
                'в' : '.--',
                'г' : '--.',
                'д' : '-..',
                'е' : '.',
                'ж' : '...-',
                'з' : '--..',
                'и' : '..',
                'й' : '.---',
                'к' : '-.-',
                'л' : '.-..',
                'м' : '--',
                'н' : '-',
                'о' : '---',
                'п' : '.--.',
                'р' : '.-.',
                'с' : '...',
                'т' : '-',
                'у' : '..-',
                'ф' : '..-.',
                'х' : '....',
                'ц' : '-.-.',
                'ч' : '---.',
                'ш' : '----',
                'щ' : '--.-',
                'ъ' : '.--.-',
                'ы' : '-.--',
                'ь' : '-..-',
                'э' : '..-..',
                'ю' : '..--',
                'я' : '.-.-', 
}

word = input("Введите слово: ")

morse_word = '' 
for letter in word:
    letter = letter.lower()
    
    print(f"{letter}: {morse_dic[letter]}")
     
    
#-------------------------------------------------------------------
    a=int(input())
    sp ["1-таблица умножения"
        "2-перевод в десятичную систему счисления"
        "3-перевод из десятичной системы счисления"
        "4-Программа кода Хэмминга"
        "5-морзянка на python"]
    if a==1:
        fb()
    elif a==2:
	fc()
    elif a==3:
        fd()
    elif a==4:
        fe()
    elif a==5:
        ff()
    def fb():
        X = int(1)
        Y = int(1)
        Z = int()
        p = int(input("введите p (2<p<10) :"))
        print(p,"-ичная таблица умножения")
        for X in range(1,p):
            z=[]
            for Y in range(1,p):
                Z = (X * Y // p)*10 + (X * Y)%p
                z.append(Z)
            print(z)
        f()
        def fc()
            
            
	
