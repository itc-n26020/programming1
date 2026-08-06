class Nigiri:
    top = "ネタ"
    price = 100

    def show_attributes(self):
        print("top: {}".format(self.top))
        print("price: {}".format(self.price))

class Katuo(Nigiri):                                                               
    top = "かつお"                                                  
    topping = "生姜とネギ"                              
    price = 100                                         

    def show_attributes(self):  
        super().show_attributes()  
        print("topping: {}".format(self.topping))  

k1 = Katuo()  
k1.show_attributes()  
