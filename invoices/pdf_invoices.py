import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

file_path = glob.glob("invoices/xl/*.xlsx")

for file in file_path:
    df = pd.read_excel(file , sheet_name="Sheet 1")
    pdf = FPDF(orientation="portrait" , unit="mm" , format="A4")
    pdf_file_path = Path(file).stem
    Pdf_file_name =  pdf_file_path.split("-")[0]
    date = pdf_file_path.split("-")[1]
    pdf.add_page()
    pdf.set_font(family="times" , size=14 , style="B")
    pdf.set_text_color(0 , 0 , 0)
    pdf.cell(w= 0 , h= 10 , txt=f"Invoice Number : {Pdf_file_name}" , align="L" , ln=1)
    pdf.cell(w= 0 , h= 10 , txt=f"Date : {date}" , align="L" , ln=1)
    pdf.output(f"invoices/pdf_file/{pdf_file_path}.pdf")
