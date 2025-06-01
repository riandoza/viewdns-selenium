# Reverse IP Lookup Scraper

A Python script to perform reverse IP lookups using SeleniumBase and BeautifulSoup to scrape data from viewdns.info.

## Features

- Performs reverse IP lookups for IP addresses
- Handles captcha challenges automatically
- Saves results to output files
- Handles errors and retries failed lookups

## Installation

1. Clone this repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a file named `target.txt` in the same directory
2. Add IP addresses to check (one per line)
3. Run the script:

   ```bash
   python main.py
   ```

## Input/Output

- **Input**: IP addresses in `target.txt` (one per line)
- **Output**:
  - Successful lookups: `result.txt`
  - Failed lookups: `recheck.txt`

## Dependencies

- Python 3.6+
- SeleniumBase
- BeautifulSoup4 (included with SeleniumBase)

## Example

1. Create `target.txt`:

   ```
   8.8.8.8
   1.1.1.1
   ```

2. Run script:

   ```bash
   python main.py
   ```

3. Check results in `result.txt` and `recheck.txt`

## Notes

- The script handles captchas automatically
- May require Chrome or Chromium browser installed
- Rate limiting may occur with too many requests
