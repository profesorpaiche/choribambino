# =========================================================================== #
# Download of weather stations data
#
# Author: Dante Castro Garro
# Date: 2023-04-22
# =========================================================================== #

# LIBRARIES
# --------------------------------------------------------------------------- #

import pandas as pd
import os
# import requests

# FUNCIONES
# --------------------------------------------------------------------------- #

# PROCEDIMIENTO
# --------------------------------------------------------------------------- #

# Opening weather stations metadata
df = pd.read_csv("metadata.csv", dtype = "str")
codes = df["code"]

# Setting the download parameters
main_url = "https://www.senamhi.gob.pe/usr/data_hist/"
header = "qc00"
format = ".txt"

# Downloading
for cd in codes:
    url = main_url + header + cd + format
    file = "data/" + cd + format
    os.system(f"""wget -O {file} {url} --no-check-certificate""")
