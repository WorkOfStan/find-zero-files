# find-zero-files

Jednoduchý nástroj pro vyhledání poškozených souborů na cloudových discích.
Kontroluje začátek každého souboru a upozorní na soubory, jejichž obsah tvoří
pouze nulové bajty.

## Požadavky

- Python 3.8 nebo novější
- žádné externí knihovny

## Použití

Skriptu předejte cestu ke složce, kterou chcete rekurzivně prohledat:

```powershell
python find_zero_files.py "G:\My Drive"
```

(Bacha na to nedávat lomítko na konec před uvozovku.)

Lze použít také relativní cestu:

```powershell
python find_zero_files.py sample
```

## Výstup

Každý zpracovaný neprázdný soubor se vypíše spolu se svou velikostí:

- `OK` – soubor je v pořádku; v terminálu se zobrazuje šedě.
- `PODEZŘELÝ` – kontrolovaná část obsahuje pouze nulové bajty; zobrazuje se
  červeně.
- `Nelze přečíst` – soubor se nepodařilo otevřít nebo načíst.

Na konci skript vypíše celkový počet podezřelých souborů. Prázdné soubory
o velikosti 0 bajtů se přeskakují. Při přesměrování výstupu do souboru se
nepoužívají terminálové barvy.

Příklad:

```text
PODEZŘELÝ: sample\190523_Smlouva_EMPTY.pdf  (11,576,977 bytes)
OK: sample\test.pdf  (14,704 bytes)

Nalezeno podezřelých souborů: 1
```

## Jak kontrola funguje

Z každého neprázdného souboru se načte prvních 4 096 bajtů. Pokud jsou všechny
nulové, soubor je označen jako podezřelý. Nástroj obsah souborů nemění.

## Testy

Automatické testy používají vzorové soubory ve složce `sample`:

```powershell
python -m unittest -v
```

Test ověřuje rozpoznání běžného i podezřelého PDF a správné terminálové barvy.
