primeiroBimestre = float(input('Digite a primeira nota: '))
segundoBimestre = float(input('Digite a segunda nota: '))
terceiroBimestre = float(input('Digite a terceira nota: '))
quartoBimestre = float(input('Digite a quarta nota: '))

media = (primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre) / 4

if media < 7.0:
    print('Você foi reprovado, com a nota final', media)
elif media > 7.0:
    print('Você foi aprovado, com a nota final', media)
