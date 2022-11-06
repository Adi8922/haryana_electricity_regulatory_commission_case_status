import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import copy 
url = "https://herc.gov.in/OnlineStatus.aspx"
paylode1 = {}
paylode2={}
paylode3={}

data = {}
final_data = []
session = requests.Session()
response1 = session.get(url,verify=False)
html_content1 = response1.content
soup1 = BeautifulSoup(html_content1,"lxml")

Headers1 = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.5",
        "Connection":"keep-alive",
        "Content-Type":"application/x-www-form-urlencoded",
        "Host":"herc.gov.in",
        "Origin":"https://herc.gov.in",
        "Referer":"https://herc.gov.in/OnlineStatus.aspx",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
    }

paylode1 = {
        "ctl00_ScriptManager_HiddenField" : "",
        "__EVENTTARGET"	: "ctl00$cphcontent$cphrightholder$ddlconnectionYearWise",
        "__EVENTARGUMENT" : "",
        "__LASTFOCUS" : "",
        "__VIEWSTATEGENERATOR" : "67A11924",
        "__SCROLLPOSITIONX" : "0",
        "__VIEWSTATEENCRYPTED" :"",
        "ctl00$ucSearch$cx" : "013280925726808751639:i85g1b47nss",
        "ctl00$ucSearch$cof" : "FORID:9",
        "ctl00$ucSearch$txtSearch" : "Enter+Your+Keywords",
        "ctl00$cphcontent$cphrightholder$ddlconnectionYearWise" : "1",
        "ctl00$cphcontent$cphrightholder$drpyear" : "0",
        "ctl00$cphcontent$cphrightholder$drppro" : "0"
}

view_state1 = soup1.find("input",attrs={"id":"__VIEWSTATE"})['value']
paylode1["__VIEWSTATE"] = view_state1
responce2 = session.post(url,headers = Headers1, data = paylode1, verify=False)
html_content2 = responce2.content
soup2 = BeautifulSoup(html_content2,"lxml")



view_state2 = soup2.find("input",attrs={"id":"__VIEWSTATE"})['value']
paylode2 = paylode1.copy()
paylode2["__EVENTTARGET"] = "ctl00$cphcontent$cphrightholder$drpyear"
paylode2["__VIEWSTATE"] = view_state2
paylode2["ctl00$cphcontent$cphrightholder$drpyear"]="2022"
responce3 = session.post(url,headers = Headers1, data = paylode2, verify=False)
html_content3 = responce3.content
soup3 = BeautifulSoup(html_content3,"lxml")



view_state3 =soup3.find("input",attrs={"id":"__VIEWSTATE"})['value']
paylode3 = paylode2.copy()
paylode3["__EVENTTARGET"] = ""
paylode3["__VIEWSTATE"] = view_state3
paylode3["ctl00$cphcontent$cphrightholder$btnsearchYearwise"] = "GO"
paylode3["ctl00$cphcontent$cphrightholder$drppro"] = "1"
responce4 = session.post(url,headers = Headers1, data = paylode3, verify=False)
html_content4 = responce4.content
soup4 = BeautifulSoup(html_content4,"lxml")
# print(soup4)
petition_ra_number = soup4.find("a",{"id":"ctl00_cphcontent_cphrightholder_gvOnlineStatus_ctl02_lnkDetails"}).text
date = soup4.find_all("td")[1].text
petitioner = soup4.find_all("td")[2].text
respondent = soup4.find_all("td")[3].text
subject = soup4.find_all("td")[4].text
status = soup4.find_all("td")[5].text

data["Petition/RA Number"] = petition_ra_number
data["Date"] = date
data["Petitioner(s)"] = petitioner
data["Respondent(s)"] = respondent
data["Subject"] = subject
data["Status"] = status
final_data.append(data)
print(final_data)