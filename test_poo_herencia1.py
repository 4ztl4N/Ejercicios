class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available= False
            print(f"El vehículo {self.brand}, ha sido vendido")
        else:
            print(f"El vehículo {self.brand} no está disponible")
    
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class Car(Vehicle):
        def start_engine(self):
             if not self.is_available:
                 return (f"El motor del coche {self.brand}, está en marcha")
             else:
                 return (f"El coche {self.brand} no está disponible")
             
        def stop_engine(self):
                 if self.is_available:
                     return (f"El motor del coche {self.brand} se ha detenido")
                 else: retur (f"El coche {self.brand} no está disponivle")


                 

        