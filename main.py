import os
import graphviz

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"
os.system(r'eralchemy -i "mssql+pyodbc://USERBD:SENHAUSERBD@INSTANCIA/DATABASE?driver=ODBC+Driver+17+for+SQL+Server" -o diagrama.er')
os.system('eralchemy -i diagrama.er -o diagrama_EVOLUTIVA.pdf')


