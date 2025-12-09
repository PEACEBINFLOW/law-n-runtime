from lnre.core_vm import LNRE
from lnre.bytecode import Instruction


def test_vm_runs_noop():
    vm = LNRE()
    vm.load([Instruction(op="NOOP", args=[])])
    vm.run()
