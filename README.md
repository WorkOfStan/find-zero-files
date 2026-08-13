# find-zero-files

A simple tool for finding corrupted files on cloud drives. It checks the beginning of each file and reports files
whose inspected content consists entirely of zero bytes.

## Requirements

- Python 3.8 or newer
- No external libraries

## Usage

Pass the script the path to the directory that you want to scan recursively:

```powershell
python find_zero_files.py "G:\My Drive"
```

When quoting a Windows path, do not put a trailing backslash immediately before the closing quotation mark.

You can also use a relative path:

```powershell
python find_zero_files.py sample
```

## Output

Each processed non-empty file is displayed with its size:

- `SUSPICIOUS` - the inspected portion contains only zero bytes; displayed in red in a terminal.
- `OK` - the file passed the check; displayed in gray in a terminal.
- `Cannot read` - the file could not be opened or read.

At the end, the script displays the total number of files that passed the check and the number of suspicious files.
Empty files with a size of 0 bytes are skipped. Terminal colors are disabled when output is redirected to a file.

### Ignored extensions

Files with the following extensions are neither checked nor included in the summary:

- `.gdoc`
- `.gsheet`
- `.gslides`

Extensions are matched case-insensitively. You can modify the list in the `IGNORED_EXTENSIONS` constant in
`find_zero_files.py`.

Example:

```text
SUSPICIOUS: sample\190523_Contract_EMPTY.pdf  (11,576,977 bytes)
OK: sample\test.pdf  (14,704 bytes)

Files OK: 1
Suspicious files found: 1
```

## How the check works

The script reads the first 4,096 bytes of every non-empty file. If all the inspected bytes are zero, it marks the file
as suspicious. The tool does not modify file contents.

## Tests

The automated tests use the sample files in the `sample` directory:

```powershell
python -m unittest -v
```

The tests verify ordinary and suspicious PDF detection, ignored Google document extensions, and terminal colors.
