# Copyright 2017 Lijun Xiao ljxiao@bu.edu

import unittest
import subprocess
import time

AUTHORS = ['ljxiao@bu.edu']

PROGRAM_TO_TEST = "collisionc_27"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=0.5)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)

def time_correction(a):
    return a.replace(".0000","")

class CollisionTestCase(unittest.TestCase):
    "empty class - write this"

    def test0(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith('col'),"wrong program name")

    def test1(self):
        strin = "one 0 0 1 1"
        correct_out = "1\none 1 1 1 1\n2\none 2 2 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2","1"],strin)
        out = time_correction(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test2(self):
        strin = "one 11111111 0 0 0\ntwo 0 0 0 0"
        correct_out = "1\none 11111111 0 0 0\ntwo 0 0 0 0\n11111111\none 11111111 0 0 0\ntwo 0 0 0 0\n" 
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1","11111111"],strin)
        out = time_correction(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test3(self):
        strin = "one 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0"       
        correct_out = "999999\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['999999'],strin)
        out = time_correction(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test4(self):
        strin = "one 0 0 0 0\n\n"
        correct_out = ""     
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        out = time_correction(out)
        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test5(self):
        strin = "one two three 0"
        correct_out = ""     
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test6(self):
        strin = "one 0 0       "
        correct_out = ""     
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test7(self):
        strin = "one 0 0 0 0"
        correct_out = ""     
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["lkgkhj"],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
 

    
    def test8(self):
        strin = "one 20 0 8 9\ntwo 90 90 -43 -42\nthree 23 32 -9 -8"
        correct_out = "7\none 76 63 8 9\ntwo -14.503104 -185.16121 -6.0796705 -38.46033\nthree -236.4969 -42.838788 -45.92033 -11.53967\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["7"],strin)
        out = time_correction(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test9(self):
        strin = "one 20 0 9 0\ntwo 80 0 -10 0\nthree 70 0 10 0"
        correct_out = "2\none 38 0 9 0\ntwo 80 0 10 0\nthree 70 0 -10 0\n8\none 0 0 -10 0\ntwo 140 0 10 0\nthree 102 0 9 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["8","2"],strin)
        out = time_correction(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

def main():
    "show how to use runprogram"

    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()
