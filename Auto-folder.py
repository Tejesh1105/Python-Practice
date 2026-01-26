import os

if(not os.path.exists("Devops')):
    os.mkdir("Devops")                  

for mk_folder in range(0, 100):
      os.mkdir(f"Devops/logfile{mk_folder+1}")
