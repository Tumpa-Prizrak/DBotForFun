from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    token: str
    owner: int
    command_prefix: str

__all__= ("Config",)
