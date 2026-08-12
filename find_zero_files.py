from pathlib import Path
import sys

root = Path(sys.argv[1])
CHECK_BYTES = 4096

found = []

for path in root.rglob("*"):
    if not path.is_file():
        continue

    try:
        if path.stat().st_size == 0:
            continue

        with path.open("rb") as f:
            data = f.read(CHECK_BYTES)

        if data and all(b == 0 for b in data):
            print(f"PODEZŘELÝ: {path}  ({path.stat().st_size:,} bytes)")
            found.append(path)

    except Exception as e:
        print(f"Nelze přečíst: {path}: {e}")

print()
print(f"Nalezeno podezřelých souborů: {len(found)}")
