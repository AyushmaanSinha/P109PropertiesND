import csv
import statistics
import pandas as pd

df = pd.read_csv("Python\P109PropertiesND\StudentsPerformance.csv")
read_list = df["reading score"].tolist()
write_list = df["writing score"].tolist()

#finding the Mean
rmean = statistics.mean(read_list)
wmean = statistics.mean(write_list)

#median
rmedian = statistics.median(read_list)
wmedian = statistics.median(write_list)

#mode
rmode = statistics.mode(read_list)
wmode = statistics.mode(write_list)

#Standard Deviation
rstd_deviation = statistics.stdev(read_list)
wstd_deviation = statistics.stdev(write_list)

print("Mean, Median, Mode & Standard Deviation of Height is {}, {}, {}, {}".format(rmean, rmedian, rmode, rstd_deviation))
print("Mean, Median, Mode & Standard Deviation of Weight is {}, {}, {}, {}".format(wmean, wmedian, wmode, wstd_deviation))
print("")

#Calculation
#Height
r1_std_dev_start, r1_std_dev_end = rmean - rstd_deviation , rmean + rstd_deviation 
r2_std_dev_start, r2_std_dev_end = rmean - (2*rstd_deviation) , rmean + (2*rstd_deviation) 
r3_std_dev_start, r3_std_dev_end = rmean - (3*rstd_deviation) , rmean + (3*rstd_deviation)

#Weight
w1_std_dev_start, w1_std_dev_end = wmean - wstd_deviation , wmean + wstd_deviation 
w2_std_dev_start, w2_std_dev_end = wmean - (2*wstd_deviation) , wmean + (2*wstd_deviation) 
w3_std_dev_start, w3_std_dev_end = wmean - (3*wstd_deviation) , wmean + (3*wstd_deviation)

#Percentage for Height
rlistdata_1_stddev = [result for result in read_list if result > r1_std_dev_start and result < r1_std_dev_end]
rlistdata_2_stddev = [result for result in read_list if result > r2_std_dev_start and result < r2_std_dev_end]
rlistdata_3_stddev = [result for result in read_list if result > r3_std_dev_start and result < r3_std_dev_end]

print("{} % of data for Height in 1st Standard Deviation".format(len(rlistdata_1_stddev)*100.0/len(read_list)))
print("{} % of data for Height in 2nd Standard Deviation".format(len(rlistdata_2_stddev)*100.0/len(read_list)))
print("{} % of data for Height in 3rd Standard Deviation".format(len(rlistdata_3_stddev)*100.0/len(read_list)))
print("")

#Percentage for Weight
wlistdata_1_stddev = [result for result in write_list if result > w1_std_dev_start and result < w1_std_dev_end]
wlistdata_2_stddev = [result for result in write_list if result > w2_std_dev_start and result < w2_std_dev_end]
wlistdata_3_stddev = [result for result in write_list if result > w3_std_dev_start and result < w3_std_dev_end]


print("{} % of data for Weight in 1st Standard Deviation".format(len(wlistdata_1_stddev)*100.0/len(write_list)))
print("{} % of data for Weight in 2nd Standard Deviation".format(len(wlistdata_2_stddev)*100.0/len(write_list)))
print("{} % of data for Weight in 3rd Standard Deviation".format(len(wlistdata_3_stddev)*100.0/len(write_list)))
print("")

print("We can conclude that the Mean, Median & Mode are almost same in case of Standard Deviation")
print("68% Data lies in 1st, 95% in 2nd and 99% in 3rd Standard Deviations")