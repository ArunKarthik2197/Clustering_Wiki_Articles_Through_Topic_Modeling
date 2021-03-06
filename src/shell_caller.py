import os
import sys
import re


preprocessed_folder_name = 'preprocessed/'
results_folder_name = 'results/'
strat=None

pwd = os.getcwd()
pwd = os.path.abspath("..")

preprocessed_folder = os.path.join(pwd,preprocessed_folder_name)
results_folder = os.path.join(pwd,results_folder_name)

print("cwd before: "+os.getcwd()+"\n")
if(len(sys.argv) == 2):
    strat = sys.argv[1]
    
else:
    print("not enough args\n")

if strat == 'preprocessed':
    os.chdir(preprocessed_folder)
    pwd2 = os.getcwd()
    os.system("sh file_concat-graph.sh")
    print("Done concatenating files in preprocessed folder\n")
elif strat == 'results':
    
    os.chdir(results_folder)
    pwd2 = os.getcwd()
    print(pwd2)
    dirs = next(os.walk("."))
    print("dirs:"+str(dirs))
    dirs = dirs[1]
    print("cwd after: "+os.getcwd()+"\n")
    cnt =0
    
    if not os.path.exists(os.path.join(results_folder, 'pic_clustering_final_results/')):
        os.mkdir(os.path.join(results_folder, 'pic_clustering_final_results/'))
        
    for x in dirs:
        if x.startswith("clusters_"):
            
            os.chdir(results_folder+x)
            os.system("sh ../file_concat-results.sh")
            os.chdir(results_folder)
            cnt+=1
    print("Done\n")
else:
    print("Invalid argument\n")
    sys.exit()
