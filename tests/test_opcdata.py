from osl154ua import opcdata
from PIL import Image

def test_raw_to_img():
    bytedata = b"\x00" * (16*16*3)
    im = opcdata.raw_to_img(16, 16, bytedata)
    assert im.tobytes() == bytedata

def test_raw_to_img_rgb_to_bgr():
    bytedata_in = b"\xFF\x0C\x0A" * (16*16)
    im = opcdata.raw_to_img(16, 16, bytedata_in)

    bytedata_out = b"\x0A\x0C\xFF" * (16*16)
    assert im.tobytes() == bytedata_out
