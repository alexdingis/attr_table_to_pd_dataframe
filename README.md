# attr_table_to_pd_dataframe

## Purpose

The purpose of this script is to transform the attribute table of a feature class or shapefile into a pandas dataframe.

## How to use

1. In your own code, make sure you have the `arcpy` and `pandas` libraries loaded
    * `pandas` should be loaded as `pd` e.g. `import pandas as pd`
    
2. Insert the function `attr_table_to_df()` to the top of your own script

3. Call the function `attr_table_to_df()`, remember that it takes the argument `fc` so you will need to pass to it a feature class
    * my_result = `attr_table_to_df(input_fc)`
    
## Think this script can be improved?

Let me know! I'd love to hear it.

    
