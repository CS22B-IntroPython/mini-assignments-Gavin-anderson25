import csv
data = open(r"C:\Users\gavin_zv\OneDrive\Documents\Homework\SJSU\Python 22B\C22B_sp25_datafiles\Week1-Review Python\drosphila.csv")
excel = csv.reader(data)
print(excel)
drosophila = []
for i in excel:
    print(i)
    drosophila.append(i)
Dm_Ds = []

def get_gene():
    for k in range(len(drosophila)):
        if drosophila[k][0] == 'Drosophila melanogaster' or drosophila[k][0] == 'Drosophila simulans':
            Dm_Ds.append(drosophila[k][2])

def gene_exp(targets):
    for k in range(len(drosophila)):
        sum = 0
        for i in list(targets):
            sum += drosophila[k][1].count(i)
        perc = sum / len(drosophila[k][1])
        if perc > 0.65:
            desig = "high"
        elif perc <= 0.65 and perc >= 0.45:
            desig = "medium"
        elif perc < 0.45:
            desig = "low"
        print(f"Gene {drosophila[k][2]} has a {desig} {targets.upper()} content.")

get_gene()
print(Dm_Ds)
gene_exp("at")

