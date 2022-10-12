from enum import Enum
import uuid
from dataclasses import asdict, dataclass, field

from fastapi import Form, Query
from imagely.domain.validators import is_jpeg


@dataclass
class JPG:
    code: uuid.UUID
    src_path: str
    extensions: tuple[str, str] = field(init=False, default=(".jpeg", ".jpg"))

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)


@is_jpeg
def allocate_jpeg(code: uuid.UUID, src_path: str) -> JPG:
    return JPG(code=code, src_path=src_path)


