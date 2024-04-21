import os as os
from os import path as ph
#需要合并的文件名
conbine_file=["capacitors.yml","categories.yml","generators.yml","geo-resources.yml","items.yml","machines.yml","material-generators.yml","mob-drops.yml","researches.yml","solar-generators.yml"]
#需要合并的文件夹名
conbine_dict=["saveditems"]
#需要合并的文件夹
#按顺序写在下面
source_dic=["海曼","逻辑工艺"]



for j in conbine_file:
    with open(j,"w") as f:
        f.truncate()
        f.close
for j in conbine_dict:
    filelist=os.listdir(j)
    for i in filelist:
        os.remove(ph.join(j,i))
        
for i in source_dic:
    for j in conbine_file:
        content=""
        try:
            with open(ph.join(i,j),"r",encoding="utf-8") as f:
                content=f.read()
                f.close()
        except:
            print("{} in {} not found\n".format(j ,i))
        with open(j,"a",encoding="utf-8") as f:
            f.write(content)
            f.write("\n")
    for j in conbine_dict:
        try:
            filelist=os.listdir(ph.join(i,j))
        except:
            print("{} in {} not found\n".format(j ,i))
            continue
        print(filelist)
        for k in filelist:
            content=""
            with open(ph.join(i,j,k),"r",encoding="utf-8") as f:
                content=f.read()
                f.close()
            with open(ph.join(j,k),"w",encoding="utf-8") as f:
                f.write(content)
                f.write("\n")
                
        
