import xml.etree.cElementTree as ET


def main():
    with open("E:\python_code\pipeline\practice1\cmd\\admin_proxy.xml", "rb") as f:
        byte_data = f.read()

    str_data = byte_data.decode("gb2312")
    root = ET.fromstring(str_data)
    print(root.tag, root.attrib)
    '''for child in root:#单层遍历
        print(child.tag, child.attrib)'''
    '''for service in root.iter('service'):#遍历根下面所有的某个子树
        print(service.tag, service.attrib)'''
    '''for one_worker_svcs in root.findall('one_worker_svcs'):#遍历当前元素直接子树
        rank = one_worker_svcs.find('rank').text
        name = one_worker_svcs.get('name')
        print(name, rank)'''


if __name__ == "__main__":
    main()
