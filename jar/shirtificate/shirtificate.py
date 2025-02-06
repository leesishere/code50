from fpdf import FPDF

pdf = fpdf.FPDF(orientation="landscape", format="A4")
# 210mm wide by 297mm tall.


pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")


