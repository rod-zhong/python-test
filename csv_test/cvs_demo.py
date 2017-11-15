import csv
import io
def write_2_csv(name):
    with open(name,"w") as csv:
        csvwriter = csv.write(csv)
        csvwriter.writerow(("row_nbr","row_name"))
        for x in range(1,100):
            csvwriter.writerow((x,"Hello"+x))

write_2_csv("demo.csv")

