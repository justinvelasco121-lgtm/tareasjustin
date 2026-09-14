def calcular_costo_proyecto(horas_desarrollo, tarifa_hora):
    
    costo_total = horas_desarrollo * tarifa_hora
    return costo_total

if __name__ == "__main__":
   
    horas = 45
    tarifa = 25.50
    
    
    resultado = calcular_costo_proyecto(horas, tarifa)
    

    print(f"El costo total del proyecto por {horas} horas a ${tarifa}/hora es: ${resultado}")