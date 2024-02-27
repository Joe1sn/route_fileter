import requests
import json
import pandas as pd

from rprint import *
from lxml import etree

search_url = "https://www.opencve.io/cve?cvss=&search={product}&page={page}"
years = []
def get_cve_json(product: str, page: int) -> list:
    header = ["CVE","Vendors","Products","Updated","CVSS v2","CVSS v3","cve-summary"]
    url = search_url.format(product=product, page=page)
    ret = []
    r =requests.get(url)
    if r.status_code == 200:
        html_tree = etree.HTML(r.text)
        table_html = html_tree.xpath('//*[@id="cves"]')
        if table_html:
            table_html = table_html[0]
        else:
            return []
        table_html = etree.tostring(table_html, pretty_print=True, encoding='utf-8')
        df_list = pd.read_html(table_html)
        df = df_list[0]
        table_data = df.values.tolist()
        table_data.insert(0,header)
        counter = 0
        for row in table_data[1:]:
            if counter%2 == 0:
                ret.append(dict(zip(header, row)))
            else:
                ret[-1].update({"cve-summary": row[0].lower()})
            counter += 1
        return ret
    else:
        return []

def result_init(result: dict, cve_list: list) -> None:
    # tmp = {name:{"overflow": 0, "RCE": 0, "command injection": 0,}}
    for cve in cve_list:
        if type(cve["Products"]) == str and (cve["CVE"][4:8] in years):
            for name in cve["Products"][2:].split(", "):
                try:
                    if name not in result.keys():
                        result.update({name:{"total cve":0, "overflow": 0, "command injection": 0,}})
                except:
                    error("Error in init, proble wrong product")
                    continue


def stastic(result: dict, cve_list: list) -> bool:
    ret = True
    result_init(result, cve_list)
    for cve in cve_list:
        if  "2023" in cve["CVE"][:9]:
            if type(cve["Products"]) == str:
                for name in cve["Products"][2:].split(", "):
                    if "overflow" in cve["cve-summary"].lower():
                        result[name]["overflow"] += 1
                    if "command injection" in cve["cve-summary"].lower():
                        result[name]["command injection"] += 1
                    result[name]["total cve"] += 1
        else:
            ret = False
    return ret

if __name__ == "__main__":
    banner()
    keywords = ["tenda","tp-link","mercury"]
    years = ["2024","2023"]
    for word in keywords:
        cve_list = get_cve_json(word,1)
        result = {}
        page = 1
        while(stastic(result, cve_list)):
            # info(word, page)
            cve_list = get_cve_json(word,page)
            page+=1
        with open(word+".log","w") as f:
            f.write(str(result))
            f.write("\n")
        info("="*0x10," "*5,word," "*5,"="*0x10)
        for i in result:
            success(i.ljust(35," "), result[i])