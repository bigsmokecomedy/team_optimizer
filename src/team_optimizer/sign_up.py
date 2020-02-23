from dataclasses import dataclass, fields
from typing import Mapping


@dataclass
class SignUp():
    email: str
    experience: int
    name: str
    set: int
    jam: str


    @classmethod
    def from_dict(cls, d:Mapping[str,str])->"SignUp":
        result = {}
        for f in fields(cls):
            for k,v in d.items():
                if f.name in k.lower():
                    result[f.name] = v
        return cls(**result)
