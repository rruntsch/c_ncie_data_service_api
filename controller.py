from c_ncie_data_service_api import c_ncie_data_service_api

api_result = c_ncie_data_service_api('daily-summaries', 'AWND,WSF2,WSF5', 'USW00094846,USW00014925,USW00023293', '2000-01-01', '2020-12-31', '90,-180,-90,180')
print(api_result.get_data())
api_result.write_data_file('c:/project_data/weather/weather_data.csv')


# National Data Buoy Center: https://www.ndbc.noaa.gov/ (Examples: AUCE, WHRI2)
# Rochester International Airport: USW00014925; Chicago O'Hare International Airport: USW00094846; San Jose International Airport: USW00023293

