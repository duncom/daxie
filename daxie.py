# -*- coding:UTF-8 -*-


#˼· �� �������������Ϊ�ַ��� ������λ��λ����� ��ʹ�ú��� �����ٴε���
#�����ͳһ�Խ������ȥ �� �Ż����ֱ��г�����ĸ������ һ���� ������  ������

def fourchar(s):
    res=''
    for i in range(0,len(s)):
        res=res+dict1[s[i]]+dict2[str(len(s)-i-1)]
    return res
#�ĸ��ַ�һ�����

def func(result):
    s1= result.replace("��Ǫ�����ʰ��","").replace("�����ʰ��","").replace("��ʰ��","")  
    s2= s1.replace("��Ǫ�����ʰ","��").replace("��Ǫ���","��").replace("�����ʰ","��")
    s3= s2.replace("��Ǫ","��").replace("���","��").replace("��ʰ","��").replace("����","��").replace("ʰ��","ʰ")
    return s3
#��ʽ���ַ��� 

def res(a):
    if (len(a)/4.0 >1):
        s=''
        t=''
        result=''
        s= a[:-4]
        t= a[-4:]
        result= fourchar(s)+"��"+fourchar(t)
    else:
        result= fourchar(a)
    return result
#��Ƭ���


dict1={"0":"��","1":"Ҽ","2":"��","3":"��","4":"��","5":"��","6":"½","7":"��","8":"��","9":"��"}
dict2={"0":"","1":"ʰ", "2":"��",  "3":"Ǫ" }

a=raw_input("please input a  number: ")

if (int(a) >0):
    print func(res(a)).decode("utf8")+u"Բ"
else:
    b=str(int(a)*(-1))
    print u"��"+func(res(b)).decode("utf8")+u"Բ"
     

#�����result �󣬴��������¼������
# "��Ǫ�����ʰ��"           ��
# "�����ʰ��"              ��    
# "��ʰ��"                 ��
# 
# "��Ǫ�����ʰ"             ��
# "��Ǫ���"                ��
# "�����ʰ"                ��
# 
# "��Ǫ"                   ��
# "���"                   ��
# "��ʰ"                   �� 
# "��" 
# "����"                 "��"
# "ʰ��"                 "ʰ"

