
import itertools
from typing import Iterable
import os
import json
import random

class Experiment:

    def __init__(self,
        folder_name,
        random_proportion = 1,
        **kwargs):

        #establish directory
        self.dirname = os.path.join(os.getcwd(),folder_name)
        if not os.path.isdir(self.dirname):
            os.mkdir(self.dirname)
        else:
            print(f"Folder with this experiment name already exists at {self.dirname}.")
            if input("Would you like to override all files in this folder?").lower() != 'y':
                exit()

        #param setup
        params = list(kwargs.keys())
        list_of_values = list(kwargs.values())

        assert all(isinstance(i,Iterable) for i in list_of_values)
        assert all(isinstance(i,str) for i in params)

        self.possible_trials = [{param:val for param, val in zip(params,trial)} \
            for trial in itertools.product(*list_of_values)]

        #select trials
        num_trials = int(random_proportion*len(self.possible_trials))
        self.trials = random.sample(self.possible_trials,num_trials)

        #add index val
        for i, trial_params in enumerate(self.trials):
            trial_params['id']=i

    def save_trials_index(self):

        filename = os.path.join(self.dirname,'trials.jsonl')
        with open(filename,'w') as f:
            for trial in self.trials:
                f.writelines(json.dumps(trial)+"\n")


if __name__ == "__main__":

    e = Experiment(
        folder_name = 'experiment1',
        a = [1,2,3,4,5],
        b = ['i','j'],
        c = [0.1,0.2,0.3,0.4]
    )

    e.save_trials_index()