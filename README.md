# Echostat for Overwatch

## Using tesseract to read Overwatch stats off the scoreboard.
Designed to be used with [this spreadsheet](https://owspreadsheet.jerrywoohu.com)

## Requirements:
1. Overwatch 1
2. 16:9 mode in game settings. Currently supports ultrawide resolutions but has not been tested with 16:10.
3. 1920x1080p screen resolution minimum. 2560x1440p recommended.
4. Subtitles off
5. Activated Windows 10 or 11 (the Activate Windows watermark messes with some readings). This is not necessary if you have a 21:9 screen as the watermark is out of the way.

## Prerequisites to run:
1. Python > 3.10
2. [tesseract](https://github.com/tesseract-ocr/tesseract) (I like to use [this installer](https://github.com/UB-Mannheim/tesseract/wiki))
3. pytesseract `pip install pytesseract`

## How to use:
1. Start the script `python ocr.py`
2. Hold tab and take a screenshot of Overwatch after the victory/defeat message
3. The script will then add the data to your clipboard to paste into the [spreadsheet](https://owspreadsheet.jerrywoohu.com)

Overwatch is a trademark of Blizzard Entertainment, Inc., in the U.S. and/or other countries.