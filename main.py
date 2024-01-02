import pandas as pd
from deep_translator import GoogleTranslator
import time

input_file_path = 'Order Export.xls'

df = pd.read_excel(input_file_path, dtype=str)

start = time.time()

def translate_to(value, language="en"):
    if value == "NAN": return value
    if not value: return value
    try:
        return GoogleTranslator(source='auto', target=language).translate(value)
    except Exception as e:
        return value

if __name__ == '__main__':

    print("Translating cells data to english............This will take about 10 min time. Be patient.")
    df = df.map(translate_to)
    print("Cells data translated successfully in ",time.time()-start)

    print("\n\nTranslating column headers data to english............")
    df = df.rename(columns=lambda x: translate_to(x, "en"))

    print("Completed tranlating in", time.time()-start)

    output_file_path = 'translated_file.xlsx'

    print("Saving to new excel file.....")
    df.to_excel(output_file_path, index=False)

    print(f"New Excel file created at: {output_file_path}")