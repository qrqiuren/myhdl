import os

from myhdl import Cosimulation

cmd = "iverilog -o bin2gray -Dwidth=%s " + \
      "../../test/verilog/bin2gray.v " + \
      "../../test/verilog/dut_bin2gray.v "
      
def bin2gray(B, G, width):
    os.system(cmd % width)
    return Cosimulation("vvp -m ../myhdl.vpi bin2gray", B=B, G=G)
               

    