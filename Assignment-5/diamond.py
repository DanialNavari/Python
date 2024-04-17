#diamond size
diamond_len = int(input("Enter Diamond Size: "))

#total stars of little diameter
total_star = diamond_len * 2

#increase stars
for i in range(1,diamond_len + 1):
    star_number = ((2*i)-1)
    show_star = '*' * star_number
    space = ' ' * int((total_star - star_number)/2)
    print(space,show_star,space)

#decrease stars
for i in range(1,diamond_len):
    star_number -= 2
    show_star = '*' * star_number
    space = ' ' * int((total_star - star_number)/2)
    print(space,show_star,space)