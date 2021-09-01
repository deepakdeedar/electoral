import scrapper
import pandas as pd

scrapper = scrapper.Scrapper()


epic_id = 'GDN0225185'
r = scrapper.start(epic_id)
print(r)
result = [r]


df = pd.DataFrame(result, columns=['c_id', 'epic_no', 'name', 'gender', 'age', 'rln_name', 'last_update', 'state',
                  'district', 'ac_name', 'ac_no', 'pc_name', 'ps_name', 'slno_inpart', 'st_code', 'ps_lat_long', 'part_no', 'part_name'])
df.to_csv('Voter.csv', index=False, encoding='utf-8')

# print(record)
# # # stop scraping
# driver.quit()
