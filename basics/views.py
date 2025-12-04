from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def area_triangulo(request):
    try:
        base = float(request.data.get('base',0))
        altura = float(request.data.get('altura',0))
    except (TypeError, ValueError):
        return Response({"error": "Parámtros Inválidos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    area = (base * altura) / 2
    return Response({
        "base": base,
        "altura": altura,
        "area": area
    })
    
@api_view(['GET'])
def tabla_multiplicar(request):
    try:
        n = int(request.query_params.get('numero',0))
    except (TypeError, ValueError):
        return Response({"error": "Número Inválido"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    tabla = [f"{n}x{i}={n*(i)}" for i in range(1,11) ]
    return Response({
        "numero": n,
        "tabla": tabla,
    })
        

@api_view(['POST'])
def contar_mayores(request):
    try:
        numeros = request.data.get('numeros',[])
        limite = request.data.get('limite',0)
    except (TypeError, ValueError):
        return Response({"error": "Parámtros Inválidos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        limite=float(limite)
        lista_numeros = [float(n) for n in numeros]
    except (TypeError, ValueError):
        return Response({"error": "Valores numéricos Inválidos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    contador = 0
    for n in lista_numeros:
        if n > limite:
            contador+= 1
    return Response({
        "numeros": lista_numeros,
        "limite": limite,
        "mayores": contador
    })


@api_view(['POST'])
def sumar_consecutivos(request):
    try:
        limite = request.data.get('limite',0)
    except (TypeError, ValueError):
        return Response({"error": "Parámtros Inválidos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    resultado = 0
    i = 1
    while i <= limite:
        resultado += i
        i+= 1
    return Response({
        "limite": limite,
        "resultado": resultado
    })



@api_view(['POST'])
def promedio(request):
    try:
        numeros = request.data.get('numeros',[])
    except (TypeError, ValueError):
        return Response({"error": "Parámtros Inválidos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_numeros = [float(n) for n in numeros]
    except (TypeError, ValueError):
        return Response({"error": "Valores numéricos Inválidos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    suma = 0
    for n in lista_numeros:
        suma+=n
    resultado = suma / len(lista_numeros)
    
    return Response({
        "numeros": lista_numeros,
        "promedio": resultado,
    })


@api_view(['POST'])
def simulador_prestamo(request):
    try:
        capital = float(request.data.get('capital'))
        tasa_anual = float(request.data.get('tasa_anual'))  # en %
        anios = int(request.data.get('anios'))
        cuotas_mostrar = int(request.data.get('cuotas_mostrar', 6))
    except (TypeError, ValueError):
        return Response({"error": "Parámetros numéricos inválidos"}, status=status.HTTP_400_BAD_REQUEST)
    if capital <= 0 or tasa_anual <= 0 or anios <= 0:
        return Response({"error": "capital, tasa_anual y anios deben ser > 0"}, status=status.HTTP_400_BAD_REQUEST)
    tasa_mensual = (tasa_anual / 100) / 12
    num_cuotas = anios * 12
    cuota = capital * tasa_mensual / (1 - (1 + tasa_mensual) ** (-num_cuotas))
    saldo = capital
    cuotas = []
    i = 1
    while i <= cuotas_mostrar and saldo > 0:
        interes = saldo * tasa_mensual
        amortizacion = cuota - interes
        saldo = max(saldo - amortizacion, 0)
        cuotas.append({
            "numero_cuota": i,
            "cuota": round(cuota, 2),
            "interes": round(interes, 2),
            "amortizacion": round(amortizacion, 2),
            "saldo_restante": round(saldo, 2),
        })
        i += 1
    return Response({
        "capital": capital,
        "tasa_anual": tasa_anual,
        "anios": anios,
        "cuota_mensual_aprox": round(cuota, 2),
        "primeras_cuotas": cuotas
    })
