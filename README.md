# Kingmed Case Report Scraper

## Overview

The Kingmed Case Report Scraper is a web scraping tool designed to retrieve comprehensive medical histories from the [Kingmed website](https://kingmed.info/Istorii-boleznye%C4%AD). These histories encompass both general and birth-related records across various clinical disciplines.

## Getting Started

### Installation and Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/HarutyunAg/kingmed-scraper
    cd kingmed-scraper
    ```

2. **Use the provided `scraper.sh` file to initiate the scraping process::**

    ```bash
    bash scraper.sh
    ```

3. **Specify the download path:**
   When prompted, enter the path where you wish to save the downloaded files. An example prompt is as follows:

    ```
    Enter the path where you want to download files: /path/to/download/files
    ```

### Manual activation.
Alternatively, if you prefer manual activation, follow the next steps.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/HarutyunAg/kingmed-scraper
    cd kingmed-scraper
    ```
   
2. **Create and activate a virtual environment using Poetry:**

    ```bash
    cd ./deps
    poetry install
    poetry shell
    cd ..
    ```

3. **Run the `main.py` file:**
   Execute the following command to initiate the scraper, which will commence downloading medical histories into the specified directory.

    ```bash
    python main.py
    ```
