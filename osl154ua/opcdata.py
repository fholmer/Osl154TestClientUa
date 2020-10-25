import opcua
import pathlib
import json
import time
from PIL import Image

def raw_to_img(width, height, rawbytes):
    im = Image.frombytes("RGB",(width, height),rawbytes)
    im = Image.frombytes("RGB",(width, height),im.convert("BGR;24").tobytes())
    return im

def sign_read(name):
    root = pathlib.Path(".", "signs", name)
    data = json.load(root.joinpath("sign.json").open("r"))

    server = data["server"]
    print(f"Connecting to {server}")

    client = opcua.Client(server)
    client.connect()

    command = client.get_node(data["tags"]["COMMAND"])
    status = client.get_node(data["tags"]["STATUS"])
    value = client.get_node(data["tags"]["VALUE"])
    active_value = client.get_node(data["tags"]["ACTIVE_VALUE"])
    image_onsign = client.get_node(data["tags"]["IMAGE_ONSIGN"])
    image_toset = client.get_node(data["tags"]["IMAGE_TOSET"])
    pixelheight = client.get_node(data["tags"]["PIXELHEIGHT"])
    pixelpp = client.get_node(data["tags"]["PIXELPP"])
    pixelwidth = client.get_node(data["tags"]["PIXELWIDTH"])

    print("Values from server:")
    height = pixelheight.get_value()
    width = pixelwidth.get_value()
    print(f"status: {status.get_value()}")
    print(f"active_value: {active_value.get_value()}")
    print(f"command: {command.get_value()}")
    print(f"value: {value.get_value()}")
    print(f"pixelpp: {pixelpp.get_value()}")
    print(f"pixelheight: {height}")
    print(f"pixelwidth: {width}")

    onsign = image_onsign.get_value()
    if onsign:
        raw_to_img(width, height, onsign).save(root.joinpath("_image_onsign.bmp"))
        print(f"image_onsign: {root}/_image_onsign.bmp")
    else:
        print(f"image_onsign: {onsign}")

    to_set = image_toset.get_value()
    if to_set:
        raw_to_img(width, height, to_set).save(root.joinpath("_image_toset.bmp"))
        print(f"image_toset: {root}/_image_toset.bmp")
    else:
        print(f"image_toset: {to_set}")

    client.disconnect()
    print("Done")

def rgb_on(name, image):
    root = pathlib.Path(".", "signs", name)
    data = json.load(root.joinpath("sign.json").open("r"))

    im = Image.open(root.joinpath(image))
    bmp = im.convert(mode="BGR;24").tobytes()

    assert data["width"] == im.width
    assert data["height"] == im.height

    server = data["server"]
    print(f"Connecting to {server}")

    client = opcua.Client(server)
    client.connect()

    command = client.get_node(data["tags"]["COMMAND"])
    value = client.get_node(data["tags"]["VALUE"])
    image_toset = client.get_node(data["tags"]["IMAGE_TOSET"])

    print(f"set_value({command}, 0)")
    command.set_value(0)
    time.sleep(1)

    print("set_values(")
    print(f"  [{value}, 9999],")
    print(f"  [{image_toset}, <bmp-data::{image}>]")
    print(")")
    client.set_values([value, image_toset], [9999, bmp])
    #value.set_value(9999)
    #image_toset.set_value(bmp)

    print("await 4 seconds")
    time.sleep(4)

    print(f"set_value({command}, 4)")
    command.set_value(4)
    time.sleep(1)

    client.disconnect()
    print("Done")
