# -*- coding: utf-8 -*-
"""
Created on Sat 2018/01/20

@author: Alex

The purpose of this script is to transform the attribute table of a feature class or shapefile to a pandas dataframe

This script was produced using Spyder 3 and Python 2.7
"""

import arcpy
import pandas as pd
import time
#
fc_input = r"C:\this\is\the\path\to\your\geodatabase\and\feature\class"
#
#
#
def attr_table_to_df(fc):
    #
    fields     = [f.name for f in arcpy.ListFields(fc) if f.type != "Date"]
    #   
    table      = []
    #
    try:
        with arcpy.da.SearchCursor(fc, fields) as cursor:
            for row in cursor:
                table.append(list(row))
        del row, cursor
        #
        df = pd.DataFrame(table, columns = fields)
        #
        return df
        #
    except Exception as e:
        print e
# ------------------------------------
#
start_time = time.time()
#
# where x is the output DataFrame returned to the user
#
x = attr_table_to_df(fc_input)
#
#
#
end_time = round(time.time() - start_time, 5)
#
print "Seconds elapsed: {0}".format(end_time)













