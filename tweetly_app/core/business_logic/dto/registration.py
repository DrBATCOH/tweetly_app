import datetime
from dataclasses import dataclass


@dataclass
class RegistrationDTO:
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    country: str
    birthdate: datetime.date

    def __str__(self) -> str:
        return f"username={self.username} email={self.email} country={self.country}"
