from pylatex import Document, Command, Section, NoEscape
from pylatex.section import Subsection
from pylatex.utils import italic

doc = Document()

doc.preamble.append(Command('title', 'Awesome Title'))
doc.preamble.append(Command('author', 'Celestino Martinez'))
doc.preamble.append(Command('date', 'March 28th 2024'))
doc.append(NoEscape(r'\maketitle'))

with doc.create(Section("A Section")) as sec:
    sec.append("Some regular Text and some ")
    sec.append(italic("italic text"))

    with doc.create(Subsection("A Subsection")) as sub:
        sub.append("Also some crazy characters like #%^$@&")

with doc.create(Section("A second section")) as sec2:
    sec2.append("Some text")






doc.generate_pdf("example_1")
