import base64
import io
import mimetypes
from PIL import Image


def supported_formats_for_mime(mime_type: str) -> list[str]:
    """Return supported Pillow formats for a given MIME type."""
    extensions = [ext[1:].upper() for ext in mimetypes.guess_all_extensions(mime_type)]
    Image.init()
    return [ext for ext in extensions if ext in Image.SAVE]


def read_image_from_src_attr(src_attr: str) -> tuple[str, Image.Image]:
    """Parse a data URI image from an HTML img src attribute."""
    if not src_attr.startswith("data:") or ";" not in src_attr or "," not in src_attr:
        raise ValueError("src_attr must be a data URI")
    header, encoded = src_attr.split(",", 1)
    mime_type = header[len("data:") : header.find(";")]
    if not mime_type:
        raise ValueError("data URI is missing a MIME type")
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    return mime_type, image
