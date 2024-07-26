from typing import Optional

from facefusion.typing import Face

FACE_REFERENCE2 = None


def get_face_reference2() -> Optional[Face]:
	return FACE_REFERENCE2


def set_face_reference2(face : Face) -> None:
	global FACE_REFERENCE2

	FACE_REFERENCE2 = face


def clear_face_reference2() -> None:
	global FACE_REFERENCE2

	FACE_REFERENCE2 = None
