import csv
import io
def write_2_csv(name):
    with open(name,"w") as csv:
        csvwriter = csv.write(csv)
        csvwriter.writerow(("row_nbr","row_name","Type"))
        for x in range(1,100):
        	if x% 2 ==0:
        		csvwriter.writerow((x,"Hello"+x,"B"))
        	elif x% 2 != 0:
        		csvwriter.writerow((x,"Hello"+x,"A"))
            

write_2_csv("demo.csv")

