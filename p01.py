#!\python311\python.exe
print ("Content-type: text/html")
print ("")

# Από δω ξεκινάει ..
# ypologismos mistodosias ypallilou.
wres=30
wm =3.5
akApod=wres *wm
foros = akApod * 0.17
kApod= akApod-foros
print ("<title>  ypologismos  mistodosias  </title>")
print ("Ωρες Εργασίας ",wres)
print ("<br>")
print ("Ωρομίσθιο  ",wm)
print ("<br>")
print (" Ακαθάριστες Αποδοχές   ",akApod ,"<br>")
print ("</b>")
print ("<u> Φόρος   ",foros ," </u> <br> ")
print (" <h1>  Καθαρές Αποδοχές ", kApod , "<h1>")
