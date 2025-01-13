# CLYMB Automation

This repository contains an automated testing framework for the CLYMB platform, implemented using the **Behave** BDD (Behavior-Driven Development) framework.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Reporting](#reporting)
- [Continuous Integration and Deployment](#continuous-integration-and-deployment)
- [Contributing](#contributing)
- [Support the Project](#support-the-project)

---

## Overview

The **CLYMB Automation** project uses `Behave` to define, manage, and execute BDD-style test cases. The framework includes features, step definitions, and utilities to automate end-to-end testing of the platform.

## Project Structure

The project is organized as follows:

```
CLYMB_AUTOMATION/
|-- .github/workflows/                       # CI/CD pipeline configuration
|   |-- build.yml                           # GitHub Actions workflow file
|
|-- assets/                                 # Additional assets for the project
|   |-- style.css                           # Stylesheets for reports
|
|-- features/                               # Behave features and steps
|   |-- steps/                              # Step definitions for Behave
|       |-- clymb.py          # Step definitions for test workflows
|       |-- appreciation_check.py               # Additional step definitions
|       |-- ...                                 # Other page-specific files
|   |-- clymb.feature               # Feature file for testing workflows
|   |-- appreciation_check.feature                    # Another feature file
|   |-- ...                                 # Other page-specific files
|
|-- pages/                                  # Page Object Model files
|   |-- login.py                            # Handles "login" functionality
|   |-- logout.py                           # Handles "logout" functionality
|   |-- admin_login.py                      # Handles "admin-login" functionality
|   |-- ...                                 # Other page-specific files
|
|-- utils/                                  # Utility functions and shared logic
|   |-- locators.py                         # Shared locators across pages
|   |-- audio.py                            # Utility for audio-related operations
|   |-- condition_for_negative_flow.py      # Utilities for handling negative flows
|   |-- ...                                 # Other utilities
|
|-- .env                                    # Environment variables file
|-- .gitignore                              # Files and directories to ignore in version control
|-- README.md                               # Project documentation and usage instructions
|-- requirements.txt                        # Python dependencies
|-- azure-pipelines.yml                     # Azure DevOps pipeline configuration
|-- Report.html                             # Test execution report (generated dynamically)
```

## Prerequisites

- Python 3.8 or higher
- Google Chrome or another supported browser
- ChromeDriver or the appropriate WebDriver for your browser
- `pip` (Python package installer)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CLYMB_AUTOMATION
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add configurations like base URL, credentials, and other sensitive information.

5. **Install WebDriver:**
   - Download the appropriate WebDriver for your browser.
   - Ensure the WebDriver path is added to your system's `PATH`.

## Running Tests

To execute all tests:
```bash
behave
```

To execute a specific feature file:
```bash
behave features/workflow.feature
```

To execute tests with specific tags:
```bash
behave --tags=@tag_name
```

To run tests in a headless browser mode:
```bash
behave --define browser=headless
```

## Reporting

To generate a detailed HTML report:
```bash
behave -f html -o Report.html
```

To generate a JSON report:
```bash
behave -f json -o Report.json
```

To open the HTML report:
```bash
start Report.html   # For Windows
open Report.html    # For macOS
```

## Continuous Integration and Deployment

### GitHub Actions

- The `build.yml` file in the `.github/workflows/` directory defines the CI pipeline.
- It automates the following steps:
  - Install dependencies.
  - Set up the environment.
  - Run tests.
  - Generate and upload test reports.

### Azure Pipelines

- The `azure-pipelines.yml` file defines the CI/CD pipeline for Azure DevOps.
- Steps include:
  1. Install Python and dependencies.
  2. Run tests with Behave.
  3. Publish test results and reports.

To trigger the pipeline:
1. Commit and push changes to the repository.
2. Ensure the pipeline is configured in the Azure DevOps project.

## Key Features

- **Behavior-Driven Development:** Scenarios are defined in Gherkin syntax for clarity and collaboration.
- **Reusable Step Definitions:** Common steps are shared across multiple features.
- **Modular Design:** Utility functions and locators are centralized for reusability.
- **Scalable Test Cases:** Organized and easy to extend for additional scenarios.
- **Customizable Reports:** Generate HTML and JSON reports with metadata like environment and tester name.

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

