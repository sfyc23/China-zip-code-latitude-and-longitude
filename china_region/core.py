#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from china_region.constants import (
    CITY_DF
)


def search(province=None, city=None, county=None):
    my_df = CITY_DF
    if province:
        province = re.sub(r'[省]{1}$', '', province)
        sp = my_df['province'].str.contains(province)
        my_df = my_df[sp]

    if city and my_df.shape[0]:
        sc = my_df['city'].str.contains(city)
        my_df_temp = my_df[sc]
        if my_df_temp.shape[0] and len(city) > 2 and city[-1] in '市盟州区县台':
            n_city = re.sub(r'[市盟州区县台]{1}$', '', city)
            sc = my_df['city'].str.contains(n_city)
            my_df_temp = my_df[sc]
        my_df = my_df_temp

    county = county if county else city
    if county:
        scc = my_df['county'].str.contains(county)
        my_df_temp = my_df[scc]

        if my_df_temp.shape[0] and len(county) > 2 and county[-1] in '市区县旗盟州区港门台尔':
            n_county = re.sub(r'[市区县旗盟州区港门台尔]{1}$', '', county)
            scc = my_df['city'].str.contains(n_county)
            my_df_temp = my_df[scc]
        my_df = my_df_temp

    return my_df.to_dict('records')


# if __name__ == '__main__':
#     ret = search(province='广西省', county='临桂')
#     print(ret)
