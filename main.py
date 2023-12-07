etelnev=["húsleves", "paradicsomleves", "gyümölcsleves"]
etelar=[1200,1100,2000]

""" Most annyi lista van, ahány tulajdonsága az adott ételnek! """

""" Úgy lenne a jobb, ha csak 1 listánk lenne, és 1 ételnek egybe kezelnénk a tulajdonságait! 
Létrehozunk egy étel típust - ez az étel általános leírását jelenti.
Konkrét étel a típus példányosításakor jön létre. """

print('Az első leves ára', etelnev[0],etelar[0])

from Etel import Etel
etelek=[]
etel=Etel("Húsleves",1200,"Leves") #pélányosítás
etelek.append(etel)
etel=Etel("Paradocsimleves",1100,"Leves")
etelek.append(etel)
etel=Etel("Pörkölt",2300,"Főétel")
etelek.append(etel)

for i in range(0, len(etelek), 1):
    print(f"Az {i}. étel: {etelek[i].nev}, {etelek[i].ar}, {etelek[i].tipus}")

print()
from Szemely import Szemely
szemelyek=[]
szemely=Szemely("Attila", 2004, 243521)
szemelyek.append(szemely)
szemely=Szemely("Levi", 2001, 876744)
szemelyek.append(szemely)
szemely=Szemely("István", 2003, 938672)
szemelyek.append(szemely)

for i in range(0, len(szemelyek), 1):
    print(f"A {i+1}. személy: {szemelyek[i].nev}, {szemelyek[i].szuldatum}, {szemelyek[i].szszam}")
    print(f"{szemelyek[i].nev}, {szemelyek[i].kor()} éves")
