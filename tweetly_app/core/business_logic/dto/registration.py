from dataclasses import dataclass
import datetime


@dataclass
class RegistrationDTO:
    username: str
    password: str
    email: str
    country: str
    birthdate: datetime.date

    def __str__(self) -> str:
        return f"username={self.username} email={self.email} country={self.country}"
