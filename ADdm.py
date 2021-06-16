matrizA=[]
matrizB=[]
print("Ingrese las dimensiones para la matriz 1")
fila=int(input("Numero de filas: "))
columna=int(input("Numero de columnas: "))
for a in range(fila):
  matrizA.append([0]*columna)

for a in range(fila):
  for b in range(columna):
    matrizA[a][b] = int(input("dato "+str(b+1)+" para la fila "+str(a+1)+": "))
resulA =[]
resul =1
for a in range(fila):
  for b in range(columna):
   resul=resul*matrizA[a][b]
  resulA.append(resul)
  resul=1

print("Ingrese las dimensiones para la matriz 2")
filab=int(input("Numero de filas: "))
columnab=int(input("Numero de columnas: "))
for a in range(filab):
  matrizB.append([0]*columnab)

for a in range(filab):
  for b in range(columnab):
    matrizB[a][b] = int(input("dato "+str(b+1)+" para la fila "+str(a+1)+": "))

resulB =[]
resul =1
for a in range(filab):
  for b in range(columnab):
   resul=resul*matrizB[a][b]
  resulB.append(resul)
  resul=1

print("la multiplicacion de matrices es: ")


for a in range(fila):
  for b in range (columna):
    print(matrizA[a][b],end=' ')
  print(" x ",end=' ')
  for c in range(columnab):
    print(matrizB[a][c],end=' ')
  print(" = ",end=' ')
  print(resulA[a]*resulB[a])
