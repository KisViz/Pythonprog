# Nev: Peter Tamas
# Neptun: JP85CD
# h: h376477
import datetime
import csv


def eltelt_ido(ora1:int, perc1:int, ora2:int, perc2:int) ->datetime.time:
    if ora1>ora2 or (ora1==ora2 and perc1>perc2):
        tmp=ora1
        ora1=ora2
        ora2=tmp
        tmp=perc1
        perc1=perc2
        perc2=tmp


    elso=datetime.datetime(2000,1,2,ora1,perc1)
    masodik=datetime.datetime(2000,1,2,ora2,perc2)

    if masodik < elso:
        masodik += datetime.timedelta(days=1)
    timee = masodik - elso

    osszes_sec = timee.total_seconds()
    #print(osszes_sec)
    hours = int(osszes_sec // 3600)
    minutes = int((osszes_sec % 3600) // 60)
    return datetime.time(hours, minutes)

# print("sima")
# print(eltelt_ido(1, 1, 3, 2))
# print(eltelt_ido(5, 23, 14, 9))
#
# print("nagyobb")
# print(eltelt_ido(22, 30, 1, 15))
# print(eltelt_ido(5, 43, 3, 55))
#
#
# print("azonos")
# print(eltelt_ido(10, 30, 10, 30))
# print(eltelt_ido(1, 1, 1, 1))
#
# print("kicsi")
# print(eltelt_ido(14, 59, 15, 0))
# print(eltelt_ido(3, 4, 3, 2))
#
# print("max")
# print(eltelt_ido(23, 59, 0, 0))
#
# print("max forditva")
# print(eltelt_ido(0, 0, 23, 59))



def kesesek(utvonal):
    adatok=[]
    maxi=None
    kiaz=None
    try:
        with open(utvonal, encoding="utf8") as fp:
            csv_reader = csv.reader(fp, delimiter=",")
            for row in csv_reader:
                for k in range(len(row)):
                    row[k]=row[k].strip()
                adatok.append(row)
            adatok=adatok[1:]
    except FileNotFoundError:
        return None
    # print(adatok)
    for i in adatok:
        nev=i[0]
        elvart=datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S")
        jott=datetime.datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S")
        #print(nev + " " + str(elvart) + " " + str(jott))
        if maxi is None or (jott-elvart) > maxi:
            maxi=jott-elvart
            kiaz=nev
    return kiaz



print(kesesek("adatok.csv"))