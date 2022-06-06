def help(mat, r, c):
    nval = mat[0][0]
    i = 0,
    j=1
    while j <c:
        tmp = mat[i][j]
        mat[i][j] = nval
        nval = tmp
        j +=1
    j -=1
    while i<r:
        tmp = mat[i][j]
        mat[i][j] = nval
        nval = tmp
        i +=1
    i -=1
    while j>=0:
        tmp = mat[i][j]
        mat[i][j] = nval
        nval = tmp
        j -=1
    j +=1
    while i>=0:
        tmp = mat[i][j]
        mat[i][j] = nval
        nval = tmp
        i -=1
    #return 

    while 0<=i<r and 0<=j<c:
        tmp = mat[i][j]
        mat[i][j] = nval
        nval = tmp
        if j<c: j+=1
        elif i<r: i+=1

            

