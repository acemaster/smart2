# import MySQLdb

# txt=open('file.txt')
# ufid=txt.read()
# # ufid=" 6c 96 ac 12"
# # ufid=ufid.strip()
# print ufid
# connection=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="studentinfo")
# cursor=connection.cursor()
# sql1="SELECT roll_number FROM map WHERE ufid="+"'"+str(ufid)+"'"
# # print sql1
# cursor.execute("""SELECT roll_number FROM map WHERE ufid=%s""",(str(ufid)))
# row=cursor.fetchone()
# print row[0]
# roll_number=row[0]
# sql2="SELECT COUNT(*) FROM mess WHERE roll_number="+str(row[0])
# cursor.execute(sql2)
# row=cursor.fetchone()
# print row[0]

# if str(row[0])=='0':
#     cursor.execute("""INSERT INTO mess VALUES (%s,%s)""",(str(roll_number),0))
#     connection.commit()

# else:
#     sql4="SELECT attendance FROM mess WHERE roll_number="+str(roll_number)
#     cursor.execute(sql4)
#     row=cursor.fetchone()
#     attendance=row[0]+1
#     print type(attendance)
#     print attendance
#     sql3="UPDATE mess SET attendance=%s WHERE roll_number=%s",(attendance,str(roll_number),)
#     cursor.execute("""UPDATE mess SET attendance=%s WHERE roll_number=%s""",(attendance,str(roll_number),))
#     connection.commit()
    
#     import webbrowser
#     textt="http://localhost:8000/manager/"+str(roll_number)
#     print textt
#     # webbrowser.open("http://localhost:8000/manager/"+str(roll_number + "/"))
#     webbrowser.open(textt)
# cursor.close()
# connection.close()

# import MySQLdb

# txt=open('file.txt')
# ufid=txt.read()


# connection=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="studentinfo")
# cursor=connection.cursor()
# sql1="SELECT roll_number FROM map WHERE ufid="+"'"+str(ufid)+"'"
# cursor.execute(sql1)
# row=cursor.fetchone()
# print row[0]
# roll_number=row[0]
# sql2="SELECT COUNT(*) FROM mess WHERE roll_number="+str(row[0])
# cursor.execute(sql2)
# row=cursor.fetchone()
# print row[0]

# if str(row[0])=='0':
#     print "Executed: "
#     cursor.execute("SELECT HOUR(SYSDATE()),SYSDATE() FROM dual")
#     row=cursor.fetchone()
#     hour=row[0]
#     date=row[1]
#     streak=0
#     print hour
#     bf=0
#     lch=0
#     dn=0
#     if hour>4 and hour<12:
#         bf=1
#     elif hour<16:
#         lch=1
#     else:
#         dn=1
#     cursor.execute("""INSERT INTO mess VALUES (%s,%s,%s,%s,%s,%s,%s)""",(str(roll_number),bf,lch,dn,1,date,streak))
#     connection.commit()

# else:
#     sql4="SELECT attendance FROM mess WHERE roll_number="+str(roll_number)
#     cursor.execute(sql4)
#     row=cursor.fetchone()
#     attendance=row[0]+1
#     cursor.execute("SELECT HOUR(SYSDATE()),SYSDATE() FROM dual")
#     row=cursor.fetchone()
#     hour=row[0]
#     date=row[1]
#     cursor.execute("SELECT bf,lh,dnr,DATEDIFF(SYSDATE(),date),streak FROM mess WHERE roll_number="+roll_number)
#     row=cursor.fetchone()
#     counter=row[3]
#     streak=row[4]
#     if counter==1:
#         streak=streak+1
#     else:
#         streak=0
#     print hour
#     bf=row[0]
#     lch=row[1]
#     dn=row[2]
#     if hour>6 and hour<12:
#         bf=bf+1
#     elif hour<16:
#         lch=lch+1
#     else:
#         dn=dn+1
#     print type(attendance)
#     print attendance
#     #sql3="UPDATE mess SET attendance=%s,bf=%s,lch=%s,dn=%s,date=%s,streak=%s WHERE roll_number=%s",(attendance,bf,,)
#     cursor.execute("""UPDATE mess SET attendance=%s,bf=%s,lh=%s,dnr=%s,date=%s,streak=%s WHERE roll_number=%s""",(attendance,bf,lch,dn,date,streak,str(roll_number),))
#     connection.commit()
#     import webbrowser
#     textt="http://localhost:8000/manager/"+str(roll_number)
#     print textt
#     # webbrowser.open("http://localhost:8000/manager/"+str(roll_number + "/"))
#     webbrowser.open(textt)
# cursor.close()
# connection.close()


