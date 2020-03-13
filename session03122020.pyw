# Codigo escrito para Laboratorio de Fundamentos de programacion
def separador(n):
  print('-'*int(n))

# Escribe una funcion para capturar la nota, que solo acepte valores entre 0 y 100
def nota():
  return

def capturas(n):
  print("Capturando los dados")
  lista = []
  for i in range(n):
    separador(50)    
    asig = str(input('> Asignaturas:'))
    nota = int(input('> Nota:'))
    lista.append([n+1,asig,nota])
  separador(50)
  return lista

# Te atreves a calcular el promedio de cada trimestre??
def promedio():
  return

def mostrar(lista):
  print("Motrando los resultados") 
  for i in range(len(lista)):
    separador(50)
    print('Trimestre #{}:'.format(i+1))
    for t in range(len(lista[i])):
      asig = str(lista[i][t][1])
      nota = int(lista[i][t][2])
      # \t activa una tabulacion
      print ('- Asig.: {0} \t Nota: {1}'.format(asig, nota))
  return
  

def main():
  t = int(input('Cuantos trimestes evaluaras? '))
  datos = []
  for i in range(t):
    print('Trimestre #{}:'.format(i+1))
    a = int(input('Cuantas asignaturas tomaste este trimeste:'))
    # Lista con [trimestre, asignaturas, notas]
    datos.append(capturas(a))
  
  mostrar(datos)

main()
