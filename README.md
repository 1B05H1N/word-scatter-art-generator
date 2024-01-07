# word-scatter-art-generator 

## Overview

This Python script generates an image with a unique pattern of words. It utilizes the PIL library for image manipulation and the `random` library for randomization. The script arranges a list of predefined words on a transparent background image, placing them at random positions with varying rotation angles and sizes, ensuring no overlap. The final image showcases a visually appealing and random arrangement of words, suitable for various creative applications.

## Requirements

- Python 3.x
- Pillow (PIL Fork): Python Imaging Library
- Access to font files (`.ttf` or `.otf`)

## Installation

1. Ensure you have Python installed on your system.
2. Install the Pillow library using pip:
   ```
   pip install pillow
   ```

## Usage

1. Modify the `words` list in the script to include the words or phrases you want to appear in the image.
2. Set the `fonts_dir` variable to the path where your `.ttf` or `.otf` font files are located.
3. Run the script:
   ```
   python random_words_pattern.py
   ```
4. The script will create an image file named `random_words_pattern.png` in the same directory.

## Customization Options

- **Font Directory**: Change `fonts_dir` to the path containing your font files.
- **Word List**: Modify the `words` list to include your desired words or phrases.
- **Image Size**: Adjust the `width` and `height` variables to change the image dimensions.
- **Font Size**: Tweak `max_font_size` to alter the starting font size.
- **Rotation Angle**: Adjust the values in `rotation_angle = random.uniform(-5, 5)` to change the range of rotation angles.

## Troubleshooting

- **Font Loading Issues**: Ensure the `fonts_dir` path is correctly set and contains valid font files.
- **Overlap of Words**: The script checks for overlap; however, in cases of high word density or large font sizes, some words may not be placed.
