# Testing Guide for Magic-Case

This document provides comprehensive information about testing the magic-case library, including how to run tests, test organization, and best practices.

## Test Structure

The test suite is organized into logical categories for better maintainability and clarity:

### Test Files

- **`tests/test_magic_case.py`** - Main comprehensive test suite
- **`tests/conftest.py`** - Shared fixtures and utilities
- **`pytest.ini`** - Pytest configuration
- **`run_tests.py`** - Test runner script

### Test Categories

The test suite is organized into the following categories:

#### 1. Basic Functionality Tests (`TestBasicFunctionality`)
- Tests basic conversion functionality for each case class
- Covers single words, empty strings, and whitespace handling
- Uses parametrized tests for comprehensive coverage

#### 2. Edge Case Tests (`TestEdgeCases`)
- Tests numbers within words, acronyms, and punctuation
- Covers path edge cases and normalization behavior
- Tests boundary conditions and special scenarios

#### 3. Cross-Conversion Tests (`TestCrossConversion`)
- Tests conversion between different case types
- Covers conversion chaining and round-trip conversions
- Ensures consistency across all case types

#### 4. Error Handling Tests (`TestErrorHandling`)
- Tests invalid input type handling
- Covers validation rules for specific case types
- Tests error conditions and exception raising

#### 5. Validation Tests (`TestValidation`)
- Tests specific behavior of specialized case types
- Covers Hungarian notation, macro case, and snake case variants
- Tests normalization and prefix handling

#### 6. Integration Tests (`TestIntegration`)
- Tests complex conversion chains
- Covers real-world usage scenarios
- Tests mixed case inputs and complex transformations

#### 7. Performance Tests (`TestPerformance`)
- Tests large input handling
- Covers repeated conversions and memory efficiency
- Stress tests for robustness

#### 8. Base Class Tests (`TestBaseCase`)
- Tests the abstract base class functionality
- Covers initialization and method behavior
- Tests abstract method implementation

#### 9. Utility Tests (`TestUtilities`)
- Tests overall system consistency
- Covers class inheritance and instantiation
- Tests naming conventions and patterns

## Running Tests

### Prerequisites

Ensure you have the required dependencies installed:

```bash
# Install pytest and coverage tools
pip install pytest pytest-cov pytest-xdist

# Or using uv (recommended)
uv add --dev pytest pytest-cov pytest-xdist
```

### Basic Test Execution

#### Run All Tests
```bash
# Using pytest directly
python -m pytest tests/

# Using the test runner script
python run_tests.py
```

#### Run Specific Test Categories
```bash
# Run only fast tests (exclude slow and performance)
python run_tests.py --fast

# Run only unit tests
python run_tests.py --unit

# Run only integration tests
python run_tests.py --integration

# Run only performance tests
python run_tests.py --performance

# Run only edge case tests
python run_tests.py --edge-case

# Run only error handling tests
python run_tests.py --error-handling
```

#### Run Tests with Coverage
```bash
# Run with coverage report
python run_tests.py --coverage

# This will generate:
# - Terminal coverage report
# - HTML coverage report in htmlcov/
```

#### Advanced Options
```bash
# Run tests in parallel (4 workers)
python run_tests.py --parallel 4

# Run tests with verbose output
python run_tests.py --verbose

# Stop after first failure
python run_tests.py --stop

# Run tests matching a pattern
python run_tests.py -k "camel"

# Run tests with specific markers
python run_tests.py -m "not slow"
```

### Using Pytest Directly

You can also use pytest directly with various options:

```bash
# Run with specific markers
pytest -m "performance" tests/

# Run with coverage
pytest --cov=magic_case --cov-report=html tests/

# Run in parallel
pytest -n 4 tests/

# Run with specific test selection
pytest tests/ -k "test_camel_case"

# Run with different output formats
pytest --tb=long tests/
pytest --tb=line tests/
pytest --tb=no tests/
```

## Test Markers

The test suite uses pytest markers for categorization:

- **`@pytest.mark.slow`** - Marks slow-running tests
- **`@pytest.mark.integration`** - Marks integration tests
- **`@pytest.mark.performance`** - Marks performance tests
- **`@pytest.mark.edge_case`** - Marks edge case tests
- **`@pytest.mark.error_handling`** - Marks error handling tests

### Filtering by Markers

```bash
# Run only fast tests
pytest -m "not slow and not performance"

# Run only integration tests
pytest -m "integration"

# Run tests with multiple markers
pytest -m "edge_case or error_handling"
```

