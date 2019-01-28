import architecture
import experiment
import numpy as np
import csv 

def main():
    # init architecture from model
    services = architecture.new('architecture_model.json').microservices

    # generate experiments
    actions = ["delay","abort"]
    experiments = []
    for ms in services:
        for op in ms.operations:
            for action in actions:
                experiments.append(experiment.Experiment(op,action))
    print("Total experiments: " + repr(len(experiments)))
    

    ## prepare csv file with count 0 for each experiment
    with open("experiments.csv", "w") as f:
        writer = csv.writer(f)
        for exp in experiments:
            line = exp.row()
            line.append(str(0))
            writer.writerow(line)


    # randomly select experiments and count in csv
    i = 0
    print("Starting selection ...")
    while i < 1000:
        index = np.random.randint(0,len(experiments))
        experiments[index].countcsv("experiments.csv")
        i = i+1
    print("Finished selection. See experiments.csv for results")

    
    

if __name__ == "__main__":
    main()