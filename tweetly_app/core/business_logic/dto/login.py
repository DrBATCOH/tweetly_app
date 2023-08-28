from dataclasses import dataclass


@dataclass
class LoginDTO:
    # username: str
    email: str
    password: str
