import Data,Schedule,department,population,GeneticAlgorithm
test = Data.data()
Popu=population.Population(3,test)
list=Popu.get_schedules()

test2=GeneticAlgorithm.GenticAlgo(list)
test2.loopuntilnumber(0)




