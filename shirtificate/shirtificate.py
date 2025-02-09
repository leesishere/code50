import sys
sys.path.append('/workspaces/21178063/shirtificate')
_PATH = '/workspaces/21178063/shirtificate'
image_path = f"{_PATH}/shirtificate.png"

from fpdf import FPDF

class PDF:
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf._name = name
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255, 255, 255)

    def write_message(self):
        self._pdf.text(x=54, y=140, text=f"{self._pdf._name} took CS50")

    def output(self, filename):
        self._pdf.output(filename)

    @property
    def name(self):
        return self._pdf._name


name = input("Name: ")
pdf = PDF(name)
pdf.write_message()
pdf.output('shirtificate.pdf')

