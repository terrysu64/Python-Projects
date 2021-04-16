#Name: Terry Su
#Date: Dec 28, 2020
#Purpose: Python questions taken from LeetCode to try during the winter 2020-2021

#Date: Jan 7, 2021
#Valid Sudoku
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self,board):

        false_count = 0

        #check rows
        for row in board:
            
            for index1, element in enumerate(row):
                
                for index2, other in enumerate(row):
                    if element == other and index1 != index2 and element != '.':
                        false_count += 1

        #check columns
        column_list = []
        
        for x in range(0,9):
            
            for column in range(0,9):
                column_list.append(board[column][x])
                
            for index1, element in enumerate(column_list):
                
                for index2, other in enumerate(column_list):
                    if element == other and index1 != index2 and element != '.':
                        false_count += 1
            column_list = [] 

        #check each box

        box_list = []
            
        #first column of boxes
        for box_num in [0,3,6]:
            
            for x in range(box_num, box_num + 3):
            
                for y in range(0,3):
                    box_list.append(board[x][y])

            for index1, element in enumerate(box_list):
                
                for index2, other in enumerate(box_list):
                    if element == other and index1 != index2 and element != '.':
                        false_count += 1

            box_list = []

        #second column of boxes
        for box_num in [0,3,6]:
            
            for x in range(box_num, box_num + 3):
            
                for y in range(3,6):
                    box_list.append(board[x][y])
            

            for index1, element in enumerate(box_list):
                
                for index2, other in enumerate(box_list):
                    if element == other and index1 != index2 and element != '.':
                        false_count += 1

            box_list = []

        #third column of boxes
        for box_num in [0,3,6]:
            
            for x in range(box_num, box_num + 3):
            
                for y in range(6,9):
                    box_list.append(board[x][y])
            

            for index1, element in enumerate(box_list):
                
                for index2, other in enumerate(box_list):
                    if element == other and index1 != index2 and element != '.':
                        false_count += 1

            box_list = []
        

        if false_count > 0:
            return False

        else:
            return True

#Date: Jan 9, 2021
#Two sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
        
def twoSum(nums,target):

    Lanswer = []

    #a simple iteration over the list to check for target sum
    for index1, integer1 in enumerate(nums):
        for index2, integer2, in enumerate(nums):

            if len(Lanswer) == 0 and integer1 + integer2 == target and index1 != index2:
                Lanswer.append(index1)
                Lanswer.append(index2)

    return Lanswer

#Date: Jan 9, 2021

#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        
def removeDuplicates(nums):

    #a simple iteration over the list to check for iterations
    ans = []
    for x in nums:
            
        if x not in ans:
            ans.append(x)

    return len(ans), ans

#Date January 11, 2021

#Given a 32-bit signed integer, reverse digits of an integer.

#Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
#For this problem, assume that your function returns 0 when the reversed integer overflows.

def reverse(x):

    #condition
    if x < -2 ** 31 or x > (2**31) - 1:
        return 0

    elif x == 0:
        return 0

    elif len(str(x)) == 1:
        return x

    #initialize

    store_p = []
    store_n = ['-']
    ans = ''

    #appending backwards into list as string and summing up
    #conversion to string then back to integer
    
    x = str(x)

    if int(x) > 0:
        for a in range(len(x)):
            store_p.append(x[len(x) - a - 1: len(x) - a])

        for y in store_p:
            ans += y
        ans = int(ans)

        return ans


    else:
        for a in range(len(x) - 1):
            store_n.append(x[len(x) - a - 1: len(x) - a])

        for y in store_n:
            ans += y
        ans = int(ans)

        return ans
    #a cool alternate function 'list[<start>:<stop>:<step>]'
    #(ex: a = '1234',
    #a[::-1]
    #'4321')

#Date: January 12, 2021

#Given n pairs of parentheses, write a function to
#generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    #choices: ( or )
    #constraints: must start with ( and end with )
    #goal: to end up generateing with ocount and ccount == 0 (no more characters to use)

    res = []
        
    def inner(curr,l,r):
    #curr is the current state of the 'possibility' we are working on
    #l is number of '(' we have left
    #r is number of ')' we have left
            
        # if current string hit n*2 then stop (the 'possibility' has been completed)
        
        if len(curr) == n*2:
            res.append(curr)
            return
            
        #branching out curr with left parens added until no more remaining
        
        if l>0:
            inner(curr+"(", l-1, r)
                
        #branching curr with right parens added if a left matches it and there are remaining
            
        if r>0 and r>l: #second condition is if the number of ( placed > number of ) placed
            inner(curr+")", l, r-1)
                    
    inner("",n,n)
    return res

#Date: Feburary 28, 2021

#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def isPalindrome(x):
    x = str(x)
    reverse = x[-1::-1] #use slice notation to reverse input; start from index -1 and step backwards by one at a time till the start

    if x == reverse:
        return True

    else:
        return False
    
#Date: March 4, 2021

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:

#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.

def isValid(s):
    #strategy: remove all the  () [] and {}, if theres still something left after, then its false

    while True:
        
        first = s.find('()')

        if first != -1:
            s = s.replace(s[first:first+2], '', 1)

        second = s.find('[]')

        if second != -1:
            s = s.replace(s[second:second+2], '', 1)

        third = s.find('{}')

        if third != -1:
            s = s.replace(s[third:third+2], '', 1)

        if first == -1 and second == -1 and third == -1:
            break

        print(s)

    if len(s) == 0:
        return True

    else: 
        return False
    
