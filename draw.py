#!/usr/bin/env python

import sys
import os
import getopt
from PIL import Image, ImageDraw, ImageColor

import config


def usage():
    print(".")


def main():
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "b:i:")

        for opt, arg in opts:
            if opt == "-b":
                config.bg_color = arg
            if opt == "-l":
                config.ipt_color = arg

    except getopt.GetoptError:
        usage()
        return

    try:
        os.mkdir("theme")
    except:
        pass

    bg_img = Image.new("RGB", (8, 8), color=ImageColor.getcolor(config.bg_color, "RGB"))
    bg_img.save("theme/background.jpg")

    panel_img = Image.new(
        "RGBA",
        (
            config.panel_size,
            config.panel_size + config.input_height * 2 + config.input_margin,
        ),
        (255, 255, 255, 0),
    )

    logo_img = Image.open("logo.png", "r")
    logo_w, logo_h = logo_img.size
    logo_offset = ((config.panel_size - logo_w) // 2, (config.panel_size - logo_h) // 2)

    panel_img.paste(logo_img, logo_offset)

    panel_draw = ImageDraw.Draw(panel_img)
    panel_draw.rectangle(
        (
            0,
            config.panel_size + config.input_margin + config.input_height,
            config.panel_size,
            config.panel_size + config.input_height * 2 + config.input_margin,
        ),
        fill=ImageColor.getcolor(config.ipt_color, "RGB"),
    )

    panel_img.save("theme/panel.png", "PNG")

    with open("theme/slim.theme", "w") as f:
        f.write(
            config.SLIM_THEMEFILE.format(
                input_x=config.input_x_offset,
                input_y=(
                    config.panel_size + config.input_height * 2 + config.input_y_offset
                ),
                font_name=config.font_name,
                font_size=config.font_size,
            )
        )


if __name__ == "__main__":
    main()
