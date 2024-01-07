# This script was written by Ibrahim Al-Shinnawi, shinnawi.com, on 2024-01-07.

import random
from PIL import Image, ImageDraw, ImageFont
import os

# Path to the fonts you want to use
fonts_dir = os.path.expanduser('/fonts')

# If the system fonts directory is not accessible, use the user's font directory
# Warning: many of your fonts will not load correctly, it may be a good idea to target the fonts by putting them in a folder
if not os.path.exists(fonts_dir) or not os.path.isdir(fonts_dir):
    fonts_dir = os.path.expanduser('~/Library/Fonts')

# List of words to be included in the pattern
words = [
    "First phrase or words", "second", "and so on"
]

# Check if the directory exists and contains font files
if os.path.exists(fonts_dir) and os.path.isdir(fonts_dir):
    available_fonts = [os.path.join(fonts_dir, f) for f in os.listdir(fonts_dir) if f.endswith('.ttf') or f.endswith('.otf')]
    random.shuffle(available_fonts)
    if not available_fonts:
        print(f"No suitable font files found in the directory: {fonts_dir}")
        exit(1)
else:
    print(f"Font directory not found: {fonts_dir}")
    exit(1)

def get_font(index, font_size):
    font_path = available_fonts[index % len(available_fonts)]
    try:
        return ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Could not load font: {font_path} with size {font_size}")
        return None

random.shuffle(words)

# Change image size in px
width, height = 2400, 1000
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))  # Transparent background
draw = ImageDraw.Draw(image)

placed_words = []

def check_overlap(x, y, text_width, text_height):
    for placed_word in placed_words:
        if (x < placed_word[0] + placed_word[2] and x + text_width > placed_word[0] and
            y < placed_word[1] + placed_word[3] and y + text_height > placed_word[1]):
            return True
    return False

def place_text(word, font_index):
    max_font_size = 50  # Start with a moderate font size
    font_size = max_font_size

    while font_size > 10:
        font = get_font(font_index, font_size)
        if font is None:
            return False

        temp_image = Image.new('L', (width, height), 0)
        temp_draw = ImageDraw.Draw(temp_image)
        temp_draw.text((0, 0), word, font=font, fill="white")
        bbox = temp_image.getbbox()
        if not bbox:
            return False
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        rotation_angle = random.uniform(-5, 5)
        rotated_image = temp_image.rotate(rotation_angle, expand=1)
        rotated_bbox = rotated_image.getbbox()
        if not rotated_bbox:
            return False
        rotated_width, rotated_height = rotated_bbox[2] - rotated_bbox[0], rotated_bbox[3] - rotated_bbox[1]

        for _ in range(100):
            x = random.randint(0, max(width - rotated_width, 1))
            y = random.randint(0, max(height - rotated_height, 1))

            if not check_overlap(x, y, rotated_width, rotated_height):
                image.paste(rotated_image.crop(rotated_bbox), (x, y), rotated_image.crop(rotated_bbox))
                placed_words.append((x, y, rotated_width, rotated_height))
                return True
        font_size -= 1  # Gradually reduce font size
    return False

for index, word in enumerate(words):
    if not place_text(word, index):
        print(f"Could not place the word: {word}")

output_path = 'random_words_pattern.png'
image.save(output_path)

print(f"Image saved to {output_path}")
