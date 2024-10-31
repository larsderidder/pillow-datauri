import base64
import io

from PIL import Image

from pillow_datauri import read_image_from_src_attr, supported_formats_for_mime


def _make_png_data_uri() -> str:
    image = Image.new("RGB", (1, 1), color=(255, 0, 0))
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    encoded = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/png;base64,{encoded}"


def test_supported_formats_for_mime():
    formats = supported_formats_for_mime("image/png")
    assert "PNG" in formats


def test_read_image_from_src_attr():
    src = _make_png_data_uri()
    mime, image = read_image_from_src_attr(src)
    assert mime == "image/png"
    assert image.size == (1, 1)
