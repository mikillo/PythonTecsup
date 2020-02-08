'''
a=float(input(print("ingrese 1er numero: \t")))
b=float(input(print("ingrese 2do numero: \t ")))
c=float(input(print("ingrese 3er numero: \t ")))
d=float(input(print("ingrese 4to numero: \t ")))
e=float(input(print("ingrese 5to numero: \t ")))
f=float(input(print("ingrese 6to numero:\t ")))
g=float(input(print("ingrese 7mo numero:\t ")))
h=float(input(print("ingrese 8vo numero:\t ")))
i=float(input(print("ingrese 9no numero:\t ")))
j=float(input(print("ingrese 10mo numero:\t ")))
print("la suma de los numeros ingresados es :",a+b+c+d+e+f+g+h+i+j)

cantidad=int(input(print("ingrese la cantidad de numeros a sumar")))
contador=1
suma=0
while contador<=cantidad:
    suma=suma+float(input(print("ingrese ",contador," numero")))
    contador+=1
print("la suma es:",suma)
print("el promedio es:",suma/cantidad)

numeros=[1,2,3,4,5,6]
suma_par=0
suma_impar=0
indice=0
while indice<len(numeros):
    if numeros[indice]%2==0:
        suma_par+=numeros[indice]
    else:
        suma_impar+=numeros[indice]
    indice+=1
print("la suma de los numeros pares es:",suma_par)
print("la suma de los numeros impares es :",suma_impar)

lista=[0,-2,3,-24,5]
positivo=[]
negativo=[]
neutro=[]
pares=[]
impares=[]
indice=0
while indice<len(lista):
    if lista[indice]==0:
        neutro.append(lista[indice])
    elif lista[indice]>0:
        positivo.append(lista[indice])
        if lista[indice]%2==0:
            pares.append(lista[indice])
        else:
            impares.append(lista[indice])
    elif lista[indice]<0:
        negativo.append(lista[indice])
        if lista[indice]%2==0:
            pares.append(lista[indice])
        else:
            impares.append(lista[indice])
    indice+=1
print("valores neutros:",neutro)
print("valores positivos:",positivo)
print("valores negativos:",negativo)
print("valores pares:",pares)
print("valores impares:",impares)

#practica calificada
#EJERCICIO1
#borramos noviembre
meses=['julio','agosto','setiembre','octubre','noviembre','diciembre']
indice=0
while indice<len(meses):
    if meses[indice]=='noviembre':
        meses[indice]=[]
    indice+=1
print(meses)

#acceder al mes de agosto con el indice negativo
meses=['julio','agosto','setiembre','octubre','noviembre','diciembre']
print(meses[-5])

#acceder al mes de diciembre con el indice positivo
print(meses[5])  

pbi={2010:148.014,2011:168.772,2012:189.024,2013:197.866,2014:203.021,2015:192.391,2016:195.432,2017:214.128,2018:225.203,2019:232.080}
print("pbi 2010 - 2011 :",(pbi[2010]+pbi[2011])/2)
print("pbi 2011 - 2012 :",(pbi[2011]+pbi[2012])/2)
print("pbi 2012 - 2013 :",(pbi[2012]+pbi[2013])/2)
print("pbi 2013 - 2014 :",(pbi[2013]+pbi[2014])/2)
print("pbi 2014 - 2015 :",(pbi[2014]+pbi[2015])/2)
print("pbi 2015 - 2016 :",(pbi[2015]+pbi[2016])/2)
print("pbi 2016 - 2017 :",(pbi[2016]+pbi[2017])/2)
print("pbi 2017 - 2018 :",(pbi[2017]+pbi[2018])/2)
print("pbi 2018 - 2019 :",(pbi[2018]+pbi[2019])/2)

lista=[13,4,22,18,17,2,14,20]
lista.sort()
lista2=lista[0:4]
lista.sort(reverse=True)
lista2.append(lista[0:4])
print(lista2)

lista1=['jose','maria','juan']
lista2=['eduardo','jose','pedro']
conjunto1=set(lista1)
conjunto2=set(lista2)
union=list(conjunto1|conjunto2)
print(union)
print("la cantidad de nombres unicos son:",len(union))


#definimos una funcion para sumar 2 numeros
def operaciones(num1,num2):
    suma=num1+num2
    resta=num1-num2
    multi=num1*num2
    div=num1/num2
    return suma,resta,multi,div
result_suma,result_resta,result_multi,result_div=operaciones(10,20)
print("la suma es:",result_suma)
print("la resta es:",result_resta)
print("la multiplicacion es:",result_multi)
print("la division es:",result_div)

#otra funcion para sumar y restar
def calcula(num1,num2,operacion):
    if operacion=="+":
        resultado=num1+num2
    if operacion=="-":
        resultado=num1-num2
    return resultado
result=calcula(1,2,"-")
print(result)

#listas

sabores=["chocolate","creama americana","vainilla",True,10,12.3]
#print(sabores[0].upper())
elemento_eliminado=sabores.pop(1)
print(elemento_eliminado)
sabores.append("esto es el ultimo")
sabores.insert(0,"objecto insertado")
print(sabores[-1])
print(sabores)

sabores=["chocolate","crema americana"]
sabores2=["vainilla","dulce de leche"]
sabores.extend(sabores2)
sabores.remove("crema americana")
print(sabores)

'''
#diccionarios
paciente1={"nombre":"juan","edad":32,"peso":70.5,"fuma":False}
paciente2={"nombre":"maria","edad":42,"peso":70.5,"fuma":False}
paciente3={"nombre":"pedro","edad":18,"peso":70.5,"fuma":False}
pacientes=[paciente1,paciente2,paciente3]
#print(pacientes)
for x in range(len(pacientes)):
    print("")
    print("---------------------------------------------")
    print("-------------- DICCIONARIO Nro ",x+1,"-----------")
    print("---------------------------------------------")
    for clave,valor in pacientes[x].items():
        print("clave --->",clave,"\t|\tvalor ---->",valor)
        
    
    
#print(paciente["nombre"])
#print(paciente["fuma"])
#print(paciente.get("edad"))
#paciente.update({"edad":18})
#valor=paciente.pop("edad")
#print(valor)
#paciente["edad"]=45
#print(paciente)
#print("edad" in paciente)












