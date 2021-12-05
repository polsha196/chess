import logging
logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

print("Введите координаты первого поля, на котором стоит Ваша фигура")
while True: 
    k=input("Координата по вертикали: ")
    try:
        val=int(k)
        if 0<int(k)<9:
            break    
        else:
            raise ValueError
    except ValueError:
        logging.error("Введена неверная координата по вертикали для начального поля!")
        print("Введено некорректное значение. Попробуйте еще раз!")
while True:
    l=input("Координата по горизонтали: ")
    try:
        val=int(l)
        if 0<int(l)<9:
            break
        else:
            raise ValueError
    except ValueError:
        logging.error("Введена неверная координата по горизонтали для начального поля!")
        print("Введено некорректное значение. Попробуйте еще раз!")
k=int(k)
l=int(l)
print("Введите координаты второго поля, куда должна прийти Ваша фигура")
while True:
    m=input("Координата по вертикали: ")
    try:
        val=int(m)
        if 0<int(m)<9:
            break
        else:
            raise ValueError
    except ValueError:
        logging.error("Введена неверная координата по вертикали для конечного поля!")
        print("Введено некорректное значение. Попробуйте еще раз!")
while True:
    n=input("Координата по горизонтали: ")
    try:
        val=int(n)
        if 0<int(n)<9:
             break
        else:
            raise ValueError
    except ValueError:
        logging.error("Введена неверная координата по горизонтали для конечного поля!")
        print("Введено некорректное значение. Попробуйте еще раз!")
m=int(m)
n=int(n)
if (k+l)%2 == (m+n)%2:
    print("Поля одного цвета")
else:
    print("Поля разного цвета")
print("Какая фигура стоит на первом поле? (ферзь, ладья, слон, конь)")
while True:
    figure=list(input()) 
    if figure == list("слон"):
        if (k+l)%2 != (m+n)%2:
            print("Слон не угражает данному полю") 
        elif abs(k-m) == abs(l-n):
            print ("Слон угрожает данному полю и может дойти до него за один ход")
        else: 
            print("Слон может дойти до данного поля за два хода")
            for i in range (-8,8):
                if abs(k*i-m) == abs(l*i-n):
                    print(abs(k*i)%8, abs(l*i)%8," -координаты поля после первого хода")
        break
    elif figure == list("ладья"):
        if k==m or l==n :
            print ("Ладья угрожает данному полю и может дойти до него за один ход")
        else: 
            print("Ладья может дойти до данного поля за два хода")
            S=abs(k-m)
            k=abs(k-S)
            print(k, l," -координаты поля после первого хода")
        break
    elif figure == list("ферзь"):
        if k==m or l==n or abs(k-m) == abs(l-n) :
            print ("Ферзь угрожает данному полю и может дойти до него за один ход")
        else: 
            print("Ферзь может дойти до данного поля за два хода")
            S=abs(k-m)
            k=abs(k-S)
            print(k, l," -координаты поля после первого хода")
        break
    elif figure == list("конь"):
        if abs(k-m)==1 and abs(l-n)==2 or abs(k-m)==2 and abs(l-n)==1 :
            print ("Конь угрожает данному полю и может дойти до него за один ход")
        else: 
            print("Конь не угрожает данному полю")
        break
    else:
        logging.error("Неверное название фигуры!")
        print("Введено некорректное значение. Попробуйте еще раз")


