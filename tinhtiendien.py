def caculatePrice(loaiDien, soDien):
    if soDien < 0:
        return 'input error'
    if loaiDien == 'sinh hoat':
        if soDien < 50:
            return soDien * 1500
        elif soDien <= 200:
            return soDien * 2000
        elif soDien <= 400:
            return soDien * 2500
        else:
            return soDien * 3500
    elif loaiDien == 'kinh doanh':
        if soDien < 100:
            return soDien * 1800 
        elif soDien < 330:
            return soDien * 2400
        elif soDien <= 400:
            return soDien * 3100
        else: return soDien * 3300
    else:
        return "input error"
