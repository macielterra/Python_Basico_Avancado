#para instalar o pacote requests: terminal>> pip3 install requests
import requests

#Fazendo requisiçao http usando request
def retorna_dados_cep(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    # print(response.text)
    # print(type(response.text))
    print(response.json())
    #print(type(response.json()))
    dadosCep = response.json()
    print(dadosCep['logradouro'])
    print(dadosCep['localidade'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    #print(response.json())
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    #retorna_dados_cep('01001000')
    #poke = retorna_dados_pokemon('pikachu')
    #print(poke['sprites']['front_shiny'])
    rep = retorna_response('https://g1.globo.com/')
    print(rep)