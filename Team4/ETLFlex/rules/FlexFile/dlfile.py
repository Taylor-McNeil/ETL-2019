import requests
import urllib.request
import shutil
from datetime import datetime

hi = datetime.now()
print(hi.strftime('%Y-%m-%d %H:%M:%S'))

# url = 'https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'
# file_name = 'testrequest.csv'
#
#
# # Download the file from `url` and save it locally under `file_name`:
# with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
#     shutil.copyfileobj(response, out_file)

# r = requests.get(url, auth=(username, password))
#
# if r.status_code == 200:
#     with open(filename, 'wb') as out:
#         for bits in r.iter_content():
#             out.write(bits)
