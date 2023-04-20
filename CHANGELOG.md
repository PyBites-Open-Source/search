# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.10] - 2023-04-20

### Added
- Caching requests calls by default. You can adjust the expiration using `CACHE_EXPIRATION_SECONDS`

### Changed
- This introduced a new method in the base class (`get_data`) to centralize use of `requests`

## [0.0.9] - 2023-04-18

### Added
- Added tests for all modules except cli.py
- Made the tool support 3.9 + 3.10 in addition to 3.11
- Set up tox to test all 3 Python versions

## [0.0.8]

### Changed
- Move podcast feed parsing to our platform

## [0.0.7]

### Added
- Added Pybites tips search

## [0.0.6]

### Added
- Added Pybites Podcast search

## [0.0.5]

### Added
- Added platform Bite (exercise) search

## [0.0.4]

### Added
- Added Pybites Youtube search

## [0.0.1] ... [0.0.3]

### Added
- Initial package creation on PDM code clinic
