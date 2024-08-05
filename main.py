import  requests,   random,      string,   ctypes,  os,  concurrent.futures
from    os          import       system
os.system("cls")


Key          = "PUT YOUR MF KEY IN HERE https://capmonster.cloud/"
proxies_list = []
class stats:

    genned = 0
    failed = 0

def Title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
Title(f"Brexy Services Webshare | discord.gg/E85ynqyrry | [G] {stats.genned} [F] {stats.failed}")

def GetCookies(proxies):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.webshare.io/', headers=headers, proxies=proxies)
    return response.cookies



def Solve():

    json = {
        "clientKey": Key,
        "task": {
            "type":"RecaptchaV2TaskProxyless",
            "websiteURL":"https://webshare.io",
            "websiteKey":"6LeHZ6UUAAAAAKat_YS--O2tj_by3gv3r_l03j9d"
        }
        }
    response = requests.get("https://api.capmonster.cloud/createTask", json=json)
    #print(response.text)
    if "taskId" in response.text:
        return response.json()['taskId']
    else:
        print("[-] Failed to fetch task id")
        Title(f"Brexy Services Webshare | discord.gg/E85ynqyrry | [G] {stats.genned} [F] {stats.failed}")
        stats.failed += 1 
        return None

def Results():

    taskid = Solve()
    if taskid is None:
        pass
    else:
        json = {
        "clientKey": Key,
        "taskId": taskid
        }
        while True:
            response = requests.get("https://api.capmonster.cloud/getTaskResult", json=json)
            #print(response.text)
            if "solution" in response.text:
                return response.json()["solution"]["gRecaptchaResponse"]
            else:
                continue
            
def CreateAccount():

    proxy_list = open('proxys.txt','r').read().splitlines()
    proxy      = random.choice(proxy_list)
    proxies    = {'http': f'http://{proxy}/','https':f'http://{proxy}/'}
    cookies    = GetCookies(proxies)
    emails     = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@proton.com']
    email      = ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + random.choice(emails)
    password   = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    captcha    = Results()

    headers  = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://proxy2.webshare.io',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://proxy2.webshare.io/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    json_data = {
        'email': email,
        'password': password,
        'tos_accepted': True,
        'recaptcha': captcha,
    }

    

    response = requests.post('https://proxy.webshare.io/api/v2/register/', cookies=cookies, headers=headers, json=json_data, proxies=proxies)
    #print(response.text)
    if "token" in response.text:
        stats.genned += 1
        Title(f"Brexy Services Webshare | discord.gg/E85ynqyrry | [G] {stats.genned} [F] {stats.failed}")
        print(f"[+] Generated account {response.json()['token']}")
        open("Results/tokens.txt", 'a').write(response.json()['token'] + "\n")
        GetProxys(response.json()['token'], proxies)
    else:
        print("[-] Failed to get token")
        stats.failed += 1
        Title(f"Brexy Services Webshare | discord.gg/E85ynqyrry | [G] {stats.genned} [F] {stats.failed}")


def GetProxys(token, proxies):

    cookies = GetCookies(proxies)

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Token ' + token,
    'cache-control': 'no-cache',
    'origin': 'https://proxy2.webshare.io',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://proxy2.webshare.io/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    params = {
        'mode': 'direct',
        'page': '1',
        'page_size': '10',
    }

    response = requests.get('https://proxy.webshare.io/api/v2/proxy/list/', params=params, cookies=cookies, headers=headers, proxies=proxies)
    #print(response.text)
   
    try:
        print("[+] Fetched 10 1gb proxies")
        for proxy in response.json()['results']:
            username = proxy['username']
            password = proxy['password']
            ip = proxy['proxy_address']
            port = proxy['port']
            format = f"{username}:{password}@{ip}:{port}"
            open("Results/proxys.txt", 'a').write(format + "\n")

    except:
        print("[-] Failed to get 10 1gb proxies")    
        pass

def GenThread():

    settings = {
        'max_workers': 30
    }

    amount = int(input(f"[/] Amount > "))
    print()
    with concurrent.futures.ThreadPoolExecutor(max_workers=settings['max_workers']) as executor:
        for i in range(int(amount)):
            executor.submit(CreateAccount)
    
    print(f"\n[+] Finished all processes")
GenThread()