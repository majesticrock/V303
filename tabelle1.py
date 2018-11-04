import numpy as np
#ohne Rauschen

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

ignore = True
werte = csv_read("phasenverschiebung.csv")

begin_table = "\\begin{table}\n"
begin_tabular = "\\begin{tabular}{cc}\n"

head = "\t$\\Delta\\phi$ & $U / V$ \\\\\n"

caption = "\\caption{Messwerte der Phasenverschiebung.}\n"
label = "\\label{tab:Tabelle 1.}\n"
end_tabular = "\\end{tabular}\n"
end_table = "\\end{table}\n"

with open("build/tabelle1.tex", "w") as t:
    t.write(begin_table)
    t.write("\\centering")

    
    t.write(begin_tabular)
    t.write("\\toprule\n")
    for line in werte:
        if(ignore):
            t.write(head)
            t.write("\\midrule\n")
            ignore = False
        else:
            t.write("\t" + line[0] + " & " + line[1] + " \\\\\n")
    t.write("\\bottomrule\n")
    #t.write("\\label{tab:(b)}\n")
    t.write("\\caption{Messwerte ohne Rauschen}\n")
    t.write(end_tabular)
    ignore = True
    t.write(begin_tabular)
    t.write("\\toprule\n")
    for line in werte:
        if(ignore):
            t.write(head)
            t.write("\\midrule\n")
            ignore = False
        else:
            t.write("\t" + line[0] + " & " + line[2] + " \\\\\n")
    t.write("\\bottomrule\n")
    #t.write("\\label{tab:(b)}\n")
    t.write("\\caption{Messwerte mit Rauschen}\n")
    t.write(end_tabular)
    t.write(label)
    t.write(caption)
    t.write(end_table)
