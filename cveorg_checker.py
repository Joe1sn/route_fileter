import requests
import json
import pandas as pd

from rprint import *
from lxml import etree

search_url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={keyword}"
detail_url = "https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve}"

def get_cve_json(keyword: str) -> dict:
    header = ["CVE","Detail"]
    url = search_url.format(keyword=keyword)
    r =requests.get(url)
    if r.status_code == 200:
        html_tree = etree.HTML(r.text)
        table_html = html_tree.xpath('//*[@id="TableWithRules"]/table')[0]
        table_html = etree.tostring(table_html, pretty_print=True, encoding='unicode')
        df_list = pd.read_html(table_html)
        df = df_list[0]
        table_data = df.values.tolist()
        table_data.insert(0,header)
        ret = [dict(zip(header, row)) for row in table_data[1:]]
        return ret
    else:
        return {}

if __name__ == "__main__":
    banner()
    print(get_cve_json("AC6"))