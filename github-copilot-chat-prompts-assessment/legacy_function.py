# Legacy function: Processes a CSV file of user data and returns a summary dictionary
# The code is intentionally messy and uses unclear variable names and logic

def proc_usr_dt(fnm):
    d = {}
    try:
        f = open(fnm, 'r')
        lns = f.readlines()
        f.close()
        for i in range(1, len(lns)):
            x = lns[i].strip().split(',')
            if len(x) < 3:
                continue
            nm = x[0]
            ag = x[1]
            ct = x[2]
            if ct not in d:
                d[ct] = {'cnt': 0, 'ages': []}
            d[ct]['cnt'] += 1
            try:
                d[ct]['ages'].append(int(ag))
            except:
                pass
    except Exception as e:
        print('err:', e)
    return d
