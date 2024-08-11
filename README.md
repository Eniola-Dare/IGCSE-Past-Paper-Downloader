# IGCSE Past Papers Downloader

This is a  Python script I wrote to automate the downloading of past papers and their corresponding marking schemes from the Xtremepapers website, to prepare for the IGCSE examination. The papers are organized by subject and year.

## Features

- Downloads question papers (qp) and marking schemes (ms) for specified subjects.
- Organizes the downloaded files into directories based on subject and year.
- Beep notifications to signal the success or failure of each download attempt.

## Requirements

- Python 3
- The following Python libraries:
  - `requests` (for making HTTP requests)
  - `winsound` (for generating beep sounds, available only on Windows)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/igcse-papers-downloader.git
   cd igcse-papers-downloader
   ```
2. **Install the requests package:**
   ```bash
   pip install requests
   ```

## Usage

1. **Run the script:**
   ```bash
   python past-paper-downloader.py
   ```
   The script will start downloading the past papers and marking schemes. The files will be saved in the Past Papers directory, with subdirectories for each subject and year.

2. **Customization:**
   - You can modify the `subjects` dictionary by adding subject name and exam code as a key (replace spaces with `%20`) and the exam code and variants as the values.
   - You can modify the `years` variable which defines the range of years for which papers will be downloaded.

## Directory Structure

After running the script, the files will be organized as follows:
```bash
Past Papers/
├── Biology
│   ├── 2016/
│   │   ├── 0610_w16_qp_22.pdf
│   │   ├── 0610_w16_ms_22.pdf
│   └── 2017/
│       ├── 0610_s17_qp_42.pdf
│       ├── 0610_s17_ms_42.pdf
├── Physics
│   ├── 2016/
│   └── 2017/
...
```

## Beep Notifications
   - A single beep indicates a successful download.
   - Two beeps in quick succession indicate that the file already exists.
   - A lower-frequency beep signals an error during the download.
