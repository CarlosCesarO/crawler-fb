from nameChurch import nameChurch
import pandas as pd

data = nameChurch()
nome = data[0]
faceb = data[1]
email = data[2]

df = pd.DataFrame({ "Nomes": nome, "Facebook": faceb, "E-mail": email })
writer = pd.ExcelWriter('EmailsCidSP.xlsx', engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)
writer.save()

