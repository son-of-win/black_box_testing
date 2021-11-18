def caculatePrice(loaiDien, soDien):
    tienDien = 0
    if soDien < 0:
        return 'input error'
    if loaiDien == 'sinh hoat':
        if soDien < 50:
            tienDien =  soDien * 1500
        elif soDien <= 200:
            tienDien =  soDien * 2000
        elif soDien <= 400:
            tienDien =  soDien * 2500
        else:
            tienDien =  soDien * 3500
    elif loaiDien == 'kinh doanh':
        if soDien < 100:
            tienDien =  soDien * 1800 
        elif soDien < 330:
            tienDien =  soDien * 2400
        elif soDien <= 400:
            tienDien =  soDien * 3100
        else: tienDien =  soDien * 3300
    
    return tienDien
