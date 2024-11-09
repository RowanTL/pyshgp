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
import random
import pandas as pd
import numpy as np

from pyshgp.gp.estimators import PushEstimator
from pyshgp.gp.genome import GeneSpawner
from pyshgp.gp.selection import Lexicase
from pyshgp.push.instruction_set import InstructionSet
from pyshgp.push.interpreter import PushInterpreter, MemoryInterpreter

sliding_window_size: int = 50

btc_usd_data: pd.DataFrame = pd.read_csv("/home/user/Documents/CS6401/pyshgp/examples/stocks/btc_usd_data.csv")
btc_usd_data.drop(["Dividends", "Stock Splits", "Date"], inplace=True, axis=1)
X: list[list[int]] = []
y: list[int] = []
for num in range(0, len(btc_usd_data) - sliding_window_size - 1):
    X.append([])
    for row in btc_usd_data[num:(num+sliding_window_size)].itertuples():
        X[num].append(row.Open)
        X[num].append(row.Close)
        X[num].append(row.High)
        X[num].append(row.Low)
        X[num].append(row.Volume)
        y.append(btc_usd_data["Close"][num+sliding_window_size+1])

y = np.array(y).reshape(-1, 1)

#inputs = btc_usd_data["Close"].to_numpy()[:-1]
#outputs = btc_usd_data["Close"].to_numpy()[1:]
#y = outputs.reshape([-1, 1])
#X = inputs.reshape([-1, 1])
# y = intc_data["Open"].to_numpy().reshape([-1, 1])
# X = np.arange(0, len(y)).reshape([-1, 1])

instruction_set = InstructionSet()
desired_instructions=[
    "float_add",
    "float_mult",
    "float_sub",
    "float_div",
    "mem_float_add",
    "mem_float_mult",
    "mem_write_float",
    "mem_read_float",
    "float_mod",
    "float_max",
    "float_dec",
    "float_sin",
    "float_cos",
    "float_tan"
]

for instruction in desired_instructions:
    instruction_set.register_core_by_name(instruction)

def random_float() -> float:
    return float(random.randint(-10, 10))

spawner = GeneSpawner(
    n_inputs=1,
    # instruction_set=InstructionSet().register_core_by_stack({"float"}),
    instruction_set=instruction_set,
    literals=[],
    erc_generators=[
        # lambda: float(random.randint(0, 10)),
        #lambda: float(random.randint(-10, 10)),
        random_float,
    ]
)


ep_lex_sel = Lexicase(epsilon=True)
interpreter: MemoryInterpreter = MemoryInterpreter(memory_size=10 , dementia_amt=60)


if __name__ == "__main__":
    est = PushEstimator(
        population_size=300,
        max_generations=100,
        simplification_steps=500,
        spawner=spawner,
        selector=ep_lex_sel,
        verbose=2,
        #memory_size=10,
        interpreter=interpreter,
        #passed_dementia_amt=20,
        parallelism=True,
    )

    est.fit(X=X, y=y)
