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
    pdf.set_font(family="times" , size=16 , style="B")
    pdf.set_text_color(45 , 64 , 5)
    pdf.cell(w= 0 , h= 30 , txt="----OTTAMA ONLINE SHOP----" , align="C" , ln=1)


    pdf.set_font(family="times" , size=14 , style="B")
    pdf.set_text_color(0 , 0 , 0)
    pdf.cell(w= 0 , h= 5 , txt=f"Invoice Number : {Pdf_file_name}" , align="L" , ln=1)

    pdf.set_font(family="times" , size=14 , style="B")
    pdf.set_text_color(0 , 0 , 0)
    pdf.cell(w= 0 , h= 10 , txt=f"Date : {date}" , align="L" , ln=1)

    # Add header 
    header = list(df.columns)
    header = [item.replace("_" , " ").title() for item in header]
    pdf.set_font(family="times" , size=10 , style="B")
    pdf.set_text_color(0 , 0 , 0)
    pdf.cell(w= 30 , h= 8 , txt= header[0] , border=1)
    pdf.cell(w= 50 , h= 8 , txt= header[1] , border=1)
    pdf.cell(w= 50 , h= 8 , txt= header[2] , border=1)
    pdf.cell(w= 30 , h= 8 , txt= header[3] , border=1)
    pdf.cell(w= 30 , h= 8 , txt= header[4] , border=1 , ln=1)

    for index , raw in df.iterrows():

        # Add table
        pdf.set_font(family="times" , size=10 , style="B")
        pdf.set_text_color(0 , 0 , 0)

        # Convert raw list into string 
        pdf.cell(w= 30 , h= 8 , txt=str(raw["product_id"])  , border=1)
        pdf.cell(w= 50 , h= 8 , txt=str(raw["product_name"])  , border=1)
        pdf.cell(w= 50 , h= 8 , txt=str(raw["amount_purchased"]) , border=1)
        pdf.cell(w= 30 , h= 8 , txt=str(raw["price_per_unit"]) , border=1)
        pdf.cell(w= 30 , h= 8 , txt=str(raw["total_price"]) , border=1 , ln=1)

    total_sum = df["total_price"].sum()
    total_pur = df["amount_purchased"].sum()
    pdf.cell(w= 30 , h= 8 , txt=""  , border=1)
    pdf.cell(w= 50 , h= 8 , txt=""  , border=1)
    pdf.cell(w= 50 , h= 8 , txt=f"Total purchased : {total_pur}" , border=1)
    pdf.cell(w= 30 , h= 8 , txt="" , border=1)
    pdf.cell(w= 30 , h= 8 , txt=f"Total Bill : {total_sum}" , border=1 , ln=1)

    pdf.set_font(family="times" , size= 14 , style="B")
    pdf.set_text_color(0 , 0 , 0)
    pdf.cell(w= 0 , h= 8 , txt=str(f"Total price is is : {total_sum}") , ln=1)
    pdf.cell(w= 0 , h= 8 , txt="Thank you" , ln=1)
    
    pdf.output(f"invoices/pdf_file/{pdf_file_path}.pdf")
