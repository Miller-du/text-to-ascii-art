# coding=utf-8
"""
    Installation:
       pip install -r requirements.txt or pip install Pillow;
       All done:3;
"""

from PIL import Image, ImageFont, ImageDraw

import argparse

'''
#############################################################
 █   █        █  █             █   █   █          █     █  █
 █   █        █  █             █  █ █  █          █     █  █
 █   █   ██   █  █   ██         █ █ █ █   ██   ██ █   ███  █
 █████  █  █  █  █  █  █        █ █ █ █  █  █  █  █  █  █  █
 █   █  ████  █  █  █  █        █ █ █ █  █  █  █  █  █  █  █
 █   █  █     █  █  █  █        █ █ █ █  █  █  █  █  █  █
 █   █   ███  █  █   ██   █      █   █    ██   █  █   ███  █
                          █
#############################################################
'''

'''
    Arguments Parser Init
'''

parser = argparse.ArgumentParser(description='Text to ASCII')
parser.add_argument('-text', help='Your text (Required)', type=str, required=True)
parser.add_argument('-char', help='Your char for ASCII (Optional, default char — █)', default='█', type=str,
                    required=False)
parser.add_argument('-space-char', help='Your space char (Optional, default space char — space¯\_(ツ)_/¯)', default=' ',
                    type=str,
                    required=False)
parser.add_argument('-gap-char', help='Your char between letters (Optional, default space char — empty)', default='',
                    type=str,
                    required=False)
parser.add_argument('-font', help='Your Font (Optional, default font — Arial)', type=str, default='Arial.ttf',
                    required=False)
parser.add_argument('-align', help='Text Align(center, left, right) (Optional, default align — left)', type=str,
                    default='left', required=False)
parser.add_argument('-spacing', help='Text Spacing (Optional, default spacing — 0)', type=int,
                    default=0, required=False)
parser.add_argument('-size', help='Font Size (Optional, default size — 10)', type=int, default=10, required=False)
parser.add_argument('-signature', help='Your Signature. \\n — for new line(Optional, default signature — mine(✿´‿`))',
                    type=str,
                    default='Made by Mikelarg\\nhttps://vk.com/mikelarg',
                    required=False)
parser.add_argument('--left', action='store_true', help='If argument is defined, script writes you signature left side',
                    required=False)
parser.add_argument('--hr', action='store_true', help='If argument is defined, script writes hr', required=False)
parser.add_argument('-hr-char', help='Your HR char', type=str, default='_',
                    required=False)
parser.add_argument('--save-image', action='store_true', help='Save text image to PNG', required=False)

'''
    Get and Filter Arguments Values
'''

args = parser.parse_args()
args.text = args.text.decode('utf-8').replace('\\n', '\n')
args.char = args.char.decode('utf-8')
args.gap_char = args.gap_char.decode('utf-8')
args.space_char = args.space_char.decode('utf-8')
args.hr_char = args.hr_char.decode('utf-8')
args.align = args.align.lower()
args.signature = args.signature.decode('utf-8')

font = ImageFont.truetype(args.font, args.size)

'''
    Get Size Of Image
'''

size = [0, 0]
text_lines = args.text.split('\n')
for line in text_lines:
    line_width, line_height = font.getsize(line)
    size[1] += line_height + args.spacing
    size[0] = max(size[0], line_width)
size = (size[0], size[1])

'''
    Draw Image
'''

image = Image.new('1', size, 1)
draw = ImageDraw.Draw(image)
draw.multiline_text((0, 0), args.text, font=font, align=args.align, spacing=args.spacing)
if args.save_image:
    image.save('out.png')

'''
    Convert Image To ASCII
'''

hr = args.hr_char * (image.width + image.width * len(args.gap_char) - 1)

if args.hr:
    print hr

up_padding = True
for row_num in range(size[1]):
    line = []
    for column in range(size[0]):
        if image.getpixel((column, row_num)):
            line.append(args.space_char)
        else:
            line.append(args.char)
            up_padding = False
    if up_padding is False:
        print args.gap_char.join(line)

if args.hr:
    print hr

'''
    Adding Signature
'''

signature = args.signature
lines = signature.split('\\n')
for line in lines:
    if args.left:
        print line
    else:
        print (' ' * (image.width - len(line))) + line