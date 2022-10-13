from enum import Enum
from typing import Union

import numpy as np
from PIL.Image import Image as PILImage
from rembg.bg import remove
from rembg.session_base import BaseSession
from rembg.session_factory import new_session

sessions: dict[str, BaseSession] = {}


class ModelType(str, Enum):
    U2NET = "u2net"
    U2NETP = "u2netp"
    U2NET_HUMAN_SEG = "u2net_human_seg"
    U2NET_CLOTH_SEG = "u2net_cloth_seg"


def remove_bg(content: bytes, **kwargs) -> Union[bytes, PILImage, np.ndarray]:
    return remove(
        content,
        **kwargs,
        session=sessions.setdefault(
            kwargs.get("model", ModelType.U2NET.value),
            new_session(kwargs.get("model", ModelType.U2NET.value)),
        ),
    )
