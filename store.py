print('Bem vindo a Loja do fabio murilo da silva')
preco = float(input('Digite o valor do produto:  '))
qtd = int(input('Digite a quantidade do produto :  '))
desconto = float(input('Digite o percentual de desconto (0-100%): '))
if preco:
  sub_total = qtd * preco
  valor_sem_desconto = sub_total * desconto / 100
  valor = sub_total - valor_sem_desconto
  valor_com_desconto = valor
  print('O valor sem desconto foi: R$ 1500.0 {:.2f}'.format(sub_total))
  print('O valor com desconto foi: R$ 1350.0 {:.2f} (desconto{10}%)'.format(valor_com_desconto, desconto))