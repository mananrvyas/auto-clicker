# Auto-Clicker for CEM 141

## Introduction

Don't you hate using iClicker, especially in CEM 141? And if it only has points for participation, why not automate it? :) Introducing **Auto-Clicker**: a lightweight script written in Python using Selenium that takes care of your iClicker participation for you.

## Features

- **Automate Participation:** Automatically handles iClicker participation in CEM 141, so you can focus on learning.
- **Lightweight:** A simple Python script that doesn't hog your resources.
- **Easy to Use:** Set it up once, and you're good to go for the entire semester.

## Requirements

Before you get started, you'll need to have a few things ready:

- **ChromeDriver:** Ensure you have ChromeDriver installed on your system. You can install it using Homebrew with the command: `brew install chromedriver`
- **Python:** This script is written in Python, so you'll need that installed as well.

## Installation

Follow these steps to get Auto-Clicker up and running:

1. **Install Requirements:** First, make sure you have ChromeDriver and Python installed on your system.
2. **Clone the Repo:** Clone this repository to your local machine or download the code directly.
    ```
    git clone github.com/mananrvyas/auto-clicker
    ```
3. **Install Python Dependencies:** Navigate to the cloned repository directory and install the required Python packages using pip.
    ```
    pip install -r requirements.txt
    ```
4. **Configure Environment:** Create a new file in the repository directory named `.env` and add your iClicker username and password in the following format:
    ```
    USERNAME = 'your_username_in_quotes'
    PASSWORD = 'your_password_in_quotes'
    COURSE_NAME = 'CXX 1XX'
    CLASS_DURATION = 'duration_in_seconds (eg: 5400)'
    ```

## Usage

Once everything is set up, you can run the script with the following command when your class starts:
  ```
  python auto-clicker.py
  ```

And that's it! You're welcome. Now, you can relax knowing your participation points are taken care of.

## Disclaimer

Please be aware of your institution's policies regarding automated participation and academic integrity. This tool is intended for educational purposes only, and users should use it responsibly.

## Contribution

Feel free to fork this repository, make improvements (use GPT vision API to provide correct answers?), or suggest changes by creating a pull request.

## License

This project is licensed under the MIT License.


