import pandas as pd
from fpdf import FPDF

csvFilePath = "online_store/008 articles.csv"

df = pd.read_csv(csvFilePath , dtype={"id" : str})

class InStock:

    def __init__(self , item_id):
        self.item_id = item_id
        self.item_name = df.loc[df["id"] == self.item_id , "name"].squeeze()
        self.item_price = df.loc[df["id"] == self.item_id , "price"].squeeze()

    def available(self):
        stock = df.loc[df["id"] == self.item_id , "in stock"].squeeze()
        if stock > 0:
            return True
        else :
            return False
        

class Invoice:
    def __init__(self , itemId , item_name , item_price):
        self.itemId = itemId
        self.name = item_name
        self.price = item_price

    def generate(self):

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=18, style="B")
        pdf.set_text_color(45 , 64 , 5)
        pdf.cell(w=0, h=15, txt="---THANK YOU FOR VISITING Y0U SHOP---", ln=1 , align="C")

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=10, txt=f"receipts id : {self.itemId.item_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=10, txt=f"Item name : {self.name.item_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=10, txt=f"Item price : {self.price.item_price}", ln=1)

        pdf.output("online_store/receipt.pdf")



print(df)
item = input ("Enter the item id : ")
in_stock = InStock(item_id= item)
in_stock1 = InStock(item)
in_stock2 = InStock(item)

if in_stock.available():
    user_input = input ("If parches item than Enter the yes or if not than press enter key : ")
    if user_input == "yes":
        invoice = Invoice(in_stock , item_name=in_stock1 , item_price=in_stock2)
        invoice.generate()
    else :
        print ("There are not stock is available")