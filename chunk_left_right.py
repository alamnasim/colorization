from pydub import AudioSegment
import glob
import os
import subprocess
import sys
import os.path

def main(dir_path): 
    file_list = []
    list1 = []
    set1 = set()
    count1=count2=0
    for original_file_name in glob.glob(os.path.join(dir_path + "/*.wav")):
        file_list.append(original_file_name)
    # print(file_list)
    start = 0
    #end = 300
    count = 0
    for ind, original_file_name in enumerate(file_list[start:]):
        # count=+1
        print(original_file_name)
        print(ind)
        if not os.path.exists('/'.join(original_file_name.split('/')[:-1])+'_left_right'):
            os.makedirs('/'.join(original_file_name.split('/')[:-1])+'_left_right')
        #print()
        new_file_name_left = '/'.join(original_file_name.split('/')[:-1])+'_left_right' + '/' + "l_"+original_file_name.split("/")[-1]
        new_file_name_right = '/'.join(original_file_name.split('/')[:-1])+'_left_right' + '/' + "r_"+original_file_name.split("/")[-1]

        #print(new_file_name)
        if not os.path.isfile(new_file_name_left) and not os.path.isfile(new_file_name_right):
        #if not os.path.exists(new_file_name):
            print(new_file_name_left)
            print(new_file_name_right)
            extract_command_left = ["sox", original_file_name, new_file_name_left, "remix", "1"]
            extract_command_right = ["sox", original_file_name, new_file_name_right, "remix", "2"]
            subprocess.run(extract_command_left)
            subprocess.run(extract_command_right)
            #print(type(extract_command))
            count1+=1
            print(count1)
        else:
            count2+=1
            continue
    print(count1)
    print(count2)
    print("total skipped:",count2)
    # #def main(original_file_name):
if __name__ == "__main__":
   main(sys.argv[1])
   # main()
