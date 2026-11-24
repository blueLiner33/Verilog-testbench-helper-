from read_write import write_file

def main_file_write(filedata, **kwargs):
    output_file = "tb_" + kwargs.get('filename')
    test_bench_add = ""
    
    for key, value in kwargs.items():
        print(f"this is the key {key}, this is the value {value}")

    if kwargs.get('tb_add'):
        test_bench_add = "_tb"
        
    if not (kwargs.get('output_file')):
        output_file = kwargs.get('output_file') + '.sv'
        
    if kwargs.get('time'):
        write_file(output_file, f"`timescale {kwargs.get('time')} / {kwargs.get('precision')}\n")

    print(filedata)
    write_file(output_file, f"module {output_file.replace(".sv","")}();\n")

    for value in filedata:
        spot_one = value.find("input")
        spot_two = value.find("output")

        if spot_one != -1 or spot_two != -1:

            #make sure that it pulls the right word and the whole word
            start = value.find("logic")
            ends = []

            comma_end = value.find(",", start)
            len_end = len(value)
            
            if comma_end != -1:
                ends.append(comma_end)
            if len_end != -1:
                ends.append(len_end)
            
            name = value[start:min(ends)] + test_bench_add + ";\n"
            write_file(output_file, "\t" + name)

    write_file(output_file, "\n")

    if kwargs.get('testcases'):
        write_file(output_file, "\tint num_tests;\n")
        write_file(output_file, "\tint num_passed;\n")
        
    
def main():
    pass

if __name__ == "__init__":
    main()