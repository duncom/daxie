# -*- coding:UTF-8 -*-


#Ë¼Â· £º ½«ÊäÈëµÄÊý×Ö×÷Îª×Ö·û´® ½øÐÐËÄÎ»ËÄÎ»µÄÊä³ö £¬Ê¹ÓÃº¯Êý ·½±ãÔÙ´Îµ÷ÓÃ
#Êä³öºó£¬Í³Ò»¶Ô½á¹û½øÐÐÈ¥ Áã ÓÅ»¯£¬·Ö±ðÁÐ³öÊä³öµÄ¸÷ÖÖÇé¿ö Ò»¸öÁã Á½¸öÁã  Èý¸öÁã

def fourchar(s):
    res=''
    for i in range(0,len(s)):
        res=res+dict1[s[i]]+dict2[str(len(s)-i-1)]
    return res
#ËÄ¸ö×Ö·ûÒ»´ÎÊä³ö

def func(result):
    s1= result.replace("ÁãÇªÁã°ÛÁãÊ°Áã","").replace("Áã°ÛÁãÊ°Áã","").replace("ÁãÊ°Áã","")  
    s2= s1.replace("ÁãÇªÁã°ÛÁãÊ°","Áã").replace("ÁãÇªÁã°Û","Áã").replace("Áã°ÛÁãÊ°","Áã")
    s3= s2.replace("ÁãÇª","Áã").replace("Áã°Û","Áã").replace("ÁãÊ°","Áã").replace("ÁãÍò","Íò").replace("Ê°Áã","Ê°")
    return s3
#¸ñÊ½»¯×Ö·û´® 

def res(a):
    if (len(a)/4.0 >1):
        s=''
        t=''
        result=''
        s= a[:-4]
        t= a[-4:]
        result= fourchar(s)+"Íò"+fourchar(t)
    else:
        result= fourchar(a)
    return result
#·ÖÆ¬Êä³ö


dict1={"0":"Áã","1":"Ò¼","2":"·¡","3":"Èþ","4":"ËÁ","5":"Îé","6":"Â½","7":"Æâ","8":"°Æ","9":"¾Á"}
dict2={"0":"","1":"Ê°", "2":"°Û",  "3":"Çª" }

a=raw_input("please input a  number: ")

if (int(a) >0):
    print func(res(a)).decode("utf8")+u"Ô²"
else:
    b=str(int(a)*(-1))
    print u"¸º"+func(res(b)).decode("utf8")+u"Ô²"
   

#è¾“å…¥ï¼š10102302   
#å£¹ä»Ÿé›¶å£¹æ‹¾ä¸‡è´°ä»Ÿåä½°é›¶è´°åœ†


#Êä³öÍêresult ºó£¬´óÖÂÓÐÒÔÏÂ¼¸ÖÖÇé¿ö
# "ÁãÇªÁã°ÛÁãÊ°Áã"           ¿Õ
# "Áã°ÛÁãÊ°Áã"              ¿Õ    
# "ÁãÊ°Áã"                 ¿Õ
# 
# "ÁãÇªÁã°ÛÁãÊ°"             Áã
# "ÁãÇªÁã°Û"                Áã
# "Áã°ÛÁãÊ°"                Áã
# 
# "ÁãÇª"                   Áã
# "Áã°Û"                   Áã
# "ÁãÊ°"                   Áã 
# "Áã" 
# "ÁãÍò"                 "Íò"
# "Ê°Áã"                 "Ê°"

