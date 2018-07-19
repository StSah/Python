from flask import Flask,request,jsonify
from signUp import insert_user_details,user_authentication,forget_password,update_password,updateData

app=Flask(__name__)

@app.route('/')
def checkserver():
	return 'Bingo!'

@app.route('/signup',methods=['POST'])
def sign_up():
    data=request.get_json()
    print('Data',data)
    op_Data,status=insert_user_details(data)
    return jsonify({'Data':op_Data,'Status':status})

@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    op_data,status=user_authentication(data)
    if status==True:
        return jsonify({'Data':op_data,'Status':status})
    if op_data ==0:
        return jsonify({'Data':op_data,'Status':status})    

@app.route('/forgetpwd',methods=['POST'])
def forget_pwd():
    data=request.get_json()
    op_data,status=forget_password(data)
    return jsonify({'Data':op_data,'Status':status})
    
@app.route('/updatepassword',methods=['GET'])    
def update_pwd():
    uname=request.args.get('username')
    password=request.args.get('pwd')
    data=update_password(uname,password)
    return data

@app.route('/updateprofile',methods=['POST'])
def update_profile():
    data=request.get_json()
    op_Data,status=updateData(data)
    return jsonify({'Data':op_Data,'Status':status})


if __name__=="__main__":
    app.run(debug=True,port=4999)

