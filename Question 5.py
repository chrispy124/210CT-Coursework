MATRIX

    MatrixAdd[M1, M2]
        NMatrix <-- [[0,0],[0,0]]
        FOR I IN RANGE [LENGTH[M1]]
            FOR J IN RANGE(LENGTH(M2))
                NMatrix <-- M1+M2
            RETURN NMatrix

    MaxrixSub[M1,M2]
        NMatrix <-- [[0,0],[0,0]]
        FOR I IN RANGE [LENGTH[M1]]
            FOR J IN RANGE [LENGTH[M2]]
                NMatrix <-- M1-M2
            RETURN NMatrix

    MatrixMulti[M1,M2]
        NMatrix <--[[0,0],[0,0]]
        FOR I IN RANGE [LENGTH[M1]]
            FOR J IN RANGE[LENGTH[M2]]
                NMatrix <--M1*M2
            RETURN NMatrix

        1Matrix <-- [4,2],[5,7]
        2Matrix <-- [3,3],[8,9]
    
