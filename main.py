from pyscript import display, document

def create_order (e):
 document.getElementById('show').innerHTML = ""

 item1 = document.getElementById("item1")
 item2 = document.getElementById("item2")
 item3 = document.getElementById("item3")
 item4 = document.getElementById("item4")
 item5 = document.getElementById("item5")

 subtotal = float(item1.value) * item1.checked + float(item2.value) * item2.checked + float(item3.value) * item3.checked + float(item4.value) * item4.checked + float(item5.value) * item5.checked * 12

 vat = subtotal * 0.12
 amount = subtotal + vat
 
 display(f'Subtotal: {subtotal}', target="show")
 display(f'VAT: {vat}', target ="show")


 display(f'Total amount: {amount}', target="show")


def generate_sku (e):
 document.getElementById("sku-show").innerHTML=""  
 category = document.getElementById("categories").value
 product = document.getElementById("product_name").value
 stock = document.getElementById("stock_quantity").value 
 category = category.upper()
 product = product.upper() 
 char = product[:3]

 SKU = category + "-" + char + "-" + stock 

 display(f'Generated SKU: {SKU}', target="sku-show")
