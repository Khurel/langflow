### JSON Document Builder

# Build a Document containing a JSON object using a key and another Document page content.

# **Params**

# - **Key:** The key to use for the JSON object.
# - **Document:** The Document page to use for the JSON object.

# **Output**

# - **Document:** The Document containing the JSON object.

from langflow import CustomComponent
from langchain.schema import Document


class JSONDocumentBuilder(CustomComponent):
    display_name: str = "JSON Document Builder"
    description: str = "Build a Document containing a JSON object using a key and another Document page content."
    output_types: list[str] = ["Document"]
    beta = True

    field_config = {
        "key": {"display_name": "Key"},
        "document": {"display_name": "Document"},
    }

    def build(
        self,
        key: str,
        document: Document,
    ) -> Document:
        documents = None
        if isinstance(document, list):
            documents = [
                Document(page_content={key: doc.page_content}) for doc in document
            ]
        else:
            documents = Document(page_content={key: document.page_content})
        self.repr_value = documents
        return documents
