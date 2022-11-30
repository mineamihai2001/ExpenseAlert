from mindee import Client, documents
from dotenv import dotenv_values
from configs.config import ENV, DOCS

api_key = dotenv_values(ENV)["API_KEY"]

class Textract:
    def __init__(self, document) -> None:
        self.client = Client(api_key=api_key)
        self.parse(document)

    def parse(self, document):
        """
        Document is a filename from the DOCS folder
        """
        input_doc = self.client.doc_from_path(f"{DOCS}\{document}")
        api_response = input_doc.parse(documents.TypeReceiptV4)
        self.document = api_response.document

    def get(self, attr):
        return getattr(self.document, attr)
