import hashlib,uuid
import sqlite3
#from mail import sendmail
def insert_user_details(data):
    con=sqlite3.connect('data.db')
    
    try:
        cur=con.cursor()
        salt=uuid.uuid4().hex
        hash = hashlib.sha512()
        hash.update(('%s%s' % (salt, data['password'])).encode('utf-8'))
        hashed_password = hash.hexdigest()        
        cur.execute("INSERT INTO userdetail(name,username,emailid,mbnos,salt,hashed_password)VALUES(?,?,?,?,?,?)",
        (data['name'],data['username'],data['emailid'],data['mbnos'],salt,hashed_password))
        con.commit()
        con.close()
        return data,True
    except Exception as e:
        print(e)
        con.close()
        return 0,False

def user_authentication(loginData):
    con=sqlite3.connect('data.db')

    try:
        cur=con.cursor()
        cur.execute("SELECT * from userdetail WHERE username=? or mbnos=? or emailid=?",(loginData['username'],loginData['mbnos'],loginData['emailid']))
        rows=cur.fetchall()
        row=rows[0]

        user_detail={
            'id':row[0],
            'name':row[1],
            'username':row[2],
            'emailid':row[3],
            'mbnos':row[4],
           
        }
        salt=row[5]
        hash=hashlib.sha512()
        hash.update(('%s%s' % (salt, loginData['password'])).encode('utf-8'))
        hashed_password=hash.hexdigest()

        if hashed_password==row[-1]:
            con.commit()
            con.close()
            return user_detail,True
        else:
            con.commit()
            con.close()
            return 0,False
    except Exception as e:
        print(e)
        con.commit()
        con.close
        return 0,True    

def forget_password(data):
    con=sqlite3.connect('data.db')

    try:
        cur=con.cursor()
        cur.execute("SELECT * from userdetail WHERE username=? or emailid=? or mbnos=?",(data['username'],data['emailid'],data['mbnos']))
        rows=cur.fetchall()
        row=rows[0]
        salt=row[5]
        hash=hashlib.sha512()
        hash.update(('%s%s' % (salt, data['updatepwd'])).encode('utf-8'))
        hashed_password=hash.hexdigest()
        if len(row)>0:
            
            #sendmail(row,hashed_password)
            con.commit()
            con.close()
            return hashed_password,True
        else:
            con.commit()
            con.close()
            return {'message':'Sorry, we cant recognize you.'},False
    except Exception as e:
        con.commit()
        con.close()
        print(e)
        return 0, False        


def update_password(username,password):
    con = sqlite3.connect('data.db')
    try:
        cur=con.cursor()
        cur.execute('UPDATE userdetail SET hashed_password = ? WHERE  username =?',(password,username))
        con.commit()
        con.close()
        return 'Your password has been changed successfully',True
    except Exception as e:
        print(e)
        con.commit()
        con.close()
        return 'Some exception occured' ,False

def updateData(data):
        con =sqlite3.connect('data.db')
        try:
            cur=con.cursor()
            cur.execute('UPDATE userdetail SET name=?,username=?,emailid=?,mbnos=? WHERE username=?',(data['name'],data['newusername'],data['emailid'],data['mbnos'],data['username']))
            con.commit()
            con.close()
            return 'Data Updated',True
        except Exception as e:
            con.commit()
            con.close()
            print(e)
            return 0, False