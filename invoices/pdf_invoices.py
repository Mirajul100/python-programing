import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

file_path = glob.glob("invoices/xl/*.xlsx")

for file in file_path:
    df = pd.read_excel(file , sheet_name="Sheet 1")
    pdf = FPDF(orientation="portrait" , unit="mm" , format="A4")

    pdf.add_page()
    file_name = Path(file).stem
    invoice_nm = file_name.split("-")[0]
    date = file_name.split("-")[1]
    pdf.set_font(family="times" , size=10 , style="B")
    pdf.set_text_color(100 , 100 ,100)
    pdf.cell(w= 0 , h= 10 , txt=f"Invoice Number: {invoice_nm}" , ln= 1)
    pdf.cell(w=0 , h=10 , txt=f"Date: {date}")
    pdf.output(f"invoices/pdf_file/{file_name}.pdf")
