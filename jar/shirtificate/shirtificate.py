from fpdf import FPDF
# 210mm wide by 297mm tall.
pdf = fpdf.FPDF(orientation="landscape", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", x=20, y=60)


pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=8)
pdf.set_fill_color(255, 255, 0)
pdf.multi_cell(w=50, text=LOREM_IPSUM[:100], new_x="LEFT", fill=True)
pdf.ln()
pdf.set_stretching(150)
pdf.multi_cell(w=50, text=LOREM_IPSUM[:100], new_x="LEFT", fill=True)


from fpdf import FPDF

pdf = FPDF()

pdf.output("pdf-with-image.pdf")
