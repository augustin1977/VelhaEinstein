class Tabuleiro:
    def __init__(self,n):
        self.solucao=[]
        self.t=[0,0,0,0,0,0,0,0,0]
        self.n=n
    def resolvidoEinstein(self):
        if (self.t[0]+self.t[1]+self.t[2]==3  or self.t[3]+self.t[4]+self.t[5]==3  or self.t[6]+self.t[7]+self.t[8]==3 
        or self.t[0]+self.t[3]+self.t[6]==3 or self.t[1]+self.t[4]+self.t[7]==3 or self.t[8]+self.t[5]+self.t[2]==3
        or self.t[0]+self.t[4]+self.t[8]==3 or self.t[2]+self.t[4]+self.t[6]==3 ):
            return False
        else:
            if sum(self.t)==self.n :
                return True
            else:
                return False
    def resolve(self,i=0):
        if self.resolvidoEinstein():
            self.solucao.append(self.t.copy())
        else:
            if i<9:
                self.resolve(i+1)
                self.t[i]=1
                self.resolve(i+1)
                self.t[i]=0
                
            
    def printSolucoes(self):
        s=""
       
        for sol in self.solucao:
            i=0

            for v in sol:
                i+=1
                if i%3==0:
                    s+=(str(v)+"\n")
                else:
                    s+=(str(v)+" ")
            s+="\n" 
        s+=f"Foram encontradas {len(self.solucao)} soluções viaveis com {self.n} casas ocupadas\n"
        return s    
    def __str__(self):
        s=""
       
        """for sol in self.solucao:
            i=0

            for v in sol:
                i+=1
                if i%3==0:
                    s+=(str(v)+"\n")
                else:
                    s+=(str(v)+" ")
            s+="\n" """
        s+=f"Foram encontradas {len(self.solucao)} soluções viaveis com {self.n} casas ocupadas\n"
        return s    


print("Jogo da velha de Einstein")
n="a"
while(not n.isdigit()):
    n= input("digite o numero de O que quer tentar por na velha:\n")
n= int(n)
t= Tabuleiro(n)
t.resolve()
print(t.printSolucoes())
