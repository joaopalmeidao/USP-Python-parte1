input_dias=int(input('Informe os segundos: '))

dias=input_dias//86400
seg_rest_dias=input_dias%86400
horas=seg_rest_dias//3600
seg_rest_horas=seg_rest_dias%3600
minutos=seg_rest_horas//60
segundos=seg_rest_horas%60


print(dias,'dias,',horas,'horas,',minutos,'minutos e',segundos,'segundos')
