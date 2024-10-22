# Contribution Guidelines

Thank you for your interest in contributing to our Python open-source project! To ensure a smooth collaboration and maintain code quality, please follow the guidelines below.

## Table of Contents

- [Code Style](#code-style)
- [Object-Oriented Design](#object-oriented-design)
- [Don't Repeat Yourself (DRY)](#dont-repeat-yourself-dry)
- [Testing](#testing)
- [Continuous Integration and Testing](#continuous-integration-and-testing)
- [Linting and Formatting](#linting-and-formatting)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Additional Recommendations](#additional-recommendations)

## Code Style

- **PEP 8 Compliance**: Ensure your code adheres to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- **Consistent Naming**: Use clear and descriptive names for variables, functions, and classes.
- **Line Length**: Limit all lines to a maximum of 79 characters.
- **Comments and Docstrings**: Provide docstrings for modules, classes, and functions. Use comments to explain complex logic.

## Object-Oriented Design

- **Encapsulation**: Use classes and objects to encapsulate data and functionality.
- **Inheritance and Polymorphism**: Utilize inheritance to promote code reuse and polymorphism for flexibility.
- **Modularity**: Break down large modules into smaller, manageable classes or functions.

## Don't Repeat Yourself (DRY)

- **Code Reusability**: Avoid code duplication by reusing functions or classes.
- **Abstraction**: Abstract common functionality into utility functions or base classes.
- **Refactoring**: If you notice repeated code, consider refactoring it into a shared component.

## Testing

- **Unit Tests**: Write unit tests for new features and bug fixes using `pytest`.
- **Coverage**: Aim for at least **80% test coverage**.
- **Running Tests**:

  ```bash
  poetry run pytest --cov=concord tests/
  ```

- **Test Cases**: Include edge cases and validate expected exceptions.

## Continuous Integration and Testing

We use **GitHub Actions** to automatically run tests and linters on all pull requests and commits to the `main` branch. To ensure your contributions pass these checks, please follow the instructions below.

### Prerequisites

- Python 3.12 or higher.
- **Poetry** installed for dependency management.

### Installing Dependencies

1. **Install Poetry**:

   ```bash
   # For Unix/macOS
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   For other installation methods, refer to the [Poetry documentation](https://python-poetry.org/docs/#installation).

2. **Install Project Dependencies**:

   Navigate to the project directory and run:

   ```bash
   poetry install
   ```

   This will create a virtual environment and install all required packages, including development dependencies.

3. **Activate the Virtual Environment** (Optional):

   ```bash
   poetry shell
   ```

   Alternatively, you can prefix commands with `poetry run` without activating the shell.

## Linting and Formatting

- **Linters**: Use linters to enforce coding standards.

    - **Flake8**: For code style and quality checks.

      ```bash
      poetry run flake8 concord/
      ```

    - **Black**: For automatic code formatting.

      ```bash
      poetry run black concord/
      ```

- **Pre-Commit Hooks**: Set up pre-commit hooks to automate linting and testing before each commit.

    1. **Install Pre-Commit Hooks**:

       ```bash
       poetry run pre-commit install
       ```

    2. **Run Pre-Commit on All Files** (Optional):

       ```bash
       poetry run pre-commit run --all-files
       ```

## Commit Messages

- **Format**: Use clear and descriptive commit messages.

    - Start with a short summary (50 characters max).
    - Follow with a blank line and a detailed description if necessary.

- **Conventional Commits**: Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for consistency.

## Pull Request Process

1. **Open a Pull Request**:

    - Fork the repository and create your feature branch.
    - Go to the original repository on GitHub.
    - Click on "New Pull Request" and select your fork and branch.
    - Provide a descriptive title and detailed description of your changes.

2. **Address Feedback**:

    - Be responsive to code review comments.
    - Make necessary changes and push them to your branch.

## Additional Recommendations

- **Issue Tracking**: Reference any related issues in your pull request description.
- **Documentation**: Update the project's documentation to reflect your changes.
- **Dependencies**: Avoid introducing new dependencies unless absolutely necessary.
- **Security**: Be mindful of security implications in your code.

---

By adhering to these guidelines, you help maintain the project's quality and ensure a seamless collaboration experience. If you have any questions, feel free to reach out to the maintainers.

Thank you for your contributions!
