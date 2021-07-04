# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0 :
	
    if saldo < pago_mensual: #Bloque para resolver la ultima cuota
    	total_pagado += saldo 
    	saldo = 0 
    
    	print( mes,round(total_pagado,2), round(saldo,2) )
    	break

    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
    	saldo -= pago_extra
    	total_pagado += pago_extra

    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado += pago_mensual
    print( mes, round(total_pagado,2), round(saldo, 2))
    mes += 1
 
print('Total pagado:', round(total_pagado, 2))
print('Cant. meses:', mes)
