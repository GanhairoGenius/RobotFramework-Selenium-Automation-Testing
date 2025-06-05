# 🤖 RobotFramework-Selenium-Automation-Testing

This project demonstrates a Selenium-based web automation testing framework built using Robot Framework and custom Python keywords. It follows best practices such as the Page Object Model (POM), modular test design, and integration with unit testing via pytest.

## 📂 Project Structure

```
RobotFramework-Selenium-Automation-Testing/
│
├── Tests/
│   ├── Test_Case_1.robot        # Robot Framework test case Version 1
│   ├── Test_Case_2.robot        # Robot Framework test case Version 2
├── Libraries/
│   ├── __init__.py              # Makes the folder a Python package
│   ├── Custom_keywords.py       # Custom Python keywords used in tests
│
├── Page_Interactions.py         # Page Object classes: DropdownElement & ContextMenu
│
├── Unit_Tests.py                # Pytest unit tests with mocks for Page_Interactions
└── README.md                    # This file
```

## Features

- Automates browser interaction using Robot Framework and SeleniumLibrary.
- Custom keywords written in Python using LibraryComponent.
- Follows Page Object Model (POM) design pattern.
- Includes unit tests using pytest and unittest.mock.
- Modular and maintainable folder structure.

## Test Cases

The Robot Framework Test cases performs:

1. Opens the browser and navigates to the target URL.
2. Accepts cookie banners.
3. Scrolls down the webpage.
4. Changes UI theme via dropdown to Materaial Main(Version 2 uses Custom Keywords) .
5. Applies underline formatting via context menu. (Version 2 uses Custom Keywords)
6. Takes a screenshot.

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/GanhairoGenius/RobotFramework-Selenium-Automation-Testing.git
cd RobotFramework-Selenium-Automation-Testing
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

##  Running the Tests

### Robot Framework Tests:
```bash
robot Tests/Test_Case_1.robot
```
```bash
robot Tests/Test_Case_2.robot
```

### Unit Tests (Pytest):
```bash
pytest Unit_Test.py
```

## 🛠️ Troubleshooting

If you see `No module named 'Custom_keywords'` or `'Page_Interactions'`, set the Python path:

```bash
export PYTHONPATH=$PYTHONPATH:./Libraries
```

Or in VS Code, add this to `.vscode/settings.json`:
```json
{
  "robot.pythonpath": [
    "Libraries"
  ]
}
```

## Screenshots

Screenshots are saved automatically in the specified `${SCREENSHOT_PATH}` variable after the test runs.
![image](https://github.com/user-attachments/assets/0c91572b-5dfe-4553-a9f6-1f7099aaac54)
