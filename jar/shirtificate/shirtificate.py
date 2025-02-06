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

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=50)
pdf.cell(text="**Lorem** __Ipsum__ --dolor--", markdown=True, new_x='LEFT', new_y='NEXT')
pdf.cell(text="\\**Lorem\\** \\\\__Ipsum\\\\__ --dolor--", markdown=True)
pdf.output("markdown-styled.pdf")

pdf.output("style.pdf")
