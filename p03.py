#!\python311\python.exe
print ("Content-type: text/html")
print ("")

# Από δω ξεκινάει ..
aposo=  10000
ept= 5
tel=aposo
stoxo= aposo * 2
print (" Αρχικό Κεφάλαιο   ", aposo , "<br>")
print (" Επιτοκιο    ", ept ) 
print ("<br>")
print ('<table border="2" style="border-collapse:collapse;">')

while tel <stoxo:
        print ("<tr>")
        print ("<td>")
        print (int(tel)) 
        print ("</td>")
        tokos = tel *ept/100.0
        tel = tel+tokos
        print ("<td>")
        print (int(tokos))
        print ("</td>")
        print ("<td>")
        print (int(tel))
        print ("</td>")
print ('</table>')