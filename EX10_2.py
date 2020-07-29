import numpy as np
vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])
vec2 = (np.pi/4) * vec1
vec2 = np.cos( vec2 )
vec3 = vec1 + 2 * vec2
vec4=mat1*vec3
print("Multipy mat1 by vec3 is:", vec4)
result=vec4
transposed=mat1.transpose(1,0)
print("mat1 transpose is:" ,transposed)
determine=np.linalg.det(mat1)
print("Determinant of mat1 is:", determine)
trace = mat1.trace()
print("trace of mat1 is", trace)
minvec=np.min(vec1)
print("minimum value of vec1 is ", minvec)
j=np.where ( minvec ==vec1)
print("j is:", j)
minmat=np.min(mat1)
print("minimum mat 1 ", minmat)

A=np.array([[17, 24, 1, 8, 15],
[23, 5, 7, 14, 16],
[ 4, 6, 13, 20, 22],
[10, 12, 19, 21, 3],
[11, 18, 25, 2, 9]])
sax1=np.sum(A,axis=-1)
sax2=np.sum(A,axis=-2)
sdia=A.diagonal()
sdia=np.sum(sdia)
sodia=np.fliplr(A)
sodia=sodia.diagonal()
sodia=np.sum(sodia)
if np.min(sax1)==np.max(sax1)== np.min(sax2)==np.max(sax2)==sdia==sodia :
    print ('This is a magic matrix')
else:
    print('Not a magic matrix')
M=np.random.rand(10,10)
print('10*10 matrix filled with random values:\n',M)
MUL=M[:5,:5]
print("MUL", MUL)
MUR=M[:5,5:10]
print("MUR", MUR)
MLL=M[5:10,:5]
print("MLL", MLL)
MLR=M[5:10,5:10]
print("MLR", MLR)

