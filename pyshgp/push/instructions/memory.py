"""
Definitions for all memory instructions.

A sigmoid function is applied to the writing aspect
of these functions. 
"""


from pyshgp.push.type_library import PushTypeLibrary
from pyshgp.push.instruction import MemoryInstruction
from math import tanh

def sigmoid(num: float) -> float:
    return 1 / (1 + abs(num))

def _mem_write(index, value, memory_arr):
    idx = int(abs(index) % len(memory_arr))
    ret_val = memory_arr[idx]
    memory_arr[idx] = tanh(value)
    return ret_val,

def _mem_read(index, memory_arr):
    idx = int(abs(index) % len(memory_arr))
    ret_val = memory_arr[idx]
    return ret_val,

def _mem_add(index, value, memory_arr):
    idx = int(abs(index) % len(memory_arr))
    # return the value in memory prior to
    # updating it as specified by
    # agapitos2016
    ret_val = memory_arr[idx]
    new_val = memory_arr[idx] + value
    memory_arr[idx] = tanh(new_val)
    return ret_val,

def _mem_mult(index, value, memory_arr):
    idx = int(abs(index) % len(memory_arr))
    ret_val = memory_arr[idx]
    new_val = memory_arr[idx] * value
    memory_arr[idx] = tanh(new_val)
    return ret_val,

def instructions(type_library: PushTypeLibrary):
    """
    These are numeric types to tell the
    MemoryInterpreter whether to push to the
    stack or not.
    """
    i = []

    # for push_type in ["int", "float"]:
    """for push_type in ["float"]:
        i.append(MemoryInstruction(
            f"mem_{push_type}_add",
            _mem_add,
            input_stacks=[push_type, push_type],
            output_stacks=[push_type],
            code_blocks=0,
            docstring="Returns original value of index, then adds the float stored at index" 
        ))

        i.append(MemoryInstruction(
            f"mem_{push_type}_mult",
            _mem_mult,
            input_stacks=[push_type, push_type],
            output_stacks=[push_type],
            code_blocks=0,
            docstring="Returns original value of index, then multiplies the float stored at index" 
        ))

        i.append(MemoryInstruction(
            f"mem_write_{push_type}",
            _mem_write,
            input_stacks=[push_type, push_type],
            output_stacks=[push_type],
            code_blocks=0,
            docstring=f"Writes a variable to memory and pushes the overwritten value to the {push_type} stack"
        ))

        i.append(MemoryInstruction(
            f"mem_read_{push_type}",
            _mem_read,
            input_stacks=[push_type],
            output_stacks=[push_type],
            code_blocks=0,
            docstring=f"Reads in a variable from memory and places it in {push_type} stack"
        ))"""

    return i
