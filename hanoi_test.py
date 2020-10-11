import os

import InputTXT as txt
import hanoi_graph as grapher

TEST_PREFIX = "[HTEST]: "
TEST_DIR = "tests_file"


def get_files_list(dirname):
    """ return relative path for test files ends with *.txt """
    res = []
    for file in os.listdir(dirname):
        if file.endswith(".txt"):
            res.append(os.path.join(dirname, file)) # print(os.path.join("/mydir", file))
    return res


def run_order_tests(tests):
    i = 0
    test_ok = 0
    test_error = 0

    for file in filelist:
        print(TEST_PREFIX + "Run test #{0} {1}".format(i,str(file)))
        i += 1

        # stage 1
        parser = txt.InputTXT()
        diskCount, column, diskCost, err = parser.ReadDisk(file)
        if err != 0:
            print(TEST_PREFIX + "FAIL")
            print(TEST_PREFIX + "ReadDisk" + str(file) + " -> errorcode " + str(err))
            test_error += 1
            continue

        order, sizeOrder, returnErr = parser.ReadOrder(file)
        if returnErr != 0:
            print(TEST_PREFIX + "FAIL")
            print(TEST_PREFIX + "ReadOrder" + str(file) + " -> errorcode " + str(err))
            test_error += 1
            continue

            # if returnErr == 0 and err == 0:
            #     graph = HanoiGraphOrder(diskCount, diskCost, order)
            #     graph.draw()

        print(TEST_PREFIX + "OK")
        test_ok += 1

    return test_ok, test_error


if __name__ == "__main__":
    print("*** HANOI TEST START ***")

    filelist = get_files_list(TEST_DIR)
    if filelist == []:
        print(TEST_PREFIX + "No files found!")
    else:
        ok, err = run_order_tests(filelist)
        print("TOTAL: {0} OK, {1} FAILED, {2} TESTED".format(ok,err,len(filelist)))
    
    print("*** HANOI TEST FINISHED ***")