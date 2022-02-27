str = "Statistic and Data Science course code is CSE303, This is Section 3 of CSE303 "
sub_str= "CSE303"

def count(s,sub):
    l=len(sub)
    count=0
    for i in range(len(s)-len(sub)+1):

        if(s[i:i+len(sub)] == sub ):
            count+=1
    return count

print("CSE303 Appeared ",count(str,sub_str),"Times")