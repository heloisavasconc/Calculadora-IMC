print('Descubra o seu Índice de Massa Corporal - IMC')
nome=str(input('Qual é o seu nome?'))
peso=float(input('Qual é o seu peso?'))
altura=float(input('Qual é a sua altura?'))
imc=peso/(altura**2)
if imc <17.0:
    print('Seu IMC está muito baixo do peso')
elif imc >= 17.0 and imc <= 18.5:
    print('Seu IMC está abaixo do peso')
elif imc > 18.5 and imc <=25.0:
    print('Parabéns! Seu peso está dentro do normal!')
elif imc > 20.0 and imc <= 30.0:
    print('Seu IMC está acima do peso normal')
else: 
    print: ('muito acima do peso!')