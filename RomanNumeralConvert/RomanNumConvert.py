#Given a string representing a Roman numeral, write a function to compute the Arabic numerical equivalent. For example roman_to_arabic("MDCCLXXVI") should return 1776.

#Numbers only repeat <= 3 times
#Only 4 and 9 based numbers are written with subtraction
def roman_to_arabic_num(numeral):
    dict = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            }

    #Check that numeral is a valid string
    if ((not isinstance(numeral,str)) or (len(numeral)==0)):
        return 0
    #if single numeral, return it
    if (len(numeral)==1):
        return dict.get(numeral[0])

    prev = dict.get(numeral[0])
    curr = 0
    ret=prev
    #loop through string and calculate
    for x in range(1,len(numeral)):
        curr = dict.get(numeral[x])
        if (prev >= curr):
            ret+=curr
        else:
            ret+= curr-prev-prev
        prev = curr
    return ret


#Write a generic function to compute various scenarios for the following optimization problem:
#A farmer owns X acres of land. She profits P1 dollars per acre of corn and P2 dollars per acre of oats.
#Her team has Y hours of labor available.
#The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre. How many acres of each can be planted to maximize profits?

#P1= corn profit/acre
#P2= oat profit/acre
#H1= corn labor/acre
#H2 = oat labor/acre

#corn profit = P1*H1
#Oat profit = P2*H2
#X =
#Y= H1*z + H2*z2
#X =Total acres
#Y=Total labor

#def max_profit(X,Y,P1,P2,H1,H2):
