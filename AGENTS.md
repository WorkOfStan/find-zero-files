# AGENTS.md

## Changes

Never remove comments. Remove comments only when they are todos that were solved, or translate them to English.

If `CHANGELOG.md` is present, describe changes there in English. Always start each changelog bullet with a verb in present tense and put it at the end of the appropriate section.

If needed, also update `CLAUDE.md` or `AGENTS.md`, whichever is present. If only `CLAUDE.md` is present, treat it as `AGENTS.md`. Keep both files in English.

Always make sure that there are no security issues in the code.

## Progress and verbose output

When adding functionality that can take noticeable time, update verbose mode progress output at the same time. Long-running stages should report when they start, periodic progress or heartbeat messages while they are running, and completion details where useful. Avoid leaving verbose users staring at a blank terminal during active work; a heartbeat around every 60 seconds is usually enough unless the surrounding code already uses a different cadence.

## Python style

Keep Python lines at or below 120 characters.

## Shell usage and PHPStan

On Windows, do not run `.sh` helper scripts directly from PowerShell. Use Git Bash explicitly.

For PHPStan:

```powershell
& "C:\Program Files\Git\bin\bash.exe" -lc "./blast.sh phpstan"
```

For PHPStan cleanup:

```powershell
& "C:\Program Files\Git\bin\bash.exe" -lc "./blast.sh phpstan-remove"
```

## Composer

When running Composer, use:

```powershell
$env:COMPOSER_CACHE_DIR = "$PWD\.composer-cache"
php "C:\ProgramData\ComposerSetup\bin\composer.phar" install
```

Do not modify Composer itself and do not run `composer self-update`.

## Python tests

When running tests, use:

```powershell
New-Item -ItemType Directory -Force .tmp
python -m pytest -q -p no:cacheprovider --basetemp=.tmp/pytest
```

Do not load pytest's cache plugin.

Ensure `.tmp` exists before running pytest because the configured `--basetemp` path expects its parent directory to already exist.

Do not inspect, lint, or recurse into `.tmp`, `.pytest-tmp`, `.pytest_cache`, `.venv`, or build artifacts.

If pytest temp cleanup fails on Windows, remove only `.tmp/pytest` and rerun tests serially.

## Python packaging

When verifying the package build, use:

```powershell
python -m build
```
