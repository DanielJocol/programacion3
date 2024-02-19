import graphviz
# Antes de comenzar debemos de ejecutar el siguiente comando en la terminal de python py -m pip install graphviz
# Luego debemos de instalar el siguiente pluggin: https://www.graphviz.org/download/
# Por ultimo cerrar todas las terminales y el programa para reiniciar y se ejecuten todos los cambios
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

class Lista:
    def __init__(self):
        self._head = None
        self._tail = None

    def insertar_al_principio(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self._head:
            self._head = nuevo_nodo
            self._tail = nuevo_nodo 
        else:
            nuevo_nodo.sig = self._head
            self._head = nuevo_nodo
    
    def insertar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self._head:
            self._head = nuevo_nodo
            self._tail = nuevo_nodo 
        else:
            self._tail.sig = nuevo_nodo
            self._tail = nuevo_nodo
    
    def eliminar_por_valor(self, valor):
        actual = self._head
        ant = None
    
        while actual:
            if actual.dato == valor:
                if ant:
                    ant.sig = actual.sig
                    if not actual.sig:
                        self._tail = ant
                else:
                    self._head = actual.sig
                    if not actual.sig:
                        self._tail = None
                return
            ant = actual
            actual = actual.sig

    def mostrar_lista(self):
        g = graphviz.Digraph('G', filename='hello.gv')
        actual = self._head
        Ant = self._head
        while actual:
        
            if Ant.dato == actual.dato:
                pass
            else:
                g.edge(str(Ant.dato), str(actual.dato))
                g.edge(str(actual.dato), str(Ant.dato))   
            Ant = actual
            actual = actual.sig

        
        g.view()  
            
        

# Crear una instancia de Lista
lis = Lista()

print("""Bienvenido al programa de listas enlazadas
ingrese una opción:
1. Insertar al principio
2. Insertar al final
3. Eliminar por valor
4. Mostrar lista
5. Salir
""")
while True:
    try:
        op_men = int(input("Ingrese el numero de opción: "))
        if op_men == 1:
            print("Usted eligio la opción 1")
            val = input("Ingrese el dato que desea insertar al inicio: ")
            lis.insertar_al_principio(val)
            
        elif op_men == 2:
            print("Usted eligio la opción 2")
            val = input("Ingrese el dato que desea insertar al final: ")
            lis.insertar_al_final(val) 
            
        elif op_men == 3:
            try:
                print("Usted eligio la opción 3")
                
                val = input("Ingrese el valor que quiere eliminar: ")
                 
            except ValueError as ve:
                print(f"Ingrese unicamente numeros")
            lis.eliminar_por_valor(val)
            
        elif op_men == 4:
            print("Usted eligio la opción 4")
            print("La lista es la siguiente: ") 
            lis.mostrar_lista()
        elif op_men == 5:
            print("Usted eligio la opción 5")
            print("Hasta luego vuelva pronto")
            break
        else:
            print("Elija una opción correcta")
    except ValueError as ve:
        print(f"Ingrese unicamente numeros")
