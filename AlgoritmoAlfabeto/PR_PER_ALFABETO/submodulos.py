from datetime import datetime


from re import X


def GetHashLevel1(cadena):
    Alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','0','1','2','3','4','5','6','7','8','9']
    caden1=(cadena.upper())
    hashx=[]

    for n in caden1:
        print(n)
        for j in Alfabeto:
            if n == j:
                hashx.append(Alfabeto.index(j))
    return hashx

def GetHashLevel2(Cadena):
    dt = datetime.now()
    ts = int(datetime.timestamp(dt))
    Matrix=[[['A','B','C'],['D','E','F'],['G','H','I']],
            [['J','K','L'],['M','N','Ñ'],['O','P','Q']],
            [['R','S','T'],['U','V','W'],['X','Y','Z',' ']],
            [['0','1','2'],['3','4','5'],['6','7','8','9']]]
    MatrixFinal=Matrix

    MatrixAux=[]
    contador=0
    limite_filas=3
    limite_columnas=4
    for i in [0,1,2,3]:
        for n in str(ts):
            #el valor que va a cambiar
            #print("imprimiendo ts:",ts)
            #print("imprimiendo n:",n)
            circleindex= int(n)%limite_filas
            MatrixAux=Matrix[i][circleindex]
            Matrix[i][circleindex]=Matrix[i][contador]   
            Matrix[i][contador]=MatrixAux
            contador=(contador+1)%limite_filas

    for i in [0,1,2]:
        for j in str(ts):
            circleindex= int(n)%limite_columnas
            MatrixAux=Matrix[circleindex][i]
            Matrix[circleindex][i]=Matrix[contador][i]   
            Matrix[contador][i]=MatrixAux
            contador=(contador+1)%limite_columnas
    Matrix_resultante=[]




    for i in Matrix:
        #print(i)
        for j in i:
            #print(j)
            for t in j:
                #print(t)
                Matrix_resultante.append(t)

    return Matrix_resultante
