# iASCII - Convert Images to ASCII Art with Optional Color

## Introduction
iASCII is a Python-based command-line tool for converting images to ASCII art, allowing users to choose from a variety of character sets and optionally add color to the output.

## Prerequisites
- Python 3.x
- Pillow (Python Imaging Library)
- Requests (HTTP for Humans)
- ansiconverter (Optional for color output)

## Installation
Before running the program, you need to install the dependencies via pip:

```shell
pip install Pillow requests ansiconverter
```

## Usage
To start the program, run the following command in your terminal:

```shell
python main.py

```

Upon execution, you will be prompted for:
- **URL**: The link to an image you wish to convert.
- **Width**: The width (in characters) of the output ASCII art.
- **Height**: The height (in characters) of the output ASCII art.
- **Characters Set**: The choice of character set for ASCII conversion, ranges from 1-8 with an option for a custom set (9).
- **Color**: Choose whether to use color in your ASCII art.
- **Brightness**: (If using color) The brightness level of the colored ASCII art.

Based on your input, iASCII will convert the selected image and display the ASCII art in the console.

The ASCII art will be saved to `out.txt` and the corresponding image URL, width, height, and character set used will be logged in `links.txt`.

## Notes
- To end the program, you may need to interrupt the loop manually by pressing `Ctrl+C`.
- The colorized output uses ANSI escape codes, so ensure your terminal supports them to view the colored ASCII art properly.
- The generated ASCII art's appearance may vary due to differences in terminal font settings and sizes.

## Files Generated
- **out.txt**: Contains the ASCII art generated from the last run of the program.
- **links.txt**: Logs the details of each execution including the image URL and settings used.