import uuid
import os

def avatar_upload_to(_, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("avatars", new_filename)
