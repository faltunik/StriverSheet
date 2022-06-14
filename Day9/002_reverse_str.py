# https://www.codingninjas.com/codestudio/problems/reverse-words_696444?topList=striver-sde-sheet-problems
# very easy

# bruteforce
def reverseString(st):
	#Write your code here.
    s = st.split()
    return " ".join(s[::-1])

# optimization
# above solution takes
# o(n) space, and is cpu intesive code

# we can travel through the string(in reverse order, and keep putting word)