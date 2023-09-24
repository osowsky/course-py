# How to use datetime module.

# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

# to use dateutil you must to install it.
# pip install python-dateutil types-python-dateutil
 
from datetime import datetime
from dateutil.relativedelta import relativedelta

initial_date = '20/12/2022'
date_format = '%d/%m/%Y'
borrow_date = datetime.strptime( initial_date, date_format )

no_of_installments = 5 # years.
final_date = borrow_date + relativedelta( years = no_of_installments )

due_date_range = relativedelta( months = 1 )
due_date = borrow_date + due_date_range
months_to_pay =  no_of_installments * 12
instalment = 1000000.0 / months_to_pay

print( f'Date of the borrow: {borrow_date.strftime( date_format )}.' )
print( f'Total of installments: {months_to_pay} months.' )
while ( due_date <= final_date ):
    print( f'Due date: {due_date.strftime( date_format )}' \
          f' --> installment: R$ {instalment:,.2f}' )
    due_date += due_date_range