## Test Fixtures

The test suite provides several shared fixtures:

### `all_case_classes`
Returns a list of all available case classes for testing.

### `sample_texts`
Provides common test texts for various case conversions.

### `case_conversion_examples`
Provides examples of case conversions for comprehensive testing.

### `edge_case_texts`
Provides texts that test edge cases and boundary conditions.

### `invalid_inputs`
Provides invalid inputs that should raise exceptions.

### `performance_test_data`
Provides data for performance and stress testing.

## Writing New Tests

### Test Naming Conventions

- Test functions should start with `test_`
- Test classes should start with `Test`
- Use descriptive names that explain what is being tested

### Test Organization

```python
class TestNewFeature:
    """Test the new feature functionality."""
    
    def test_basic_functionality(self):
        """Test basic functionality of the new feature."""
        # Test implementation
        
    def test_edge_case(self):
        """Test edge case handling."""
        # Test implementation
        
    @pytest.mark.parametrize("input,expected", [
        ("test1", "result1"),
        ("test2", "result2"),
    ])
    def test_multiple_scenarios(self, input, expected):
        """Test multiple scenarios with parametrization."""
        # Test implementation
```

### Using Fixtures

```python
def test_with_fixtures(sample_texts, all_case_classes):
    """Test using shared fixtures."""
    for case_class in all_case_classes:
        # Test implementation using sample_texts
```

### Adding Markers

```python
@pytest.mark.performance
def test_performance_characteristic():
    """Test performance characteristics."""
    # Test implementation
```

## Test Coverage

### Coverage Goals

- **Line Coverage**: Target 95%+
- **Branch Coverage**: Target 90%+
- **Function Coverage**: Target 100%

### Running Coverage

```bash
# Generate coverage report
python run_tests.py --coverage

# View HTML report
open htmlcov/index.html
```

### Coverage Configuration

Coverage is configured in `pytest.ini` and can be customized:

```ini
[tool:pytest]
addopts = --cov=magic_case --cov-report=html --cov-report=term
```

## Continuous Integration

### GitHub Actions

The test suite is designed to work with GitHub Actions. Tests should:

- Run on multiple Python versions
- Include coverage reporting
- Run both unit and integration tests
- Provide clear failure reporting

### Pre-commit Hooks

Consider adding pre-commit hooks for:

- Running tests before commit
- Checking code coverage
- Running linting tools

## Debugging Tests

### Verbose Output

```bash
# Run with verbose output
python run_tests.py --verbose

# Or with pytest
pytest -v tests/
```

### Debugging Specific Tests

```bash
# Run only failing tests
pytest tests/ -k "test_name" -v

# Run with full traceback
pytest --tb=long tests/ -k "test_name"
```

### Using PDB

Add `import pdb; pdb.set_trace()` to your test code for interactive debugging.

## Best Practices

### 1. Test Isolation
- Each test should be independent
- Use fixtures for setup and teardown
- Avoid test interdependencies

### 2. Descriptive Names
- Test names should clearly describe what is being tested
- Use descriptive variable names
- Add docstrings to complex tests

### 3. Parametrized Tests
- Use `@pytest.mark.parametrize` for testing multiple scenarios
- Group related test cases together
- Provide clear parameter names

### 4. Edge Cases
- Test boundary conditions
- Test invalid inputs
- Test empty and extreme values

### 5. Performance Considerations
- Mark slow tests appropriately
- Use session-scoped fixtures for expensive setup
- Consider parallel execution for large test suites

### 6. Error Handling
- Test both success and failure cases
- Verify correct exception types and messages
- Test error conditions thoroughly

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're running tests from the correct directory
2. **Fixture Errors**: Check fixture scope and dependencies
3. **Coverage Issues**: Verify coverage configuration in `pytest.ini`
4. **Performance Issues**: Use markers to exclude slow tests during development

### Getting Help

- Check pytest documentation: https://docs.pytest.org/
- Review existing test patterns in the codebase
- Use verbose output to debug test failures
- Check test markers and filtering options

## Contributing

When adding new tests:

1. Follow the existing test organization patterns
2. Use appropriate test markers
3. Add comprehensive test coverage
4. Update this documentation if needed
5. Ensure tests pass on all supported Python versions

## Test Maintenance

### Regular Tasks

- Review test coverage reports
- Update tests when adding new features
- Remove obsolete tests
- Optimize slow-running tests
- Update test documentation

### Monitoring

- Track test execution time
- Monitor coverage trends
- Identify flaky tests
- Review test failure patterns
