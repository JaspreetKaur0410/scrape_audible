# Scrape Audible

This project is designed to scrape book data from [Amazon Audible](https://www.audible.com/search) using Python. The data includes key attributes of audiobooks such as title, author, narrator, and book length.

## Features

The script extracts the following attributes:
- **Title**: Name of the audiobook.
- **Author**: Author of the audiobook.
- **Narrator**: Narrator of the audiobook.
- **Length**: Duration of the audiobook.

## Tools & Technologies

- **IDE**: PyCharm
- **Language**: Python
- **Libraries**:
  - `selenium` (for web scraping)
  - `pandas` (for data processing and storage)

---


## Getting Started

### Instructions in Code

```bash
# Step 1: Clone the Repository
git clone https://github.com/yourusername/scrape_audible.git
cd scrape_audible

# Step 2: Create a Virtual Environment
python -m venv virtualenv

# Step 3: Activate the Virtual Environment
# On Windows:
virtualenv\Scripts\activate

# On macOS/Linux:
source virtualenv/bin/activate

# Step 4: Install Required Packages
pip install selenium pandas

# Step 5: Download and Configure ChromeDriver
# 1. Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/
# 2. Ensure it matches your Google Chrome version.
# 3. Place the 'chromedriver' executable in the project directory or add it to your PATH.

# Step 6: Run the Script
python scrape_audible.py

scrape_audible/
│
├── scrape_audible.py         # Main script for scraping
├── README.md                 # Project documentation
└── virtualenv/               # Virtual environment (optional, not committed)



