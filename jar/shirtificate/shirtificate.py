'''
from fpdf import FPDF
# 210mm wide by 297mm tall.

pdf = FPDF(orientation="landscape", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", x=20, y=60)
pdf.set_font("Helvetica", size=8)
pdf.set_fill_color(255, 255, 255) # White

#pdf.multi_cell(w=50, text=LOREM_IPSUM[:100], new_x="LEFT", fill=True)
pdf.ln()
#pdf.set_stretching(150)
#pdf.multi_cell(w=50, text=LOREM_IPSUM[:100], new_x="LEFT", fill=True)


pdf.cell(text="This")
pdf.set_font(style="B")
pdf.cell(text="is")
pdf.set_font(style="I")
pdf.cell(text="a")
pdf.set_font(style="U")
pdf.cell(text="PDF")
pdf.output("style.pdf")

#pdf.output("shirtificate.pdf")
'''
'''
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=50)
pdf.cell(text="**Lorem** __Ipsum__ --dolor--", markdown=True, new_x='LEFT', new_y='NEXT')
pdf.cell(text="\\**Lorem\\** \\\\__Ipsum\\\\__ --dolor--", markdown=True)
pdf.output("markdown-styled.pdf")

pdf.output("style.pdf")
'''

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'PDF with Markdown-styled Text', 0, 1, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.set_text_color(0, 0, 0)  # Set text color to black

# Manually styled text
pdf.multi_cell(0, 10, '**Lorem** __Ipsum__ --dolor--')

# Escape characters in the text
pdf.multi_cell(0, 10, '\\**Lorem\\** \\\\__Ipsum\\\\__ --dolor--')

# Debugging print statements
print("Page count:", pdf.page_no())
print("Text color:", pdf.text_color)

pdf.output("styled-text.pdf")


