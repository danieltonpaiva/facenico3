from typing import Optional

from facefusion.typing import Face

FACE_REFERENCE2 = None


def get_face_reference() -> Optional[Face]:
	return FACE_REFERENCE2


def set_face_reference(face : Face) -> None:
	global FACE_REFERENCE2

	FACE_REFERENCE2 = face


def clear_face_reference() -> None:
	global FACE_REFERENCE2

	FACE_REFERENCE2 = None
