from Instagram import Instagram
def logout():
    while True:
        controller = int(input("Cikis yapmak istiyorsanız '1', baska bir islem yapmak istiyorsanız '2' giriniz.\n"
                           "Girdi: "))
        if(controller == 1):
            site.logout()
            exit()
        elif(controller == 2):
            pass
            break
        else:
            print("Hatali bir girdide bulundunuz!")
            continue

# chromeDriverLocation = input("Lütfen chromedriver.exe'nin bulunduğu konumu giriniz: ")
username= input("Lütfen kullanıcı adınızı giriniz: ")
password = input("Lütfen şifrenizi giriniz: ")
site = Instagram.getInstance()
site.goToWebsite()
site.giveUsernameAndPassword(username,password)
site.login()
while True:
    selector=int(input("1-) Takip Ettiklerin\n2-) Takip Ettiğin Halde Seni Takip Etmeyenler\n3-) Takip Ettiğin Halde Seni Takip Etmeyenleri Takipten Cik\n4-)Mesaj Gonder\nNOT:EGER UYGULAMANIN DUZGUN CALISMASINI ISTIYORSANIZ 1. KOMUTU CALISTIRMANIZ TAVSIYE EDILIR!\nGirdi: "))
    if(selector == 1):
        site.following()
        control = logout()
        if (control == 1):
            break
    elif(selector == 2):
        site.whoNotFollowingMe()
        control = logout()
        if (control == 1):
            break
    elif(selector == 3):
        site.unfollowWhoNotFollowingMe()
        control = logout()
        if (control == 1):
            break
    elif(selector == 4):
        user = input("Kisi Adini Giriniz: ")
        message = input("Mesaji Giriniz: ")
        site.sendMessage(user,message)
        control=logout()
        if(control == 1):
            break

    else:
        print("Hatali Bir Giriş Yaptınız")
        continue


# site.sendMessage("emrhnggk","Sen şaşırdııı???")
# site.logout()