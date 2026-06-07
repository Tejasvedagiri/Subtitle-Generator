import os
import logging

logger = logging.getLogger(__name__)
logger.info("Imported utils.folder module")


def ensure_parent_dir(path: str) -> None:
    """Ensure the parent directory of `path` exists. No-op if path has no parent.

    Args:
        path: File or directory path whose parent should exist.
    """
    parent = os.path.dirname(path)
    if not parent:
        return
    try:
        os.makedirs(parent, exist_ok=True)
        logger.info("Ensured parent directory exists: %s", parent)
    except Exception:
        logger.exception("Failed to ensure parent directory: %s", parent)
