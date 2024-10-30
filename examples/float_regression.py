"""The ReLU function is a common activation function used in artifical neural netoworks.

```
relu(x) = max(0, x)
```

The Leaky ReLU function is a variant of the ReLU function designed to avoid
having nodes "die". Its definition is as follows.

```
leaky_relu(x) = max(0.1x, x)
```

This problem attempts to synthesize a program that computes the output of both
the ReLU and LeakyReLU functions.

"""
import numpy as np
import random

from pyshgp.gp.estimators import PushEstimator
from pyshgp.gp.genome import GeneSpawner
from pyshgp.gp.selection import Lexicase
from pyshgp.push.instruction_set import InstructionSet


# def target_function(x: float) -> (float, float):
    # """Generate a training data point."""
    # return max(0.0, x), max(0.1 * x, x)

def target_function(x: float) -> float:
    return (x ** 2) + (x / 3) - 0.5,


X = np.arange(-5.0, 5.0, 0.5).reshape([-1, 1])
y = np.array([target_function(x[0]) for x in X])

instruction_set = InstructionSet()
desired_instructions=[
    "float_add",
    "float_mult",
    "float_sub",
    "float_div",
    "mem_float_add",
    "mem_float_mult"
]

for instruction in desired_instructions:
    instruction_set.register_core_by_name(instruction)

spawner = GeneSpawner(
    n_inputs=1,
    # instruction_set=InstructionSet().register_core_by_stack({"float"}),
    instruction_set=instruction_set,
    literals=[],
    erc_generators=[
        # lambda: float(random.randint(0, 10)),
        lambda: round(random.uniform(0, 5), 1),
    ]
)


ep_lex_sel = Lexicase(epsilon=True)


if __name__ == "__main__":
    est = PushEstimator(
        population_size=300,
        max_generations=50,
        simplification_steps=500,
        spawner=spawner,
        selector=ep_lex_sel,
        verbose=2,
        memory_size=10
    )

    est.fit(X=X, y=y)
