## La classe cerchio 


Importiamo il modulo con le funzioni matematiche:

    import math
    
Se ora abbiamo bisogno del pi greco ad esempio basterà scrivere:

    PI = math.pi
    print("valore di PI:", PI) 

Le classi in Python possono essere definite in modo semplice:

    class Cerchio:
      pass
      
Definita la classe possiamo di chiarare un oggetto della classe cerchio, ossia una variabile che possiamo considerare a tutti 
gli effetti come un cerchio sul piano:

    c = Cerchio()

Possiamo ora fissare il centro e il raggio del cerchio:

    c.x = 2
    c.y = 2
    c.r = 10

e poi muoverlo nel piano, ingrandirlo o renderlo piccolo a piacere.

### Inizializzazione al momento della creazione

Esiste la possibilità di creare un cerchio con centro e raggio predefinito in modo da evitare il calcolo 
dell'area o della circonferenza di un cerchio non ancora inizializzato:

    class Circle:
        def __init__(self, cx=0, cy=0, r=1):
            self.raggio = r
            self.x = cx
            self.y = cy
        pass
  
  In questo modo qualsiasi cerchio venga creato con la chiamata:
  
      c = Cerchio()
   
  avrà di default raggio r=1 e centro nell'origine. Mentre con la chiamata:
  
     c1 = Circle(2,2,10)
  
  verrà creato un cerchio di raggio 10 e centro in (2,2) sul piano:
  
     print(c.x, c.y, c.raggio)
  
 ### Funzioni di calcolo interne
    
 Aggiungendo ora la funzioni di calcolo interne:
 
    def area(self):
        return print("area=", math.pi * self.radius*self.radius)

    def circonferenza(self):
        return print("circonferenza=", 2*math.pi * self.radius)
        
  diventa possibile stampare circonferenza e area delle circonferenze create senza dover conoscere le formule:
  
      print("area =", c.area())
      print("Circonferenza, c.circonferenza)
  
  La classe avrà pertanto la seguente struttura:
  
     class Circle:
         def __init__(self, cx=0, cy=0, r=1):
            self.raggio = r
            self.x = cx
            self.y = cy
         def area(self):
            return print("area=", math.pi * self.radius*self.radius)

         def circonferenza(self):
            return print("circonferenza=", 2*math.pi * self.radius)    
        
         pass
         
Allo stesso modo possiamo creare una funzione interna che stampi tutti i dati della circonferenza:

    def print_info(self):
        print("")
        print("x=", self.x)
        print("y=",self.y)
        print("raggio=",self.radius)
        self.circonferenza()
        self.area()
    
Aggiungendo questa funzione diventa possibile richiedere informazioni sulla circonferenza che stiamoi maneggiando:


    c1.print_info()
    c2.print_info()



