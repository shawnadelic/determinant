class matrix:
    def __init__(self,size,array=[]):
        if size < 2:
            raise ValueError
        self.size = size
        self.array = array
    def add_row(self,row):
        if len(row) != self.size:
            raise ValueError
        else:
            self.array.append(row)
    def get_value(self,col,row):
        return self.array[col][row]
    def get_sub_matrix(self,row,col):
        sub_matrix = matrix(self.size-1,[])
        for i, r in enumerate(self.array):
            if i!= row:
                sub_matrix.add_row([c for j, c in enumerate(r) if j!=col])
        return sub_matrix
    def __repr__(self):
        return "Matrix: {}\nSize: {} x {}".format(self.array,self.size,self.size)

def find_determinant(m):
    if m.size == 2:
        array = m.array
        return array[0][0] * array[1][1] - array[1][0] * array[0][1]
    else:
        submatrices = [ [(p[0],p[1]),m.get_sub_matrix(0,p[1])] for p in
                [ (0,s) for s in range(m.size)] ]
        return sum( [ m.get_value(s[0][0],s[0][1]) * (-1 if i%2 else 1) * find_determinant(s[1]) for i,s in enumerate(submatrices) ])

#Defines a 4x4 test matrix
def define_test_matrix(size):
    test_matrix = matrix(size)
    for h in range(size):
        test_matrix.add_row([w + (h*size) for w in range(size)])
    return test_matrix

size = int(raw_input("Enter size (n*n) of matrix: "))

A = matrix(size)
print "Enter first row for {}*{} matrix:".format(size,size)
for s in range(size):
    row = [int(i) for i in raw_input().split(" ")]
    A.add_row(row)

print "Determinent:", find_determinant(A)
