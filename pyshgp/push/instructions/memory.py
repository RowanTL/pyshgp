"""Definitions for all memory instructions."""


from pyshgp.push.type_library import PushTypeLibrary
from pyshgp.push.instruction import SimpleInstruction, MemoryInstruction
from pyshgp.utils import Token
from pyshgp.push.instructions.numeric import _add, _mult
from pyshgp.push.accessible import memory_arr

def _mem_write(index, value):
    idx = int(abs(index % len(memory_arr)))
    try:
        ret_val = memory_arr[idx]
    except Exception as e:
        pass
    memory_arr[idx] = value
    return ret_val,

def _mem_read(index):
    idx = int(abs(index % len(memory_arr)))
    try:
        ret_val = memory_arr[idx]
    except Exception as e:
        pass    
    return memory_arr[idx],

def _mem_add(index, value):
    idx = int(abs(index % len(memory_arr)))
    # return the value in memory prior to
    # updating it as specified by
    # agapitos2016
    try:
        ret_val = memory_arr[idx]
    except Exception as e:
        pass
    memory_arr[idx] = memory_arr[idx] + value
    return ret_val,

def _mem_mult(index, value):
    idx = int(abs(index % len(memory_arr)))
    try:
        ret_val = memory_arr[idx]
    except Exception as e:
        pass   
    memory_arr[idx] = memory_arr[idx] * value
    return ret_val,

def instructions(type_library: PushTypeLibrary):
    """
    These are numeric types to tell the
    MemoryInterpreter whether to push to the
    stack or not.
    """
    i = []

    # for push_type in ["int", "float"]:
    for push_type in ["float"]:
        i.append(MemoryInstruction(
            f"mem_{push_type}_add",
            _mem_add,
            input_stacks=[push_type, push_type],
            output_stacks=[push_type],
            code_blocks=0,
            docstring="C"
        ))

        i.append(MemoryInstruction(
            f"mem_{push_type}_mult",
            _mem_mult,
            input_stacks=[push_type, push_type],
            output_stacks=[push_type],
            code_blocks=0,
            docstring="Calls numeric _mult but with some memory shenanigans in MemoryInterpreter"             
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
        ))

    return i
