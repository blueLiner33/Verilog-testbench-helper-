from read_write import read_file
from file_writer import main_file_write
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog="vtbc",
        description="Adds basic verilog test bench information"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    
    parser.add_argument(
        "filename",
        help="Input file to process"
    )
    
    parser.add_argument(
        "--tbn",
        action="store_true",
        help="adds tb to every variable"
    )
    
    parser.add_argument(
        "--output", "-o",
        default = True,
        help="Specify the output filename default tb_(your file name). Auto adds the file extension .sv"
    )

    parser.add_argument(
        "--time", "-t",
        default = False,
        help="Adds time_unit varibles the value following it is what time scale. It requires a time scale to be choosen, possible options s, ms, us, ns, ps, or fs. Has to have number infront of choose."
    )

    parser.add_argument(
        "--precision", "-p",
        default = "1ns",
        help="Adds precision varibles the value following it is what precision for time. Possible options s, ms, us, ps, or fs"
    )

    parser.add_argument(
        "--testc", "-tc",
        action="store_true",
        help="Adds variables for testcases"
    )

    return parser.parse_args()

def main():
    args = parse_args()
    file_data = read_file(str(args.filename))
    main_file_write(file_data, filename = args.filename,
                    tb_add = args.tbn, output_file = args.output,
                    time = args.time,
                    precision = args.precision,
                    testcases = args.testc)
    
if __name__ == "__main__":
    main()