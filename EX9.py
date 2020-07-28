class Time:
    """Hour=0
    Minute=0
    Second=0"""
    def __init__(self,h_value=0,m_value=0,s_value=0):
        self.Hour=h_value
        self.Minute=m_value
        self.Second=s_value
        
    def __str__(self):
        return str(self.Hour) +':' + str(self.Minute) +':'+ str(self.Second)
    
    def __repr__(self):
        return str(self.Hour) +':' + str(self.Minute) +':'+ str(self.Second)
    
    def __add__(self,other):
        add_h=self.Hour+other.Hour
        add_m=self.Minute+other.Minute
        add_s=self.Second+other.Second
        if add_s >= 60:
            add_m += (add_s//60)
            add_s %= 60

        if add_m >= 60:
            add_h += (add_m//60)
            add_m %= 60
        
        if add_h >= 24:
            add_h %= 24                
        return str(add_h)+':' + str(add_m) +':'+ str(add_s)
    
    def __sub__(self,other):
        return str(self.Hour-other.Hour)+':' + str(self.Minute-other.Minute)\
               +':'+ str(self.Second-other.Second)
    
    def __lt__(self,other):
        if self.Hour < other.Hour:
            return True
        elif (self.Hour == other.Hour or self.Hour > other.Hour) \
              and self.Minute < other.Minute:
            return True
        elif (self.Minute == other.Minute or self.Minute > other.Minute) \
             and self.Second < other.Second:
            return True
        else:
            return False
    """    
    def __gt__(self,other):
        if self.Hour > other.Hour:
            return True
        elif self.Minute > other.Minute:
            return True
        elif self.Second > other.Second:
            return True
        else:
            return False
    """
    def __ne__(self, other):
             if self.Hour!=other.Hour \
                and self.Minute!=other.Minute and self.Second != other.Second:
                  return True
             else:
                  return False
    
    def __eq__(self, other):
             if self.Hour==other.Hour \
                and self.Minute==other.Minute and self.Second == other.Second:
                  return True
             else:
                  return False
        
    def show(self):
        return str(self.Hour) +':' + str(self.Minute) +':'+ str(self.Second)

"""
h=int(input('Hour :'))
m=int(input('Minute :'))
s=int(input('Second :'))
t1=Time(h,m,s)
t1.Hour=h
t1.Minute=m
t1.Second=s"""
t1=Time(12,34,56)
t2=Time(10,10,10)
print('T1: ',t1.show())
print('T2: ',t2.show())
print('t1 > t2 :',t1 > t2)
print('t1 < t2 :',t1 < t2)
print('t1 == t2 :',t1 == t2)
print('t1 != t2 :',t1 == t2)
print('t1 == t1 :',t1 == t1)
