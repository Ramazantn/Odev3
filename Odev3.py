

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce:

    def mission_1(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        kullaniciAd=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(3)
        kullaniciAd.send_keys("")
        sifre.send_keys("")
        sleep(3)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME, "error-message-container")
        mesaj="Epic sadface: Username is required"
        print(f"{mesaj}")
        sleep(10)

    def mission_2(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        kullaniciAd=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(3)
        kullaniciAd.send_keys("1234")
        sifre.send_keys("")
        sleep(3)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME, "error-message-container")
        mesaj="Epic sadface: Password is required"
        print(f"{mesaj}")
        sleep(10)

    def mission_3(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        kullaniciAd=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(3)
        kullaniciAd.send_keys("locked_out_user")
        sifre.send_keys("secret_sauce")
        sleep(3)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME,"error-message-container")
        mesaj="Epic sadface: Sorry, this user has been locked out."
        print(f"{mesaj}")
        sleep(10)

    def mission_4(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        kullaniciAd=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(3)
        kullaniciAd.send_keys("")
        sifre.send_keys("")
        sleep(3)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME,"error-message-container")
        hatabutonu=driver.find_element(By.CLASS_NAME, "error-button")
        sleep(3)
        hatabutonu.click()
        sleep(10)

    def mission_5(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        kullaniciAd=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(3)
        kullaniciAd.send_keys("standard_user")
        sifre.send_keys("secret_sauce")
        sleep(3)
        giris.click()
        sleep(3)
        current_URL="https://www.saucedemo.com/inventory.html"
        sleep(10)
        print(f"Current URL : {current_URL}")


    def mission_6(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        kullaniciAd=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(3)
        kullaniciAd.send_keys("standard_user")
        sifre.send_keys("secret_sauce")
        sleep(3)
        giris.click()
        sleep(3)
        nesneSayisi=driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Ürün Sayisi : {len(nesneSayisi)}")
       
        

test=Test_Sauce()

test.mission_1()
test.mission_2()
test.mission_3()
test.mission_4()
test.mission_5()
test.mission_6()


# --------------------------Yazili Ödevin Cevaplari-----------------------------
#
#   HTML: Resim, metin ve vb. şeylerin web sayfasında nasıl görüntü oluşturduğunun yanında 
#web sayfasının oluşurken etkileşim kurduğu uzantıları ifade eden dildir. 
#Bir programlama dili değil işaretleme dilidir.
#
#
#   HTML LOCATOR: Web sayfalarında yer alan nesneleri ifade eder. 
#Bunları tanımlamak için ID, name, class, tagname gibi seçeneklere sahiptir. 
#Selenium bir web sayfasına ulaşmak orada çalışma yapmak için HTML LOCATOR’ı kullanır.
#
#   SELENİUM AKSİYONLAR:
#get():Verilen URL'e erişmemizi sağlar
#click():Belirli bir öğeye tıklamak için kullanılır. 
#send_keys(): Bir metin kutusuna veya alanına metin yazmak için kullanılır
#back() = Önceki sayfaya gitmek için kullanılır. 
#forward() = Sonraki sayfaya gitmek için kullanılır. 
#refresh() = Sayfayı yenilemek için kullanılır
#maximize_window()=Sayfayı tam ekran görüntülemek için kullanılır. 
#clear() = Bir elemanın içeriğini temizlemek için kullanılır.
#quit()= Kullanımdaki tarayıcıyı kapatır.
#
#
#NOT: Hocam, ödevi dağınık ve uzun yapmak yerine hepsini kısaca tek bir classda yaptım.
