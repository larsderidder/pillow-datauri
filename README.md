# pillow-datauri

Repository: https://github.com/larsderidder/pillow-datauri
Helpers for parsing image data URIs and checking supported formats in Pillow.

## Install

```bash
git clone https://github.com/larsderidder/pillow-datauri.git
cd pillow-datauri
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install .
```

## Usage

```python
from pillow_datauri import read_image_from_src_attr, supported_formats_for_mime

mime, image = read_image_from_src_attr("data:image/png;base64,...")
formats = supported_formats_for_mime("image/png")
```

## Development

```bash
pip install -e .[dev]
pytest
```
