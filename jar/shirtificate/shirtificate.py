from fpdf import FPDF

pdf = fpdf.FPDF(orientation="landscape", format="A5")

pdf = fpdf.FPDF(orientation="landscape", format="A4")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")


