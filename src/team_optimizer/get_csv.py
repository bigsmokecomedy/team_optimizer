import csv
from io import StringIO
from typing import Iterator, Any

import requests

from src.team_optimizer.sign_up import SignUp

CSV_SOURCE:str = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR2TLMPl7zw8TxmMYhF7nIRzSZfF02p2hFBiT7Px_zYPw8tsE-Cr45FQrG7la_CE_A3GbQRQo4RsDLG/pub?output=csv"



def get_csv(csv_source:str = CSV_SOURCE)->Iterator[Any]:
    with requests.Session() as s:
        text:str = s.get(csv_source).content.decode("UTF-8")
        reader = csv.reader(text.splitlines(), delimiter=",")
        headers = next(reader)


    for row in reader:
        yield dict(zip(headers, row))

def get_sign_ups()->Iterator[SignUp]:
    for d in get_csv():
        yield SignUp.from_dict(d)

if __name__ == "__main__":
    result = list(get_sign_ups())
    import pprint
    pprint.pprint(result)



