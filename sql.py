import sqlite3
digits=[]
new_dict={}
def init():
    for i in range(26):
         new_dict[i]=chr(ord('a')+i)
    for i in range(26):
         new_dict[26+i]=chr(ord('A')+i)
    for i  in range(10):
        new_dict[52+i]=chr(ord('0')+i)        
def base64(a):
    while a>0 :
        digits.append(a%62)
        a=a/62
    digits.reverse()
conn = sqlite3.connect("test.db")
print "opened"
init()
#conn.execute('''Create table url1(url_name varchar(20) not null );''')
url=raw_input("enter the url which you want to shorten");
cur=conn.execute("select rowid,url_name from url1 where url_name=?",(url,))
fg=0
for i in cur:
    fg=1
    val = i[0]
    break
if(fg == 1 ):
    #print val
    base64(val)
else:
    conn.execute("insert into url1 values(?)",(url,))
    conn.commit()
    cur=conn.execute("select rowid,url_name from url1 where url_name=?",(url,))
    for c in cur:
        val=c[0]
    #print val
    base64(val)
s="http://www.short.ty/"
#print new_dict[0]
for m in digits:
    s=s + new_dict[m]
print s;
conn.close()
