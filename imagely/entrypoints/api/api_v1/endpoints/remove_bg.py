from dataclasses import dataclass
from enum import Enum

from asyncer import asyncify
from fastapi import APIRouter, Depends, File, Form, Query, UploadFile
from rembg.bg import remove
from rembg.session_base import BaseSession
from rembg.session_factory import new_session
from starlette.responses import Response

from imagely.entrypoints.api.utils import aget

sessions: dict[str, BaseSession] = {}


class ModelType(str, Enum):
    U2NET = "u2net"
    U2NETP = "u2netp"
    U2NET_HUMAN_SEG = "u2net_human_seg"
    U2NET_CLOTH_SEG = "u2net_cloth_seg"


@dataclass
class CommonQueryPostParams:
    model: ModelType = Form(
        default=ModelType.U2NET,
        description="Model to use when processing image",
    )
    # a_m represents alpha_matting
    a_m: bool = Form(default=False, description="Enable Alpha Matting")
    a_m_foreground_threshold: int = Form(
        default=240,
        ge=0,
        le=255,
        description="Alpha Matting (Foreground Threshold)",
    )
    a_m_background_threshold: int = Form(
        default=10,
        ge=0,
        le=255,
        description="Alpha Matting (Background Threshold)",
    )
    a_m_erode_size: int = Form(
        default=10, ge=0, description="Alpha Matting (Erode Structure Size)"
    )
    only_mask: bool = Form(default=False, description="Only Mask")
    post_process_mask: bool = Form(default=False, description="Post Process Mask")


router = APIRouter()


def im_without_bg(content: bytes, commons: CommonQueryPostParams) -> Response:
    return remove(
        content,
        session=sessions.setdefault(
            commons.model.value, new_session(commons.model.value)
        ),
        alpha_matting=commons.a_m,
        alpha_matting_foreground_threshold=commons.a_m_foreground_threshold,
        alpha_matting_background_threshold=commons.a_m_background_threshold,
        alpha_matting_erode_size=commons.a_m_erode_size,
        only_mask=commons.only_mask,
        post_process_mask=commons.post_process_mask,
    )


@router.post(
    path="/",
    summary="Remove from Stream or File",
    description="Removes the background from an image sent within the request itself.",
)
async def remove_bg(
    file: UploadFile = File(
        default=None,
        description="Image file (byte stream) that has to be processed.",
    ),
    url: str = Query(
        default=None, description="URL of the image that has to be processed."
    ),
    commons: CommonQueryPostParams = Depends(),
):
    if url:
        content = await aget(url)
    elif file:
        content = file
    else:
        return Response(status_code=400)
    return Response(
        await asyncify(im_without_bg)(content, commons),
        media_type="image/png",
        status_code=200,
    )
