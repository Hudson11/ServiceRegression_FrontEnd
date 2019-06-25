import Service.ServiceRegression as sr

'''data = {
    "firebaseUrl": "https://mpm2ee-f8daf.firebaseio.com",
	"targetAttribute": "temperatura",
	"independentVariables": ["PH","umidade"],
	"idNode": "ESP-1"
}

headers = {'Content-type':'application/json', 'Accept':'application/json'}

response = sr.postServiceLinear(value=data)
print(response.status_code)
print(response.content)

response = sr.getServiceLinear()
print(response.status_code)
print(response.content)

response = sr.postServiceSvr(value=data)
print(response.status_code)
print(response.content)

response = sr.getServiceSvr()
print(response.status_code)
print(response.content)

response = sr.postServiceMlp(value=data)
print(response.status_code)
print(response.content)

response = sr.getServiceMlp()
print(response.status_code)
print(response.content)'''

data = {
	'-LdjDXvi4e2qfANZ3PVO': {
		'data': '2019-04-30', 
		'hora': '14:09', 
		'id': 'ESP-1', 
		'idReference': '-LdjDXvi4e2qfANZ3PVO', 
		'regiao': 'Interna', 
		'sensores': [
			{'dado': '98', 'tipo': 'PH'}, 
			{'dado': '77', 'tipo': 'umidade'}, 
			{'dado': '27', 'tipo': 'temperatura'}]
		}, 
		'-LdjDedD0pOQBG6LaO-m': {
			'data': '2019-04-30', 
			'hora': '14:10', 
			'id': 'ESP-1', 
			'idReference': 
			'-LdjDedD0pOQBG6LaO-m', 
			'regiao': 'Interna', 
			'sensores': [
				{'dado': '98', 'tipo': 'PH'}, 
				{'dado': '77', 'tipo': 'umidade'}, 
				{'dado': '27', 'tipo': 'temperatura'}]
		}
}


