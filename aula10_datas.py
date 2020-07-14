from datetime import date,time,datetime,timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)

    #convertendo pro formato brasileiro
    data_conv = data_atual.strftime('%d/%m/%Y')
    data_conv2 = data_atual.strftime('%A %B %Y')
    print(data_conv)
    print(data_conv2)

def trabalhando_com_time():
    horario = time(hour=15, minute=18,second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(type(horario))
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime('%d/%m/%Y - %H:%M:%S')
    data_atual_dia = data_atual.strftime('%d/%m/%Y')
    data_atual_hora = data_atual.strftime('%H:%M:%S')
    print(data_atual)
    print(data_atual_str)
    print(data_atual_dia)
    print(data_atual_hora)
    print(data_atual.year)
    print(data_atual.date())

    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabbado','Domingo')
    print(tupla[data_atual.weekday()])

    data_str = '01/01/2020'
    data_convertida = datetime.strptime(data_str,'%d/%m/%Y')#converte p/ datetime e usa seus metodods
    print(data_convertida)

    data_convertida_menos1 = data_convertida - timedelta(days=365)
    print(data_convertida_menos1)





if __name__ == "__main__":
    
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()