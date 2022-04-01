def cont_empresaNF(Nota_fiscal, empresa):
    cont = 0
    for emp in Nota_fiscal:
        if 'Rod_Raff' in emp.values() != False:
            cont += 1
    nf = cont
    return nf
