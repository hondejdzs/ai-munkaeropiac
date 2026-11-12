# DOKUMENTÁCIÓ
## AI Munkaerőpiac – Adatelemzés Python segítségével

### 1. Bevezetés

A projekt témája a mesterséges intelligencia munkaerőpiacának vizsgálata. A mesterséges intelligencia egyre nagyobb szerepet tölt be a modern gazdaságban, ezért fontos megvizsgálni, hogyan változnak az ehhez kapcsolódó munkalehetőségek, fizetések és elvárt készségek.

A program Python nyelven készült, és a NumPy könyvtár segítségével végez statisztikai számításokat.

### 2. A projekt célja

A projekt célja egy adatkészlet feldolgozása és elemzése öt összetett kérdés alapján.

Az elemzés segítségével megvizsgálható:
- Az AI-állások fizetési szintje.
- A tapasztalat és a fizetés kapcsolata.
- A leggyakoribb munkakörök.
- A munkavégzési formák közötti különbségek.
- A legkeresettebb technikai készségek.

### 3. Adatforrás

Az elemzéshez használt adatállomány a Kaggle oldaláról származik.

Adatkészlet neve:
Global AI Job Market & Salary Trends 2025

Adatforrás:
https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025

Az adatok CSV formátumban kerülnek beolvasásra.

### 4. Felhasznált technológiák

**Python:** A program elkészítéséhez használt programozási nyelv.

**NumPy:** Statisztikai számítások elvégzésére szolgáló könyvtár.

**CSV:** Az adatok tárolására és beolvasására használt fájlformátum.

**Visual Studio Code:** A program fejlesztési környezete.

### 5. Az elemzési kérdések bemutatása

#### 1. kérdés: Mekkora az AI-állások fizetése?

A program kiszámítja:
- Az átlagfizetést.
- A mediánfizetést.
- A legalacsonyabb fizetést.
- A legmagasabb fizetést.

Alkalmazott NumPy-függvények:
- `np.mean()`
- `np.median()`
- `np.min()`
- `np.max()`

#### 2. kérdés: Hogyan függ össze a tapasztalat és a fizetés?

A program tapasztalati szintenként csoportosítja az állásokat, majd kiszámítja az egyes csoportok átlagfizetését.

Cél: megvizsgálni, hogy a nagyobb szakmai tapasztalat együtt jár-e magasabb fizetéssel.

#### 3. kérdés: Melyek a leggyakoribb AI-munkakörök?

A program megszámolja az egyes munkakörök előfordulását, majd megjeleníti az öt leggyakoribbat.

A munkakörökhöz tartozó átlagfizetés is megjelenik.

#### 4. kérdés: Melyik munkavégzési forma fizet a legjobban?

A program három fő kategóriát vizsgál:
- Helyszíni munkavégzés.
- Hibrid munkavégzés.
- Távoli munkavégzés.

Az egyes kategóriák átlagfizetését hasonlítja össze.

#### 5. kérdés: Melyek a legkeresettebb technikai készségek?

A program megszámolja, hogy az álláshirdetésekben mely technikai készségek fordulnak elő leggyakrabban.

Az eredmény a tíz leggyakoribb készséget mutatja be.

### 6. A program működése

A program működése a következő lépésekből áll:

1. A szükséges könyvtárak betöltése.
2. A CSV-adatállomány megnyitása.
3. Az adatok beolvasása.
4. A hibás vagy hiányzó fizetési adatok kiszűrése.
5. Az adatok csoportosítása.
6. A statisztikai számítások elvégzése.
7. Az eredmények megjelenítése a konzolon.

### 7. Alkalmazott függvények

| Függvény | Feladat |
|---|---|
| `np.mean()` | Átlag számítása |
| `np.median()` | Medián számítása |
| `np.min()` | Minimum meghatározása |
| `np.max()` | Maximum meghatározása |
| `Counter()` | Előfordulások megszámlálása |
| `defaultdict()` | Adatok csoportosítása |

### 8. Összegzés

A projekt során egy modern témához kapcsolódó adatkészlet feldolgozása történt meg.

Az elemzés öt különböző szempont alapján vizsgálja az AI-munkaerőpiacot.

A feladat segítségével bemutatható a Python programozási nyelv, a NumPy könyvtár és az alapvető statisztikai adatelemzési módszerek alkalmazása.

### 9. Futtatás

A NumPy telepítése:

`pip install numpy`

A program indítása:

`python ai_munkaeropiac.py`

A program futtatásához az adatállománynak a Python-fájllal azonos mappában kell lennie.