import re


def formatting(date: str):

    char_pattern = r'[a-zA-Z]*[-._:\s/]*'
    char = re.findall(char_pattern, date)
    print("char:", char)
    
    if char:
        for x in char:
            date = date.replace(x, "")
        
    print("date:", date)
        
    d = date[0:2]
    m = date[2:4]
    y = date[-2:] 

    formatted_date = d + "." + m + "." + y
    return formatted_date