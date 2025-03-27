from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait" , unit='mm' , format="A4")
df = pd.read_csv("pdf/topics.csv")

for index , raw in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="times" , style="B" , size=24)
    pdf.set_text_color(100 , 100 , 100)
    pdf.cell(w= 0 , h=20 , txt=raw["Topic"] , align="L" , ln=1)
    pdf.line(10 , 25 , 200 , 25)

pdf.output("output.pdf")