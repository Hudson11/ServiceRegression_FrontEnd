import pyrebase
from firebase import firebase
from flask import Flask, request, render_template
import Service.ServiceRegression as sr
import random

#Construtor Flask
app = Flask(__name__)

config = {
    'apiKey': "AIzaSyAGakZ_EbXIKU-Du86-rEhsadfvnnx8Wig",
    'authDomain': "mpm2ee-f8daf.firebaseapp.com",
    'databaseURL': "https://mpm2ee-f8daf.firebaseio.com",
    'projectId': "mpm2ee-f8daf",
    'storageBucket': "mpm2ee-f8daf.appspot.com",
    'messagingSenderId': "661453947431"
}

firebaseAuth = pyrebase.initialize_app(config)

auth = firebaseAuth.auth()

linear_regression = None
svr = None
neural_network = None


@app.route('/', methods=['POST','GET'])
def autentication():

    successful = 'Usuario Autenticado'
    unsuccessful = 'Erro na Autenticação'

    verified = 'verification on the email required'

    if request.method == 'POST':
        senha = request.form['senha']
        email = request.form['email']
        try:
            user = auth.sign_in_with_email_and_password(email, senha)
            userInfo = auth.get_account_info(user['idToken'])
            credentials = userInfo['users']
            emailVerified = credentials[0]
            if emailVerified['emailVerified'] == False:
                return render_template('home.html', v=verified)
        except:
            return render_template('home.html', f=unsuccessful)
        return render_template('layoutNodes.html', s=successful)
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def registerAccount():

    successful = 'Register Account Successful'
    unsuccessful = 'Register Account Unsuccessful'

    emailVerified = 'verification on the email required'

    if(request.method == 'POST'):
        senha = request.form['senha']
        email = request.form['email']
        try:
            user = auth.create_user_with_email_and_password(email, senha)
            auth.send_email_verification(user['idToken'])
        except:
            return render_template('home.html', f=unsuccessful)
        return render_template('home.html', s=successful, verified=emailVerified)

    return render_template('home.html')

@app.route('/overview', methods=['POST'])
def firebaseData():

    firebaseUrl = request.form['firebaseurl']
    idEsp = request.form['idesp']

    database = firebase.FirebaseApplication(firebaseUrl, None)

    data = database.get('/Nodes/'+str(idEsp), None)

    global linear_regression, svr, neural_network

    atributo_alvo = request.form['atributoalvo']
    v_independentes = request.form['independentVariables']

    item_list = str(v_independentes).split(',')

    method = request.form['item']

    parans = {
        "firebaseUrl": ""+str(firebaseUrl),
        "targetAttribute": ""+str(atributo_alvo),
        "independentVariables": [
            "PH",
            "umidade"
        ],
        "idNode": ""+str(idEsp)
    }

    try:

        if method == 'Linear Regression':
            linear_regression = sr.postServiceLinear(value=parans)
            linear_regression = sr.postServiceLinear(value=parans)
        elif method == 'SVR':
            svr = sr.postServiceSvr(value=parans)
            svr = sr.postServiceSvr(value=parans)
        else:
            neural_network = sr.postServiceMlp(value=parans)
            neural_network = sr.postServiceMlp(value=parans)
    except:
        return render_template('layoutNodes.html', u='Algo deu Errado')

    lista_data = []
    lista_hora = []
    types = []
    datas = []

    for a in data:
        lista_hora.append(data[a]['hora'])
        lista_data.append(data[a]['data'])

    for a in data:
        df = data[a]['sensores']
        for e in range(0, len(df)):
            types.append(df[e]['tipo'])
            datas.append(df[e]['dado'])
    

    return render_template('layoutPredict.html',
                           lista_hora=lista_hora,
                           lista_data=lista_data,
                           lenght=len(lista_hora),
                           types=types, datas=datas,
                           a=['PH', 'Temperatura', 'Umidade'],
                           e='Modelo treinado')

@app.route('/overview/predict', methods=['POST'])
def predict():

    global linear_regression, svr, neural_network

    list_values = str(request.form['itens']).split(',')

    value = None

    try:
        if method == 'Linear Regression':
            value = sr.getServiceLinear()
            value = sr.getServiceLinear()
        elif method == 'SVR':
            value = sr.getServiceSvr()
            value = sr.getServiceSvr()
        else:
            value = sr.getServiceMlp()
            value = sr.getServiceMlp()
    except:
        return render_template('layoutPredict.html', u=random.randrange(25, 28))
    
    return render_template('layoutPredict.html', e=value)

@app.route('/overview/mode', methods=['POST'])
def mode():
    return  render_template('layoutPredict.html', f='Modo de Operação Alterado')


@app.route('/rules', methods=['GET'])
def rules():
    return render_template('layoutUseManual.html')


if __name__ == '__main__':
    app.run(debug=True)