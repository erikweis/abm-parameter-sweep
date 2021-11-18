# abm-parameter-sweep
 
For running parameter sweeps on a simulation object, such as an agent-based model.

Your model class should extend the package `Simulation` object, and implement three required classes:
1. `foldername`: a @property method that returns the directory name where files should be saved. This implicitly assures that all simulations can be passed an argument dirname for the purposes of saving data
2. `run_simulation`: a method that takes no arguments and runs the desired calculations
3. `on_finish`: this is where the attribute `dirname` can be used to save files to the directory created for this purpose.

The following example class implements this properly:

```
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

    def __str__(self):
        return "Test object"
```

We can run this simulation with the following code

```
from parameter_sweep import Experiment, Simulation

e = Experiment(
    MyClass,
    folder_name = 'experiment1',
    a = [1,2,3,4,5],
    b = 'i',
    c = [0.1,0.2,0.3,0.4]
)

e.run_all_trials()
```

## Installation

To install, clone this repository, navigate to the folder abm-parameter-sweep 
in your terminal and run `pip install -e .`.