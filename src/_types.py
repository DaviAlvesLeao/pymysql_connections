from dataclasses import dataclass

@dataclass
class DtConfig:
    host: str
    port: int
    user: str
    password: str
    db: str