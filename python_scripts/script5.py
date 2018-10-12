
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

batch="2015"
semester="VI"
branch="CS"


driver = webdriver.Firefox()
driver.get('http://14.139.205.172/web_new/Default.aspx')
#time.sleep(5)

result=[]


for roll in range(1,94):
    #if(roll==8):
    #    continue;
    try:
        elem=driver.find_element_by_id('txtRegno')
        elem.clear()
        if(len(str(roll))==1):
            r = "00" + str(roll)
        else:
            r = "0" + str(roll)
        elem.send_keys(batch+"UG"+branch+r)
        driver.find_element_by_id('btnimgShow').click();
        driver.find_element_by_xpath("//select[@name='ddlSemester']/option[text()='"+semester+"']").click()
        driver.find_element_by_id('btnimgShowResult').click()
        name=driver.find_element_by_id('lblStudentName').text
        SG=driver.find_element_by_id('lblSPI').text
        CG=driver.find_element_by_id('lblCPI').text
        stud=[name,SG,CG]
        result.append(stud)
    except Exception:
        driver.get('http://14.139.205.172/web_new/Default.aspx')

driver.quit()


result_SG=sorted(result,key=lambda x:x[1], reverse=True)
result_CG=sorted(result,key=lambda x:x[2], reverse=True)

file_sg=open(batch+"_"+branch+"_"+semester+"_"+"sorted_by_SG.tsv",'w')

file_sg.write("Rank,Name,SG,CG\n");
for i in range(len(result_SG)):
    file_sg.write(str(i+1)+"\t"+str(result_SG[i][0])+"\t"+str(result_SG[i][1])+"\t"+str(result_SG[i][2])+"\n")


file_cg=open(batch+"_"+branch+"_"+semester+"_"+'sorted_by_CG.tsv','w')

file_cg.write("Rank,Name,SG,CG\n");
for i in range(len(result_CG)):
    file_cg.write(str(i+1)+"\t"+str(result_CG[i][0])+"\t"+str(result_CG[i][1])+"\t"+str(result_CG[i][2])+"\n")
file_sg.close()
file_cg.close()
