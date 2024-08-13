# Wikipedia Selenium Automation

This project is a Selenium-based automation testing solution for Wikipedia using Python. The tests are structured using the Page Object Model (POM).

## Features

- **Selenium WebDriver**: Automates web browser interaction.
- **Page Object Model (POM)**: A design pattern for better test code maintainability.
- **Pytest**: A powerful testing framework for running and organizing test cases.
- **Configurable WebDriver**: The WebDriver setup is flexible, allowing for browser options like starting Chrome maximized.

## Project Structure

```plaintext
project/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── search_results_page.py
│
├── tests/
│   └── test_wikipedia_search.py
│
├── requirements.txt
├── README.md
└── conftest.py
```

- **`pages/`**: Contains Page Object Model (POM) classes for different pages.
- **`tests/`**: Contains test scripts.
- **`requirements.txt`**: Python dependencies for the project.
- **`README.md`**: This file.
- **`conftest.py`**: Pytest configuration and fixture setup.

## Getting Started

### Prerequisites

- **Operating System**: This guide assumes you are using a Unix-like OS (Linux, macOS), but it can be adapted for Windows.
- **Python 3.7 or Higher**: Ensure Python is installed on your machine.
- **Google Chrome**: Make sure the Google Chrome browser is installed.
- **ChromeDriver**: Ensure ChromeDriver is installed and accessible in your system's PATH.

### Installing Python

#### Linux/macOS:

Python 3 is usually pre-installed. You can verify this by running:

```bash
python3 --version
```
If Python 3 is not installed, install it via your package manager:

**Ubuntu/Debian:**

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```
**macOS (using Homebrew):**

```bash
brew install python3
```
**Windows:**

Download Python 3 from the official website: [python.org](https://www.python.org/).

### Checkout the Repository

Clone the repository:

```bash
git clone https://github.com/jacqueswest/wikipedia.git
cd wikipedia
```
### Setting Up a Virtual Environment (Optional but Recommended)

Create a virtual environment:

```bash
python3 -m venv venv
```
Activate the virtual environment:

**Linux/macOS:**

```bash
source venv/bin/activate
```
**Windows:**

```bash
venv\Scripts\activate
```
### Install the Project Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```
### Running the Tests

### Running the Tests with HTML Reporting

The project is configured to automatically generate an HTML report of the test results. Simply run the following command:

```bash
pytest tests/test_wikipedia_search.py
```


### Summary

- **`pytest.ini` Configuration**: By adding `--html=report.html --self-contained-html` to the `addopts` in `pytest.ini`, HTML reporting is now automatic.
- **Run Tests**: Simply run `pytest`, and the report will be generated automatically.
- **Open Report**: Simply run open report.html on windows. Or copy and paste the location path in your browser.
This setup ensures that every time you or someone else runs the tests, an HTML report will be created, making it easier to review and share the test results.

### Example of the HTML Test Report

![html_report.png](images%2Fhtml_report.png)