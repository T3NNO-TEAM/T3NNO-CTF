from hashid import HashID

def hash_checker(hash: str) -> list:
    algo_list = []

    hash_class = HashID()

    result = hash_class.identifyHash(hash)
    limit = 0
    
    for algo in result:
        limit += 1
        if limit == 3+1:
            break
        
        algo_list.append(algo.name.replace("-", ""))
        
    return algo_list
