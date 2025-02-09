import sys
sys.path.append('/workspaces/21178063/shirtificate')
_PATH = '/workspaces/21178063/shirtificate'
image_path = f"{_PATH}/shirtificate.png"

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, orientation='landscape', format='A4'):
        super().__init__(orientation=orientation, format=format)
        self._name = ""
        self.add_page()

    def header(self):
        self.set_font('Helvetica', 'B', 50)
        self.set_text_color(0, 0, 0)  # Set text color to black
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='c')

    @name.setter
    def name(self,myname):
        self._name = myname


pdf = PDF()
pdf.name = input("Name: ")

pdf.set_font_size(30)
pdf.set_text_color(0, 0, 0)
pdf.text(x=47.4,y=140, text=f"{pdf.name} took CS50")

pdf.image('shirtificate.png',w=pdf.w/2)

# Output PDF
pdf.output('shirtificate.pdf')

