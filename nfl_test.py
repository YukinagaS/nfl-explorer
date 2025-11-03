import nfl_data_py as nfl
from datetime import datetime
import requests
import os

# Initialize Excel File
# date_string = datetime.now().strftime('%Y%m%d-%H%M%S')
# excel_path = f'./XLSX/record{date_string}.xlsx'
# print(f'Recording to: {excel_path}')

"""
Download all season results and save to Excel.
"""
#seasons = range(1999, 2026)
#df = nfl.import_schedules(seasons)
#df.to_excel(excel_path, engine='openpyxl', index=False)

"""
Download all team image assets.
"""
team_info = nfl.import_team_desc()
url_columns = [
    'team_logo_espn',
    'team_wordmark',
    'team_logo_squared'
    ]

for col in url_columns:
    os.makedirs(f'IMG/{col}', exist_ok=True)

    for index, row in team_info.iterrows():
        url = row[col]
        imagename = url.split('/')[-1]
        filename = f'IMG/{col}/{imagename}'

        response= requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded:{filename}')
        else:
            print(f'Failed to download:{url}')
