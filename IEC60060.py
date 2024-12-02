# ===== Modificar ======

import math
Tipo = 1

    # 1 - AC
    # 2 - DC
    # 3 - Impulso

# == Valores Medidos == %
P = 1013    # Presión [hPa]
T = 22.7    # Temperatura en Grados Celsius [C°]
R = 50.25   # Porcentaje de Humedad [%]
L = 0.5    # Distanica de ruptura [m]


# = Estimación U_50 = %
U_50v = 90     # [in kilovolt Peak]
    # en otro caso usar: U_50 = 1.1*U_med

# ======================

Lista_tipo = ['AC', 'DC', 'Impulso']
D = 'IEC60060 - Tipo de descarga: ' + Lista_tipo[Tipo-1]
print(D)
print(' ')

print('============= Correción: =================')
print('kt = k1*k2, con:')
print('k1 = δ^m  &  k2 = k^w \n')

print('========== Valores Medidos: ==============')
print('(P) Presión                  =', P, '[hPa]')
print('(T) Temperatura              =', T, '[°C]')
print('(R) %% de humedad relativa   =', R, '[%]')
print('(U_50) Disruptive-discharge voltage   =', U_50v, '[kV]')
print('(L) Minimum discharge path   =', L, '[m]\n')

print('================ Nota1: ==================')
print(' Para U_m < 72.5 [kV] o L < 0.5[m] \n actualmente (2002) no se puede especificar \n ninguna corrección de humedad. (-> k2 = 1). \n')

print('============== Cálculos: =================')


# ====== Valores Normales ===== %
P_o = 1013     # Presión [hPa]
T_o = 20       # Temperatura [C°]
H_o = 11       # Humedad Absuluta [g/m^3]

# ====== Cálculos IEC60060 ===== %
h     = (6.11* R * math.exp(17.6*T / (243+T)))  / (0.4615*(273+T))    # Humedad absoluta

delta = (P/P_o)*((273+T_o)/(273+T))                                # Densidad relativa del aire
aux   = h/delta                                                   

print('δ =', delta, '[-]')

sup = 15
if Tipo == 1:
    k = 1 +  (0.014 * ( (h/delta) - 11 )) -  (0.00022 * ( (h/delta) - 11 )**2)
elif Tipo == 2:
    k = 1 +  (0.012 * ( (h/delta) - 11 ))
else:
    k = 1 +  (0.010 * ( (h/delta) - 11 ))
    sup = 20
print('k =', k, '[-]\n')

if (aux >= 1) and (aux <= sup):
    print('h/δ =', aux, '\n Dentro del rango:\n 1 [g/m^3] < h/δ <', sup, '[g/m3]\n')
else:
    print('h/')
    