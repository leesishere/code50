import sys
sys.path.append('/workspaces/21178063/shirtificate')
_PATH = '/workspaces/21178063/shirtificate'
image_path = f"{_PATH}/shirtificate.png"

from fpdf import FPDF
'''
class PDF(FPDF):
    def __init__(self, name, orientation='Portrait', format='A4'):
        super().__init__(orientation=orientation, format=format)
        self._name = name
        self.add_page()
        self.set_font('Helvetica', 'B', 50)
        self.set_text_color(0, 0, 0)  # Set text color to black
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self.image('shirtificate.png',w=self.w)
        self.set_font_size(30)
        self.set_text_color(255, 255, 255)
        self.text(x=47.5, y=140, text=f"{name} took CS50")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, myname):
        self._name = myname
'''
class PDF:
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, text=f"{name} took CS50")

    def output(self, filename):
        self._pdf.output(filename)

name = input("Name: ")
pdf = PDF(name)

pdf.output('shirtificate.pdf')

