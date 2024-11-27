class TextProcessorModel:
    """
    Model sederhana untuk memproses teks.
    """

    def __init__(self, text):
        self.text = text

    def word_count(self):
        """
        Menghitung jumlah kata dalam teks.
        """
        return len(self.text.split())

    def char_count(self):
        """
        Menghitung jumlah karakter dalam teks (tanpa spasi).
        """
        return len(self.text.replace(" ", ""))

    def summary(self):
        """
        Mengembalikan ringkasan teks, seperti jumlah kata dan karakter.
        """
        return {
            "word_count": self.word_count(),
            "char_count": self.char_count()
        }
