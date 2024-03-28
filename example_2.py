from pylatex import Document, Section, Command
from pylatex.section import Subsection
from pylatex.utils import NoEscape, italic

class MyDocument(Document):
    def __init__(self):
        super().__init__()

        self.preamble.append(Command('title', 'Awesome Title'))
        self.preamble.append(Command('author', 'Celestino Martinez'))
        self.preamble.append(Command('date', 'March 28th 2024'))
        self.append(NoEscape(r'\maketitle'))

    def fill_document(self):
        with self.create(Section("A Section")) as sec_1:
            sec_1.append("Some regualar text and some ")
            sec_1.append(italic("italic text"))

            with sec_1.create(Subsection('A Subsection')) as sub_sec_1:
                sub_sec_1.append("Also have some crazy characters like #$%^")

    
if __name__ == '__main__':

    doc = MyDocument()

    doc.fill_document()

    with doc.create(Section("A Second Section")) as sec_2:
        sec_2.append("Some text")

    doc.generate_pdf('example_2')

    
