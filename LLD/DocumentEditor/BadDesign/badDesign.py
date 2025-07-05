class DocumentEditor:
    elements = []

    def addText(self, text):
        self.elements.append(text)

    def addImage(self, image):
        self.elements.append(image)

    def render(self):
        for element in self.elements:
            if element.endswith(".txt"):
                print(f"Rendering text: {element}")
            elif element.endswith(".jpg") or element.endswith(".png"):
                print(f"Rendering image: {element}")

    def saveToFile(self):
        with open("LLD\DocumentEditor.py\document.txt", "w") as file:
            for element in self.elements:
                if element.endswith(".txt"):
                    file.write(f"Text: {element}\n")
                elif element.endswith(".jpg") or element.endswith(".png"):
                    file.write(f"Image: {element}\n")


if __name__ == "__main__":
    editor = DocumentEditor()
    editor.addText("Hello World.txt")
    editor.addImage("image1.jpg")
    editor.addImage("image2.png")
    editor.render()
    editor.saveToFile()
    print("Document saved successfully.")
