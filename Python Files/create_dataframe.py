# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:13:01 2021

@author: Irtza
"""

def get_headers_dataframe(header_color):
    final_header=['HR','Tperi','Tblood','Pulse','SpO2','ABP','PAP','etCO2','awRR','NBP','etCO2','mCO2']
    header=[]
    for i in header_color:
        for j in final_header:
            if i==j:
                header.append(j)
    
    header=list(OrderedDict.fromkeys(header))
    df = pd.DataFrame(columns = header)
    return df,header

def df_values(df,header,value):
     
    if len(value)<len(header):
        value.extend([str(0)]*(len(header)-len(value)))
    length_df = len(df)
    df.loc[length_df] = value[:len(header)]
   # df = df.append(pd.DataFrame([value],columns=header), ignore_index=True)
    print(df)
    return df