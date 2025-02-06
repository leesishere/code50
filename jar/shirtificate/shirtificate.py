from fpdf import FPDF

pdf = fpdf.FPDF(orientation="landscape", format="A4",(210, 297))
pdf = FPDF('P', 'mm', (100, 150))

# 210mm wide by 297mm tall.



pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")


