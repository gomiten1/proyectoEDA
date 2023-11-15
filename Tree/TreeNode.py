class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
    
    def __str__(self):
        return str(self.key) + "->" + self.value


class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t 
        self.keys = [None] * (2 * t - 1) 
        self.C = [None] * (2 * t) 
        self.n = 0 
        self.leaf = leaf 
        
    def insertNonFull(self, data):
       
        i = self.n - 1 
        if self.leaf: 
            while i >= 0 and self.keys[i].key > data.key: 
         
                self.keys[i+1] = self.keys[i] 
                i -= 1 
            self.keys[i+1] = data 
            self.n += 1 
        else: 
            while i >= 0 and self.keys[i].key > data.key: 

                i-=1 
            if self.C[i+1].n == 2 * self.t - 1: 
                self.splitChild(i+1, self.C[i+1]) 
                if self.keys[i+1].key < data.key: 
                    i+=1
            self.C[i+1].insertNonFull(data)
    

            
    def splitChild(self, i, y):
 
        z = BTreeNode(y.t, y.leaf) 
        z.n = self.t - 1 
        for j in range(self.t - 1):
    
            z.keys[j] = y.keys[j + self.t]
        if not y.leaf:
            for j in range(self.t):
     
                z.C[j] = y.C[j + self.t]
        y.n = self.t - 1
        for j in range(self.n, i, -1):
 
            self.C[j+1] = self.C[j]
        self.C[i+1] = z
        for j in range(self.n - 1, i-1, -1): 

            self.keys[j+1] = self.keys[j] 
        self.keys[i] = y.keys[self.t - 1]
        self.n += 1
        
   
        
    def traverse(self, l):
     
        for i in range(self.n):
      
            if not self.leaf:
                self.C[i].traverse(l+1)
            print("\t" * l, l, self.keys[i], end='')
            print()
        if not self.leaf:
            self.C[i+1].traverse(l+1) 
            
    
            
    def search(self, k):
   
        i = 0 
        while i < self.n and k > self.keys[i].key: 
    
            i += 1 
        if i < self.n and k == self.keys[i].key: 
            return self.keys[i].value
        if self.leaf:
            return None
        return self.C[i].search(k)     
    
