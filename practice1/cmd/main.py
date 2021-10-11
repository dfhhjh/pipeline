import xml.etree.cElementTree as ET
import psutil

'''class Service_box:
    def __init__(self):
        Service_box.display = ""
        Service_box.bit64 = ""

def getservice_box(pname, service_box):
    n_service_box = Service_box()
    for ele in service_box:
        if ele.tag == 'name':
            n_service_box.display = ele.text
        elif ele.tag == 'price':
            n_service_box.bit64 = ele.text
    pname[n_service_box.display] = n_service_box
    return pname'''

def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid

def main():
    with open("E:\python_code\pipeline\practice1\cmd\\admin_proxy.xml", "rb") as f:
        byte_data = f.read()
    str_data = byte_data.decode("gb2312")
    root = ET.fromstring(str_data)
    pname = []
    for service_box in root.iter('service_box'):  # 遍历根下面所有的某个子树
        at = service_box.attrib.get("display")
        pname.append(at)
    for i in pname:
        if isinstance(checkprocess(i), int):
                print("进程存在")
        else:
                print("进程不存在")

if __name__ == "__main__":
    main()