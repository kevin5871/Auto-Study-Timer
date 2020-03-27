## 인터넷 강의 듣기 툴

## 자동화 학습 타이머 

## GUI는 나중에 개발 예정.

## ver 1.0 / made by sfcatz

from selenium import webdriver
import platform
import shutil
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException, NoSuchWindowException
import time

print("자동화 학습 타이머 v 1.0\n\n")
print("브라우저 선택\n")
print("1. 파이어폭스 (권장)\n")
print("2. 크롬\n")
print("3. 인터넷 익스플로러\n")
print("※ 주의 : 브라우저가 미리 깔려있어야합니다!\n")
print("※ 인터넷 익스플로러는 권장하지 않음 / 두 브라우저가 없을 때 사용하세요.\n")
print("※ 인터넷 익스플로러는 '''레지스트리'''를 건드립니다.\n\n3번을 입력하여 인터넷 익스플로러를 실행하면 레지스트리를 통한 시스템 변조에 동의한 것으로 간주합니다.\n")
choice = int(input())
print("OS 확인 중...")
print(platform.architecture()[0])
if(platform.architecture()[0] == '32bit') :
    if(choice == 2) :
        print("크롬 브라우저는 버전이 맞지 않을 시 작동이 되지 않습니다. 크롬의 버전을 확인한 후 깔아주세요.")
        print("현재 이 프로젝트에서 사용가능한 크롬 브라우저 버전은 ''80'' 입니다.")
        shutil.copy2('Drivers/Chrome/chromedriver.exe', 'chromedriver.exe')
        driver = webdriver.Chrome()
    elif(choice == 1) :
        print("파이어폭스 브라우저의 버전이 60 미만일 시 사용이 불가능합니다. 파이어폭스의 버전을 확인해주세요.")
        shutil.copy2('Drivers/Firefox/geckodriver(32).exe', 'geckodriver.exe')
        driver = webdriver.Firefox()
    elif(choice == 3) :
        print("인터넷 익스플로러는 권장하지 않습니다. 가급적 다른 브라우저를 다운받아 이용해주세요.")
        print("사용 가능한 버전 : ''11''")
        shutil.copy2('Drivers/IE/IEDriverServer(32).exe', 'IEDriverServer.exe')
        cap = DesiredCapabilities().INTERNETEXPLORER
        cap['ignoreZoomSetting'] = True
        driver = webdriver.Ie(capabilities=cap, executable_path=r'IEDriverServer.exe')
    else :
        print("ERROR")
        quit()
elif(platform.architecture()[0] == '64bit') :
    if(choice == 2) :
        print("크롬 브라우저는 버전이 맞지 않을 시 작동이 되지 않습니다. 크롬의 버전을 확인한 후 깔아주세요.")
        print("현재 이 프로젝트에서 사용가능한 크롬 브라우저 버전은 ''80'' 입니다.")
        shutil.copy2('Drivers/Chrome/chromedriver.exe', 'chromedriver.exe')
        driver = webdriver.Chrome()
    elif(choice == 1) :
        print("파이어폭스 브라우저의 버전이 60 미만일 시 사용이 불가능합니다. 파이어폭스의 버전을 확인해주세요.")
        shutil.copy2('Drivers/Firefox/geckodriver(64).exe', 'geckodriver.exe')
        driver = webdriver.Firefox()
    elif(choice == 3) :
        print("인터넷 익스플로러는 권장하지 않습니다. 가급적 다른 브라우저를 다운받아 이용해주세요.")
        print("사용 가능한 버전 : ''11''")
        shutil.copy2('Drivers/IE/IEDriverServer(64).exe', 'IEDriverServer.exe')
        cap = DesiredCapabilities().INTERNETEXPLORER
        cap['ignoreZoomSetting'] = True
        driver = webdriver.Ie(capabilities=cap, executable_path=r'IEDriverServer.exe')
    else :
        print("ERROR")
        quit()

driver.get('https://www.ebsi.co.kr/index.jsp')
accept = 0
while True :
    try:
        if(driver.current_url.find('https://www.ebsi.co.kr') == -1 and driver.current_url.find('http://www.ebsi.co.kr')) :
            print("WARNING : EBSi 홈페이지에서 벗어났습니다. EBSi 홈페이지로 리다이렉트됩니다.")
            driver.get('https://www.ebsi.co.kr/index.jsp')
        window_before = driver.window_handles[accept]
        window_after = driver.window_handles[accept+1]
        driver.switch_to.window(window_after)
        if(driver.current_url.find('https://www.ebsi.co.kr') == -1 and driver.current_url.find('http://www.ebsi.co.kr')) :
            log = driver.current_url
            driver.close()
            driver.switch_to.window(window_before)
            print("WARNING : 새로운 탭(EBSi 관련 제외)을(를) 생성하였습니다. 해당 탭을 닫습니다.")
            print("해당 탭의 URL : " + log)
        else :
            print("INFO : 허용 탭이 열렸습니다. 현재 활성화 탭 : " + str(accept+1))
            accept += 1
    except IndexError :
        continue
    except NoSuchWindowException :
        print("INFO : 활성 탭이 닫혔습니다. 현재 활성화 탭 : " + str(accept - 1))
        accept -= 1
        if(accept == -1) :
            print("WARNING : 모든 탭이 닫혔습니다. 프로그램이 종료됩니다.")
            time.sleep(1)
            quit()
        window_before = driver.window_handles[accept]
        driver.switch_to.window(window_before)
        continue


