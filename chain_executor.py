import os
import qpso_rcpsp as prog
import sys

"""
	Python scipt for automatic execution of QPSO program
	on multiple files.
"""


n = 32		# just change this and rest is automatic
prog.n = n
m = n-2

def reset_globals():
	prog.pred_list = []
	prog.succ_list = []
	prog.duration = []
	prog.res_req_list = []
	prog.max_resources = []

	prog.n = n
	prog.m = n-2 
	# Global bests
	prog.gBest_pos = [0 for x in range(0, n)]
	prog.gBest_vel = [0 for x in range(0, n)]
	prog.gBest_cost = sys.maxint
	prog.best_solution = []

	for i in range(0, n):
	    prog.pred_list.append([])
	    prog.succ_list.append([])
	    prog.res_req_list.append([])
	    prog.duration.append(0)
	prog.particles = [prog.Particles() for x in range(0, m)]
    
#list of optimals
optimals = []
def parseOptimals(filename):
    f = open(filename)
    i = 1
    for line in f:
        if i in range(23,503):
            numbers = map(float, line.split())
            optimals.append(numbers[2])
        i = i+1    




if __name__ == '__main__':

	#parsing the given optimal values
	parseOptimals("j30opt.sm")
	print optimals
	reset_globals()
	folder_name = 'j%d' % (n-2)
	os.chdir(os.path.join("/home/yash/Desktop/Work/Projects/QPSOinRCPSP/Dataset/%s.sm"%folder_name))   

	sd = 0

	u = 1
	while u<49:
		l = 1
		while l<11:
			filename = "j%d%d_%d.sm" % (n-2,u,l)
			print "Running on file: ", filename, " Time: ",
			answer = prog.execute_on_file(filename)
			optimal_ans = optimals[(u-1)*10 + l-1]
			a = (1.0*(answer - optimal_ans))/optimal_ans
			print "SD = ",a
			sd = sd+a
			reset_globals()
			l = l+1
		u = u+1	 
		print sd 
	print "final sd/50: ",sd/480 