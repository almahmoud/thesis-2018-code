import random
import math
import sys
import re

args = sys.argv

template = "template.js"
arb_tot = 9
arb = 6
arb2 = 1


if "-h" in args or len(args) < 2:
	print "Navon v0.1"
	print "\nThis script will generate the qualtrics code with the specified parameters and save it to the speciied filename."
	print "\n\nMandatory Parameters:\nThese parameters are mandatory for the script to run."
	print "     -b block-number"
	print "         is the number of the currentBlock"
	print "     -o \"filename.js\""
	print "         points to the relative path of the file to create to write the resulting javascript file."
	print "     -t [E,G,L]"
	print "         indicates the block type. Can be either e for even, G for global-leaning, or L for local-leaning."
	print "     -n total-number"
	print "         indicates the total number of tasks per block. Ratio will be 75:25 for uneven blocks."
	print "\n\nOptional Parameters:\nThese parameters are optional, with respective default values if not specified."
	print "     -i"
	print "         indicates whether instructions should be printed (default = omit)"
	print "     -p 3000"
	print "         specifies the number of milliseconds to wait before the beginning of task when the instructions are ommitted (default = 3000)"
	print "     -d"
	print "         indicates different letters to be used (for the end of task)"
	print "     -orderGL G,L,G,L,G,L,"
	print "         optional ordering of global/local blocks. Partial orders can also be assigned, using R for randomized letters."

else:
	if "-b" not in args:
		print "ERROR: Block Number not specified. Use -b to specify block number. Use -h for help."
	else:
		b = args.index("-b") + 1
		block_number = str(args[b])

	if "-t" not in args:
		print "ERROR: Block Type not specified. Use -t [E,G,L] to specify block type. Use -h for help."
	else:
		t = args.index("-t") + 1
		block_type = str(args[t])

	if "-n" not in args:
		print "ERROR: Block count not specified. Use -n to specify the total number of trials per block. Use -h for help."
	else:
		n = args.index("-n") + 1
		total = int(args[n])

	if "-o" not in args:
		print "ERROR: Output filename not specified. Use -o filename.js to specify an output filename. Use -h for help."
	else:
		o = args.index("-o") + 1
		output_file = str(args[o])

	if "-i" in args:
		instr = "true"
	else:
		instr = "false"

	if "-d" in args:
		pool = "2"
	else:
		pool = "1"

	if "-p" in args:
		p = args.index("-p") + 1
		pause = str(args[p])
	else:
		pause = "3000"

	orderI = []
	limitG = 0
	limitL = 0

	if 'e' in block_type or 'E' in block_type:
		dom = [0,1]
		limitG = int(math.floor(total/2))
		limitL = int(math.ceil(total/2))

	elif 'g' in block_type or 'G' in block_type:
		dom = [1]
		limitG = int(math.floor(0.75*total))
		limitL = int(math.ceil(0.25*total))

	elif 'l' in block_type or 'L' in block_type:
		dom = [0]
		limitG = int(math.ceil(0.25*total))
		limitL = int(math.floor(0.75*total))

	current_g = limitG
	current_l = limitL

	if "-orderGL" in args:
		orderGL = args.index("-orderGL") + 1
		list_order = str(args[orderGL]).split(",")
		countG = 0
		countL = 0
		for each in list_order:
			if 'G' in each or 'g' in each:
				countG += 1
			if 'L' in each or 'l' in each:
				countL += 1
		for each in list_order:
			if ('G' in each or 'g' in each) and total > 0 and current_g > 0 :
				countG = countG - 1
				orderI.append(1)
				current_g = current_g - 1
				total = total - 1
			elif ('L' in each or 'l' in each)  and total > 0 and current_l > 0:
				countL = countL - 1
				orderI.append(0)
				current_l = current_l - 1
				total = total - 1
			elif total > 0:
				y = random.randint(0,1)
				x = random.randint(0,arb_tot)
				if y not in dom and len(orderI) > 1 and y == orderI[-2]:
					if x > arb:
						y = (y + 1) % 2
				if y not in dom and len(orderI) > 0 and y == orderI[-1]:
					if x > arb2:
						y = (y + 1) % 2
				if y is 0 and (current_l - countL) > 0:
					current_l = current_l - 1
					total = total - 1
					orderI.append(0)
				elif y is 1 and (current_g - countG) > 0:
					current_g = current_g - 1
					total = total - 1
					orderI.append(1)

	while total > 0:
		y = random.randint(0,1)
		x = random.randint(0,arb_tot)
		if y not in dom and len(orderI) > 1 and y == orderI[-2]:
			if x > arb:
				y = (y + 1) % 2
		if y not in dom and len(orderI) > 0 and y == orderI[-1]:
			if x > arb2:
				y = (y + 1) % 2
		if y is 0 and current_l > 0:
			current_l = current_l - 1
			total = total - 1
			orderI.append(0)
		elif y is 1 and current_g > 0:
			current_g = current_g - 1
			total = total - 1
			orderI.append(1)

	orderN = []
	nums = [0,1,2,3]

	total = int(limitG + limitL)

	for x in range(0,total):
		if len(nums) == 1:
			nums = [0,1,2,3]
		y = random.randint(0,3)
		while y not in nums or (len(orderN) > 0 and orderN[-1] == y) or (len(orderN) > 1 and ((y < 2 and orderN[-1] < 2 and orderN[-2] < 2) or (y >= 2 and orderN[-1] >= 2 and orderN[-2] >= 2))):
			nums = [0,1,2,3]
			y = random.randint(0,3)
		nums.remove(y)
		orderN.append(y)

	limitG = str(limitG)
	limitL = str(limitL)

	final_orderI = []
	final_orderN = []

	for eachNum in orderI:
		final_orderI.append(str(eachNum))
	for eachNum in orderN:
		final_orderN.append(str(eachNum))

	in_template = ["###instr###", "###pause###", "###orderi###", "###ordern###", "###block_number###", "###limitl###", "###limitg###",  "###pool###"]
	to_replace = [instr, pause, "["+ ",".join(final_orderI) + "]", "["+ ",".join(final_orderN) + "]", block_number, limitL, limitG, pool]
	new_lines = []
	with open(template, 'r') as original:
		lines = original.readlines()
		for line in lines:
			match = re.search(r'(###\w+###)', line)
			if match:
				current = str(match.group(1))
				if current not in in_template:
					print "INTERNAL ERROR IN TEMPLATE REPLACEMENT"
				else:
					ind = in_template.index(current)
					new_lines.append(line.replace(current,to_replace[ind]))
			else:
				new_lines.append(line)

	with open(output_file, 'w') as out:
		out.write("".join(new_lines))

