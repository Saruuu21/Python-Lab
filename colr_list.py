color_list1=set(input("Enter list1 colors(comma):").split(","))
color_list2=set(input("Enter list2 colors(comma):").split(","))
diff=color_list1 -color_list2
print("colors only in list1=",diff)
