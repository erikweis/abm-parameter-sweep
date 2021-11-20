
from .simulation import Simulation

import itertools
from typing import Iterable
import os
import json
import random
import shutil

class Experiment:

    def __init__(self,
        simulation_class: Simulation,
        folder_name = None,
        random_proportion = 1,
        iterations_per_grid_point = 1, 
        **kwargs):

        #validate simulation class
        if not issubclass(simulation_class,Simulation):
            raise TypeError("The input simulation_class should extend `Simulation`")
        self.simulation_class = simulation_class

        #create folder if not provided
        i = 0
        if not folder_name:
            while os.path.isdir(f'experiment_{i}'):
                i += 1
            folder_name = f'experiment_{i}'

        #establish directory
        self.dirname = os.path.join(os.getcwd(),folder_name)
        if not os.path.isdir(self.dirname):
            os.mkdir(self.dirname)
        else:
            print(f"Folder with this experiment name already exists at {self.dirname}.")
            if input("Would you like to override all files in this folder? (y or n)").lower() == 'y':
                shutil.rmtree(self.dirname)
                os.mkdir(self.dirname)

        self.trials_setup(kwargs,random_proportion)
        self.save_trials_index()


    def trials_setup(self,kwargs,random_proportion,iterations_per_grid_point):
        
        params = list(kwargs.keys())
        list_of_values = list(kwargs.values())

        assert all(isinstance(i,Iterable) for i in list_of_values)
        assert all(isinstance(i,str) for i in params)

        self.possible_trials = [{param:val for param, val in zip(params,trial)} \
            for trial in itertools.product(*list_of_values)]

        #select trials
        num_trials = int(random_proportion*len(self.possible_trials))
        trials = random.sample(self.possible_trials,num_trials)
        self.trials = [t for _ in range(iterations_per_grid_point) for t in trials]
        

    def _run_trial(self, trial_dir, trial_params):

        sim = self.simulation_class(dirname=trial_dir,**trial_params)
        sim.run_simulation()
        sim.on_finish()

    def run_all_trials(self,debug = False):

        for i,trial_params in enumerate(self.trials):
            trial_dir = os.path.join(self.dirname,f"trial_{i}")
            os.mkdir(trial_dir)

            if debug:
                self._run_trial(trial_dir,trial_params)
            else:
                try:
                    self._run_trial(trial_dir,trial_params)
                except Exception as exception:
                    if debug:
                        print(exception)
                    print("Error Running Simulation with the following params:")
                    for k,v in trial_params.items():
                        print(f"{k}: {v}")

                trial_params['id']=i


    def save_trials_index(self):

        filename = os.path.join(self.dirname,'trials.jsonl')
        with open(filename,'w') as f:
            for trial in self.trials:
                f.writelines(json.dumps(trial)+"\n")