import MySQLdb

txt=open('file.txt')
ufid=txt.read()


connection=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="studentinfo")
cursor=connection.cursor()
sql1="SELECT roll_number FROM map WHERE ufid="+"'"+str(ufid)+"'"
cursor.execute(sql1)
row=cursor.fetchone()
print row[0]
roll_number=row[0]
sql2="SELECT COUNT(*) FROM mess WHERE roll_number="+str(row[0])
cursor.execute(sql2)
row=cursor.fetchone()
print row[0]

if str(row[0])=='0':
    print "Executed: "
    cursor.execute("SELECT HOUR(SYSDATE()),SYSDATE() FROM dual")
    row=cursor.fetchone()
    hour=row[0]
    date=row[1]
    streak=0
    print hour
    bf=0
    lch=0
    dn=0
    guest=0
    if hour>4 and hour<12:
        bf=1
    elif hour<16:
        lch=1
    else:
        dn=1
    print "Executed"
   # sql5="insert into mess values('"+str(roll_number)+"', "+bf+", "+lch+", "+dn+", "+1+", "+date+", "+streak+", "+hour+", "+guest+");"
    #print sql5
    cursor.execute("""INSERT INTO mess VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(str(roll_number),bf,lch,dn,1,date,streak,hour,guest))
    connection.commit()

else:
    sql4="SELECT attendance FROM mess WHERE roll_number="+str(roll_number)
    print "Else"
    cursor.execute(sql4)
    row=cursor.fetchone()
    attendance=row[0]
    cursor.execute("SELECT HOUR(SYSDATE()),SYSDATE() FROM dual")
    row=cursor.fetchone()
    hour=row[0]
    date=row[1]
    cursor.execute("SELECT bf,lh,dnr,DATEDIFF(SYSDATE(),date),streak,hours,guest FROM mess WHERE roll_number="+str(roll_number))
    row=cursor.fetchone()
    counter=row[3]
    streak=row[4]
    hour2=row[5]
    guest=row[6]
    if counter==1:
        streak=streak+1
    else:
        streak=0
    print hour
    bf=row[0]
    lch=row[1]
    dn=row[2]
    if hour>6 and hour<12:
        bf=bf+1
    elif hour<16:
        lch=lch+1
    else:
        dn=dn+1
   
    if hour-hour2<2:
        guest=guest+1
    else:
        attendance=attendance+1


    print type(attendance)
    print attendance
    #sql3="UPDATE mess SET attendance=%s,bf=%s,lch=%s,dn=%s,date=%s,streak=%s WHERE roll_number=%s",(attendance,bf,,)
    cursor.execute("""UPDATE mess SET attendance=%s,bf=%s,lh=%s,dnr=%s,date=%s,streak=%s,hours=%s,guest=%s WHERE roll_number=%s""",(attendance,bf,lch,dn,date,streak,hour2,guest,str(roll_number),))
    connection.commit()
    import webbrowser
    # textt="http://localhost:8000/manager/"+str(roll_number)
    # print textt
    # webbrowser.open("http://localhost:8000/manager/"+str(roll_number + "/"))
    # webbrowser.open(textt)
cursor.close()
connection.close()