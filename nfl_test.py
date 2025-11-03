import nfl_data_py as nfl
from datetime import datetime

# Initialize Excel File
date_string = datetime.now().strftime('%Y%m%d-%H%M%S')
excel_path = f'./XLSX/record{date_string}.xlsx'
print(f'Recording to: {excel_path}')

seasons = range(1999, 2026)
df = nfl.import_schedules(seasons)

df.to_excel(excel_path, engine='openpyxl', index=False)
