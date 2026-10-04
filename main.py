from pyscript import display, document

def SKU_generator(event=None):
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("stock_qty").value

    if product_name.strip() == "":
        document.getElementById("sku_output").innerHTML = (
            "<span style='color:red;'>Americano</span>"
        )
        return

    if stock_qty.strip() == "":
        document.getElementById("sku_output").innerHTML = (
            "<span style='color:red;'>50</span>"
        )
        return

    stock_qty = int(stock_qty)

    category_code = category[:3].upper()
    product_code = product_name[:4].upper()

    sku = category_code + "-" + product_code + "-" + str(stock_qty)

    document.getElementById("sku_output").innerHTML = (
        "<div>Generated SKU:</div>"
        "<div class='generated-sku'>" + sku + "</div>"
    )


def create_order(event=None):

   
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")


   
    price1 = 99
    price2 = 129
    price3 = 159
    price4 = 159
    price5 = 129


   
    subtotal = (
        float(price1) * prod1.checked +
        float(price2) * prod2.checked +
        float(price3) * prod3.checked +
        float(price4) * prod4.checked +
        float(price5) * prod5.checked
    )

    tax_rate = 0.12

    tax = subtotal * tax_rate

    total = subtotal + tax


    receipt = "<h3>Receipt</h3>"



    if prod1.checked:
        receipt += """
        <div class="receipt-row">
            <span>Americano</span>
            <span>₱99.00</span>
        </div>
        """

    if prod2.checked:
        receipt += """
        <div class="receipt-row">
            <span>Spanish Latte</span>
            <span>₱129.00</span>
        </div>
        """

    if prod3.checked:
        receipt += """
        <div class="receipt-row">
            <span>Cold Brew</span>
            <span>₱159.00</span>
        </div>
        """

    if prod4.checked:
        receipt += """
        <div class="receipt-row">
            <span>Affogato</span>
            <span>₱159.00</span>
        </div>
        """

    if prod5.checked:
        receipt += """
        <div class="receipt-row">
            <span>Caramel Macchiato</span>
            <span>₱129.00</span>
        </div>
        """



    if subtotal == 0:
        receipt = """
        <div style="text-align:center; color:#888;">
            Please select at least one item.
        </div>
        """

        document.getElementById("show").innerHTML = receipt
        return

    receipt += f"""
        <div class="receipt-row receipt-total">
            <span>Subtotal</span>
            <span>₱{subtotal:.2f}</span>
        </div>

        <div class="receipt-row">
            <span>VAT (12%)</span>
            <span>₱{tax:.2f}</span>
        </div>

        <div class="receipt-row receipt-total">
            <span>Total</span>
            <span>₱{total:.2f}</span>
        </div>
    """


    document.getElementById("show").innerHTML = receipt
