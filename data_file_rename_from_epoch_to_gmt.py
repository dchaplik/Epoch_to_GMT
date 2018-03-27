from os import rename, listdir
import time, re, shutil

def new_file_name(working_file_name, newtm):
#	print ('working file name, new time: '), working_file_name, newtm
	print ('')
	final_name=working_file_name[0:12]+newtm+'gmt'+'.txt'
#        print working_file_name /t+ final_name
	shutil.copy2(working_file_name, final_name)



fnames=listdir('.')

for fname in fnames:
	input_file_name=fname
#	print ('Print original file name: '), input_file_name+'\n'	
	epoch_gmt_part=re.match(r'(acu_logdata)_(\S+).(txt)$', input_file_name);
	if epoch_gmt_part:
		epocht = epoch_gmt_part.group(2)
		outtm = time.gmtime(float(epocht))
		newtm=time.strftime('%Y-%m-%d'+'_'+'%H:%M:%S', outtm)
		data_file=input_file_name
#		print newtm, data_file
		new_file_name(data_file, newtm)
	else:
		print ('No match')
new_file_name(data_file, newtm)


