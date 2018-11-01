#!/usr/bin/python
import random
import Instruction
import xml.sax
import RandInstructionGen
#import TemplGen

#Create XML parser to read the ISA XML to populate the instruction set
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

#Create Instruction set object to hold instruction set
instructionSet = RandInstructionGen.InstructionSet()
parser.setContentHandler(instructionSet)
parser.parse("isa.xml")

#Initialize random generator
random.seed(10)

#Create random instruction generator
randInstructGen = RandInstructionGen.RandInstructionGen(instructionSet)
randInstructGen.read_config('defaultConfig.cfg')

#temp
randInstructGen.start_test_gen("test1.S")

#Create template generator
