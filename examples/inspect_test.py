from pyshgp.push.interpreter import InspectInterpreter
from pyshgp.push.config import PushConfig
from pyshgp.push.instruction_set import InstructionSet
from pyshgp.push.program import ProgramSignature, Program
from pyshgp.push.interpreter import InspectInterpreter

from tests.support import load_code, get_program

instruction_set = InstructionSet().register_core_by_stack({"int", "float", "bool", "string", "char", "code", "exec", "vector_int", "vector_float", "vector_bool", "vector_string", "vector_char"})

def print_program(name: str, sig: ProgramSignature, inputs = []) -> None:
    interpreter = InspectInterpreter(instruction_set)
    prog = get_program(name, sig, interpreter)
    states = interpreter.run(prog, inputs)
    
    for num, state in enumerate(states):
        print(f"{num}: {state}")

    return

"""
def example_test(push_config: PushConfig, instr_set: InstructionSet):
    name = "path/to/json"
    sig = ProgramSignature(arity=1, output_stacks=["float"], push_config=push_config)
"""

def test_program_relu_1(push_config: PushConfig):
    name = "relu_via_max"
    sig = ProgramSignature(arity=1, output_stacks=["float"], push_config=push_config)
    print_program(name, sig)

if __name__ == "__main__":
    test_program_relu_1(PushConfig())