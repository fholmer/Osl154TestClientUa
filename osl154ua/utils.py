import pathlib
import json
from PIL import Image, ImageDraw

def get_sign_path(sign):
    root = pathlib.Path(".", "signs", sign)
    if not root.is_dir():
        raise ValueError(f"config not found for sign: '{sign}'")
    return root

def create_sign_data(name, server, tag, width, height, tags_dict):
    root = pathlib.Path(".", "signs", name)
    root.mkdir(parents=True, exist_ok=True)
    for i in range(1, 5):
        img = Image.new('RGB', (width, height), color = (0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rectangle([(1,1), (width-2, height-2)], outline=(255,255,255))
        d.text((4,4),  "R", fill=(255, 0, 0), align="center")
        d.text((28,4), "G", fill=(0, 255, 0), align="center")
        d.text((56,4), "B", fill=(0, 0, 255), align="center")
        d.multiline_text((4,32), f"RGB sign\ntest #{i}", fill=(255, 255, 255), align="left")
        img.save(root.joinpath(f"{i}.bmp"))
    json.dump({
        "server": server,
        "tag_prefix": tag,
        "width": width,
        "height": height,
        "tags": {
            "COMMAND": tags_dict.get("COMMAND", ".".join((tag, "COMMAND"))),
            "STATUS": tags_dict.get("STATUS", ".".join((tag, "STATUS"))),
            "VALUE": tags_dict.get("VALUE", ".".join((tag, "VALUE"))),
            "ACTIVE_VALUE": tags_dict.get("ACTIVE_VALUE", ".".join((tag, "ACTIVE_VALUE"))),
            "IMAGE_ONSIGN": tags_dict.get("IMAGE_ONSIGN", ".".join((tag, "IMAGE_ONSIGN"))),
            "IMAGE_TOSET": tags_dict.get("IMAGE_TOSET", ".".join((tag, "IMAGE_TOSET"))),
            "PIXELHEIGHT": tags_dict.get("PIXELHEIGHT", ".".join((tag, "PIXELHEIGHT"))),
            "PIXELPP": tags_dict.get("PIXELPP", ".".join((tag, "PIXELPP"))),
            "PIXELWIDTH": tags_dict.get("PIXELWIDTH", ".".join((tag, "PIXELWIDTH"))),
            }
        },
        root.joinpath("sign.json").open(mode="w")
    )
