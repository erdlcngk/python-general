from selenium import webdriver
import time


class Instagram:
    __instance = None
    __driver=None
    __username=None
    __password=None
    followingNameList=None

    def __init__(self):

        if(Instagram.__instance!=None):
           print("Singleton bir objedir.")
        else:
            self.__driver=webdriver.Chrome()
            Instagram.__instance = self

    @staticmethod
    def getInstance():
        if (Instagram.__instance == None):
            return Instagram()
        return Instagram.__instance

    def goToWebsite(self):
        self.__driver.get("https://www.instagram.com/")

    def giveUsernameAndPassword(self,username,password):
        self.__username = username
        self.__password = password

    def login(self):
        #kullanıcı adı ve şifresi verilen bir hesaba giriş yapar.

                try:
                    self.__driver.maximize_window()
                    time.sleep(3)
                    self.__driver.find_element_by_name("username").send_keys(self.__username)
                    self.__driver.find_element_by_name("password").send_keys(self.__password)
                    self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
                    time.sleep(5)
                    self.__driver.find_element_by_class_name("sqdOP.yWX7d.y3zKF").click()
                    time.sleep(3)
                    self.__driver.find_element_by_class_name("aOOlW.HoLwm").click()

                except:
                    print("Eşleşmeyen kullanıcı adı ve şifre girmiş olabilirsiniz veya internete bağlı olmayabilirsiniz.\nBilgilerinizi yeniden gözden geçiriniz.")

        #login tamamlandı

    def logout(self):
        #giriş yapılmış hesaptan çıkış yapar.
        if(Instagram.__instance!=None):
            while(True):
                try:
                    time.sleep(3)
                    self.__driver.get("https://www.instagram.com/")
                    time.sleep(2)
                    self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span').click()
                    time.sleep(2)
                    self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div').click()
                    time.sleep(3)
                    self.__driver.close()
                    break
                except:
                    print("Bir hata ile karşılaşıldı.\nGiriş yapmamış olabilirsiniz.")
                    continue
        else:
            print("Lütfen giriş yapınız!")
        #logout tamamlandı.

    def sendMessage(self,user,content):
        #önce kullanıcı seçiliyor sonra mesaj içeriği
        while(True):
            try:
                time.sleep(2)
                self.__driver.get("https://www.instagram.com/"+user)
                time.sleep(2)
                self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
                time.sleep(2)
                self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(content)
                time.sleep(1)
                self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                break
            except:
                print("Bir hata oluştu")
                continue
    #sendMessage tamamlandı.

    def following(self):
        self.__driver.get("https://www.instagram.com/" + self.__username)
        time.sleep(3)
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(2)
        while(True):
            time.sleep(2)
            holder = self.__driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')
            self.__driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', holder)
            time.sleep(0.5)
            try:
                checker=self.__driver.find_element_by_class_name("By4nA")
                print("Scrolled")
            except:
                print("Liste Sonuna Kadar Yüklendi.")
                break

        time.sleep(1)
        followingClass=self.__driver.find_element_by_class_name("PZuss")
        time.sleep(1)
        followingList = followingClass.find_elements_by_class_name("Jv7Aj.mArmR.MqpiF")
        file = open("TakipEdilenListesi.txt","w")

        for user in followingList:
            file.write(user.text+"\n")
        file.close()

        for followingUser in followingList:
            self.__followingNameList=followingUser.text
            print(self.__followingNameList)
    def whoNotFollowingMe(self):
        file = open("TakipEdilenListesi.txt", "r")
        usernameList = list(map(str.strip, file.readlines()))
        file.close()
        file = open("KendiniTakipEtmeyenler.txt", "a")
        file.write(f"'{self.__username}' adli hesabin takip ettikleri ama kendisini takip etmeyenler:\n ")
        saver = []
        for gotoUser in usernameList:  # takip edilen listesindeki kişileri tek tek gezme
            self.__driver.get("https://www.instagram.com/" + gotoUser)  # Kişilerei gitme
            time.sleep(1.5)
            if (int(self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title").replace(".","")) <= 10000):  # Gidilen kişinin takip ettiği kişinin kaçtan büyük olması gerektiği kontrol
                self.__driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()  # Gidilen kişinin takip ettikleri butonu
                time.sleep(3)
                if (self.__driver.find_element_by_class_name("Jv7Aj.mArmR.MqpiF").text == self.__username):
                    pass
                else:

                    self.__driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()  # Gidilen kişinin takip ettikleri sayfasını kapatma butonu
                    time.sleep(0.5)
                    saver.append(gotoUser)
            else:
                pass
        for save in saver:
            file.write(save + "\n")
        file.write("\n")
        file.close()
    def unfollowWhoNotFollowingMe(self):
        file = open("TakipEdilenListesi.txt","r")
        usernameList = list(map(str.strip, file.readlines()))
        file.close()
        file = open("TakiptenCikilanlar.txt", "a")
        file.write(f"'{self.__username}' adli hesaptan takipten cikilanlar:\n ")
        saver=[]
        for gotoUser in usernameList: #takip edilen listesindeki kişileri tek tek gezme
            try:
                self.__driver.get("https://www.instagram.com/"+gotoUser) #Kişilerei gitme
                time.sleep(1.5)
                if (int(self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text.replace(".","")) <= 10000): #Gidilen kişinin takip ettiği kişinin kaçtan büyük olması gerektiği kontrol
                    self.__driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click() #Gidilen kişinin takip ettikleri butonu
                    time.sleep(3)
                    if (self.__driver.find_element_by_class_name("Jv7Aj.mArmR.MqpiF").text == self.__username):
                        pass
                    else:

                        self.__driver.find_element_by_xpath(
                            '/html/body/div[6]/div/div/div[1]/div/div[2]/button').click() #Gidilen kişinin takip ettikleri sayfasını kapatma butonu
                        time.sleep(0.5)
                        saver.append(gotoUser)

                        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click() #gidilen sayfadaki insan simgesi butonu
                        time.sleep(0.5)
                        self.__driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click() #takipten çık butonu
                else:
                    pass
            except:
                pass
                try:
                    # self.__driver.find_element_by_xpath(
                    #     '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
                    # self.__driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                    print(f"{gotoUser} bir sayfa hesabıdır.")
                except:
                    pass
        for save in saver:
            file.write(save+"\n")
        file.write("\n")
        file.close()








        #instagramdaki bütün takip ettikleri alınacak ve bir listeye atanacak. Atanan listedeki bütün kişilerin profiline gidilecek ve
        #takip ettikleri listesinin ilk elemanın hrefi(linki) giriş yapan user'in username'i ile eşleşiyor mu kontrol edilecek.