#Alternative through stacking: check for 'first in first out' (better time complexity)

def isValid2(s):
    dic = {'(':')', '[':']', '{':'}'}
    current = []

    for y in range(0,len(s)): #scan each character of the string at a time
        
        if s[y:y+1] in dic: #if its an open bracket add it to array
            current.append(s[y:y+1])

        else: #if its a closed bracket

            if len(current) == 0: #if it matches nothing at all, string is invalid
                return False

            elif s[y:y+1] == dic[current[-1]]: #if it matches most recent open bracket
                current.pop()

            else: #if it doesnt match most recent open bracket, string is invalid
                return False

    if len(current) == 0:
        return True

#Date: March 6, 2021

#Given an array 'nums' and a value 'val',
#remove all instances of that value in-place and return the new length.
        
def removeElement(nums,val):
    
    while nums.count(val) != 0: #track how many elements in nums still = val
        nums.remove(val) #remove the elements that = val

    return len(nums)

#Date: March 6, 2020

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):
    #append the new version entirely to the tail of the original. Then remove the original
    leng = len(matrix) 
    current = []
    count = 0
    
    for x in range(0,leng):
        
        for y in range(1,leng + 1):
            current.append(matrix[(y+count) * -1][x]) #its y + count because there will be new parts of the new matrix(final objective) tailgating the original one

        count += 1

        matrix.append(current)
        current = []

    for x in range(0,leng):
        matrix.pop(0)

    return

#Date: March 8, 2021

#Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):

    #use sliding window/2 pointer method
    
    longest = 0
    start = 0
    seen = {}

    for end, char in enumerate(s): #END pointer consistently moves forward by 1 index at a time

        if char in seen and seen[char] >= start: #if character has been seen AND has its last occurence in front of the START pointer, 
            start = seen[char] + 1               #then move START pointer to one index in front of it

        seen[char] = end #continue updating characters and most recent index
        longest = max(longest, end - start + 1) #continue compare current longest substring length with pointer distance

    return longest

#Date: March 14, 2021

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

def findMedianSortedArrays(nums1,nums2):
    #join the two arrays together then keep removing min and max values till we acheive the median

    nums1 += nums2

    while len(nums1) > 2:
        nums1.remove(max(nums1))
        nums1.remove(min(nums1))

    if len(nums1) == 1:
        return nums1[0]

    else:
        return (nums1[0] + nums1[1]) / 2

#Date: April 3, 2021
#Alternative solution: join and sort two lists, then use length of list to determine median (better time complexity)

def findMedianSortedArrays2(nums1,nums2):

    nums1 = sorted(nums1 + nums2)

    if len(nums1) % 2 == 0:
        return (nums1[(len(nums1) // 2) - 1] + nums1[(len(nums1) // 2)]) / 2

    else:
        return nums1[(len(nums1) // 2)]

#Date: April 11, 2021

#Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):
    #loop through the center of the possible palidrome (an index in s or two adjacent indices) and expand out.
    
    ans = ''

    for index in range(0,len(s)): #for each index, expand from the index AND from the index+next index (i.e something like expanding from "bb" for a palindrome "abba")
        
        curr = expand(s,index,index)
        if len(curr) > len(ans):
            ans = curr

        if index < len(s) - 1:
            curr = expand(s,index,index+1)
            
            if len(curr) > len(ans):
                ans = curr
                
    return ans

def expand(s,left,right): #function to call on, expands outwards from given index(s) while the substring is a valid palindrome

    curr = ''

    while left >= 0 and right < len(s) and s[left:right+1] == s[left:right+1][::-1]:

        if len(s[left:right+1]) > len(curr):
            curr = s[left:right+1]

        left -=1
        right += 1

    return curr

#Date: April 12, 2021
#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

#The algorithm for myAtoi(string s) is as follows:

#1. Read in and ignore any leading whitespace.

#2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
#   This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.

#3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.

#4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
#   If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

#5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
#   Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

#6. Return the integer as the final result.

def myAtoi(s):
    sign = True #sign value of integer (True = +ve, False = -ve)
    ints = ['0','1','2','3','4','5','6','7','8','9']
    start = 0
    end = 0
    count = 0
    
    s = s.strip() #1

    if s[0:1] == '-': #2
        sign = False
        s = s[1:]
        
    elif s[0:1] == '+':
            s = s[1:]


    while s[end:end+1] in ints: #3
        end += 1
    s = s[start:end]


    while s[count:count+1] == '0': #4,5
        count += 1
    s = s[count:]

    if s != '':
        s = int(s)

        if sign == False:
            s = s * -1

    else:
        s = 0

    if s > (2**31) - 1: #clamping s within range if out of range
        s = (2**31) - 1

    elif s < -1 * (2**31):
        s = -1 * (2**31)

    return s #6

#Date: April 16, 2021
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    #compare prefixes through checking one character at a time
    
    longest = ''
    count = 1
        
    if strs == [] or '' in strs:
        return ''            
        
    else:
        while all(sub[:count] == strs[0][:count] for sub in strs) == True and count <= min([len(s) for s in strs]): #stop checking when prefix stops matching
            count += 1                                                                                              #or when length of shortest string is exceeded

        return strs[0][:count-1]

    
    
