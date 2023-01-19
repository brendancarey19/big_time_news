class PreSum:

    def __init__(self, pgraphs, title):
        self.pgraphs = pgraphs
        self.title = title
        self.sentences = []
        self.summary = None
        self.parse_paragraphs()
        self.join_summary()

    def get_sentence(self, pgraph):
        """
        Get first sentence of a paragraph
        """
        return pgraph.split(".")[0]

    def parse_paragraphs(self):
        for paragraph in self.pgraphs:
            self.sentences.append(self.get_sentence(paragraph))

    def join_summary(self):
        self.summary =  '. '.join(self.sentences) + "."
