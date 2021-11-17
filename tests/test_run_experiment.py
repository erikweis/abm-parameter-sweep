from parameter_sweep import Experiment, Simulation
import os
import shutil

class MyClass(Simulation):

    def __init__(self,dirname,a=None, b=None,c=None):
        self._dirname = dirname

    @property
    def dirname(self):
        return self._dirname

    def run_simulation(self):
        pass

    def on_finish(self):
        fname = os.path.join(self.dirname,'test.txt')
        with open(fname,'w') as f:
            f.write("hello")


def test_run_experiment():

    if os.path.isdir('experiment1'):
        shutil.rmtree('experiment1')

    e = Experiment(
        MyClass,
        folder_name = 'experiment1',
        a = [1,2,3,4,5],
        b = 'i',
        c = [0.1,0.2,0.3,0.4]
    )
    e.run_all_trials()


    assert os.path.isdir('experiment1')
    assert os.path.isfile('experiment1/trials.jsonl')
    for i in range(len(e.trials)):
        assert os.path.isdir(f'experiment1/trial_{i}')