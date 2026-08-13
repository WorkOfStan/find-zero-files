from pathlib import Path
import sys


CHECK_BYTES = 4096
IGNORED_EXTENSIONS = {".gdoc", ".gsheet"}
GRAY = "\033[90m"
RED = "\033[91m"
RESET = "\033[0m"


def colored(text, color):
    if sys.stdout.isatty():
        return f"{color}{text}{RESET}"
    return text


def scan(root):
    found = []
    ok_count = 0

    for path in Path(root).rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in IGNORED_EXTENSIONS:
            continue

        try:
            size = path.stat().st_size
            if size == 0:
                continue

            with path.open("rb") as file:
                data = file.read(CHECK_BYTES)

            if data and all(byte == 0 for byte in data):
                message = f"PODEZŘELÝ: {path}  ({size:,} bytes)"
                print(colored(message, RED))
                found.append(path)
            else:
                message = f"OK: {path}  ({size:,} bytes)"
                print(colored(message, GRAY))
                ok_count += 1

        except Exception as error:
            print(f"Nelze přečíst: {path}: {error}")

    print()
    print(f"Souborů v pořádku: {ok_count}")
    print(f"Nalezeno podezřelých souborů: {len(found)}")
    return found


if __name__ == "__main__":
    scan(Path(sys.argv[1]))
