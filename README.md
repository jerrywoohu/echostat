# Echostat for Overwatch

## Using tesseract to read Overwatch stats off the scoreboard.

Designed to be used with [this spreadsheet](https://owspreadsheet.jerrywoohu.com)

## Requirements
1. Overwatch 1
2. 16:9 mode. You can play on an ultrawide but must select 16:9. This has not been tested on 16:10.
3. 1920x1080 screen resolution minimum. Higher resolutions offer better OCR accuracy.
4. Subtitles off
5. Activated Windows 10 or 11 (the Activate Windows watermark messes with stats in the bottom left). This is not necessary if you have an ultrawide as the watermark is out of the way.

## Prerequisites to run
1. Python > 3.10
2. [tesseract](https://github.com/tesseract-ocr/tesseract) (I like to use [this installer](https://github.com/UB-Mannheim/tesseract/wiki))
3. pytesseract `pip install pytesseract`

## How to use
1. Start the script `python ocr.py`
2. With the scoreboard visible (Tab), press Win+F3
3. The script will then add the data to your clipboard to paste into the [spreadsheet](https://owspreadsheet.jerrywoohu.com)

## Configuration
* Ensure the tesseract install location is correct in the `functions.py` file
* Edit the `USER_CONFIG.py` file to setup your columns and extra stats
* The hotkey in `ocr.py` used to trigger the script

## Known Issues
* `11` often gets read as `0`. For example, 11 deaths often gets read as 0 deaths

Overwatch is a trademark of Blizzard Entertainment, Inc., in the U.S. and/or other countries.