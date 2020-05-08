# username = input('Your username ')
# Email = input('your email ')
# password = input('choose a suitable password ')
# fullname = input('what is your fullname? ')

f = open("staff.txt",'w')
staffDetails = str("1." )+str("Tara, Taradebby@gmail.com, Taradee, Omotara Kuds \n")
f.write(staffDetails)

f = open("staff.txt",'a')
staffDetails2 = str("2. " )+str("korede, korede419@gmail.com, smarter, Korede Ibukunoluwa")
f.write(staffDetails2)
f.close()

f = open("customer.txt", "w")
