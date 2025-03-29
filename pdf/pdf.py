from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait" , unit='mm' , format="A4")
pdf.set_auto_page_break(auto=False , margin=0)
df = pd.read_csv("pdf/topics.csv")

for index , raw in df.iterrows():
    # Header section
    pdf.add_page()
    pdf.set_font(family="times" , style="B" , size=24)
    pdf.set_text_color(100 , 100 , 100)
    pdf.cell(w= 0 , h=20 , txt=raw["Topic"] , align="L" , ln=1)

    for i in range(25 , 298 , 10):
        pdf.line(10 , i , 200 , i)

    # Footer section
    pdf.ln(255)
    pdf.set_font(family="times" , style="I" , size=8)
    pdf.set_text_color( 45 , 64 , 5)
    pdf.cell(w=0 , h=10 , txt=raw["Topic"] , align="R")

    for i in range(raw["Pages"] - 1):
        pdf.add_page()

        # Footer section
        pdf.ln(275)
        pdf.set_font(family="times" , style="I" , size=8)
        pdf.set_text_color(180 , 180 , 180)
        pdf.cell(w=0 , h=10 , txt=raw["Topic"] , align="R")


        for i in range(25 , 298 , 10):
            pdf.line(10 , i , 200 , i)

pdf.output("pdf/output.pdf")