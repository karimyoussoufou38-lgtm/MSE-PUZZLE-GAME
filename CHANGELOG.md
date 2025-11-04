# Changelog

All notable changes to the MSE (Multiple Substitution Encryption) project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [29.0.0] - 2025-11-05

### Added
- Enhanced error handling and logging throughout the codebase
- `get_encryption_stats()` function for analyzing encryption metrics
- `verify_encryption()` function for testing encryption integrity
- Comprehensive unit test suite in `tests/test_mse.py`
- Detailed security analysis document (`docs/SECURITY_ANALYSIS.md`)
- Quick start guide (`QUICKSTART.md`) in English and French
- Example programs in `examples.py`
- Complete API documentation in README
- Type hints for better code clarity
- Input validation for all public functions

### Changed
- Improved README with bilingual documentation (EN/FR)
- Enhanced MSE.py with better exception handling
- Modernized code structure and formatting
- Updated documentation to include security disclaimers
- Improved code comments and docstrings

### Fixed
- Empty string handling
- Whitespace-only input validation
- Error messages are now more descriptive
- Clipboard functionality made optional (graceful degradation)

### Security
- Added detailed security analysis with break time estimations
- Documented vulnerabilities and limitations
- Clear warnings about inappropriate use cases
- Recommendations for proper cryptography when needed

### Documentation
- Added comprehensive README in English and French
- Created detailed security analysis report
- Added quick start guide
- Included usage examples
- API reference documentation
- Vulnerability assessment

## [28.0.0] - 2024-01-30

### Changed
- General code improvement and optimization
- Performance enhancements

## [27.x.x] - 2023

### Changed
- Various updates and bug fixes throughout 2023

## [Initial Release] - 2019-01-22

### Added
- Initial implementation of MSE encryption system
- Block A: Text complexification
- Block B: Character substitution
- Block C: Obfuscation layer
- Key library generation
- Configuration system
- Basic tools and utilities

---

## Version Naming Convention

MSE uses the following version naming convention:

**MAJOR.MINOR.PATCH [CODENAME]**

- **MAJOR**: Significant changes, breaking changes to API
- **MINOR**: New features, improvements, non-breaking changes
- **PATCH**: Bug fixes, small improvements
- **CODENAME**: Fun names for major versions

### Codenames
- v29.0.0: [Enhanced Edition]
- v28.0.0: [JOSH]

---

## Future Roadmap

### Planned for v30.0.0
- [ ] GUI interface for easier use
- [ ] Advanced obfuscation techniques
- [ ] Configurable encryption strength levels
- [ ] Integration with popular puzzle platforms
- [ ] Mobile app support
- [ ] Web-based encryption tool

### Under Consideration
- [ ] Custom character set support
- [ ] Multiple language databases
- [ ] Export/import encrypted puzzles
- [ ] Puzzle difficulty analyzer
- [ ] Collaborative puzzle creation tools

---

## Contributing

We welcome contributions! Please see CONTRIBUTING.md for guidelines.

Major contributors:
- Enron Group - Original author and maintainer

---

## Support

For questions, bug reports, or feature requests:
- Email: contact@enrongroup.fr
- Website: http://enrongroup.fr
- Issue Tracker: [GitHub Issues]

---

**Note**: This project prioritizes puzzle creation and educational value over cryptographic security. For securing sensitive data, please use industry-standard encryption solutions.
