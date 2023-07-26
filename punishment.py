def do_punishment(first_part, second_part, nb_lines):
    if (nb_lines == 0) : 
        return ""
    a = first_part.rstrip()
    a = a.strip()
    b = second_part.strip()
    b = b.rstrip()
    if b.endswith("."):
         return (a +" "+b+" ")*(nb_lines -1) + (a + " "+ b)
    else :
        return (a+ " "+b +"."+" ")*(nb_lines-1) + (a+" "+b +".")
   
