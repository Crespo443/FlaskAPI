from model import TextProcessorModel

def process_text_service(text):
    """
    Memproses teks menggunakan TextProcessorModel.
    """
    model = TextProcessorModel(text)
    return model.summary()
