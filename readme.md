# Blind Drive subtitle extractor

The blind drive game has subtitles for various languages. Unfortunately though, it's not accessible for screen reader users. I tried to read it using lion, but it did not work as expected.

# Usage

The game has subtitle data as a csv file, and you need to find it inside the game's data directory. Once you found the subtitles.csv file, copy it near this script. Run extract.py --help for usage and adjust options to get subtitles for your preferred language. If libraries are missing, run pip install -r requirements.txt .

# Notes

Do not use the extracted data except for checking inaccessible translations. Respect the copyright holders.
