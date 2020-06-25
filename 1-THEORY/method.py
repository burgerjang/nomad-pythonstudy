#!/usr/bin/python3

def get_num():
    nums=[]
    str_num=""
    str_num2=""
    res = 0
    expr=list(raw_input('Calculate  '))
    
#    math_expression = {
#        'plus': lambda a,b: a+b,
#        'minus': lambda a,b: a-b,
#        'multiple': lambda a,b: a*b,
#        'divide': lambda a,b: a/b,
#        'mod': lambda a,b: a%b,
#        'pow': lambda a,b: a**b
#    }

    for i in expr:
        nums.append(i)

    if nums[0] == "-":
        for ele in nums:
            str_num += ele
        return int(str_num)
    else:
        for ele in range(len(nums)):
            if nums[ele] == "+" or nums[ele] == "-" or nums[ele] == "*" or nums[ele] == '/' or nums[ele] == "%":
                if nums[ele+1] == "*":
                    for tmp in range(ele):
                        str_num += nums[tmp]
                    in_1=int(str_num)

                    for tmp2 in range(ele+2,len(nums)):
                        str_num2 += nums[tmp2]
                    in_2=int(str_num2)
                    res = in_1**in_2
                else:
                    for tmp in range(ele):
                        str_num += nums[tmp]
                    in_1=int(str_num)

                    for tmp2 in range(ele+1,len(nums)):
                        str_num2 += nums[tmp2]
                    in_2=int(str_num2)

                    if nums[ele] == "+":
#                        res = math_expression['plus']
                        res = in_1+in_2
                    elif nums[ele] == "-":
#                        res = math_expression['minus']
                        res = in_1-in_2
                    elif nums[ele] == "*":
#                        res = math_expression['multiple']
                        res = in_1*in_2
                    elif nums[ele] == "/":
#                        res = math_expression['divide']
                        res = in_1/in_2
                    elif nums[ele] == '%':
#                        res = math_expression['mod']
                        res = in_1%in_2
                return res
def main():
    print("result = %s"%get_num())

main()
