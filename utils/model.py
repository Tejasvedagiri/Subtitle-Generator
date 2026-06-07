import logging

logger = logging.getLogger(__name__)
logger.info("Imported utils.model module")


def load_model(model_name="large-v3"):
    import whisper
    logger.info("Loading model: %s", model_name)
    return whisper.load_model(model_name)