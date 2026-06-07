def load_model(model_name="large-v3"):
    import whisper
    return whisper.load_model(model_name)