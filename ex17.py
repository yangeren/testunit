#from sys import argv
#from os.path import exists
#script, from_file, to_file = argv
#print "Copying from %s to %s" % (from_file, to_file)
## we could do these tow on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
#print "The input file is %d bytes long" % len(indata)
#print "Does the output file exists? %r " %exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to above."
#raw_input()
#out_file = open(to_file,"a")
#out_file.write(indata)
#print "Alright, all done."
#out_file.close()
#in_file.close()



a = raw_input("filename")
b = raw_input("filename again")
#c = open(a).read()
open(b,"a").write(open(a).read())

print len(open(b).read())