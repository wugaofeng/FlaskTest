# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request,render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm   #导入继承父类
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired
import systemutils

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[Length(min=6,max=12,message='用户名长度为6~12位'),DataRequired(message='用户名不能为空')])
    userpass = PasswordField('密码',validators=[Length(min=6,max=12,message='密码长度为6~12位'),DataRequired(message='密码不能为空')])
    submit = SubmitField('登录')

@app.route('/')
def index():
    if 'username' in session:
        return render_template('user.html',name= escape(session['username']))
    return render_template('user.html')

@app.route('/systeminfo',methods=['GET','POST'])
def systeminfo():

    isLogin = False
    if 'username' in session:
        isLogin = True
    if request.method == 'GET':
        hostname = systemutils.get_host_name()
        localip = systemutils.get_ip_address('eth0')
        wifiip = systemutils.get_ip_address('wlan0')
        ssid = systemutils.get_parameter_value('SSID')
        wifipasswd = systemutils.get_parameter_value('PASSPHRASE')
        return render_template('system_stat.html',hostname=hostname,localip=localip,wifiip=wifiip,ssid=ssid,wifipasswd=wifipasswd,isLogin=isLogin)
    else:
        pass

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        wifiip = request.form['txt_wifiip']
        ssid = request.form['txt_ssid']
        wifipasswd = request.form['txt_wifipasswd']
        systemutils.set_parameter_value('GATEWAY', wifiip)
        systemutils.set_hosts_value(wifiip)
        systemutils.set_parameter_value('SSID', ssid)
        systemutils.set_parameter_value('PASSPHRASE',wifipasswd)
        systemutils.get_text_sh_str('sudo /home/pi/create_ap_restart.sh')
        return redirect(url_for('systeminfo'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()  #实例化form对象
    # if request.method == 'POST':
    #     if form.validate_on_submit():  #数据正确 并且验证csrf通过
    #         print(request.form.get('userpass'))
    #         print(request.form.get('username'))
    #         return '数据提交成功'
    # return render_template('login.html', form=form)

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

#重启设备
@app.route('/rest', methods=['GET', 'POST'])
def reboot():
    if 'username' in session:
        systemutils.system_reboot()
        return jsonify({'status': '0', 'errmsg': '重启成功'})
    else:
        return jsonify({'status':'-1','errmsg':'没有权限重启设备'})

#客户端列表
@app.route('/list', methods=['GET', 'POST'])
def AP_list():
    apList = systemutils.get_ap_client_list()
    if(len(apList) > 0):
        del apList[len(apList)-1]
        del apList[0]
    return render_template('ap_list.html', apList=apList)

#文本内容切词
@app.route('/cut')
def cut():
    return render_template('content_cut.html')

@app.route('/app/' , methods=['GET','POST'])
def appurl():
    if request.method == 'GET':
        id   = request.args.get('id','0')
        name = request.args.get('name','test')
        return 'id:%s ,name:%s' % (id,name)
    else:
        return 'null'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
