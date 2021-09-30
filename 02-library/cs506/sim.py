def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    dis = 0
    for i in range(len(x)):
        dis += abs(x[i]-y[i])

    return dis

def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(set(x)) + len(set(y))) - intersection
    if union == 0:
        return "undefine"
    else: 
        return float(intersection) / union

def cosine_sim(x, y):
    
    inner = 0
    x_sum = 0
    y_sum = 0 

    for i in range(len(x)):
        inner += x[i]*y[i]
        x_sum += (x[i])**2
        y_sum += (y[i])**2
    
    x_sum = x_sum**(1/2)
    y_sum = y_sum**(1/2)
    prod = x_sum * y_sum


    if prod == 0:
        return "undefined"
    else: 
        return inner/(prod)


# Feel free to add more
