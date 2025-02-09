import sys
sys.path.append('/workspaces/21178063/shirtificate')
_PATH = '/workspaces/21178063/shirtificate'
image_path = f"{_PATH}/shirtificate.png"

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name, orientation='P', format='A4'):
        super().__init__(orientation=orientation, format=format)
        self._name = name
        self.add_page()

    def header(self):
        self.set_font('Helvetica', 'B', 50)
        self.set_text_color(0, 0, 0)  # Set text color to black
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='c')
        self.image('shirtificate.png',w=self.w/2)

    @name.setter
    def name(self,name):
        self._name = name


pdf = PDF(input("Name: "))


pdf.set_font_size(30)
pdf.set_text_color(0, 0, 0)
pdf.text(x=47.4,y=140, text=f"{pdf.name} took CS50")



# Output PDF
pdf.output('shirtificate.pdf')

