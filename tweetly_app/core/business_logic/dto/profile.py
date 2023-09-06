import datetime
from typing import Optional
from dataclasses import dataclass
from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class ProfileDTO:
    avatar: Optional[InMemoryUploadedFile]
    status: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    old_password: str
    new_password: str
    email: Optional[str]
    country: str
    birthdate: datetime.date
