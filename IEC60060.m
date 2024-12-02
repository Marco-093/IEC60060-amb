clc
clear all
format short

% ===== Modificar ======

Tipo = 3;
    % 1 - AC
    % 2 - DC
    % 3 - Impulso

% == Valores Medidos == %
P = 1012 ;   %   Presión                         [hPa]
T = 20.1     ;    %    Temperatura en Grados Celsius   [C°]
R = 54.85      ;   %   Porcentaje de Humedad           [%]
L =  0.03    ;   %   Distanica de ruptura [m]

% = Estimación U_50 = %
U_50v =  60 ;   %   [in kilovolt Peak]
    %en otro caso usar: U_50 = 1.1*U_med



% ======================


Lista_tipo = {'AC', 'DC', 'Impulso'};
D = ['IEC60060 - Tipo de descarga: ' , Lista_tipo{Tipo}]; 
disp(D)
disp(' ')

fprintf('============= Correción: ================= \n');
fprintf('kt = k1*k2, con: \n');
fprintf('k1 = δ^m  &  k2 = k^w \n \n');

fprintf('========== Valores Medidos: ============== \n');
fprintf('(P) Presión                 = %g [hPa] \n', P);
fprintf('(T) Temperatura             = %g      [°C] \n', T);
fprintf('(R) %% de humedad relativa   = %g      [%%] \n', R);
fprintf('(U_50) Disruptive-discharge voltage  = %g    [kV] \n', U_50v);
fprintf('(L) Minimum discharge path  = %g     [m] \n \n', L);

fprintf('================ Nota1: ================== \n');
fprintf(' Para U_m < 72.5 [kV] o L < 0.5[m] \n actualmente (2002) no se puede especificar \n ninguna corrección de humedad. (-> k2 = 1). \n \n');

fprintf('============== Cálculos: ================= \n');


% ====== Valores Normales ===== %
P_o = 1013  ;   %   Presión             [hPa]
T_o = 20    ;   %   Temperatura         [C°]
H_o = 11    ;   %   Humedad Absuluta    [g/m^3]

% ====== Cálculos IEC60060 ===== %
h     = (6.11* R * exp(17.6*T / (243+T)))  / (0.4615*(273+T)) ; % Humedad absoluta
delta = (P/P_o)*((273+T_o)/(273+T))                           ; % Densidad relativa del aire
aux   = h/delta                                               ;


fprintf('δ = %g [-]  \n', delta);


sup =15;
if Tipo == 1
    k = 1 +  (0.014 * ( (h/delta) - 11 )) -  (0.00022 * ( (h/delta) - 11 )^2);
elseif Tipo == 2
    k = 1 +  (0.012 * ( (h/delta) - 11 )) ;
else
    k = 1 +  (0.010 * ( (h/delta) - 11 )) ;
    sup = 20;
end
fprintf('k = %g [-] \n \n', k);

if (aux >= 1) && (aux <= sup)
    fprintf('h/δ = %g \n Dentro del rango: \n 1 [g/m^3] < h/δ < %d [g/m3] \n \n', aux, sup);
else
    fprintf('h/δ = %g \n Fuera del rango: \n 1 [g/m^3] < h/δ < %d [g/m^3] \n \n', aux, sup);
end
