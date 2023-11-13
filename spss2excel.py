import pandas as pd
import sys
import os
from datetime import datetime

def convert_spss_to_excel(spss_file):
    if not os.path.isfile(spss_file):
        print("Datei nicht gefunden: ", spss_file)
        return

    df = pd.read_spss(spss_file)

    current_time = datetime.now().strftime("%d_%m_%H%M%S")

    excel_file = os.path.splitext(spss_file)[0]+"_"+current_time + ".xlsx"

    df.to_excel(excel_file, index=False)
    print("Datei gespeichert als: ", excel_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bitte geben Sie genau einen Dateinamen an.")
    else:
        spss_file = sys.argv[1]
        convert_spss_to_excel(spss_file)
