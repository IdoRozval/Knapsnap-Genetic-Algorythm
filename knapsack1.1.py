from random import randint

def chromosom():
    chromosom = [randint(0,1) for j in range(5)]
    return validate(chromosom)
                
def population(size):
    return [chromosom() for j in range(size)]

def validate(chromosom):
    totalweight = 0
    for i in range(len(chromosom)):
        if chromosom[i] == 1:
            if items[i][1] + totalweight < 16:
                totalweight += items[i][1]
            else:
                chromosom[i] = 0
    return chromosom
    
def get_population(population):
    st = ""
    for chromosom in population:
        st = st + str(chromosom) + " " + str(get_fitness(chromosom)) + "\n" 
    return st[:-1]

def get_fitness(chromosom):
    fitness = 0
    for i in range(len(chromosom)):
        if chromosom[i] == 1:
            fitness += items[i][0]
    return fitness

def choose_parents(population):
    """
    return a list containing the indexs of the chosen parents for mating
    """
    chosen_index = []
    total = sum([get_fitness(chromosom) for chromosom in population])
    while len(chosen_index) != 5:
        partial = randint(0,total)
        for i in range(len(population)):
            partial += get_fitness(population[i])
            if partial > total and i not in chosen_index:
                chosen_index.append(i)
                break
    return chosen_index

def crossover(parents):
    """
    returns new offsprings drieved from the gived parents
    """
    offsprings = []
    for i in range(len(parents)/2):
        crosspoint = randint(1,4)
        base = parents[i][:crosspoint]
        base.extend(parents[i+1][crosspoint:])
        offsprings.append(validate(base))
        base = parents[i][crosspoint:]
        base.extend(parents[i+1][:crosspoint])
        offsprings.append(validate(base))
    return offsprings  
        
def mutation(offsprings):
    """
    switch one beat and validate offspring
    """
    for i in range(len(offsprings)):
        if 0 < randint(1,100) < 11:
            index = randint(0,4)
            if offsprings[i][index] == 0:
                offsprings[i][index] = 1
            else:
                offsprings[i][index] = 0
            offsprings[i] = validate(offsprings[i])
    return offsprings
                
def regenerate(population,offsprings):
    """
    switch the least fitness individuals in the population with the new offsprings
    """
    population = sorted(population, key = lambda x: get_fitness(x))
    for i in range(len(offsprings)):
        population[i] = offsprings[i]
    return population
    
    
            

        
        
        
    
    
    
        
        
items = {0:[10,4],1:[4,12],2:[1,1],3:[2,1],4:[2,2]}   
pool = population(10)
counter = 10
finest = 0


while counter > 0:
    indexs = choose_parents(pool) # choosing the best parents
    offsprings = crossover([pool[index] for index in indexs]) # mating...
    offsprings = mutation(offsprings) # nobody's perfect
    pool = regenerate(pool,offsprings) # introducing offsprings to the pool

    current = max([get_fitness(chromosom) for chromosom in pool])
    if current > finest:
        counter = 10
        finest = current
    else:
        counter -= 1
        
best = sorted(pool,key = lambda x: get_fitness(x))[-1]
print best, get_fitness(best)















