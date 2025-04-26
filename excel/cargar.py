import pandas as pd

hospitales = pd.read_csv('/workspaces/estructurasDatos/excel/hospital.csv')
hospitales['AÑO'] = hospitales['AÑO'].str.replace(',','')
hospitales['AÑO'] = hospitales['AÑO'].astype(int)
print(hospitales.head())
print(hospitales.dtypes)
