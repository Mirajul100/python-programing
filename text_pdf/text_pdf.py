from fpdf import FPDF
import glob
from pathlib import Path

file_path = glob.glob("text_pdf/text/*.txt")
pdf = FPDF(orientation="portrait" , unit="mm" , format="A4")

for path in file_path:
    file = Path(path).stem
    name = file.title()
    pdf.add_page()

    pdf.set_font(family="times" , style="BU" , size=14)
    pdf.set_text_color( 0 , 0 , 0)
    pdf.cell(w= 0 , h= 12 , txt=name, align="L" , ln=1)

    with open (f"{path}" , "r") as file:
        content = file.read()

    pdf.set_font(family="times" , size=12 , style="BI")
    pdf.set_text_color(45 , 64 , 5)
    pdf.multi_cell(w= 0 , h= 6 , txt=content)


    
pdf.output(f"text_pdf/pdf_file.pdf")