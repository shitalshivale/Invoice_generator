# Invoice_generator
# Invoice Generator

This project is an Invoice Generator that reads sales data from an Excel file, generates PDF invoices for each customer, and provides a Streamlit UI for easy interaction and downloading of the generated invoices.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Read sales data from an Excel file.
- Generate invoices for each customer as PDF files.
- Customize invoice details such as company name, address, and tax rate.
- Streamlit UI for uploading the Excel file and downloading the generated invoices.

## Requirements

- Python 3.7 or later
- pandas
- openpyxl
- jinja2
- pdfkit
- streamlit

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/invoice-generator.git
    cd invoice-generator
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install `wkhtmltopdf`:

    - Download `wkhtmltopdf` from [here](https://wkhtmltopdf.org/downloads.html) and install it.
    - Update the path to `wkhtmltopdf.exe` in `logic.py` if necessary.

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run ui.py
    ```

2. Upload the Excel file containing sales data using the provided UI.

3. Download the generated PDF invoices using the download buttons.

## Project Structure

```plaintext
invoice-generator/
│
├── logic.py                # Contains all the logic for reading data, generating invoices, and creating PDF files
├── ui.py                   # Contains the Streamlit UI
├── requirements.txt        # Contains a list of required Python packages
└── README.md               # This file
