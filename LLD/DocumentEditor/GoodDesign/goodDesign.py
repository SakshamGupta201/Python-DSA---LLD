from abc import ABC, abstractmethod


class DocumentElement(ABC):
    @abstractmethod
    def render(self):
        pass


class TextElement(DocumentElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        print(f"Rendering text: {self.text}")


class ImageElement(DocumentElement):
    def __init__(self, image):
        self.image = image

    def render(self):
        print(f"Rendering image: {self.image}")


class VideoElement(DocumentElement):
    def __init__(self, video):
        self.video = video

    def render(self):
        print(f"Rendering video: {self.video}")


class Document:
    def __init__(self):
        self.elements: list[Document] = []

    def add_element(self, element: DocumentElement):
        self.elements.append(element)

    def render(self):
        for element in self.elements:
            element.render()


class PersistentStorage(ABC):
    @abstractmethod
    def save(self, document: Document):
        pass


class FileStorage(PersistentStorage):
    def __init__(self, filename):
        self.filename = filename

    def save(self, data: str):
        with open(self.filename, "w") as file:
            file.write(data)


class DBStorage(PersistentStorage):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save(self, data: str):
        # Simulate saving to a database
        print(f"Saving to database: {data}")


class DocumentEditor:
    def __init__(self, document: Document, storage: PersistentStorage):
        self.document = document
        self.storage = storage

    def add_text(self, text):
        text_element = TextElement(text)
        self.document.add_element(text_element)

    def add_image(self, image):
        image_element = ImageElement(image)
        self.document.add_element(image_element)

    def add_video(self, video):
        video_element = VideoElement(video)
        self.document.add_element(video_element)

    def render(self):
        self.document.render()

    def save_to_file(self):
        data = ""
        for element in self.document.elements:
            if isinstance(element, TextElement):
                data += f"Text: {element.text}\n"
            elif isinstance(element, ImageElement):
                data += f"Image: {element.image}\n"
            elif isinstance(element, VideoElement):
                data += f"Video: {element.video}\n"
        self.storage.save(data)
        print("Document saved successfully.")


if __name__ == "__main__":
    doc = Document()
    storage = FileStorage("LLD/DocumentEditor/GoodDesign/document.txt")
    editor = DocumentEditor(doc, storage)

    editor.add_text("Hello World")
    editor.add_image("image1.jpg")
    editor.add_image("image2.png")

    editor.render()
    editor.save_to_file()
