data = {}
with open("XNSE-BAJAJ_AUTO.csv") as b, open("data-writes.txt", "w+") as w:
    pricelist = []
    for rec in b:
        rec = rec.strip()
        cols = [x.strip('"') for x in rec.split(',')]
        if cols[2] == "Open" or cols[2] == "High":
            continue
        if cols[1] in data:
             data[cols[1].strip()].append(float(cols[2]))
        else:
             data[cols[1].strip()] = [float(cols[2])]
    for year in data:
        avg_price = round(sum(data[year]) / len(data[year]), 2)
        w.write("Avg price for {} is {} \n".format(year, avg_price))