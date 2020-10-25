import os
import pathlib
import json
from PIL import Image, ImageDraw

def list_signs():
    root = pathlib.Path(".", "signs")
    print("Available signs:")
    for d in root.iterdir():
        print(f" * {d.name}")

def create_sign_data(name, server, tag, width, height):
    root = pathlib.Path(".", "signs", name)
    root.mkdir(parents=True, exist_ok=True)
    img = Image.new('RGB', (width, height), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([(1,1), (width-2, height-2)], outline=(255,255,255))
    d.text((4,4),  "R", fill=(255, 0, 0), align="center")
    d.text((28,4), "G", fill=(0, 255, 0), align="center")
    d.text((56,4), "B", fill=(0, 0, 255), align="center")
    d.multiline_text((4,32), "Test of\nRGB Sign", fill=(255, 255, 255), align="center")
    img.save(root.joinpath("1.bmp"))
    json.dump({
        "server": server,
        "tag_prefix": tag,
        "width": width,
        "height": height,
        "tags": {
            "COMMAND": ".".join((tag, "COMMAND")),
            "STATUS": ".".join((tag, "STATUS")),
            "VALUE": ".".join((tag, "VALUE")),
            "ACTIVE_VALUE": ".".join((tag, "ACTIVE_VALUE")),
            "IMAGE_ONSIGN": ".".join((tag, "IMAGE_ONSIGN")),
            "IMAGE_TOSET": ".".join((tag, "IMAGE_TOSET")),
            "PIXELHEIGHT": ".".join((tag, "PIXELHEIGHT")),
            "PIXELPP": ".".join((tag, "PIXELPP")),
            "PIXELWIDTH": ".".join((tag, "PIXELWIDTH")),
            }
        },
        root.joinpath("sign.json").open(mode="w")
    )
