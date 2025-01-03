# CLYMB_AUTOMATION

## Overview
This project is a Selenium-based test automation framework written in Python. It uses pytest as the testing framework and is designed to test the functionality of the CLYMB application.

## Project Structure
The project is organized as follows:

```
CLYMB_AUTOMATION/
|-- pages/                                      # Page Object Model files  
|   |-- login.py                                # Handles login page functionality  
|   |-- logout.py                               # Handles logout page functionality  
|
|-- tests/                                      # Test cases for various functionalities  
|   |-- __init__.py                             # Marks this directory as a Python package  
|   |-- clymb.py                                # Test cases related to CLYMB functionality  
|   |-- clymb_reload_refresh_check.py           # Tests for reload and refresh scenarios  
|   |-- clymb_positiveflow_with_ifcondition.py  # Tests positive flow scenarios with conditional logic  
|   |-- clymb_test.py                           # General tests for CLYMB features  
|   |-- clymb_appreciation_submit.py            # Tests for submitting appreciation under various scenarios  
|   |-- appreciation_check.py                   # Tests for appreciation functionality  
|   |-- ask_for_help.py                         # Tests scenarios involving 'ask for help' feature  
|
|-- utils/                                      # Utility functions and shared logic  
|   |-- aftermood.py                            # Manages 'after mood' functionality  
|   |-- appreciation.py                         # Contains logic for appreciation functionality  
|   |-- audio.py                                # Provides audio-related utilities  
|   |-- condition_for_negative.py               # Utilities for handling negative conditions  
|   |-- emotions_function.py                    # Utilities for emotion-related operations  
|   |-- locators.py                             # Centralized locators for web elements  
|   |-- responsible_decision_making.py          # Functions for responsible decision-making  
|   |-- self_management.py                      # Utilities for self-management features  
|   |-- social_awareness.py                     # Functions for promoting social awareness  
|
|-- .env                                        # Environment variables file  
|-- .gitignore                                  # Specifies files and directories to ignore in version control  
|-- README.md                                   # Project documentation and usage instructions  
|-- Reports.html                                # Consolidated HTML report for multiple tests  
```
## Prerequisites
- Python 3.8 or higher
- Google Chrome or another supported browser
- ChromeDriver or the appropriate WebDriver for your browser

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CLYMB_AUTOMATION
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add a `.env` file for environment variables (e.g., base URL, credentials).

## Running Tests

To execute all tests:
```bash
pytest
```

To execute a specific test file:
```bash
pytest tests/<test_file_name>.py
```

To generate a detailed report:
```bash
pytest --html=report.html --self-contained-html
```
To generate a customized detailed report:
```bash
pytest --html=report.html --self-contained-html --metadata "Environment" "Production" --metadata "Tester" "Your Name"
```
To open report
```bash
pytest start report.html
```
To execute a specific test file to generate report :
```bash
pytest tests/<test_file_name>.py --html=report.html --self-contained-html --metadata "Environment" "Production" --metadata "Tester" "Your Name"
```

## Key Features
- **Page Object Model (POM):** All web page interactions are encapsulated in the `pages` directory.
- **Reusable Utilities:** Commonly used functions and locators are located in the `utils` directory.
- **Environment Management:** Supports `.env` file for configurable variables.
- **Scalable Test Cases:** Organized in the `tests` directory, with dedicated files for specific features and scenarios.

## Contribution
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

Happy Testing!
