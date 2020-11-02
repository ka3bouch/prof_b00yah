#
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random,datetime,string , os ,time ,subprocess , sys

#os.environ['DISPLAY'] = ':0'

#new_cmd="hammaelmadani"
new_cmd=sys.argv[1]
new_cmd2="agoon007"




def get_firefox_profile_temp():
    if sys.platform in ['linux', 'linux2']:
        import subprocess
        cmd2 = "ls -d /tmp/rust_mozprofile.*/"
        p = subprocess.Popen([cmd2], shell=True, stdout=subprocess.PIPE)
        FF_PRF_DIR2 = p.communicate()[0][0:-2]
        FF_PRF_DIR_DEFAULT_DEFAULT2 = str(FF_PRF_DIR2,'utf-8')
    elif sys.platform == 'win32':
        import os
        import glob
        APPDATA = os.getenv('APPDATA')
        FF_PRF_DIR = "%s\\Mozilla\\Firefox\\Profiles\\" % APPDATA
        PATTERN = FF_PRF_DIR + "*default*"
        FF_PRF_DIR_DEFAULT = glob.glob(PATTERN)[0]
 
    return FF_PRF_DIR_DEFAULT_DEFAULT2

def get_firefox_profile_dir():
    if sys.platform in ['linux', 'linux2']:
        import subprocess
        cmd = "ls -d /root/.mozilla/firefox/*.default/"
        p = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE)
        FF_PRF_DIR = p.communicate()[0][0:-2]
        FF_PRF_DIR_DEFAULT = str(FF_PRF_DIR,'utf-8')
    elif sys.platform == 'win32':
        import os
        import glob
        APPDATA = os.getenv('APPDATA')
        FF_PRF_DIR = "%s\\Mozilla\\Firefox\\Profiles\\" % APPDATA
        PATTERN = FF_PRF_DIR + "*default*"
        FF_PRF_DIR_DEFAULT = glob.glob(PATTERN)[0]
 
    return FF_PRF_DIR_DEFAULT

profile_name=get_firefox_profile_dir()
print(profile_name)

firefox_options = Firefox_Options()
firefox_options.binary = "/root/firefox/firefox";

url_booyah='https://booyah.live/channels/20128881'
firefox_options.add_argument("--headless")
url_google="https://accounts.google.com/login"

def build_driver():

	driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver13', firefox_profile=profile_name ,options=firefox_options)
	driver.maximize_window()
	return driver



def starter():
	try:
		#l0g(" [ ok ] ")
		display = Display(visible=1, size=(1024, 1024))
		display.start()
		init_fire()
		driver=build_driver()
		#driver.get(url_google)
		#google_login(driver)
		#about:preferences
		driver.get(url_booyah)
		#driver.maximize_window()
		check_web(driver)
		time.sleep(5)
		dish(driver)
		time.sleep(2)
		display.stop()
	except:
		print("something wrong")
		driver.quit()
		starter()


def check_web(driver):
	try:
		print("web page CHECK .....")
		eto_firstName=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-login.components-button.components-button-size-small.components-button-type-outlined-light.desktop.components-button-inline')))
#		eto_firstName.send_keys(Keys.F11)
		eto_firstName.click()
		google_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-login.btn-login-google')))
		google_button.click()
		print("web page working sleep 10")
		time.sleep(10)
		#check_web(driver)
		window_before = driver.window_handles[0]
		window_after = driver.window_handles[1]
		#print (window_before)
		#print (window_after)
		time.sleep(3)
		driver.switch_to_window(window_after)
		google_identifier=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,'identifierId')))
		print("o     o    o    o   o   o  k")
		google_identifier.click()
		google_identifier.send_keys(new_cmd,Keys.RETURN)
		print("send email")
		time.sleep(7)
		google_shit=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,'password')))
		google_shit.click()
		time.sleep(2)
		google_shit.send_keys(new_cmd2,Keys.RETURN)
		print("send pass")
		time.sleep(7)
		print("check if loggin page")
		driver.switch_to_window(window_before)
		time.sleep(2)
		#components-avatar-image
		b00ya_avatar=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.components-avatar-image')))
		print("login is ok")
	except:
		print("something wrong")
		driver.quit()
		starter()



def init_fire():
	print("init_fire")
	try:
		os.system("pkill firefox")
		os.system("rm -rf /tmp/*")
	except:
		print("some_error")




def finish_stuff(driver):
	print("finish_stuff")
	tmp_prof=get_firefox_profile_temp()
	profile_name=get_firefox_profile_dir()
	print(tmp_prof+" "+profile_name)
	rm_old_prof="rm -rf "+profile_name+"/*"
	print(get_firefox_profile_temp())
	copy_new_pro="cp -r "+tmp_prof+"/* "+profile_name+"/"
	os.system(rm_old_prof)
	print("remove old profile")
	os.system(copy_new_pro)
	print("copy new profile")
	time.sleep(5)
	#input()
	#driver.quit()

def dish(driver):

	#driver.get("about:preferences")
	input()
	print("finish_stuff")
	oo=driver.get_cookies()
	print("driver coockies :"+str(oo))
	tmp_prof=get_firefox_profile_temp()
	profile_name=get_firefox_profile_dir()
	print(tmp_prof+" "+profile_name)
	rm_old_prof="rm -rf "+profile_name+"/*"
	print(get_firefox_profile_temp())
	copy_new_pro="cp -r "+tmp_prof+"/* "+profile_name+"/"
	
	print("remove old profile")
	time.sleep(2)
	os.system(rm_old_prof)

	print("copy new profile")
	time.sleep(7)

	os.system(copy_new_pro)

	time.sleep(7)
	rm_new_pro="rm "+profile_name+"/*.corrupt"
	os.system(rm_new_pro)
	time.sleep(5)
	driver.quit()
	print("compress new profile")


init_fire()
starter()


#https://github.com/ka3bouch/prof_b00yah/raw/master/muz_prof/default.tar.bz2
