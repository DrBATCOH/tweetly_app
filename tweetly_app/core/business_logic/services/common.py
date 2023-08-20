from __future__ import annotations
import sys
import uuid
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def optimize_image(file: InMemoryUploadedFile) -> InMemoryUploadedFile:
    format = file.content_type.split("/")[-1].upper()
    output = BytesIO()
    with Image.open(file) as image:
        image.thumbnail(size=(200, 150))
        image.save(output, format=format, qulity=100)
    return InMemoryUploadedFile(
        file=output,
        field_name=file.field_name,
        name=file.name,
        content_type=file.content_type,
        size=sys.getsizeof(output),
        charset=file.charset
    )
