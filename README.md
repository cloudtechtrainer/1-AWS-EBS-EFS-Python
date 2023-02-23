# 1-EBS-EFS-Python
## Test a python program that uses files present in EBS and EFS
-(1) Launch a Amazon Linux EC2 Instance  
-(2) Create EBS Volume  
-(3) Attach the EBS volume to the running EC2 instance  
-(4) Run below commands to convert the EBS volume into a File system and then mount to directory in EC2 Instance  
“sudo file -s /dev/xvdf” - to check the volume type, if it returns 'Data', run below commands  
“sudo mkfs -t xfs /dev/xvdf” - to make file system out of volume  
“mount /dev/xvdf <new dir name>” - in the place new dir name, create a new directory and provide that  
-(5) Create input and output directories and place the input file in input directory  
-(6) Now create a new file 'test.py' and paste the python program from this directory  
-(7) Replace the path of input and output files based on the directries created  
-(8) Run the program and check the output  
