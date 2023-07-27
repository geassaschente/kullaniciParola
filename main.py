

#if a and b  true false
#if a or b
# kullanıcı parola girme

defkullanici = "yazilimcibebe"
defparola = "1234"

kullanici = input("Kullanıcı Adı:")
parola = input("Parolanız:")

if ((defkullanici == kullanici) and (parola == defparola)):
    print("yazılım bilimi sitesine hoş geldiniz")
elif ((defkullanici != kullanici) and (parola == defparola)):
    print("kullanıcı adını yanlış girdiniz")
elif ((defkullanici == kullanici) and (parola != defparola)):
    print("parolayı yanlış girdiniz")
else :
    print("tekrar deneyiniz")