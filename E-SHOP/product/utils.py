import uuid
import os
from django.conf import settings


def product_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/images/", filename)
