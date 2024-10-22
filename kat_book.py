#!\python311\python.exe
print ("Content-type: text/html")
print ("")

# Από δω ξεκινάει ..
import cgi
form=cgi.FieldStorage()
kodikos = form["kod_bibliou"].value
titlos =form["titlos"].value
syg =form["sygrafeas"].value
# strarts the main program
print "<h1>   emfanisi stoixeia bibliou  </h1>"
print "kodikos bibliou   " 
print kodikos
print "<h2>"
print "Titlos bibliou "
print titlos 
print "</h2>"
print "Sygrafeas bibliou"
print syg
print "<br>"