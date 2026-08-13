# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### `Added` for new features

### `Changed` for changes in existing functionality

### `Deprecated` for soon-to-be removed features

### `Removed` for now removed features

### `Fixed` for any bugfixes

### `Security` in case of vulnerabilities

## [0.1.0] - 2026-08-13

feat: check all files in a folder for not containing just zeroes

### Added

- Scans directories recursively and checks the first 4,096 bytes of every non-empty file for zero-only content.
- Skips Google Docs, Sheets, and Slides placeholder files and reports unreadable files without stopping the scan.
- Displays color-coded results, file sizes, and a final summary of files that passed the check and suspicious files.
- Includes automated tests and sample PDF files for ordinary and suspicious-file detection.

[Unreleased]: https://github.com/WorkOfStan/find-zero-files/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/WorkOfStan/find-zero-files/releases/tag/v0.1.0
