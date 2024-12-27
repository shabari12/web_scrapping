# Web Scraper for Chennai Restaurants

This project is a web scraper that collects the names of restaurants in Chennai from the Dineout website. The scraper uses Selenium and BeautifulSoup to navigate the website and extract restaurant names.

## Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment (optional):
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download ChromeDriver and ensure it is in your PATH. You can download it from [here](https://chromedriver.chromium.org/downloads).

## Usage

Run the scraper using the following command:
```sh
python app.py