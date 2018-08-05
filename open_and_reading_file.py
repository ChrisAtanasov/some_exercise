# i will try to open a catalog with products and manipulating the items inside

product_number=[]


with open("text_for_reading", 'r', encoding='UTF-8') as p:
    for line in p:
        each_line=line.strip()
        splittet_line=each_line.split(",")
        product_number.append(splittet_line[0])


for num in product_number:
    print(num)

#here we read the file and after that we print all the product number from the catalog


