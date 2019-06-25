import requests

linearRegressionGetPost = 'https://module-predict-data.herokuapp.com/prediction/linearRegression'
svrRegressionGetPost = 'https://module-predict-data.herokuapp.com/prediction/svrRegression'
mlpRegressionGetPost = 'https://module-predict-data.herokuapp.com/prediction/mlpRegression'

headers = {'Content-type':'application/json', 'Accept':'application/json'}

def getServiceLinear():
    '''
    :return: Retorno da requisição GET
    '''
    return requests.get(linearRegressionGetPost, headers=headers)

def postServiceLinear(value):
    '''
    :param dict: Dicionário contendo as informações de entrada para a requisição
    :return: Retorno da requisição POST
    '''
    return requests.post(linearRegressionGetPost, json=value, headers=headers)

def getServiceSvr():
    '''
    :return: Retorno da requisição GET
    '''
    return requests.get(svrRegressionGetPost, headers=headers)

def postServiceSvr(value):
    '''
    :param dict: Dicionário contendo as informações de entrada para a requisição
    :return: Retorno da requisição POST
    '''
    return requests.post(svrRegressionGetPost, json=value, headers=headers)

def getServiceMlp():
    '''
    :return: Retorno da requisição GET
    '''
    return requests.get(mlpRegressionGetPost, headers=headers)

def postServiceMlp(value):
    '''
    :param dict: Dicionário contendo as informações de entrada para a requisição
    :return: Retorno da requisição POST
    '''
    return requests.post(mlpRegressionGetPost, json=value, headers=headers)