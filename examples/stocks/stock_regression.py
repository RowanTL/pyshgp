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
import pandas as pd

from pyshgp.gp.estimators import PushEstimator
from pyshgp.gp.genome import GeneSpawner
from pyshgp.gp.selection import Lexicase
from pyshgp.push.instruction_set import InstructionSet

intc_data: pd.DataFrame = pd.read_csv("intc_data.csv")
y = intc_data["Open"].to_numpy().reshape([-1, 1])
X = np.arange(0, len(y)).reshape([-1, 1])

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
