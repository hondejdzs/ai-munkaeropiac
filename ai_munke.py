import csv
import numpy as np
from collections import Counter, defaultdict

import os

FAJL = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "ai_job_dataset.csv"
)

def szam_ertek(ertek):
    try:
        return float(str(ertek).replace(",", "").replace("$", "").strip())
    except (ValueError, TypeError):
        return None

def atlag(lista):
    if lista:
        return np.mean(lista)
    return 0

def main():

    try:
        with open(FAJL, "r", encoding="utf-8-sig") as fajl:
            adatok = list(csv.DictReader(fajl))
    except FileNotFoundError:
        print("Nem található a CSV fájl!")
        return

    if not adatok:
        print("Az adatfájl üres!")
        return

    szukseges = [
        "salary_usd",
        "job_title",
        "experience_level",
        "remote_ratio",
        "required_skills"
    ]

    for oszlop in szukseges:
        if oszlop not in adatok[0]:
            print("Hiányzó oszlop:", oszlop)
            return

    fizetesek = []
    tapasztalat = defaultdict(list)
    munkakorok = Counter()
    munkakor_fizetes = defaultdict(list)
    tavmunka = defaultdict(list)
    keszsegek = Counter()

    for sor in adatok:

        fizetes = szam_ertek(sor["salary_usd"])

        if fizetes is None or fizetes <= 0:
            continue

        fizetesek.append(fizetes)

        szint = sor["experience_level"].strip()
        munkakor = sor["job_title"].strip()

        tapasztalat[szint].append(fizetes)
        munkakorok[munkakor] += 1
        munkakor_fizetes[munkakor].append(fizetes)

        remote = sor["remote_ratio"].strip()

        if remote == "0":
            tipus = "Helyszini"
        elif remote == "50":
            tipus = "Hibrid"
        elif remote == "100":
            tipus = "Tavmunka"
        else:
            tipus = "Egyeb"

        tavmunka[tipus].append(fizetes)

        skill_szoveg = sor["required_skills"].replace("|", ",")

        for skill in skill_szoveg.split(","):
            skill = skill.strip()

            if skill:
                keszsegek[skill] += 1

    if not fizetesek:
        print("Nincs elemezhető fizetési adat!")
        return

    print("\n===== AI MUNKAERŐPIAC ELEMZÉSE =====")
    print("Elemzett álláshirdetések:", len(fizetesek))

    # 1. kérdés: Fizetések elemzése
    print("\n1. ÁTLAGOS FIZETÉSEK")

    print("Átlag:", round(np.mean(fizetesek), 2), "USD")
    print("Medián:", round(np.median(fizetesek), 2), "USD")
    print("Minimum:", np.min(fizetesek), "USD")
    print("Maximum:", np.max(fizetesek), "USD")

    # 2. kérdés: Fizetés tapasztalat szerint
    print("\n2. FIZETÉS TAPASZTALAT SZERINT")

    for szint, ertekek in sorted(tapasztalat.items()):
        print(
            szint,
            "átlag:",
            round(atlag(ertekek), 2),
            "USD"
        )

    # 3. kérdés: Leggyakoribb munkakörök
    print("\n3. LEGGYAKORIBB MUNKAKÖRÖK")

    for nev, darab in munkakorok.most_common(5):
        print(
            nev,
            "-",
            darab,
            "állás",
            "- átlagfizetés:",
            round(atlag(munkakor_fizetes[nev]), 2)
        )

    # 4. kérdés: Munkavégzés és fizetés kapcsolata
    print("\n4. FIZETÉS MUNKAVÉGZÉS SZERINT")

    for tipus, ertekek in sorted(tavmunka.items()):
        print(
            tipus,
            "- átlagfizetés:",
            round(atlag(ertekek), 2),
            "USD"
        )

    # 5. kérdés: Leggyakoribb készségek
    print("\n5. LEGGYAKORIBB KÉSZSÉGEK")

    for nev, darab in keszsegek.most_common(10):
        print(nev, "-", darab, "előfordulás")

    print("\n===== AZ ELEMZÉS BEFEJEZŐDÖTT =====")


if __name__ == "__main__":
    main()