import datetime

import tabula
import os
import pandas as pd
from db_config import config

Ingestion_timestamp = datetime.datetime.today().strftime('%d-%m-%Y')
tstmp = str(Ingestion_timestamp)

try:
    merchant = '98eb4e08'

    pdf_name = f'{merchant}.pdf'
    # pdf_path = f'{config.pdf_path}{pdf_name}'
    pdf_path = r"C:\Users\admin\Downloads\98eb4e08.pdf"

    csv_name = f'{merchant}_{tstmp}.csv'
    csv_path = f'{config.csv_path}{csv_name}'




    # tabula.convert_into(pdf_path, csv_path, output_format="json", pages='all',lattice=True)
    # # tabula.convert_into(pdf_path, csv_path, output_format="csv", pages='all', lattice=False)
    # print(f'CSV created on path....{csv_path}')


#  ****************************************************************************************************************************


    # df = tabula.read_pdf(pdf_path, pages='all', lattice =True,stream=False)[1]
    # df.columns = df.columns.str.replace('\r', ' ')
    # print('')
    #
    # excel_name = csv_name = f'{merchant}_{tstmp}.xlsx'
    # writer = pd.ExcelWriter(excel_name,engine='xlsxwriter')
    # row = 0
    # spaces = 0
    # # df = pd.DataFrame(columns=['MERCHANT_NAME','STORE_NAME','Address','City','State'])
    # for df in df_list:
    #     df.to_excel(writer,startrow=row , startcol=0,index=False)
    #     row = row + len(df.index) + spaces + 1
    # writer.save()


#  ****************************************************************************************************************************


    # df2 = pd.DataFrame(columns=['MERCHANT_NAME','STORE_NAME','Address','City','State'])
    # dfs = tabula.read_pdf(pdf_name, pages='all')
    # for df in dfs:
    #     df2 = df2.append(df, ignore_index=True)
    # print('')


#  ****************************************************************************************************************************

except Exception as e:
    print(e)