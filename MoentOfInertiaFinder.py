print("""************************************************
MOMENT OF INERTIA FINDER
************************************************
""")
print("""
Welcome to the program.
This program an consol program.
This program produced for help user when he/she trying the find and moment of inertia.
Program may be primitive and may be have problems because i am learning coding and i decided to try write a program about my lectures.
Program going to ask you for objects and their areas. 
First of all program going to fing center of area.
You have choice that you can find moment of inertia for (0,0).
This program Produced by Cagrı REIS-05/07/2022- You can find me at https://github.com/lastshady
""")
giris = input("For entering program press 'g', if you want tot leave program press 'q': ")
while (True):
    objeler = list()
    alansırası = []
    top_alan = 0
    x1_statik_moment = 0
    y1_statik_moment = 0
    sıralama = []
    IXX = 0
    IYY = 0
    IXXYY = 0
    if (giris == "g"):
        giris2 = input(
            "If you want to find moment of inertia for center of area press 'a', if you want for (0,0) press 's'. If you want to leave program press 'q': ")
        if (giris2 == "a"):
            obje_sayisi_1 = int(input("How many object that you want to study with?"))
            for obje in range(1, obje_sayisi_1 + 1):
                IXX = 0
                IYY = 0
                IXXYY = 0
                obje_tipi = input("Please enter your object type(circle, circle/2, circle /4, rectangle, triangle")
                if (obje_tipi == "rectangle"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        kenar1 = float(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = float(input("Please enter the second and last edge: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = - (kenar1 * kenar2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((kenar1*kenar2**3)/12)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    elif (deger == "+"):
                        kenar1 = float(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = float(input("Please enter the second and last edge: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = (kenar1 * kenar2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((kenar1 * kenar2 ** 3) / 12)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    else:
                        print("ERROR!")
                        break
                elif (obje_tipi == "triangle"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        kenar1 = float(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = float(input("Please enter the second and last edge: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = - (kenar1 * kenar2 / 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((kenar1 * kenar2 ** 3) / 36)
                        self_moment_inertia1 = (-(kenar1**2 * kenar2**2)/72)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia, self_moment_inertia1]
                        alansırası.append(dizi)
                    elif (deger == "+"):
                        kenar1 = float(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = float(input("Please enter the second and last edge: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = (kenar1 * kenar2 / 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((kenar1 * kenar2 ** 3) / 36)
                        self_moment_inertia1 = (-(kenar1**2 * kenar2 ** 2) / 72)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia, self_moment_inertia1]
                        alansırası.append(dizi)
                    else:
                        print("ERROR!")
                        break
                elif (obje_tipi == "circle"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        r = float(input("Enter your object's radius: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = - (3.14 * r ** 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((3.14 * r ** 4)/4)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    elif(deger == "+"):
                        r = float(input("Enter your object's radius: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = (3.14 * r ** 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((3.14 * r ** 4) / 4)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    else:
                        print("ERROR!")
                        break
                elif (obje_tipi == "circle/2"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        r = float(input("Enter your object's radius: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = - ((3.14 * r ** 2) / 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((3.14 * r ** 4) / 8)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    elif (deger == "+"):
                        r = float(input("Enter your object's radius: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = ((3.14 * r ** 2) / 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((3.14 * r **4)/8)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    else:
                        print("ERROR!")
                        break
                elif (obje_tipi == "circle/4"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        r = float(input("Enter your object's radius: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = - ((3.14 * r ** 2) / 4)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((3.14 * r ** 4) / 16)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    elif (deger == "+"):
                        r = float(input("Enter your object's radius: "))
                        x_coord = float(input("Enter your object's X coordinate: "))
                        y_coord = float(input("Enter your object's Y coordinate: "))
                        area = ((3.14 * r ** 2) / 2)
                        x_statik_moment = area * y_coord
                        y_statik_moment = area * x_coord
                        self_moment_inertia = ((3.14 * r ** 4) / 16)
                        dizi = [area, x_statik_moment, y_statik_moment, x_coord, y_coord, self_moment_inertia]
                        alansırası.append(dizi)
                    else:
                        print("ERROR!")
                        break
                else:
                    print("ERROR!")
                    break
            for i in range(0, obje_sayisi_1):
                top_alan = top_alan + alansırası[i][0]
                y1_statik_moment = y1_statik_moment + alansırası[i][1]
                x1_statik_moment = x1_statik_moment + alansırası[i][2]
            Xg = (x1_statik_moment / top_alan)
            Yg = (y1_statik_moment / top_alan)
            for k in range(0, obje_sayisi_1):
                if (len(dizi) == 7):
                    IXX = IXX + (alansırası[k][5] + alansırası[k][0] * (alansırası[k][3] - Yg) ** 2)
                    IYY = IYY + (alansırası[k][5] + alansırası[k][0] * (alansırası[k][4] - Xg) ** 2)
                    IXXYY = IXXYY + (alansırası[k][6] + alansırası[k][0] * (alansırası[k][4] - Xg) * (alansırası[k][3] - Yg))
                else:
                    IXX = IXX + (alansırası[k][5] + alansırası[k][0] * (alansırası[k][3] - Yg) ** 2)
                    IYY = IYY + (alansırası[k][5] + alansırası[k][0] * (alansırası[k][4] - Xg) ** 2)
                    IXXYY = IXXYY + (alansırası[k][0] * (alansırası[k][4] - Xg) * (alansırası[k][3] - Yg))
            I1 = (((IXX + IYY) / 2) + (((IXX - IYY) / 2) ** 2 + (IXXYY) ** 2) ** 0.5)
            I2 = (((IXX + IYY) / 2) - (((IXX - IYY) / 2) ** 2 + (IXXYY) ** 2) ** 0.5)
            print("Xg = {0}".format(Xg))
            print("Yg = {0}".format(Yg))
            print("IX = {0}".format(IXX))
            print("IY = {0}".format(IYY))
            print("IXY = {0}".format(IXXYY))
            print("I1 = {0}".format(I1))
            print("I1 = {0}".format(I2))
            # buraya final yazılacak.
        elif (giris2 == "s"):
            obje_sayisi_2 = int(input("How many object that you want to study with?"))
            for obje in range(1, obje_sayisi_2 + 1):
                obje_tipi = input("Please enter your object type(circle, circle/2, circle /4, rectangle, triangle): ")
                if obje_tipi == "circle":
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        r = int(input("Enter your object's radius: "))
                        x_coord = int(input("Enter your object's X coordinate: "))
                        y_coord = int(input("Enter your object's Y coordinate: "))
                        area = float((3.14 * r ** 2))
                        IX = - (float(3.14 * r ** 4) / 4 + area * float(y_coord + 0) ** 2)
                        IY = - (float(3.14 * r ** 4) / 4 + area * float(x_coord + 0) ** 2)
                        IXY = - (area * float(y_coord + 0) * float(x_coord + 0))
                        dizi = [area, IX, IY, IXY]
                        sıralama.append(dizi)
                    elif (deger == "+"):
                        r = int(input("Enter your object's radius: "))
                        x_coord = int(input("Enter your object's X coordinate: "))
                        y_coord = int(input("Enter your object's Y coordinate: "))
                        area = (3.14 * r ** 2)
                        IX = ((3.14 * r ** 4) / 4 + area * (y_coord) ** 2)
                        IY = ((3.14 * r ** 4) / 4 + area * (x_coord) ** 2)
                        IXY = (area * (y_coord) * (x_coord))
                        dizi = [area, IX, IY, IXY]
                        sıralama.append(dizi)
                    else:
                        print("ERROR!")
                        break
                elif (obje_tipi == "triangle"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        kenar1 = int(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = int(input("Please enter the second and last edge: "))
                        x_coord = int(input("Enter your object's X coordinate: "))
                        y_coord = int(input("Enter your object's Y coordinate: "))
                        area = (kenar1 * kenar2) / 2
                        IX = -((kenar1 * kenar2 ** 3) / 36 + area * (y_coord - 0) ** 2)
                        IY = -((kenar2 * kenar1 ** 3) / 36 + area * (x_coord - 0) ** 2)
                        IXY = -(-((kenar1**2 * kenar2**2)/72) + area * (y_coord - 0) * (x_coord - 0))
                        dizi = [area, IX, IY, IXY]
                        sıralama.append(dizi)
                    elif (deger == "+"):
                        kenar1 = int(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = int(input("Please enter the second and last edge: "))
                        x_coord = int(input("Enter your object's X coordinate: "))
                        y_coord = int(input("Enter your object's Y coordinate: "))
                        area = kenar1 * kenar2 / 2
                        IX = ((kenar1 * kenar2 ** 3) / 36 + area * (y_coord - 0) ** 2)
                        IY = ((kenar2 * kenar1 ** 3) / 36 + area * (x_coord - 0) ** 2)
                        IXY = (-(((kenar1**2 * kenar2**2)/72)) + area * (y_coord - 0) * (x_coord - 0))
                        dizi = [area, IX, IY, IXY]
                        sıralama.append(dizi)
                    else:
                        print("ERROR!")
                        break
                elif (obje_tipi == "circle/2"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        durum = input("If your circle's curve is facing down type 'n', if not type 'h': ")
                        if (durum == "n"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 2
                            IX = - ((3.14 * r ** 4) / 8 - (3.14 * r ** 2 / 2) * (4 * r / (3 * 3.14)) ** 2) + area * (y_coord - (4 * r / (3 * 3.14) ** 2)) ** 2
                            IY = - (3.14 * r ** 4 / 8) + (area) * (x_coord) ** 2
                            IXY = area * (y_coord - 0) * (x_coord - 0)
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "h"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 2
                            IX = - (((3.14 * r ** 4) / 8 - (3.14 * r ** 2 / 2) * (4 * r / (3 * 3.14)) ** 2) + area * (y_coord + (4 * r / (3 * 3.14) ** 2)) ** 2)
                            IY = - ((3.14 * r ** 4 / 8) + (area) * (x_coord) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        else:
                            print("ERROR!")
                            break
                    elif (deger == "+"):
                        durum = input("If your circle's curve is facing down type 'n', if not type 'h': ")
                        if (durum == "n"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 2
                            IX = (((3.14 * r ** 4) / 8 - (3.14 * r ** 2 / 2) * (4 * r / (3 * 3.14)) ** 2) + area * (y_coord - (4 * r / (3 * 3.14) ** 2)) ** 2)
                            IY = ((3.14 * r ** 4 / 8) + (area) * (x_coord) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "h"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 2
                            IX = (((3.14 * r ** 4) / 8 - (3.14 * r ** 2 / 2) * (4 * r / (3 * 3.14)) ** 2) + area * (y_coord + (4 * r / (3 * 3.14) ** 2)) ** 2)
                            IY = ((3.14 * r ** 4 / 8) + (area) * (x_coord) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        else:
                            print("ERROR!")
                            break
                    else:
                        print("HATA!")
                        break
                elif (obje_tipi == "circle/4"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        durum = input(
                            "If your circle's curve is facing down and facing left type'nl', if down and right type 'nr', if up and left type 'ul', if up and right type'ur' please: ")
                        if (durum == "nl"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord - (4 * r / (3 * 3.14))) ** 2)
                            IY = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord - (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "nr"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord - (4 * r / (3 * 3.14))) ** 2)
                            IY = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord + (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "ul"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord + (4 * r / (3 * 3.14))) ** 2)
                            IY = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord - (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "ur"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord + (4 * r / (3 * 3.14))) ** 2)
                            IY = - (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord + (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        else:
                            print("ERROR!")
                            break
                    elif (deger == "+"):
                        durum = input(
                            "If your circle's curve is facing down and facing left type'nl', if down and right type 'nr', if up and left type 'ul', if up and right type'ur' please: ")
                        if (durum == "nl"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord - (4 * r / (3 * 3.14))) ** 2)
                            IY = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord - (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "nr"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord - (4 * r / (3 * 3.14))) ** 2)
                            IY = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord + (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "ul"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord + (4 * r / (3 * 3.14))) ** 2)
                            IY = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord - (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        elif (durum == "ur"):
                            r = int(input("Enter your object's radius: "))
                            x_coord = int(input("Enter your object's X coordinate: "))
                            y_coord = int(input("Enter your object's Y coordinate: "))
                            area = (3.14 * r ** 2) / 4
                            IX = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (y_coord + (4 * r / (3 * 3.14))) ** 2)
                            IY = (((3.14 * r ** 4 / (16)) - (3.14 * r ** 4 / (4)) * (4 * r / (3 * 3.14)) ** 2) + (3.14 * r ** 2 / (4)) * (x_coord + (4 * r / (3 * 3.14))) ** 2)
                            IXY = (area * (y_coord - 0) * (x_coord - 0))
                            dizi = [area, IX, IY, IXY]
                            sıralama.append(dizi)
                        else:
                            print("ERROR!")
                            break
                    else:
                        print("HATA!")
                        break
                elif (obje_tipi == "rectangle"):
                    deger = input("If object is negative, please type '-', if positive, please type '+': ")
                    if (deger == "-"):
                        kenar1 = int(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = int(input("Please enter the second and last edge: "))
                        x_coord = int(input("Enter your object's X coordinate: "))
                        y_coord = int(input("Enter your object's Y coordinate: "))
                        area = kenar1 * kenar2
                        IX = -((kenar1 * kenar2 ** 3) / 12 + area * (y_coord - 0) ** 2)
                        IY = -((kenar2 * kenar1 ** 3) / 12 + area * (x_coord - 0) ** 2)
                        IXY = -(area * (y_coord - 0) * (x_coord - 0))
                        dizi = [area, IX, IY, IXY]
                        sıralama.append(dizi)
                    elif (deger == "+"):
                        kenar1 = int(input("Please enter the first edge (That must be parallel to x accent.) : "))
                        kenar2 = int(input("Please enter the second and last edge: "))
                        x_coord = int(input("Enter your object's X coordinate: "))
                        y_coord = int(input("Enter your object's Y coordinate: "))
                        area = kenar1 * kenar2
                        IX = ((kenar1 * kenar2 ** 3) / 12 + area * (y_coord - 0) ** 2)
                        IY = ((kenar2 * kenar1 ** 3) / 12 + area * (x_coord - 0) ** 2)
                        IXY = (area * (y_coord - 0) * (x_coord - 0))
                        dizi = [area, IX, IY, IXY]
                        sıralama.append(dizi)
                    else:
                        print("HATA!")
                        break
                else:
                    print("ERROR!")
                    break
            for i in range(0, obje_sayisi_2):
                IXX = IXX + sıralama[i][1]
                IYY = IYY + sıralama[i][2]
                IXXYY = IXXYY + sıralama[i][3]
            I1 = (((IXX + IYY) / 2) + (((IXX - IYY) / 2) ** 2 + (IXXYY) ** 2) ** 0.5)
            I2 = (((IXX + IYY) / 2) - (((IXX - IYY) / 2) ** 2 + (IXXYY) ** 2) ** 0.5)
            print("IX = {0}, IY = {1}, IXY ={2}, I1 = {3}, I2 = {4}".format(IXX, IYY, IXXYY, I1, I2))
            # buraya final yazılacak.
        elif (giris2 == "q"):
            print("Leaving.")
            break
        else:
            print("ERROR!")
            break
    elif (giris == "q"):
        print("Leaving.")
        break
    else:
        print("ERROR!")
        break