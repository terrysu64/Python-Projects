#Name: Terry Su 
#Date: Dec 28, 2020
#Purpose: My leetcode journey

#Date: Jan 7, 2021
#testid Sudoku
#Determine if a 9 x 9 Sudoku board is testid. Only the filled cells need to be testidated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be testid but is not necessarily solvable.
#Only the filled cells need to be testidated according to the mentioned rules.

class Solution:
    def istestidSudoku(self,board):

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
    #constestts: must start with ( and end with )
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

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is testid.
#An input string is testid if:

#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.

def istestid(s):
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

def istestid2(s):
    dic = {'(':')', '[':']', '{':'}'}
    current = []

    for y in range(0,len(s)): #scan each character of the string at a time
        
        if s[y:y+1] in dic: #if its an open bracket add it to array
            current.append(s[y:y+1])

        else: #if its a closed bracket

            if len(current) == 0: #if it matches nothing at all, string is intestid
                return False

            elif s[y:y+1] == dic[current[-1]]: #if it matches most recent open bracket
                current.pop()

            else: #if it doesnt match most recent open bracket, string is intestid
                return False

    if len(current) == 0:
        return True

#Date: March 6, 2021

#Given an array 'nums' and a testue 'test',
#remove all instances of that testue in-place and return the new length.
        
def removeElement(nums,test):
    
    while nums.count(test) != 0: #track how many elements in nums still = test
        nums.remove(test) #remove the elements that = test

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
    #join the two arrays together then keep removing min and max testues till we acheive the median

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

def expand(s,left,right): #function to call on, expands outwards from given index(s) while the substring is a testid palindrome

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
    sign = True #sign testue of integer (True = +ve, False = -ve)
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

#Date: May 2, 2021
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#Return the answer in any order.
    
def letterCombinations(digits):
    if digits == '': return [] #if we receive empty string
        
    maps = {             #construct hash table to link digits to respective characters
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
    res = []
    
    def build(curr, count): #for each digit (in order) branch out all possibilities using an initial for loop
                            #use recursion to add on sequential possibilities (characters associated with 'next' digit)
                            #and stop/append answers once we've reached end of digit sequence.
            
        if count == len(digits):
                res.append(curr)
            
        else:
            for char in maps[digits[count]]:
                build(curr+char,count+1)
            
                        
    for char in maps[digits[0]]:
            build(char,1)
                  
    return res

#Date: May 7, 2021
#Given an array of integers nums sorted in ascending order, find the starting and ending position (inclusive) of a given target testue.
#If target is not found in the array, return [-1, -1].

def searchRange(nums,target):
    try:
        start = nums.index(target) #aquire starting index of target
            
    except testueError: #if the target doesnt exist (question solved)**
        return [-1,-1]
        
    end = start #set default ending index to be equal to start
    curr = target
        
    while curr == target: #Increment index by one and stop when the testue in the array no longer = the target
            
        end += 1
            
        try:
            curr = nums[end]
            
        except IndexError: #if the array ends, then break the loop as well
            break
        
    return [start, end-1] #because we increment, THEN CHECK, the final end testue will be one more than expected

#Date: May 25, 2021:
#Given a string containing just the characters '(' and ')', find the length of the longest testid (well-formed) parentheses substring.

def longesttestidParentheses(s):
    #use stack where we always have a BASE INDEX (could be at [0] or higher) and acts as index of most recent '(' - 1 or index of ')' that rendered the current sub-parenthesis' intestid and acts as new start
    #(except for initial state of -1)
        
    #when theres '(' we push the index onto the stack, 
    #and when it gets matched we:
        # 1. pop the '(' index it matches with
        # 2. find max testid current sub-parenthesis' length by doing current index - base index
        
    #we can encouter 2 issues that render the sub-parenthesis' intestid:
        # a. more ')' than '('
            #solution: since after the pop() the stack will be empty, we simply ignore 2. and set the ')' index as new BASE INDEX
        # b. extra '('s that arent getting matched
            #solution: BASE INDEX is automatically shifted to match most recent '(' when we append the indexs of '('

            
    stack = [-1]    
    res = 0
        
    for index,curr in enumerate(s):
            
        if curr == '(':
            stack.append(index)
            
        elif curr == ')':
                
            stack.pop()
                
            try:
                res = max(res, index - stack[-1]) #by doing index - stack[-1] we match ')' with most recent '(' and protect against cases like ()(()
                
            except IndexError: #when stack is empty, AKA: theres more ')' than '('
                stack.append(index)
        
    return res

#Date: May 27, 2021 
#Given an array of distinct integers candidates and a target integer target,
#return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

#The same number may be chosen from candidates an unlimited number of times.
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.

#It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

def combinationSum(candidates,target):

    #a recursive method to branch out all possibilities and only keeping those who add up to target

    res = []
        
    def scan(ans,target):
            
        if target == 0:
            if sorted(ans) not in res:
                res.append(sorted(ans))
            return
            
        elif target < 0:
            return
            
        for num in candidates: #looping over every candidate and substract from how far we are to acheiving the target
                                                #we keep track of used candidates, and how far we are from current testue
            scan(ans+[num],target-num)
        
    scan([],target)

    return res

#Date: May 30, 2021 
#Write a program to solve a Sudoku puzzle by filling the empty cells.
#**each cell is filled with a string

#A sudoku solution must satisfy all of the following rules:
#Each of the digits 1-9 must occur exactly once in each row.
#Each of the digits 1-9 must occur exactly once in each column.
#Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#The '.' character indicates empty cells.

#A DFS solution

def possible(board,testue,r,c): #r = row, c = column

    box_coor = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], #box coordinates by row
                [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
                [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
                [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
                [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
                [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
                [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]]
        
    #check row
    if testue in board[r]:
        return False

    #check column
    if testue in [x[c] for x in board]:
        return False

    #check box
    for box in box_coor:
        if (r,c) in box:
            if testue in [board[spot[0]][spot[1]] for spot in box]:
                return False
        
    return True

ans = 0
def solveSudoku_oneAns(board):

    global ans

    if ans == 0:
        
        empty = 0
        for r in board:
            for c in r:
                if c == '.':
                    empty += 1
        if empty == 0:
            ans += 1
            return print(board)

        r,c = None,None
            
        for r_index, r_testue in enumerate(board):
            if '.' in r_testue:
                r,c = r_index, r_testue.index('.')
                break
            
        if r != None:
            for num in range(1,10):
                            
                pos = possible(board,str(num),r,c)

                if pos == True:
                    board[r][c] = str(num)
                    solveSudoku_oneAns(board)
                    board[r][c] = '.'

    else:
        return

def solveSudoku_allAns(board):
    empty = 0
    for r in board:
        for c in r:
            if c == '.':
                empty += 1
    if empty == 0:
        return print(board)

    r,c = None,None
            
    for r_index, r_testue in enumerate(board):
        if '' in r_testue:
            r,c = r_index, r_testue.index('.')
            break
            
    if r != None:
        for num in range(1,10):
                            
            pos = possible(board,str(num),r,c)

            if pos == True:
                board[r][c] = str(num)
                solveSudoku_allAns(board)
                board[r][c] = '.'

#Date: June 3, 2021 
#Given a collection of candidate numbers (candidates) and a target number (target),
#find all unique combinations in candidates where the candidate numbers sum to target.

#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.

def combinationSum2(candidates,target):
        
    res = []
        
    def push(used,left,needed,count): #needed is testue needed to acheive target
        if needed < 0:
            return
            
        elif needed == 0:
            if sorted(used) not in res:
                res.append(sorted(used))
            return
        
        else:
            for index,testue in enumerate(left):
                push(used+[testue],[j for i,j in enumerate(left) if i != index],needed-testue,count+1)
        
    push([],candidates,target,0)
       
    return res

#Date: June 10, 2021
#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in REVERSE order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def convert(arr): #convert array to Linked List 
    if arr[0]:
        res = ListNode()
        
        for index,element in enumerate(arr): #we can use a SHALLOW COPY variable to traverse the linked list and append each digit
            curr = res
            while curr.next:
                curr = curr.next
            curr.test = element

            if index != len(arr) - 1: #exception for last testue in array (we dont want an extra empty node)
                curr.next = ListNode()

    return res
            
def addTwoNumbers(l1,l2): 
    
    curr1,curr2 = l1,l2
    test1 = []
    test2 = []
        
        
    while curr1 != None: #reverse digits in linked lists and store as array
            
        test1.insert(0, str(curr1.test))
        curr1 = curr1.next
        
    while curr2 != None:
            
        test2.insert(0, str(curr2.test))
        curr2 = curr2.next
        

    target = [int(x) for x in list(str(int(''.join(test1)) + int(''.join(test2))))] #add two integers once reversed
    target.reverse() #reverse the result 
        
    res = convert(target)

    return res

#alternate solution (better time + memory complexity):
#sorta like doing (sorta like 123
                            # 345
                        #  +---------but from the opposite side

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def addTwoNumbers2(l1,l2):

    carry = 0
    res = n = ListNode(0) #n is shallow copy of res

    while l1 or l2 or carry: #checking if 'carry' exists is for the last digit's carryover
                 # 0 or None -> False in most languages
        if l1:
            carry += l1.test
            l1 = l1.next
                
        if l2:
            carry += l2.test #do the addition without the carryover digit first
            l2 = l2.next
            
        carry, test = divmod(carry, 10) #divmod returns quotient,remainder
        n.next = n = ListNode(test) #n is shallow copy of n.next so we can traverse the linked list
            
    return res.next

#Date: June 14, 2021
#Merge two sorted linked lists and return it as a sorted list.
#The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def mergeTwoLists(l1,l2):

    if l1 == None and l2 == None:
        return
        
    curr1, curr2 = l1, l2
    conv = []
        
    while curr1: #all testues in both linked-lists are appended to a single array
        conv.append(curr1.test) 
        curr1 = curr1.next
        
    while curr2:
        conv.append(curr2.test)
        curr2 = curr2.next
        
    conv.sort() #the array is sorted


    #the array is re-converted into a linked-list 
    ans = curr = ListNode()
    for i,x in enumerate(conv):
            
        curr.test = x
            
        if i != len(conv)-1:
            curr.next = curr = ListNode()
        
    return ans
    
#Date: June 16, 2021
#Given an unsorted integer array nums, find the smallest missing positive integer.
#You must implement an algorithm that runs in O(n) time

def firstMissingPositive(self, nums):
        
    store = set([i for i in nums])
    ans = 1
        
    while ans in store: #prevents O(n^2) as sets have lookup of O(1)
                        #a set is implemented as testues in a hash table
        ans += 1
            
    return ans

#Date: June 17, 2021
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       testue

#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two one's added together.
#12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right.
#However, the numeral for four is not IIII. Instead, the number four is written as IV.
#Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
#There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.

def romanToInt(s):
    
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    ans = 0

    #Ideally, we can iterate through the string and sum up corresponding testues to the symbols one by one
    #The only exception is in scenarios where there is a sub-string with the testue of 4 * 10^x (x = 0 or xEZ+)
        #to solve this we can check if testue of very next index > testue at current index and substract testue at current index if true
    
    for i in range(0, len(s) - 1):
            
        if roman[s[i]] < roman[s[i+1]]:
            ans -= roman[s[i]]
                
        else:
            ans += roman[s[i]]
                
    return ans + roman[s[-1]] #for the last index of string so we dont encounter IndexError

#Date: June 18, 2021
#Given a sorted array of distinct integers and a target testue, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums,target):
    #use divide and conquer
    #Note: len(), and indexing have a time complexity of O(1)
        
    #special conditions:
    if len(nums) == 0: #nums is empty
        return 0
        
    if len(nums) == 1: #nums only has one testue
        if target <= nums[0]:
                return 0
            
        elif target > nums[0]:
            return 1
        
    if target > nums[-1]: #target is larger than everything
        return len(nums)
        
    if target < nums[0]: #target is smaller than everything
        return 0
        
        
    def divide(curr,leftbound,rightbound): #leftbound and rightbound is index range of curr relative to nums
        #1. break the array to left and right
        #2. check 

        left, right = curr[:len(curr)//2], curr[len(curr)//2:]
        left_compare, right_compare = left[-1], right[0]

        if target == left_compare: #target found!
            return leftbound + len(left) - 1

        elif target == right_compare: #target found!
            return leftbound + len(left)

        #target must be in left somewhere, in right somewhere, or doesnt exist
        elif target > right_compare:
            return divide(right,leftbound+len(left),rightbound)

        elif target < left_compare:
            return divide(left,leftbound,rightbound-len(right))

        else: #target doesnt exist
            return leftbound + len(left)

    return divide(nums,0,len(nums)-1)

#Date: June 19, 2021
#Given the head of a linked list, REMOVE the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def removeNthFromEnd(head):

    curr = head
    length = len_linked_list(head) #find length of linked list first

    #special conditions
    if head == None or head.next == None: #if linked list is empty or only has one node
        return
        
    if n == length: #if the first node needs to be removed
        return head.next
        
    for x in range(0,length-n-1): #find node before the nth node from end; we need to add the -1 as we start initially on the head node as we traverse
        curr = curr.next
        
    curr.next = curr.next.next #this resets the sucessor of the node BEFORE the removed node to the node initially AFTER the removed node
    return head
    
def len_linked_list(linked_list = None):
        
    count = 0
    curr = linked_list
        
    while curr:
        curr = curr.next
        count += 1
        
    return count

#Date: June 22, 2021 
#Given the root of a binary tree, determine if it is a testid binary search tree (BST).
#A testid BST is defined as follows:
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

def istestidBST(root):
        
    #a preorder DFS method; if any node ever fails to meet definition of BST in its sub-tree, we return false
    #Note: float('inf') and float('-inf') are indefinely large and small float testues
        
    if root == None: #reached bottom of a branch
        return True 
        
    if root.test <= largerThan or root.test >= lessThan:
        return False
        
    return istestidBST(root.left, root.test, largerThan) and \
           istestidBST(root.right, lessThan, root.test)
           #if we proceed left, all children nodes must <= current node from now and on
           #if we proceed right, all children nodes must >= current node from now and on

#Date: June 25, 2021 
#You are a professional robber planning to rob houses along a street.
#Each house has a certain amount of money stashed,
#the only constestt stopping you from robbing each of them is that adjacent houses have security systems connected
#and it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums): #Brute force and bad time complexity
        
    #use recursion (starting from an initial house) and 
    #branch possibilities of next house by index order. We will then find the maximum sum stolen 
    #and return it as the answer.
        
        
    #special case (no input)
    if nums == []:
        return 0
        
    ans = []
        
    def next_house(start,house_index,total):                  
        ans.append(total)
        return
            
        for i,money in enumerate(nums[house_index + 2:]): #branching out to next possible houses
                
            next_house(start,house_index + 2 + i, total + money)
        
    for i,first in enumerate(nums[0:2]): #we start with first two houses because you cant go from house 0 --> 1 or 1 --> 2
                                         #but aside from that, you can jump to the same houses from these start points; starting at each house would be redundant
        next_house(i,i,first)
            
    return max(ans)

#alternative
def rob2(nums):

    #use dynamic programming to break the array into "sub-problems" O(n)
    #while traversing the array, we keep track of MAX AMOUNT THAT CAN BE ROBBED UP TO THE CURRENT HOUSE WE'RE ON (using 'total' array)
        
    #to do that, we consider 3 indices/houses of nums at a time to take into account
    #adjacent houses that cant be robbed, but might hold more money (total sum-wise up to that point) than the current total.
        
    #https://www.youtube.com/watch?v=73r3KWiEvyk

    #special conditions
    if len(nums)==0:
        return 0
    if len(nums) == 1 or len(nums) == 2:
        return max(nums)
			
    total = [max(nums[0:i]) for i in range(1,3)] #setting up first 2 indices of dp array

    for i in range(2, len(nums)):
        total.append(max(nums[i] + total[i-2], total[i-1])) #Should we skip the current house and stick with the maximum amount up to the last house,
                                                            #or add the money in the current house the maximum amount
                                                            #up to the second last house (to decide maximum up to the current house)??
        
    return total[-1]

#Date: June 29, 2021
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
        
    #O(n^2) time (pretty slow run time)
    #iterate through each day and check every day that follows to determine each possible "profit"; we keep track of max profit at all times
        
    max_profit = 0
    count = 0
        
    while count <= len(prices) - 2: #stop on second last day
            
        buy = prices[count]
            
        for sell in prices[count + 1:]:
            max_profit = max(max_profit, sell-buy)
            
        count += 1
        
    return max_profit

#alternative
def maxProfit2(prices):
    #O(n) traversal solution
    #we keep track of minimum price (transient) as we iterate through the array, and find possible profits given that minimum price
    #this also insures that buying date < selling date chronologically
        
    minimum_buy = float('inf')
    max_profit = 0
        
    for price in prices:
        minimum_buy = min(minimum_buy,price)
        max_profit = max(max_profit, price - minimum_buy)
        
    return max_profit

#Date: July 2, 2021
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
        
    #an O(n) approach using dynamic programming
    #we base the code mainly on the fact that climbStairs(n) = climbStairs(n-1) + climbStairs(n-2);
    #the only ways to get directly onto the nth step is from the n-1th or n-2th.
        
    #special case
    if n <= 2:
        return n
        
    dp = [1,2]
    for step in range(2,n):
        dp[0], dp[1] = dp[1], dp[0] + dp[1] #we replace the testues instead of appending to end of array to avoid O(n) worst scenario
        
    return dp[-1]

#Date: July 3, 2021 
#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Your goal is to reach the last index in the minimum number of jumps.
#You can assume that you can always reach the last index.

def jump(nums):
        
    #an intuitive O(n^2) brute force/dynamic programming solution
    #in essence we want to find the smallest # of jumps to each index and eventually make our way to the end.
    #to accomplish this, we will loop through each index in 'nums' while checking all
    #possible positions that we can jump to from that particular index; we keep track of the least amount of jumps that
    #we need to reach each visited index in a hash table.
        
    ans = {n: float('inf') for n in range(0,len(nums))} 
    ans[0] = 0
        
    if len(nums) == 1:
        return 0
        
    for start,max_jump in enumerate(nums):
        for end in range(start+1, start+max_jump+1): #visiting each possible index we can jump to 
                
            ans[end] = min(ans[end], ans[start] + 1) #we use min() incase the index we jumped to has already been visited with a smaller # of jumps.
                
            if end == len(nums) - 1: #our return condition; if we reach the end
                return ans[end]
            
#alternative with better time complexity
def jump2(nums):
    #The idea is to maintain a transient frame between two pointers: left and right,
    #which represent a range of indexes that can be reached with a minimum of 'x' jumps.
    #Left initialy set to be 0 and right set to be nums[0]. Hence, points between 0 and nums[0]
    #can be reached using just 1 jump. Next, we want to find points I can reach using 2 jumps... and so on;
    #our new left will be set equal to right, and our new right will be set equal to the farest point we
    #can reach by two jumps. which is:

    #right = max(i + nums[i] for i in range(left, right + 1)

    if len(nums) == 1: 
        return 0
        
    left, right = 0, nums[0]
    jumps = 1
        
    while right < len(nums) - 1:
        jumps += 1
        nxt_right = max([i + nums[i] for i in range(left, right + 1)]) #furtherst of all possible next positions 
        left, right = right, nxt_right
            
    return jumps

#Date: July 6, 2021
#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permute(nums):
        
    #recursive DFS approach; approximately O(2^n) time due to recursive call stack
    #base case: when permutation length = nums = length
    #arguments: current permutation, whats left in nums for us to use
        
    ans = []
        
    def helper(curr, remaining):
        
        if len(remaining) == 0: #base case; theres nothing left to add to the permutation
            ans.append(curr)
            return
          
        for i, next_elem in enumerate(remaining): #add each possible "next testue" to the current permutation and recurse
            helper(curr + [next_elem], remaining[:i] + remaining[i+1:])
          
        
    helper([],nums)
        
    return ans

#Date: July 7, 2021
#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

def permuteUnique(nums):
    
    #dfs + dynamic programming solution
    #similar solution to previous question. However, each time we add the next layer to
    #each individual permutation we check if a particular number has already been used (avoids duplicates and unecessary run time) through a hash table.
        
    res = []
                
    def dfs(nums, path, res):
        
        used = {}

        if not nums: #base case to stop the dfs recursion
            res.append(path)
            return

        for i in range(len(nums)):

            if used.get(nums[i]):
                continue #returns to begenning of loop while ignoring rest of the code
                    
            used[nums[i]] = True
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
                
    dfs(nums, [], res)
    return res

#Date: July 9, 2021
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs):
        
    #to approach this we must note that all anagrams will produce the same string if sorted
    #with that in noted, we can group anagrams together with a hash table when traversing 'strs'; the key will be the sorted anagram and the testue will the anagrams
        
    res = {}
        
    for word in strs:
            
        if not res.get(temp := tuple(sorted(word))): #we use a tuple over an array because its hashable
            res[temp] = [word]
            continue
            
        res[temp].append(word)
        
    return res.testues()

#Date: July 10, 2021
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
    #an iterative dynamic programming approach O(n)
        
    #we initialize a current subarray to start at nums[0], for every next index we may either choose to keep its testue in our current subarray,
    #or choose to start a new subarray at that testue.
    #if we choose to keep the testue (if testue + current sum of subarray > testue), we add the testue to the sum of our current subarray
    #otherwise, we will start a new subarray at nums[i]
        
    #to actually solve the question however, it is important to note,that we will keep track of our desired answer (contiguous subarray with largest sum)
    #by comparing the current sum of each subarray at every index and keeping track of the max testue. 
        
    sub_array_sum = nums[0] #sum of current subarray, from a particular start index to another index (both currently 0)
    res = nums[0]
        
    for i in range(1,len(nums)):
        sub_array_sum = max(sub_array_sum + nums[i], nums[i]) #in this context, nums[i] marks a potential start to a new subarray
        res = max(res, sub_array_sum)
        
    return res

#Date: July 11, 2021
#Given an m x n matrix, return all elements of the matrix in spiral order.

def spiralOrder(matrix):
        
    #an O(n) solution where n is number of total elements
    #while the matrix still holds element, we peel layers in this sequence:
    #1.top row (rightwards), 2.right (downwards), 3.bottom (leftwards), 4.left (upwards)
        
    ans = []
        
    def done(matrix):
            
        if len(matrix) == 0: #either whole matrix is empty
            return True
            
        count = 0 #or every array in the matrix is empty
        for arr in matrix:
            if len(arr) != 0:
                count += 1
        if count == 0:
            return True
            
        return False
        
    while True:
            
        #1.
        ans += [j for j in matrix[0]]
        matrix.pop(0)
            
        if done(matrix):
            return ans
            
        #2.
        ans += [j[-1] for j in matrix]
        for row in matrix:
            row.pop()
                
            if done(matrix):
                return ans
            
        #3.
        ans += [matrix[-1][i*-1] for i in range(1,len(matrix[-1])+1)]
        matrix.pop()

        if done(matrix):
            return ans
                     
        #4.
        ans += [matrix[i*-1][0] for i in range(1,len(matrix)+1)]
        for row in matrix:
            row.pop(0)
                
        if done(matrix):
            return ans
            
    return ans

#Date: July 13, 2021
#Given a linked list, swap every two adjacent nodes and return its head.
#You must solve the problem without modifying the testues in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def swapPairs(self):

    #5 step solution: iterate through 2 nodes at a time always have shallow copies of: the first node, the second node, and the node previous to the first node
        
    prev = dummy = ListNode()
    curr = dummy.next = head
        
    while curr and curr.next:
            
        first = curr
        second = curr.next
            
        #1.
        first.next = second.next
            
        #2.
        prev.next = second
            
        #3.
        second.next = first
            
            
        #4/5.
        prev = second.next
        curr = prev.next
            
        
    return dummy.next

#Date: July 17, 2021
#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.

def canJump(nums):
        
    #An O(n) traversal solution; we continuously update the maximum index we can potentially reach, up to and including a particular index.
    #if an index within the nums is ever beyond our max reach --> its impossible to reach the end. 
        
    max_reach = 0
        
    for i, j in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i+j)
            
    return True

#Date: July 18, 2021
#Given an array of intertests where intertests[i] = [starti, endi],
#merge all overlapping intertests, and return an array of the non-overlapping intertests that cover all the intertests in the input.

def merge(intertests):
        
    #an O(n^2*log n) solution
    #Assuming starting point of intertests are increasing... we will start with one initial (current) intertest to focus on,
    #and traverse the remaining intertests while checking the following:
        
    #1. if start > current end --> add new intertest
    #2. if start <= current end and end > current end --> current end = end
        
    intertests = sorted(intertests, key=lambda x: x[0])
    ans = [intertests[0]]
        
    for i in range(1, len(intertests)):
            
        if intertests[i][0] > ans[-1][1]:
            ans.append(intertests[i])
            
        elif intertests[i][1] > ans[-1][1]:
            ans[-1][1] = intertests[i][1]
        
    return ans

#Date: July 19, 2021
#Given a string s consists of some words separated by spaces,
#return the length of the last word in the string. If the last word does not exist, return 0.
#A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(self, s: str) -> int:
        
    #An O(n) solution; traverse the string backwards and stop when we see a space and + have already seen a non-space character in the past 
        
    seen_char = False
    count = 0
        
    for i in range(1,len(s)+1):
            
        if seen_char and s[i*-1] == ' ':
            return count
            
        if s[i*-1] != ' ':
            seen_char = True
            count += 1
        
    return count

#Date: July 20, 2021
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.

def mergeKLists(lists):
        
    #A O(2n+nlog n) --> O(n+nlog n) solution
    #Change into array data structure, sort, then convert back
        
    temp = []
        
    def ll_to_arr(head):
        curr = head
        while curr:
            temp.append(curr.test)
            curr = curr.next
        
    def arr_to_ll(arr):
        curr = dummy = ListNode()
        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next
                
    for head in lists:
        ll_to_arr(head)
    temp.sort()
        
    return arr_to_ll(temp)

#Date: July 20, 2021
#Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

def generateMatrix(n):
        
    #keep track of our position (i.e row, column) in the matrix and traverse in the following order: right, down, left, up
        
    #we change directions given two cases:
    #1. we receive an index error (we went outside of the given dimensions)
    #2. we have reached a spot that has already been filled
              
    matrix = [[None for x in range(0,n)] for y in range(0,n)]
        
    curr, filled = [0,-1], 0 
    #[row, column]

       
    while filled < n*n:
            
        #right
        curr[1] += 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[1] += 1
                    
                else:
                    curr[1] -= 1
                    break
                
            except IndexError:
                curr[1] -= 1
                break
            
            
        #down
        curr[0] += 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[0] += 1
                    
                else:
                    curr[0] -= 1
                    break
                
            except IndexError:
                curr[0] -= 1
                break
            
            
        #left
        curr[1] -= 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[1] -= 1
                    
                else:
                    curr[1] += 1
                    break
                
            except IndexError:
                curr[1] += 1
                break
            
        #up
        curr[0] -= 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[0] -= 1
                    
                else:
                    curr[0] += 1
                    break
                
            except IndexError:
                curr[0] += 1
                break
                        
    return matrix

#Date: July 23, 2021 
#Given the head of a linked list, rotate the list to the right by k places.

def rotateRight(head,k):
        
    #O(kn) time; worst case of O(n^2) time.
    #for each rotation we traverse to the end of the linked list and bring the last node to the head
    #the minimum number of iterations/rotations needed is calculated by:

    #round(((k / length) - (k // length)) * length), where length is the length of the linked list
      
        
    if (not head) or (not head.next):
        return head
        
    def len_ll(head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next      
        return count
        
    length = len_ll(head)
    iterations = round(((k / length) - (k // length)) * length)
            
    for x in range(0,iterations):
            
        curr = head
        while curr.next.next:
            curr = curr.next
            
        hold = curr.next
        curr.next = None
        hold.next = head
        head = hold
            
    return head

#Date: July 24, 2021
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?

def uniquePaths(m,n):

    #an O(mn) time dynammic programming approach
    #possbilities of getting to matrix[row][column] = matrix[row-1][column] + matrix[row][column-1]
        
    matrix = [[1] + [None for i in range(0,n-1)] for j in range(0,m)]
    matrix[0] = [1 for i in range(0,n)]
        
    for r in range(1,m):
        for c in range(1,n):
            matrix[r][c] = matrix[r][c-1] + matrix[r-1][c]
        
    return matrix[m-1][n-1]

#Date: July 25, 2021
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time.
#The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#Now consider if some obstacles are added to the grids. How many unique paths would there be?
#An obstacle and space is marked as 1 and 0 respectively in the grid.

def uniquePathsWithObstacles(obstacleGrid):
        
    #O(3mn + m) time
    #1. we first traverse the matrix to convert all the 0s to 1s and vice versa
    #2. from there, we need to add an additional layer of of 0s to wrap the top and left of the matrix to overcome situations where there obstacles blockade an entire row
    #3. ultimately we will traverse the matrix and take the same approach as the previous question

    #3.
    def helper(matrix,m,n):
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c] != 0 and (r!=1 or c!=1):
                    matrix[r][c] = matrix[r][c-1] + matrix[r-1][c]

        return matrix[-1][-1]

    #1. 
    for r in range(0,rows:=len(obstacleGrid)):
        for c in range(0,cols:=len(obstacleGrid[0])):     
            if obstacleGrid[r][c] == 1: obstacleGrid[r][c] = 0
            else: obstacleGrid[r][c] = 1

    #2.
    for r in range(0,rows):
        obstacleGrid[r].insert(0,0)
    obstacleGrid.insert(0,[0 for i in range(0,cols+1)])
        

    return helper(obstacleGrid, rows+1, cols+1)

#Date: July 26, 2021
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#Note: You can only move either down or right at any point in time.

def minPathSum(grid):
        
    #dynamic programming O(mn + m + n) time solution
    #minPathSum(grid[r][c]) = minimum of current box + top box and current box + left box
        
    #initialize the first row to be all 1s
    for r in range(1,rows:=len(grid)):
        grid[r][0] = grid[r][0] + grid[r-1][0]
        
    #initialize the first column to be all 1s
    for c in range(1,cols:=len(grid[0])):
        grid[0][c] = grid[0][c] + grid[0][c-1]
        
    for r in range(1,rows):
        for c in range(1,cols):
            grid[r][c] = min(grid[r][c]+grid[r-1][c], grid[r][c]+grid[r][c-1])
        
    return grid[-1][-1]

#Date: July 27, 2021
#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
        
    #Best time: O(1), average time: O(n), worst case: O(2n)
        
    for i in range(1,len(digits)+1):
            
        digits[i*-1] = digits[i*-1] + 1
            
        #if there isnt any digit to carry over, we are finished
        if len(str(digits[i*-1])) == 1:
            return digits
            
        #if there is a digit to carry over but we are already on the 0th index, we insert and extra 1 in the front of the array
        elif i == len(digits):
            digits[0] = 0
            digits.insert(0,1)
            return digits
            
        #if there is a digit to carry over, we add it to the previous index
        else:
            digits[i*-1] = digits[i*-1] - 10
    return

#Date: July 28, 2021
#Given two binary strings a and b, return their sum as a binary string.

def addBinary(a,b):
        
    #1. make sure the two binary strings are of equal length
    if (l_a := len(a)) > (l_b := len(b)): 
        b = ''.join(['0' for i in range(0,l_a-l_b)]) + b
            
    if l_b > l_a: 
        a = ''.join(['0' for i in range(0,l_b-l_a)]) + a
        
    #2. do the addition digit-by-digit by traversing backwards
    #ans has length of len(a) + 1 in case the last digit has a carry-over
    ans = ['0' for i in range(0,len(a)+1)]
    for i in range(-1,-1*(1+len(ans)),-1):
            
        if i > -1*len(ans):
            ans[i] = str(int(ans[i]) + int(a[i]) + int(b[i]))
            
        #situation adressing a possible carry-over to the next digit
        if int(ans[i]) > 1:
            ans[i-1],ans[i] = str(divmod(int(ans[i]),2)[0]), str(divmod(int(ans[i]),2)[1])
        
    if ans[0] == '0': return ''.join(ans[1:])
    return ''.join(ans)

#Date: July 29, 2021
#Given a non-negative integer x, compute and return the square root of x.
#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

#Note: You are not allowed to use any built-in exponent function or operator,

def mySqrt(x):
        
    #An O(log n) time divide and conquer solution
    #we have a transient range of numbers for which the answer could be in, and continuously etestuate the average of the range (num) to be the potential solution
    #if it occurs that num is too large, we cut the range down to the smaller half; and vice versa if num is too small
        
    frame = [0,(x//2)+2]
    num = (frame[0] + frame[1]) // 2
        
    while True:
        
        if num * num <= x and (num+1) * (num+1) > x:
            return num
            
        elif num * num < x:
            frame = [num, frame[1]]
            num = (frame[0] + frame[1]) // 2
            
        else:
            frame = [0,num]
            num = (frame[0] + frame[1]) // 2

#Date: July 29, 2021:
#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

def myPow(x,n):
        
    #An optimized recursive solution
        
    if not n:
        return 1
        
    if n < 0: #a^-b = 1/a^b
        return 1 / myPow(x, -n)
        
    if n % 2 == 1: 
        return x * myPow(x, n-1)
        
    return myPow(x*x, n/2) #since a^b = (a^2)^b/2; this is done for the sake of optimization

#Date: July 29, 2021
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
        
    #An average O(n^2) time traversal solution with memoization
    #for each 0 we encounter, we update the entire row and column to 0s, but on the condition that the row/column has not been updated yet
        
    row_cache = {}
    column_cache = {}
        
    for r in range(0,rows := len(matrix)):
        for c in range(0,cols := len(matrix[0])):
    
            if matrix[r][c] == 0:
                    
                if not row_cache.get(r):
                    for i in range(0,cols):
                        if matrix[r][i] != 0:
                            matrix[r][i] = '0' #we use strings so we only consider the initial 0s
                    row_cache[r] = True
                    
                if not column_cache.get(c):
                    for i in range(0,rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = '0'
                    column_cache[c] = True
    return

#Date: July 31, 2021
#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.

def sortColors(nums):
        
    """
    Do not return anything, modify nums in-place instead.
    """
    #Dutch flag algorithm; one-pass and O(n) time
    #other feasible solutions: bubble sort O(n^2), insertion/selection sort O(2n)
        
    low,mid,high = 0,0,len(nums)-1
        
    while mid <= high:
            
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            low += 1
            mid += 1
         
        elif nums[mid] == 1:
            mid += 1
            
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1

#August 1, 2021:
#Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
#You may return the answer in any order.

def combine(n,k):
        
    #A dfs recursive approach
    #we build each combination (curr) individually - one number per call
    #a new recursive call must add on a number greater than the previous to the current combination (this is to avoid creating overlaps/permutations instead of combinations)
        
        
    res = []
        
    def dfs(rem, curr):
            
        if len(curr) == k:
            res.append(curr)
            return 
            
        for i in range(len(rem)):
            dfs(rem[i+1:], curr+[rem[i]])
        
    dfs([x for x in range(1,n+1)], [])
    return res

#August 2, 2021:
#Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(nums):
        
    #a dfs recursive solution
    #the same approach as the previous question besides the prodcedure of appending our current combination to the global answer on every recursive call
        
    ans = []
        
    def dfs(curr,rem):
            
        ans.append(curr)
        if rem == 0:
            return
            
        for i in range(0,len(rem)):
            dfs(curr+[rem[i]], rem[i+1:])
    
    dfs([],nums)
    return ans

#August 3, 2021
#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def deleteDuplicates(head):
        
    #An O(n) traversal solution
    #We keep track of all seen testues in a hash table 
    #if we come across a testue that has already be seen, we remove it
        
    seen = {}
    prev = None
    curr = head
        
    while curr:
            
        if not seen.get(curr.test):
            seen[curr.test] = True
            prev = curr
            curr = curr.next
            
        else:
            curr = curr.next
            prev.next = curr
        
    return head

#Date: August 4, 2021
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
#The same letter cell may not be used more than once.

def exist(board,word):
        
    #A recursive dfs solution
    #From each position on the board, we branch out possible paths to neighboring cells that might contain the word;
    #for each recursive branch, we keep track of the matched characters (of the word), and the traversed positions (so we dont traverse the same cell twice).
        
    #1. if at any point the current position on the board mismatches the word, we halt the current recursive branch 
        
    #2. if all characters of the word are matched, we update the global answer (to be returned) to true
          
    ans = False
        
    def dfs(r,c,pointer,traversed):
            
        nonlocal ans
                
        if board[r][c] == word[pointer]:
                
            if pointer == len(word)-1:
                ans = True
                return
                
            #right
            if c < len(board[0])-1 and not traversed.get((r,c+1)):
                traversed[(r,c+1)] = True
                dfs(r,c+1,pointer+1,traversed)
                traversed.pop((r,c+1))
                    
            #left
            if c > 0 and not traversed.get((r,c-1)):
                traversed[(r,c-1)] = True
                dfs(r,c-1,pointer+1,traversed)
                traversed.pop((r,c-1))
                    
            #up
            if r > 0 and not traversed.get((r-1,c)):
                traversed[(r-1,c)] = True
                dfs(r-1,c,pointer+1,traversed)
                traversed.pop((r-1,c))
                
            #down
            if r < len(board)-1 and not traversed.get((r+1,c)):
                traversed[(r+1,c)] = True
                dfs(r+1,c,pointer+1,traversed)
                traversed.pop((r+1,c))
        return
        
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            dfs(i,j,0,{(i,j):True})
    return ans

#August 5, 2021
#Given the head of a linked list and a testue x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def partition(head,x):
        
    #An O(n) traversal solution using dummy nodes and external memory
    #we group together all node testues < x in one linked list, and all other nodes in another linked list while preserving their "relative positions"
    #ultimately, we will join together the two lists in their respective order (smaller nodes --> other nodes)
        
    curr_o = others = ListNode()
    curr_s = smaller = ListNode()
    curr = head
        
    while curr:
            
        if curr.test < x:
            curr_s.next = ListNode(curr.test)
            curr_s = curr_s.next
            
        else:
            curr_o.next = ListNode(curr.test)
            curr_o = curr_o.next
                
        curr = curr.next
                
    curr_s.next = others.next
    return smaller.next

#August 5, 2021
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
#representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1,n,nums2,m):
    """
    Do not return anything, modify nums1 in-place instead.
    """
        
    #intuitive O('n' + nlogn) time solution
        
    nums1[m:] = nums2[:n]
    nums1.sort()

#August 7, 2021:
#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def reverseBetween(head):
        
    #an O(n) traversal solution
    #we divide the linked list into 3 sections using dummy nodes: left/right of the section (left-right) of interest, and the section of interest itself
    #regarding the section of interest in particular, we will reverse the desired portion of the linked list as we traverse it
    #finally, we'll concatenate the 3 sections together and return the result
        
    l_trav = l = ListNode(0)
    sec = None
    r_trav = r = ListNode(0)
    hold = None
        
    curr,node = head,1
    while curr:
            
        if node < left:
            l_trav.next = ListNode(curr.test)
            l_trav = l_trav.next
                
        elif node > right:
            r_trav.next = ListNode(curr.test)
            r_trav = r_trav.next
            
        else:
            sec, sec.next= ListNode(curr.test), sec

            if node == left:
                hold = sec
                
        curr = curr.next
        node += 1
        
    l_trav.next = sec
    hold.next = r.next
       
    return l.next

#Date: August 8, 2021
#Given a string s containing only digits, return all possible testid IP addresses that can be obtained from s. You can return them in any order.
#A testid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros.
#For example, "0.1.2.201" and "192.168.1.1" are testid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are intestid IP addresses. 

def restoreIpAddresses(s):
        
    #a dfs solution
    #we seek to insert the dots in the given string one at a time to form a potentially testid adress
    #we able to insert a dot at a given index under the following coditions:
        #1. there will be enough characters remaining to insert the remaining dots (e.g we can only insert the first dot if there at a minimum of 3 characters that will follow the dot)
        #2. the integer that comes before the dot must have a maximum of 3 characters between 0 and 255
        #3. the integer in question must to start with a 0
    #Once, we've inserted 3 testid dots, we append our current possibility to an array of solutions
                
    ans = []
        
    def dfs(curr,dot,depth):
            
        if depth == 3:
            if curr[dot:] != '' and int(curr[dot:]) >= 0 and int(curr[dot:]) <= 255:
                if not (len(curr[dot:]) >= 2 and curr[dot] == '0'):
                    ans.append(curr)
                    return
            return
            
        for i in range(dot+1,dot+4):
            if len(curr[i:]) >= 3-depth:
                if int(curr[dot:i]) >= 0 and int(curr[dot:i]) <= 255:
                    if not (len(curr[dot:i]) >= 2 and curr[dot] == '0'): 
                        dfs(curr[:i] + '.' + curr[i:],i+1,depth+1)
                     
    dfs(s,0,0)
    return ans

#Date: August 9, 2021
#Given the root of a binary tree, return the postorder traversal of its nodes' testues.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def postorderTraversal(root):
        
    ans = []
        
    def dfs(node):
            
        nonlocal ans
            
        if node:
            dfs(node.left)
            dfs(node.right)
            ans += [node.test]
                
    dfs(root)
    return ans

#Date: August 9, 2021
#Given the root of a binary tree, return the inorder traversal of its nodes' testues.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def inorderTraversal(root):
        
    ans = []
        
    def dfs(node):
            
        nonlocal ans
            
        if node:
            dfs(node.left)
            ans += [node.test]
            dfs(node.right)
                  
    dfs(root)
    return ans

#Date: August 9, 2021
#Given the root of a binary tree, return the preorder traversal of its nodes' testues.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def preorderTraversal(root):
        
    ans = []
        
    def dfs(node):
            
        nonlocal ans
            
        if node:
            ans += [node.test]
            dfs(node.left)
            dfs(node.right)
                  
    dfs(root)
    return ans

#August 10, 2021
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same testue.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def isSameTree(p,q):
        
    #a bfs solution
    #we check both trees simultaneously - one layer at a time
    #if at any point, the layers do not match up, the answer is falsified
    #if both layers comprise only of None testued nodes (meaning we cleared the whole tree), we return true
        
    if p == None:
        p = TreeNode(None)
    if q == None:
        q = TreeNode(None)
            
    def next_layer(layer):
            
        for i in range(0,len(layer)):
                
            if type(layer[i].test) == int:
                if layer[i].left:
                    layer += [layer[i].left]
                else:
                    layer += [TreeNode(None)]
                if layer[i].right:
                    layer += [layer[i].right]
                else:
                    layer += [TreeNode(None)]
            else:
                layer += [TreeNode(None), TreeNode(None)]
            
        return layer
            

    def bfs(p_layer, q_layer):
            
        if any(p_layer[i].test != q_layer[i].test for i in range(0,len(p_layer))):
            return False
        elif all(node.test == None for node in p_layer + q_layer):
            return True
            
        prev = len(p_layer)
        p_layer, q_layer = next_layer(p_layer), next_layer(q_layer)
                    
        return bfs(p_layer[prev:],q_layer[prev:])
                
    return bfs([p],[q])

#August 12, 2021
#You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake.
#Recover the tree without changing its structure.
#Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def recoverTree(root):
        
    """
    Do not return anything, modify root in-place instead.
    """
        
    #inorder dfs solution; we will exploit the fact that the an INORDER dfs traversal for a binary tree will always return
    #the node testues in increasing order due to its nature
    #thus, given the two nodes we will need to swap, 
    #[1] the first node will always be greater then its next node, 
    #and [2] the second node will always be smaller than its previous node. 
    #Otherwise, there will be more than one swap required - which is impossible.
        
    node1 = None
    node2 = None
    prev = TreeNode(float(-inf))
        
    def dfs(node):
            
        nonlocal node1, node2, prev
            
        if node:
            dfs(node.left)
                
            if not node1 and prev.test >= node.test: #[1]
                node1 = prev
                
            if prev.test >= node.test: #[2]
                node2 = node
                
            prev = node
                
            dfs(node.right)
        return
        
    dfs(root)
    node1.test,node2.test = node2.test,node1.test
    return

#Date August 13, 2021
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def isSymmetric(root):
    
    #a dfs traversal solution, starting from the children of the root node, we compare each set of symmetrical nodes by recursing with the outer pair and inner pair of the current node 
    #if all pairs have cleared the tree without having been falsified, we return True
    
    def trav(l,r):
        if not any([l,r]): return True
        if not all([l,r]) or l.test!=r.test: return False
        return trav(l.left,r.right) and trav(l.right,r.left)
    
    return trav(root.left,root.right)

#Date: August 16, 2021
#Given the root of a binary tree, return the level order traversal of its nodes' testues. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def levelOrder(root):
        
    #a layer-by-layer bfs traversal. 
        
    res = []
        
    if root == None:
        return []
        
    def bfs(layer):
            
        nonlocal res
        if layer == []:
            return
            
        res.append([n.test for n in layer])
            
        for i in range(0,prev := len(layer)):
                
            if layer[i].left:
                layer += [layer[i].left]
                
            if layer[i].right:
                layer += [layer[i].right]
        bfs(layer[prev:])
            
    bfs([root])
    return res

#Date: August 17, 2021
#Given the root of a binary tree, return the zigzag level order traversal of its nodes' testues.
#(i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def zigzagLevelOrder(root):
        
    #a bfs solution; however, we iterate through the nodes from each layer in reverse order to how they were appended and create the next layer, through either a node.left -> node.right -> next node or a node.right -> node.left -> next node parrtern, while iterating through the current layer#
        
    #take the binary tree [3,9,20,null,null,15,7] for instance
        
    #layer 0: root
    #layer 1: iterating in reverse [3] => [20,9]
    #layer 2: iterating in reverse [20,9] => [15,7]
        
    def check_left(node):
        if node.left:
            return node.left
        return None
        
    def check_right(node):
        if node.right:
            return node.right
        return None
            
    def helper(layer, count):
        
        nonlocal res
            
        if len(layer) == 0:
            return
            
        res.append([node.test for node in layer])
            
        temp = []
        for i in range(-1,-((len(layer))+1),-1):
   
            if count % 2 == 1:
                if check_right(layer[i]):
                    temp += [layer[i].right]
                if check_left(layer[i]):
                    temp += [layer[i].left]
                
            else:
                if check_left(layer[i]):
                    temp += [layer[i].left]
                if check_right(layer[i]):
                    temp += [layer[i].right]
                        
        helper(temp,count+1 )
        
    if root == None:
        return []
        
    res = []
        
    helper([root], 1)
    return res

#Date: August 18, 2021
#Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
#An integer m is a divisor of n if there exists an integer k such that n = k * m.

import math
def isThree(n):
        
    #an O(n) solution; given that 1 and n must be factors of n, check for other possible factors from n till square root of n (to avoid overlap)
        
    divs = 2
        
    for i in range(2,int(math.sqrt(n))+1):
            
        if n/i == n//i:
            if i == math.sqrt(n):
                divs += 1
            else:
                divs += 2
        
    if divs == 3:
        return True
    return False

#Date: August 19, 2021
#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def maxDepth(root):
        
    #a pre-order traversal while keeping track of the current depth (which will allow the global answer to constantly be updated)
    
    ans = 0
        
    def dfs(node, depth):
        
        nonlocal ans
        
        ans = max(ans,depth)
        
        if node.left != None:
            dfs(node.left, depth+1)
        
        if node.right != None:
            dfs(node.right, depth+1)
        
        return
    
    if root != None:
        dfs(root,1)
        return ans
    return 0

#Date: August 22, 2021
#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node NEVER DIFFERS BY MORE THAN ONE.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def sortedArrayToBST(nums):
        
    #divide and conquer + recursion; for each recursive call, we assign the lower half of testues to the left sub-tree and the other half to the right
        
    if not nums:
        return 
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])

    return root

#Date August 22, 2021
#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a testue greater than X.
#Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def goodNodes(root):
        
    #preorder dfs + keeping track of max_testue on each path 
    
    def helper(node,max_test):
        
        nonlocal good
        
        if node:
            if node.test >= max_test:
                good += 1

            helper(node.left,max(node.test,max_test))
            helper(node.right,max(node.test,max_test))        
        return 
    
    good = 0
    helper(root,float('-inf'))
    return good

#Date: August 22, 2021
#Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    
    #preorder traversal: swap every pair of branches
    
    def dfs(node):
        
        if node:
            node.left,node.right = node.right,node.left
            dfs(node.left)
            dfs(node.right)
    
    dfs(root)
    return root

#Date: August 22, 2021
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def minDepth(root):
        
    def dfs(node,depth):
        nonlocal ans
        
        if node:
            if not (node.left or node.right):
                ans = min(ans,depth)
            
            dfs(node.left,depth + 1)
            dfs(node.right,depth + 1)
        return
    
    ans = float('inf')
    dfs(root,1)
    if not root: return 0
    return ans

#Date: August 22, 2021
#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
#adding up all the testues along the path equals targetSum.
#A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def hasPathSum(root,targetSum):
        
    #preorder dfs; go down every possible path and check the sums

    def dfs(node,curr):
        nonlocal ans
        
        if node:
            
            if not (node.left or node.right) and curr == targetSum:
                ans = True
                return
            
            if node.left:
                dfs(node.left,curr+node.left.test)
            
            if node.right:
                dfs(node.right,curr+node.right.test)
    
    ans = False
    if not root: return False
    dfs(root,root.test)
    return ans

#Date: August 23, 2021
#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node testues in the path equals targetSum. Each path should be returned as a list of the node testues, not node references.
#A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def pathSum(root,targetSum):
        
    #pre order dfs
    
    def dfs(node, curr, used):
        nonlocal ans
    
        if curr == targetSum and not (node.left or node.right):
            ans += [used]

        if node.left:
            dfs(node.left, curr + node.left.test, used + [node.left.test])

        if node.right:
            dfs(node.right, curr + node.right.test, used +[node.right.test])
        
        return
    
    ans = []
    if not root: return []
    dfs(root,root.test,[root.test])
    return ans
                    
#Date: August 23, 2021
#Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
#Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
#The tests are generated such that there is exactly one solution. You may not use the same element twice.

def twoSum(numbers,target):
        
    #simple O(n) 2 pointer method (start at very left and right of array respectively); increment left pointer if current sum is too small and decrement the right if vice-versa

    p1, p2 = 0, len(numbers)-1

    while True:
        
        curr = numbers[p1] + numbers[p2]
        
        if curr == target:
            return [p1+1, p2+1]
        
        elif curr < target:
            p1 += 1
            
        else:
            p2 -= 1

#Date: August 23, 2021
#Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def findTarget(root,k):

    #dfs and keep track of seen node testues, if testue needed to aquire sum of k when added with current node testue has been traversed -> return true
        
    def dfs(node,curr,seen):
        
        if node:
            
            rem = k-node.test
            if rem in seen:
                return True
            seen[node.test] = True
            
            return dfs(node.left,curr+node.test,seen) or dfs(node.right,curr+node.test,seen)
        return False

    return dfs(root,0,{})
  
#Date: August 24, 2021
#There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
#Each second, you may perform one of the following operations:

#1. Move the pointer one character counterclockwise or clockwise.
#2. Type the character the pointer is currently on.

#Given a string word, return the minimum number of seconds to type out the characters in word.

def minTimeToType(word):
        
    #O(2n); for each spin, check if its faster to spin CW or CCW by comparing index differences (their distance)
    
    wheel = {j:i for i,j in enumerate(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])}
    ans = 0
    curr = 'a'
    
    for x in word:
        ans+=min(abs(wheel[curr] - wheel[x]), 26 - abs(wheel[curr] - wheel[x]) )
        curr = x
        
    return ans + len(word) # + len() to take into account typing time

#Date: August 24, 2021
#You are given an n x n integer matrix. You can do the following operation any number of times:

#Choose any two adjacent elements of matrix and multiply each of them by -1.
#Two elements are considered adjacent if and only if they share a border.

#Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

def maxMatrixSum(matrix):

    #the key is to realizing that, given an unlimited number of moves, we can always have either no negatives or only 1 negative left. 
    #There are two scenarios that fufill this claim:

    #1. if the number of -ves + 0s are even, we can make them all positives by moving the negative signs across the matrix until each one finds a pair
    #2. if the number of -ves + 0s are even, the same applies, except we can choose to leave out the testue of smallest magnitude to be a -ve at the end 
    #   (which doesnt necessarily need to be an initial -ve)
        
    negs, ans,smol = 0, 0, float('inf')
    for r in matrix:
        for c in r:
            if c <= 0:
                negs += 1
            smol = min(smol,abs(c))

    for r in matrix:
        ans += sum([abs(i) for i in r])
    
    if negs%2==0:
        return ans

    return ans-(2*smol)

# #Date: August 25, 2021
# #You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Definition for a Node.
# class Node:
#     def __init__(self, test: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.test = test
#         self.left = left
#         self.right = right
#         self.next = next

def connect(root):
        
    #bfs with queue - a recursive layer-by-layer traversal
    
    def bfs(layer):
        
        if all(node == None for node in layer):
            return
        
        for i in range(0,prev:=(len(layer))-1):
            layer[i].next = layer[i+1]
            layer += [layer[i].left, layer[i].right]
        
        bfs(layer[prev+1:]+[None])
    
    bfs([root,None])
    return root

    #Date: August 25, 2021
    #Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

    def judgeSquareSum(c):
        
        #O(sqrt n) solution using two pointer technique
        
        left, right = 0, int(c**0.5)

        while left <= right:
            
            res = left ** 2 + right ** 2

            if res == c:
                return True
            
            elif res < c:
                left += 1
                
            elif res > c:
                right -= 1
                
        return False

#Date: August 27, 2021
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

def lengthOfLIS(nums):
        
    #an established O(n^2) dynamic programming algorithm
    #keep track of a symmetric dp array to that keeps track of the max increasing subsequence up to each index (is transient)
    #for each index in nums, loop through all the previous indexes in dp to check which prior index would allow it to have the largest increasing subsequence
    
    dp = [1]*len(nums)

    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
                
    if not nums: return 0
    return max(dp)   

#August 27, 2021
#Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
#An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
#A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
#For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).      

def findLUSlength(strs):
        
    #an intuitive/brute force approach; make all subsequences recursively and compare lengths out of all subseqences that have only been seen once
    
    def helper(curr, rem):
        
        if not curr:
            return
        
        if curr in seen:
            seen[curr] = False
        else:
            seen[curr] = len(curr)
        
        for i in range(0,len(rem)):
            helper(curr+rem[i], rem[i+1:])
        return
    
            
    seen = {' ':-1}    
    for s in strs:
        for i in range(0,len(s)):
            helper(s[i],s[i+1:])

    return max(seen[x] for x in seen if seen[x])

#Date: August 29, 2021
#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def generate(numRows):
        
    #an intuitive iterative solution; each row starting from the 2nd is formulated by 1,sequence of sums derived from upper row (the length of which is equitestent to one less than the upper row),and another 1 
    
    ans = [[1]]
    
    for i in range(1,numRows):
        ans += [[1] + [ans[-1][i]+ans[-1][i+1] for i in range(0,len(ans[-1])-1)] + [1]]
    
    return ans

#Date: August 29, 2021
#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def getRow(rowIndex):
        
    #clever O(n) solution using the zip() to generate row; essentially, to form a subsequent row, we generate two copies of the current row and shift one by an index forward. Then, we add each corresponding index. This works beause it allows each testue of the current row to be sumed with the testue to its left (in the row) while including the two additional 1s on the edge. 
    
    #e.g (to forming the 5th row):
    
    #[0,1,4,6,4,1] (shifted 1 index forward)
    #[1,4,6,4,1,0]
    #+--------------
    #[1,5,10,10,5,1]
    
    row = [1]
    
    for n in range(0,rowIndex):
        row = [i+j for i,j in zip([0]+row,row+[0])]
        
    return row

#Date: August 29, 2021
#It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# Note: The boy can buy the ice cream bars in any order.

def maxIceCream(costs,coins):
        
    #simple O(n log n) greedy algorithm
    
    ans = 0
    
    for n in sorted(costs):
        coins -= n
        if coins >= 0:
            ans += 1
            continue
        break
        
    return ans

#Date: August 30, 2021
#Given a triangle array, return the minimum path sum from top to bottom.
#For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

def minimumTotal(triangle):
        
    #O(n) time/memory bottom-up dynammic programming solution; at each position we must we will move either leftwards or rightwards down to accumulate up to the minimum sum. 
    #Thus, beginning from positions in the second last row, we decide which direction to take starting from that position and store the minimum sum acheived in a dp array. This is repeated as we move upwards in the triangle; the final answer will be dp[0][0]
    
    dp = triangle
    for i in range(-2,-(len(triangle)+1),-1):
        for j in range(0,len(dp[i])):
            dp[i][j] = min(dp[i][j]+dp[i+1][j],dp[i][j]+dp[i+1][j+1])
            
    return dp[0][0]

#Date August 31, 2021
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
        
    #intuitive O(n^2) time solution; for each index (a potential starting point for a triplet), run the 2sum algorithm on all the other subsequent indexes.
    
    def helper(test, arr):
        nonlocal ans
        seen = {}
        for n in arr:
            if 0-test-n in seen:
                if (temp := sorted([test,n,0-test-n])) not in ans:
                    ans += [temp]
            seen[n] = True
        return
    
    ans = []
    for i in range(0,len(nums)-2):
        helper(nums[i],nums[i+1:])
    return ans

#Date: September 1, 2021
#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def isPalindrome(s):
        
    #intuitive O(n) time solution with two pointers
    
    dic = {'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True, 'g': True, 'h': True, 'i': True, 'j': True, 'k': True, 'l': True, 'm': True, 'n': True, 'o': True, 'p': True, 'q': True, 'r': True, 's': True, 't': True, 'u': True, 'v': True, 'w': True, 'x': True, 'y': True, 'z': True, '0': True, '1': True, '2': True, '3': True, '4': True, '5': True, '6': True, '7': True, '8': True, '9': True}
    s = ''.join([j.lower() for j in s if j.lower() in dic])
    left,right = 0,len(s)-1
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        return False
    return True

#Date: September 2, 2021
#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

def isMatch(s,p):
        
    #great explanation: https://www.youtube.com/watch?v=l3hda49XcDE
    
    #an O(n^2) dynammic programming approach
    #essentially as we traverse a dp matrix (rows and columns represent indices of the string and pattern respectively) for each cell in the dp matrix, we are comparing if string[:row] == pattern[:column] under a series of conditions
    
    dp = [[False for c in range(0,len(p)+1)] for r in range(0,len(s)+1)]
    dp[0][0] = True
    
    #deals with edge case patterns that would match '' (e.g a*, a*b*c*)
    for i in range(1,len(dp[0])):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            
            #the index in the string matches the index of the pattern (while both are letters) or the index in the pattern is .
            if s[i-1] == p[j-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
                continue
            
            #if theres a star in the index in the pattern theres two conditions: 
            #1. if the character before the star is repeated 0 times
            #2. the character before the star is repeated < 0 times
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2] #repetition = 0
                if s[i-1] == p[j-2] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j] 
                continue
                
            #respective indexes in the string and pattern are letters that do not match 
            dp[i][j] = False
            
    return dp[-1][-1]

#Date: September 2, 2021
#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
        
    #solution using sets (O(1) lookup time); for each testue in nums, check if it could be the smallest of a consequtive sequence and keep extending the sequence for as long as possible
    
    nums, ans = set(nums), 0
    
    for n in nums:
        if not n-1 in nums:
            count = n
            while count in nums:
                count += 1
            ans = max(ans, count-n)
    
    return ans

#Date: September 3, 2021
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

def maxProfit(prices):
        
    #An interative O(n) time solution. The idea behind the solution mostly reflects the question: "best time to buy and sell stock I". 
    
    #Essentially, given a current stock at hand, we either switch to a cheaper stock if there's one available, or we sell the stock WHENVER theres a price > buy price becuase we dont have to worry about high prices that were missed; we could just buy the another stock and make back the missed profit
    
    curr,ans = prices[0], 0
    
    for n in prices[1:]:
        if n < curr:
            curr = n
        elif n > curr:
            ans += n-curr
            curr = n
    
    return ans

#Date: September 3, 2021
#You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

def sumNumbers(root):
        
    #preorder dfs: while traversing down a branch, we keep track our current number; we ill add it to the sum when its reached a leaf node
    
    def dfs(node,curr):
        nonlocal ans
        if not (node.left or node.right): 
            ans += int(curr)
            return
        if node.left: dfs(node.left, curr+str(node.left.test))
        if node.right: dfs(node.right, curr+str(node.right.test))
        return
    
    ans = 0
    dfs(root,str(root.test))
    return ans

#September 4, 2021 (Bi-weekly contest 60)
# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

def findMiddleIndex(nums):
    
    #intuitive O(n); traverse through list and check for potential "middle index"

    for i in range(0,len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

#September 4, 2021 (Bi-weekly contest 60)
# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answe in any order.


def findFarmland(land):
    
    #extend as far right as possible, then do the same downwards
    
    ans,seen = [],{}
    
    def right(r,c):
        while c<len(land[0]) and land[r][c]:
            print(r,c)
            c+=1
        return c-1
    
    def down(r,c):
        while r<len(land) and land[r][c]:
            r+=1
        return r-1
    
    for i in range(0,len(land)):
        for j in range(0,len(land[0])):
            if land[i][j]:
                
                if (i,j) in seen:
                    continue

                m_right,m_down = right(i,j), down(i,j)
                for r in range(i,m_down+1):
                    for c in range(j,m_right+1):
                        seen[(r,c)] = True

                ans += [[i,j,m_down,m_right]]
    
    return ans

#Date: September 4, 2021
#Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#A region is captured by flipping all 'O's into 'X's in that surrounded region.

def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    
    #An O(2mn) time solution; the first O(mn) traversal is to preform a bfs on all tiles attached to edge 'O' tiles (can't convert to 'X's); the second is to convert all remaining 'O's into 'X's
    
    def bfs(curr,r,c):
        if not curr: return
        prev = len(curr)
        for n in range(0,prev):
            i,j = curr[n][0],curr[n][1]
            board[i][j] = 'A'
            for x,y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x_n = i+x
                y_n = j+y
                if x_n >= 0 and x_n < r and y_n >= 0 and y_n < c and board[x_n][y_n] == "O":
                    curr += [(x_n,y_n)]
        bfs(curr[prev:],r,c)

    
    q,r,c = [],len(board),len(board[0])
    if not r or q: return

    for i in range(r):
        for j in range(c):
            if (i==0 or j==0 or i==r-1 or j==c-1) and board[i][j] == "O":
                q += [(i,j)]
                
    bfs(q,r,c)

    for i in range(r):
        for j in range(c):   
            if board[i][j] == "O": 
                board[i][j] = "X"
            elif board[i][j] == "A":
                board[i][j] = "O"
    
    return 

#Date: September 5, 2021
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(prices) -> int:
        
    #O(n) solution; b1,s1,b2,s2 represent our maximum net profit after the first purchase, first sale, second purchase, and second sell respectively. This is testid since s1,b2, and s2 are dependant on the previous transactions. 
    
    #Additionally, changes in s1 (i.e better selling price for first purchase that would theoretically change the transaction b1 b2 s2 s1) won't follow through all the way to s2 as the final b2,s2 testues are based on earlier b1,s1 testues
    
    b1,s1,b2,s2 = -prices[0], float('-inf'), float('-inf'), float('-inf')
    
    for n in prices:
        b1 = max(b1,-n)
        s1 = max(s1, b1+n)
        b2 = max(b2, s1-n)
        s2 = max(s2, b2+n)
    
    return s2

#Date: September 6, 2021
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.

class Solution:
    def partition(s):
        
        #dfs solution. Ideally, on each recursive call, we want to check for all possible palindrome segements of the string from a starting index (which is initially 0); as we discover palindrome segements, we increment the starting index by calling recursing the dfs funtion and we append the segment to our current partition sequence (curr). 
        
        def dfs(ans,curr,rem):
            
            if not rem:
                ans += [curr]
                return
            
            for i in range(len(rem)):
                if self.check_pal(rem[:i+1]):
                    dfs(ans,curr+[rem[:i+1]],rem[i+1:])
            return ans 
        
        return dfs([],[],s)
        
    def check_pal(self,seg):
        left,right = 0,len(seg)-1
        while left < right:
            if seg[left] != seg[right]:
                return False
            left += 1
            right -= 1
        return True

#Date: September 6, 2021
#A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.
# You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was released.
# The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].
# Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key may not have had the same duration.
# Return the key of the keypress that had the longest duration. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.

def slowestKey(releaseTimes, keysPressed):
        
    #O(n) time; for each release time, we compare the current hold time to the previous and make updates depending on the respective outcomes (either longer hold time or same hold time) 
    
    ans, prev, max_hold = '',0,0
    
    for i,j in enumerate(releaseTimes):
        if (hold := j-prev) > max_hold:
            max_hold = hold
            ans = keysPressed[i]
        elif hold == max_hold:
            ans = max(ans,keysPressed[i])
        prev = j
    
    return ans

#Date: September 7, 2021
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

def minCut(s):
        
    #O(n^2) 1-D dynammic programming solution
    #dp[i] ultimately represents the solution to s[:i+1]
    #Essentially, for each substring within s, if the substring is a testid palindrome, we attempt to minimize the total cuts up to the end of the substring by checking if we can reduce dp[end of substring] by overriding it with dp[start of substring-1]+1 (becuase we will only require one more cut given that dp[:start of substring] is not a palindrome). 
    #It may not always be the case, however, that dp[end of substring] gets overrided as it may already by the minimum solution
    
    leng = len(s)
    dp = [n for n in range(-1,leng)]
    
    for i in range(leng):
        for j in range(i,leng):
            if s[i:j+1]==s[i:j+1][::-1]:
                dp[j+1] = min(dp[j+1], dp[i]+1)
                    
    return dp[-1]

#Date: September 7, 2021
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

def isMatch(s,p):
        
    #pretty much same O(n^2) dynammic programming approach as regular expression matching besides the fact that we check dp[i][j-1] for the end of a '*' sequence in the dp matrix 
    
    #dp rows represent the string and columns represent the pattern
    
    dp = [[False for c in range(len(p)+1)] for r in range(len(s)+1)]
    dp[0][0] = True
    
    #edge case because '*' can also represent nothing
    for n in range(1,len(dp[0])):
        if p[n-1]=='*': dp[0][n] = dp[0][n-1]
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            
            #1. characters in string are same or the index in the pattern is '?':
            if s[i-1]==p[j-1] or p[j-1]=='?':
                dp[i][j] = dp[i-1][j-1]
            
            #2. index in pattern is '*'
            elif p[j-1]=='*':
                
                #i. its the end of the sequence/sequence is empty (or)
                #ii. s[i-1] is a part of the sequence
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            
            #3. characters are different
    
    return dp[-1][-1]

#Date: September 8, 2021
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    
    #prefix sum array; O(n) initialization time and O(1) sum time

    def __init__(self, nums):
        self.ps = [nums[0]]
        for n in nums[1:]:
            self.ps += [n+self.ps[-1]]

    def sumRange(self, left, right) -> int:
        if left==0:
            return self.ps[right]
        return self.ps[right]-self.ps[left-1]

#Date: September 8, 2021
# Given an integer array nums, handle multiple queries of the following types:
# Update the testue of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int test) Updates the testue of nums[index] to be test.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    
    #A solution using fendwick trees: average O(n) time init and O(logn) time update/sumRange

    def __init__(self, nums):
        self.nums = nums
        self.bit = [0]+nums
        for i in range(1,length:=len(self.bit)):
            if (j:=i+(i&-i)) < length:
                self.bit[j] += self.bit[i]
        return
        
    def update(self, index, test) -> None:
        i,diff = index+1,test-self.nums[index]
        self.nums[index] = test
        while i < len(self.bit):
            self.bit[i] += diff
            i += i&-i
        return

    def sumRange(self, left, right) -> int:
        
        def prefix_sum(i):
            res = 0
            while i>0:
                res += self.bit[i]
                i -= i&-i
            return res
        
        return prefix_sum(right+1) - prefix_sum(left)

#Date: September 9, 2021
# You are given an integer n. You have an n x n binary grid grid with all testues initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

def orderOfLargestPlusSign(n,mines):
        
    #a O(n^2) time dynammic programming solution, we check how far each cell can extend in each direction - the minimum of the 4 directions (or the maximum order of a "plus sign" centered in that cell will be dp[i][j])
    
    mines = {tuple(mine) for mine in mines}
    dp = [[float('inf')]*n for i in range(n)]
    
    #right
    for i in range(n):
        count = 1
        for j in range(n):
            if (i,j) in mines: 
                count = 0
            dp[i][j] = min(dp[i][j], count)
            count += 1
   
    #left
    for i in range(-1,-(n+1), -1):
        count = 1
        for j in range(-1,-(n+1), -1):
            if (n+i,n+j) in mines: 
                count = 0
            dp[i][j] = min(dp[i][j], count)
            count += 1                
            
    #down
    for i in range(n):
        count = 1
        for j in range(n):
            if (j,i) in mines: 
                count = 0
            dp[j][i] = min(dp[j][i], count)
            count += 1
    
    #up 
    for i in range(-1,-(n+1), -1):
        count = 1
        for j in range(-1,-(n+1), -1):
            if (n+j,n+i) in mines: 
                count = 0
            dp[j][i] = min(dp[j][i], count)
            count += 1
    
    return max(max(dp[i]) for i in range(n))

#Date: September 10, 2021
#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from collections import deque
def numIslands(grid):
        
    #a bfs solution; for each '1', expand the island for as long as possible while marking all visited '1' cells with '0'/seen. Each completed expansion/bfs seach will suggest a distinct island
    
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                grid[i][j] = '0'
                self.bfs(grid,(i,j))
                ans += 1
    return ans

def bfs(self,grid,pos):
    q = deque([pos])
    while q:
        I,J = q.popleft()
        for i,j in [I+1,J],[I,J+1],[I-1,J],[I,J-1]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                q.append((i,j))

#Date: September 11, 2021
# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

def removeStones(stones):
        
    #A disjoint set solution. Each stone is considered its own disjoint set initially; everytime we run into a neighbor stone (a stone in the same column/row as a stone in another disjoint set), we will unify the two sets. The maximum # of stones we'll ultimately be able to remove is equitestent to #of stones - #of disjoint sets that remain
    
    def find(parent, i):
        if parent[i]==-1:
            return i
        return find(parent, parent[i])

    def union(parent, x, y):
        xset = find(parent, x)
        yset = find(parent, y)
        if xset==yset: return
        parent[xset] = yset
    
    dsu = {tuple(pos):-1 for pos in stones}
    for i in range(len(stones)):
        for j in range(i+1,len(stones)):
            if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                union(dsu,tuple(stones[i]),tuple(stones[j]))
    
    return len(stones)-sum([1 for x in dsu if dsu[x]==-1])

#Date: September 11, 2021
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums):
        
    #An O(n) dynammic solution solution; we cannot rob both the first and last house. Thus, we will take the maximum we can rob between cases where we exclude the first/last houses respectively
    
    def helper(dp): 
        dp[1] = max(dp[0],dp[1])
        for i in range(2,len(dp)):
            dp[i] = max(dp[i]+dp[i-2],dp[i-1])
        return dp[-1]
    
    if len(nums) in {1,2}: return max(nums)
    return max(helper(nums[1:]), helper(nums[:-1]))

#Date: September 12, 2021
#https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, test = 0, neighbors = None):
        self.test = test
        self.neighbors = neighbors if neighbors is not None else []
"""
def cloneGraph(node): 
    
    #A dfs solution with a hash table (which is formmatted as such -> node object: copy of node object). For cloned nodes, if a neighbor node has already been copied, add it to its adjacency list, otherwise, create it first.
    
    def dfs(seen,node):
        for adj in node.neighbors:
            if adj not in seen:
                seen[adj] = Node(adj.test)
                dfs(seen,adj)
            seen[node].neighbors += [seen[adj]]
    
    if not node: return
    seen = {node: Node(node.test)}
    dfs(seen,node)
    return seen[node]

#Date: September 13, 2021
#https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(isConnected):
        
        #a disjoint set union-find implementations with an O(n^2) runtime; the number of disjoint sets ultimately = number of provinces
        
        n = len(isConnected)
        dtstr = {x:-1 for x in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]: self.union(dtstr,i,j)
        return sum([1 for x in dtstr if dtstr[x]==-1])
        
    def find(self,dtstr, i): #with path compression to optimize
        if dtstr[i]==-1: return i
        dtstr[i] = self.find(dtstr, dtstr[i])
        return dtstr[i]
        
    def union(self,dtstr,i,j):
        I,J = self.find(dtstr,i), self.find(dtstr,j)
        if I==J: return
        dtstr[I] = J

#Date: September 14, 2021
#https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
def findKthLargest(nums,k):
        
    #An O(nlogn) time approach using a min heap (I think its more elegant than using .sort() lol). Essentially, the root of the heap will always maintain the smallest element of the heap; will limit the heap to k elements while ensuring they are k of the largest elements (that have been traversed).

    hp = []

    for n in nums:
        heapq.heappush(hp, n)
        if len(hp) > k: heapq.heappop(hp) #heappop = removing root node

    return hp[0]

#Date: September 17, 2021
#https://leetcode.com/problems/single-number-ii/

def singleNumber(nums):
        
    #same O(n) implementation as single number I
    
    seen = {}
    
    for n in nums:
        if n not in seen:
            seen[n] = 1
            continue
        return n
    
#Date: September 18, 2021
#https://leetcode.com/contest/biweekly-contest-61/problems/count-number-of-pairs-with-absolute-difference-k/

def countKDifference(nums,k):

    #O(n^2) intutive solution

    ans = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)): 
            if abs(nums[i]-nums[j]) == k:
                ans += 1
    return ans

#Date: September 18, 2021
#https://leetcode.com/contest/biweekly-contest-61/problems/find-original-array-from-doubled-array/

def findOriginalArray(changed):
        
    #O(nlogn) time. The theory behind the solution is to keep track of the frequency of each number's apperance. We will traverse the array in increasing order (because if the array were to be "doubled" it would be the smallest elements that would be multiplied by 2) and everytime we come across a number, we deduct its frequency by one. Moreover, if its double still has a frequency > 1, we reduce the its frequency by one as well. 
    
    if len(changed)%2==1 or not changed: #odd length can't be "doubled array"
        return []
    
    counter, ans = Counter(changed), []

    for n in sorted(changed):
        if counter[n]: 
            counter[n] -= 1
            if counter[n*2]:
                counter[n*2] -= 1
                ans += [n]
                
    if len(ans)*2==len(changed):
        return ans
    return []

#Date: September 18, 2021
#https://leetcode.com/problems/maximum-length-of-pair-chain/submissions/

def findLongestChain(pairs):
        
    #A common greedy implementation; we would like to continuously select the chains that end ASAP given a starting index point
    
    start, ans = float('-inf'), 0
    
    for inter in sorted(pairs, key=lambda p:p[1]):
        if inter[0] > start:
            ans += 1
            start = inter[1]
    
    return ans

#Date: September 19, 2021
#https://leetcode.com/problems/trapping-rain-water/

def trap(height):
        
    #a stack approach. We keep track of the highest elevation we've encountered so far; for every smaller elevation, we will append their testues to a stack. Given such there are two possible calculations we can make:
    
    #1. we encounter an elevation that < tallest but can still trap water:
        
        #we'll see how much it can trap and flatten out all holes that were filled (to prevent repeated calculations)
    
    #2. we encounter an elevation that >= tallest
    
        #we will fully calculate the water trapped between previous tallest elevation and new tallest elevation
    
    stack,l_m,ans = [],0,0
    
    for h in height:
        if not l_m:
            l_m = h
            continue
        
        #full calculation
        if h >= l_m:
            while stack:
                ans += l_m - stack.pop()
            l_m = h
            continue
        
        #partial calculation
        i = -1
        while stack and i >= -len(stack) and h > stack[i]:
            ans += h-stack[i]
            stack[i] = h
            i -= 1
           
        stack += [h]
        
    return ans

#Date: September 22, 2021
#https://leetcode.com/problems/gas-station/

def canCompleteCircuit(gas,cost):
        
    #A worst case O(n^2) time solution; try starting on a station if net gas gained/lost is positive by the time you get to the next. If that station allows us to complete the loop, return its index.
    
    net = [gas[i]-cost[i] for i in range(len(gas))]
    
    for i,j in enumerate(net):
        possi = i
        if j >= 0:
            curr = 0 
            for _ in range(len(net)):
                if curr < 0 : break
                if i == len(net): i=0
                curr += net[i]
                i += 1
            if curr >= 0:
                return possi
    
    return -1

#Date: September 24, 2021
#https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3986/

def tribonacci(n):
        
    #intuitive recursive solution with memoization optimization
    
    def helper(n,seen):
        
        if n==0: return 0
        if n in [1,2]: return 1
        
        if n in seen: return seen[n]
        seen[n] = helper(n-1,seen)+helper(n-2,seen)+helper(n-3,seen)
        
        return seen[n] 
    
    return helper(n,{})

#Date: September 25, 2021
#https://leetcode.com/problems/binary-search/submissions/

def search(nums,target):
        
        #iterative implementation of binary search
        
        l,h = 0,len(nums)-1
        while l <= h:
            i = (l+h)//2
            if (curr:=nums[i]) == target: return i
            elif curr > target: h = i-1
            else: l = i+1
        return -1

#Date: September 25, 2021
#https://leetcode.com/submissions/detail/560805870/

from collections import deque
def shortestPath(grid,k):
    
    #bfs: queue contents = row,column,remaining barrier destructions
    
    def bfs(queue,steps,seen):
        for i in range(len(queue)):
            pos = queue.popleft()
            r,c = pos[0],pos[1]
            if grid[r][c] == 1:
                if pos[2] > 0: pos[2] -= 1
                else: continue
            seen.add((r,c))
            if (r,c) == (len(grid)-1,len(grid[0])-1): return steps #base case
            for R,C in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= R < len(grid) and 0 <= C < len(grid[0]) and (R,C) not in seen:
                    queue += [[R,C,pos[2]]]
        return queue
        
    q = deque([[0,0,k]]) 
    seen = set()
    steps = 0
    while q:
        if type(next_layer := bfs(q,steps,seen)) == int:
            return next_layer
        q = next_layer
        steps += 1
        
    return -1

#Date: September 25, 2021
#https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import bisect
def jobScheduling(startTime,endTime,profit):
        
        #O(nlogn) dynammic programming solution, an enhanced solution built-upon the O(n^2) approach. At each job, we have two choices:
        
        #1. skip the job --> dp[i] = dp[i-1]
        #2. take the job; if we chose this option, we will be building upon the most recent non-overlapping job (if it exists)
        
        #this algorithm prevents the repetitive comparisons from dp[i] to dp[j] in the O(n^2) solution
        
        jobs = sorted(zip(startTime,endTime,profit), key=lambda x:x[1])
        ends,dp = [x[1] for x in jobs], [jobs[0][2]]+[0]*(len(jobs)-1)
        
        for i in range(1,len(dp)):
            
            #skip job 
            dp[i] = dp[i-1]
            
            #take job
            chain = bisect.bisect_right(ends,jobs[i][0])-1

            #compares the two options
            dp[i] = max(dp[i],jobs[i][2]+(dp[chain] if chain>=0 else 0))
        
        return dp[-1]

#September 26, 2021
#https://leetcode.com/problems/min-cost-climbing-stairs/

def minCostClimbingStairs(cost):
        
    #O(n) dynammic programming, the minimum cost of reaching stair 'i' is will be attained from climbing up from the cheapest option between the last 2 stairs 
    
    if len(cost) == 2: return min(cost)
    
    for i in range(2,len(cost)):
        cost[i] = min(cost[i]+cost[i-1],cost[i]+cost[i-2])
    
    return min(cost[-1],cost[-2])

#September 26, 2021
#https://leetcode.com/problems/edit-distance/

def minDistance(word1,word2):
        
    #an O(mn) time 2-D dynammic programming approach (very similar to wildcard or expression matching where dp[i][j] is determined from a set of comparable conditions). Columns and rows represent word1 and word 2 respectively.
    
    #There will be two main cases:
    
    #1. the last letters of the two dp strings match:
        #dp[i][j] = top left corner
    
    #2. the last letters dont match:
        #dp[i][j] = min(replace (top left corner) , insert (left) , delete (top)) + 1 (becuase they are operations)
    
    dp = [[n for n in range(len(word1)+1)]] + [[i]+[0]*len(word1) for i in range(1,len(word2)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if word1[j-1]==word2[i-1]: 
                dp[i][j] = dp[i-1][j-1]
                continue
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
    
    return dp[-1][-1]

#October 1, 2021
#https://leetcode.com/problems/longest-common-subsequence/submissions/

def longestCommonSubsequence(text1,text2):

    #classic O(n^2) time 2-d dynammic programming solution (rows = text1, cols = text2). If two characters in dp cell are the same, max-substring increases in length by 1
    
    dp = [[0 for _ in range(len(text2)+1)] for __ in range(len(text1)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if text1[i-1]==text2[j-1]: 
                dp[i][j] = dp[i-1][j-1]+1
                continue
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) #check left/top because word2 could be continuing off a substring in word1 and vice versa
    return dp[-1][-1]

#October 2, 2021:
#https://leetcode.com/contest/biweekly-contest-62/problems/convert-1d-array-into-2d-array/
def construct2DArray(original,m,n):
        
    #O(n) intuitive solution
    
    if m*n != len(original):
        return []

    ans,curr,count = [],[],1
    for x in original:
        curr += [x]
        count += 1
        if count == n+1:
            ans += [curr]
            curr = []
            count = 1
    return ans

#October 2, 2021
#https://leetcode.com/contest/biweekly-contest-62/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

def numOfPairs(nums,target):
        
    #O(n^2) intuitive solution
    
    ans = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target and i!=j: ans +=1

    return ans

#October 2, 2021:
#https://leetcode.com/problems/max-consecutive-ones-iii/

def longestOnes(nums,k):
        
    #O(n) two pointer approach; while we attempt to extend our right pointer we can run into the following scenarios:
    
    #1. run into a 1:
        #keep extending
    
    #2. run into a 0:
        #increment the left pointer until theres space for the 0 (if we dont have any more k left)
        #otherwise keep extending
    
    ans, l = 0, 0
    
    for r in range(len(nums)):
        if nums[r] == 0:                       
            if not k:                        
                while nums[l] != 0 : l += 1
                l += 1
            else : 
                k -= 1                     
        ans = max(ans,r-l+1)    
        
    return ans

#Date: October 2, 2021
#https://leetcode.com/contest/biweekly-contest-62/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey,k):
        
        #same idea behind max consecutive ones III, we just need to determine the longest subarray with at most k 'F's or 'T's
        
        pos1,pos2 = [(1 if x=='T' else 0) for x in answerKey], [(1 if x=='F' else 0) for x in answerKey] #possibilities that answer will be subarray of 'T's and 'F's respectively
        return max(self.solve(pos1,k),self.solve(pos2,k))
        
    def solve(self,arr,k):
        res,l = 0,0
        for i in range(len(arr)):
            if arr[i]==1: 
                res = max(res,i-l+1)
                continue
            if not k:
                while arr[l]!=0:
                    l += 1
                l += 1
            else: k -= 1
            res = max(res,i-l+1)
        return res

#Date: October 3, 2021
#https://leetcode.com/problems/island-perimeter/

def islandPerimeter(grid):
        
    #intuitive O(mn) solution, for each piece of land, check if any sides are exposed to water (consist of the perimeter)
    
    def testid(r,c):
        if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]: return False
        return True
    
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]: ans += sum((1 if testid(I,J) else 0) for I,J in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]])
    return ans

#Date: October 4, 2021
#https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/

def maxSubarraySumCircular(nums):
        
        #O(n) kadane's algorithm; ans = max(the max subarray sum, the total sum - the min subarray sum) because there are 2 cases (either max subarray is or is not circular)
        
        cma,cmi,gma,gmi = [nums[0]]*4
        for n in nums[1:]:
            cma = max(n,n+cma)
            cmi = min(n,n+cmi)
            gma = max(gma,cma)
            gmi = min(gmi,cmi)
        
        if all(x<0 for x in nums): return gma #edge case
        return max(gma,sum(nums)-gmi)

#Date: October 8, 2021
#https://leetcode.com/problems/copy-list-with-random-pointer/

def copyRandomList(head):
        
        #two-pass O(n) solution using hashmaps; first iteration will be creating the base linked list {old node:new node} and the second will connect the random nodes
        
        if not head: return None
        
        copy = {None:None} 
        
        #1. 
        curr = head
        while curr:
            copy[curr] = Node(curr.test)
            curr = curr.next

        #2.
        curr = head
        while curr:
            newnode = copy[curr]
            newnode.next,newnode.random = copy[curr.next],copy[curr.random]
            curr = curr.next
        
        return copy[head] 

#October 8, 2021
#https://leetcode.com/problems/maximal-square/submissions/

def maximalSquare(matrix):

    #An o(mn) time 2-d top down dynammic programming solution.
    #we initialize the dp matrix with ones in row/column 0 and traverse the rest; while preforming this, and if we run into a case where matrix[i][j]==1, there are two cases:
        
        #1. it cannot build on an existing square:
            #dp[i][j]==1
        
        #2. it can build onto an existing square:
            #dp[i][j] must be wrapped from left to top with testid testues in dp matrix and will build on the least of the three testues
        
    ans = 0
    dp = [[(1 if matrix[r][c]=='1' and (r==0 or c==0) else 0) for c in range(len(matrix[0]))] for r in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if all([i,j]) and int(matrix[i][j]):
                dp[i][j] = max(1,(min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1 if all([dp[i-1][j],dp[i-1][j-1],dp[i][j-1]]) else 0))
            ans = max(ans,dp[i][j]**2)
    

    return ans

#Date: October 9, 2021
#https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

from collections import Counter
def waysToPartition(nums,k_):
        
        #An O(n) time solution; keep psa and frequency hashmaps for occurences of psa testues on both left and right of partitions. This allows us to check for the maximum partitions both with and without using the k testue change.
        
        #given a psa, number of partitions == freq[psa[-1]//2] if the total sum of the array % 2 == 0 in the first place
        
        ans = 0
        psa = [nums[0]]
        for n in nums[1:]:
            psa += [psa[-1]+n]
        r_freq,l_freq = Counter(psa),Counter()
        
        #no k usage
        if psa[-1]%2==0: ans = r_freq[psa[-1]//2] - (1 if psa[-1]==psa[-1]//2 else 0)
            
        
        #k usage
        for i in range(len(psa)):
            
            diff = k-nums[i]

            if (psa[-1]+diff)%2==0:
                ans = max(ans,l_freq[(psa[-1]+diff)//2] + r_freq[((psa[-1]+diff)//2)-diff] - (1 if psa[-1]==((psa[-1]+diff)//2)-diff else 0)) 
                
            l_freq[psa[i]] += 1
            r_freq[psa[i]] -= 1
            
        
        return ans

#Date: October 9, 2021
#https://leetcode.com/problems/word-break/submissions/

def wordBreak(s,wordDict):
        
    #O(nm) time dynammic programming solution. dp[i] = answer for s[:i]. For dp[i] to hold true it must build on a previous substring whose dp[i]==True while also having the substring between the previous/current indices in question to exist within wordDict.
    
    dp,wds = [True]+[False]*len(s), set(wordDict)
    
    for i in range(1,len(dp)):
        for j in range(i):
            if all([dp[j],s[j:i] in wds]):
                dp[i] = True
                break
    
    return dp[-1]

#October 9, 2021
#https://leetcode.com/problems/bitwise-ors-of-subarrays/submissions/

def subarrayBitwiseORs(arr):
        
    #An O(n) time set approach; the crux of the solution lies in the set "curr"; as we traverse the array, curr keeps track of all distinct answers if we build on previous contiguous testues. Hence, this allows us to constantly update res with new curr testues
    
    curr,res = set(),set()
    for n in arr:
        curr={n|x for x in curr}|{n}
        res |= curr
    return len(res)

#October 11, 2021
#https://leetcode.com/problems/linked-list-cycle/submissions/

def hasCycle(head):
        
    #O(n) time and O(1) space solution; flag the testue of each node we visited with 'N'. If we see 'N' twice before finishing the list traversal, there is a cycle
    
    while head:
        if head.test=='N': return True
        head.test = 'N'
        head = head.next
    return False

#October 11, 2021:
#https://leetcode.com/problems/linked-list-cycle-ii/submissions/

def detectCycle(head):
        
    #O(n) time solution with hashmap, set will hold seen node
    
    i,seen = 0,set()
    while head:
        if head in seen: return head
        seen.add(head)
        head = head.next
        i += 1
    return None

#October 11, 2021
#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/

def longestIncreasingPath(matrix):
        
    #dfs + memoization. The key is to realize that the intuitive dfs holds numerous repeats in calculations. Given that the answer starting from a position i,j has already been calculated, the next time we manage to reach that respective position, we can simply chain onto it.
    
    def testid(i,j):
        if 0<=i<len(matrix) and 0<=j<len(matrix[0]): return True
        return False
    
    @cache
    def dfs(i,j):
        res = 1
        for I,J in [[r,c] for r,c in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]] if testid(r,c)]:
            if matrix[I][J] > matrix[i][j]: res = max(res,1+dfs(I,J))
        return res
    
    return max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))

#Date: October 14, 2021
#https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(nums):
        
    #O(n) two-pass solution. Consider each subarray seperated by a 0 as seperate by nature. Within each of these subarrays, there may either contain an even or odd number of negative integers; the main point to realize is that if the count of negative integers is odd, the maximum sub-subarray would contain either all but the leftmost/rightmost negative integer.
    
    def traverse(s,e,dirc):
        curr,res = 1,float('-inf')
        for i in range(s,e,(1 if dirc=='r' else -1)):
            curr *= nums[i]
            res = max(res,curr)
            if nums[i]==0: curr = 1
        return res
    
    return max(traverse(0,len(nums),'r'),traverse(len(nums)-1,-1,'l'))

#October 15, 2021
#https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/submissions/

def getMaxLen(nums):
        
    #Same O(n) two-pass concept as previous solution except our curr holds more information as we traverse:
    
    #curr = [longest +ve product subarr,length of subarr on hold (cannot contribute to curr[0] yet) because there are an odd # of -ve numbers ,#of -ve numbers in current subarr]
    
    def trav(dirc):
        ans,curr = 0,[0]*3 #[+,temp,-]
        for n in nums[::dirc]:
            if not n: 
                curr=[0]*3
                continue    
            if n<0: 
                curr[1] += 1
                curr[2] += 1
                if curr[2]==2: 
                    curr[0] += curr[1]
                    curr[1],curr[2] = 0,0
            else:
                if curr[2]%2==1: curr[1] += 1
                else: curr[0] += 1
            ans = max(ans,curr[0])
        return ans
    
    return max(trav(1),trav(-1))

#Date: October 15, 2021
#https://leetcode.com/problems/max-points-on-a-line/

def maxPoints(points):
        
    #An O(n^2) math solution; for each point, we take advantage of the small constestts and traverse all other points and group together all points with the same slope through a dictionary; we can then update our local answer to the global answer
    
    ans = 0 
    for i in points:
        curr,dup,lines = 0,0,{}
        for j in points:
            if i==j: 
                dup += 1
            else:
                if i[0]==j[0]: m = float('inf') #vert
                else: m = (j[1]-i[1])/(j[0]-i[0])
                lines[m] = (lines[m] if m in lines else 0)+1
                curr = max(curr,lines[m])
        ans = max(ans,curr+dup)
    return ans

#Date: October 16, 2021
#https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

def minMovesToSeat(seats,students):
     
    #sort the seats and students and move each student to the seat closest in proximity
        
    seats.sort()
    students.sort()
    ans = 0
    for i in range(len(seats)-1,-1,-1):
        ans += abs(seats[i]-students[i])
    return ans

#Date: October 16, 2021
#https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

def winnerOfGame(colors):
        
    #find 3 or more consecutive 'A's or 'B' to determine number of moves that can be made by both players
    
    a,b = 0,0
    ca,cb = 0,0
    for x in colors:
        if x=='A': 
            cb = 0
            ca += 1
            if ca >= 3: a += 1
        else:
            ca = 0
            cb += 1
            if cb >= 3: b += 1
    if a>b: return True
    return False

#Date: October 16, 2021
#https://leetcode.com/problems/container-with-most-water/submissions/

def maxArea(height):
        
    #An O(n) time solution; essentially we need to find the largest area
    #to do so, we will maintain two pointers two start at the maximum possible width. In order to accomodate for possible area increases due to height, we will either increment or decrement the left and right pointers respectively to attain potentially larger heights
    
    ans,l,r = 0,0,len(height)-1
    while l<r:
        ans = max(ans,(r-l)*min(height[l],height[r]))
        if height[l]<height[r]: l+=1
        else: r-=1
    return ans

#Date: October 17, 2021
#https://leetcode.com/problems/word-break-ii/

def wordBreak(s,wordDict):
        
    #Intuitive O(2^n) dfs. 
    
    def dfs(curr,rem,wds):
        nonlocal ans
        if not rem: 
            ans += [curr[1:]]
            return
        for i in range(len(rem)):
            if rem[:i+1] in wds: dfs(curr+' '+rem[:i+1],rem[i+1:],wds)
    
    ans = []
    dfs('',s,set(wordDict))
    return ans

#Date: October 17, 2021
#https://leetcode.com/problems/path-sum-iii/

class Solution:
    def pathSum(self, root, targetSum):
        
        #keep a prefix sum array (stored in hashmap) starting from each node (tip of a path) and dfs to find all paths that branch down from there. If psh[current sem - target] exists, then a testid path has been found.
        
        from collections import defaultdict
        
        self.res,self.psh = 0,defaultdict(int)
        self.psh[0] = 1 #extra 0 because no nodes also counts as a possible path
        
        def dfs(node,curr):
            if not node: return
            curr += node.test
            self.res += self.psh[curr-targetSum]
            self.psh[curr] += 1
            dfs(node.left,curr)
            dfs(node.right,curr)
            self.psh[curr] -= 1
        
        dfs(root,0)
        return self.res

#Date: October 18, 2021
#https://leetcode.com/problems/lru-cache/submissions/

class LRUCache:
    
    from collections import deque
    
    #We will use a deque to keep track of most recently used keys
    
    def __init__(self, capacity: int): #O(n)
        self.cache, self.cap = {}, capacity
        self.prevs = deque()

    def get(self, key: int) -> int: #O(1)
        if key in self.cache: 
            self.prevs.remove(key)
            self.prevs += [key]
            return self.cache[key]
        return -1

    def put(self, key: int, testue: int) -> None: #O(1)
        if not self.cap: return
        if key not in self.cache: 
            self.prevs += [key]
        else: 
            self.prevs.remove(key)
            self.prevs += [key]
        self.cache[key] = testue
        if len(self.cache) > self.cap: self.cache.pop(self.prevs.popleft())

#Date: October 20, 2021
#https://leetcode.com/problems/reverse-words-in-a-string/submissions/

def reverseWords(s):
        
    #a one pass O(n) solution put words in queue and join together
    
    from collections import deque
    ans,curr = deque(),''
    for x in s:
        if x==' ' and curr: 
            ans.appendleft(curr)
            curr = ''
            continue
        if x!=' ': curr += x
    if curr: ans.appendleft(curr)
    return ' '.join(ans)

#Date: October 20, 2021
#https://docs.google.com/document/d/1SqwKqJAgzEPRT6zIDaM21DU5dzglY4BODkMKIR7u0IM/edit

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = float('-inf')
    
    def maxPathSum(self, root) -> int:
        
        #an O(2^n) dfs + subtree dynammic programming solution. for each sub-root, the answer is equal to the maximum of the node itself, the node+left or right subtree, or the node + both subtrees. However, when passing the testue up to calculate the answer for the parent nodes, we only take the max between the node and the node + left or right subtree as we must maintain the definition of a "path"
        
        def dfs(node):
            if not node: return 0
            l,r = dfs(node.left),dfs(node.right)
            res = max(node.test,node.test+l,node.test+r,node.test+l+r) 
            self.ans = max(self.ans,res)
            return max(node.test,node.test+l,node.test+r)
        
        dfs(root)
        return self.ans

#Date: October 21, 2021
#https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/

import random
class RandomizedSet:
    
    #Intuitive O(1) solution with standard sets

    def __init__(self):
        self.rngs = set()

    def insert(self, test: int) -> bool:
        if test in self.rngs: return False
        self.rngs.add(test)
        return True

    def remove(self, test: int) -> bool:
        if test not in self.rngs: return False
        self.rngs.remove(test)
        return True

    def getRandom(self) -> int:
        return random.sample(self.rngs,1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(test)
# param_2 = obj.remove(test)
# param_3 = obj.getRandom()

#Date: October 21, 2021
#https://leetcode.com/problems/sort-list/

def sortList(head):
        
    #O(nlogn) array solution. Append all nodes then sort
    
    if not head: return None 
    
    arr = []
    curr = head
    while curr:
        arr += [curr]
        curr = curr.next
    arr = sorted(arr, key=lambda x:x.test)
    for i in range(len(arr)):
        arr[i].next = (arr[i+1] if i!=len(arr)-1 else None)
    return arr[0]

#October 21, 2021
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
        
    #O(logn) intuitive binary search: if m > r --> pull left to mid (minimum testue is between m and r), if m < r: pull right to mid (minimum testue is between l and m because m to r is strictly increasing)
    
    l,r = 0,len(nums)-1    
    while True:
        if l==r: return nums[l]
        if r-l==1 : return min(nums[l],nums[r]) #an edge case that defies the general algorithm
        m = (l+r)//2
        if nums[m]>nums[r]: l = m
        else: r = m

#October 22, 2021
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

def findMin(nums):
        
    #same idea as "Find Minimum in Rotated Sorted Array" with an extra condition. Time complexity is O(n) in the worst case 
    
    l,r = 0, len(nums)-1
    while l < r:
        m = (l+r)//2
        if nums[m] > nums[r]: #ans has to be between m+1 and r
            l = m+1
        elif nums[m]==nums[r]: #only case where this would happen is when nums[l] = nums[m] = nums[r], so we decrement and try and re-enter the binary search
            r -= 1
        else:
            r = m #ans has to be between l and m
    return nums[l]

#October 22, 2021
#https://leetcode.com/problems/min-stack/submissions/

class MinStack:

    def __init__(self): #O(1)
        self.stack = [] #each node is (testue,minimum up to testue)

    def push(self, test: int) -> None: #O(1)
        if not self.stack: self.stack += [(test,test)]
        else: self.stack += [(test,min(test,self.stack[-1][1]))]

    def pop(self) -> None: #O(1)
        self.stack.pop()

    def top(self) -> int: #O(1)
        return self.stack[-1][0]

    def getMin(self) -> int: #optimize to O(1) using dp
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(test)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Date: October 23, 2021
#https://leetcode.com/problems/best-sightseeing-pair/submissions/

def maxScoreSightseeingPair(testues):
        
    #O(n) dp solution; we can manipulate the formula tests[i]+tests[j]+i-j so that we continuously update a local max variable with the most idea tests[i]+i testue. We can then use this to influence a global max that will be equal to local_max + tests[j] - j
    
    loc,ans = 0,0
    for i,j in enumerate(testues):
        ans = max(ans,loc+j-i)
        loc = max(loc,i+j)
    return ans

#October 23, 2021
#https://leetcode.com/problems/search-a-2d-matrix/submissions/

def searchMatrix(matrix,target):
        
    #binary search in matrix; we will have a custom index from 0 to n*m - 1
    #i,j = custom//cols, custom % cols
    
    l,r = 0,len(matrix)*(cols:=len(matrix[0]))-1
    while l<=r:
        m = (l+r)//2
        i,j = m//cols, m%cols
        if (curr:=matrix[i][j])==target: return True
        elif curr > target: r=m-1
        else: l=m+1
    return False

#Date: October 23, 2021
#https://leetcode.com/problems/dungeon-game/

def calculateMinimumHP(matrix):

    #O(mn) time bottom-up dp, we can only move left or up from the algorithm's standpoint. 
    
    #similar concept as the top-down dp used for problems that require the shortest distance from top left corner to bottom right corner
    
    for i in range(-1,-(len(matrix)+1),-1):
        for j in range(-1,-(len(matrix[0])+1),-1):
            if all([i==-1,j==-1]): 
                matrix[i][j] = (abs(matrix[i][j])+1 if matrix[i][j]<0 else 1) 
                continue
            if j!= -1:
                prev = matrix[i][j]
                matrix[i][j] = 1 if matrix[i][j+1]-matrix[i][j]<=0 else matrix[i][j+1]-matrix[i][j]
            if i!= -1:
                if j==-1: matrix[i][j] = 1 if matrix[i+1][j]-matrix[i][j]<=0 else matrix[i+1][j]-matrix[i][j]
                else: matrix[i][j] = min(matrix[i][j], 1 if matrix[i+1][j]-prev<=0 else matrix[i+1][j]-prev) 
    
    return matrix[0][0]

#Date: October 23, 2021
#https://leetcode.com/problems/count-complete-tree-nodes/

class Solution:
    def __init__(self):
        self.ans = 0
        
    def countNodes(self, root) -> int:
        
        #intuitive solution
        
        def dfs(node):
            if not node: return
            self.ans += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans

#October 24, 2021
#https://leetcode.com/problems/next-greater-element-i/submissions/

def nextGreaterElement(nums1,nums2):
        
    #O(n^2) intuitive hashmap solution
    
    dic = {j:i for i,j in enumerate(nums2)}
    ans = []
    for n in nums1:
        pos = [temp for x in dic if (x>n and (temp:=dic[x]-dic[n])>0)]
        ans += [nums2[dic[n]+min(pos)] if pos else -1]
    return ans

#Date: October 28, 2021
#https://leetcode.com/problems/sliding-window-maximum/submissions/

def maxSlidingWindow(nums,k):
        
        #An O(n) deque/priority queue solution. We will keep a deque with indices (that is kept in reversed key=their testue). On each window position, we will simply return deque[nums[0]]
        
        from collections import deque
        dq = deque([])  
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]: dq.pop() #removing all smaller elements
            dq += [i]
            if i+1 >= k: ans += [nums[dq[0]]]
            if i-dq[0]+1 >= k: dq.popleft() #if window moves out of range
        return ans

#Date: October 28,2021
#https://leetcode.com/problems/rotting-oranges/

def orangesRotting(grid):
        
        #Intuitive O(2^n) BFS solution, keep searching until you've either rotted all the fresh oranges or till you've hit a limit (no more oranges you can contaminate)
        
        seen,fr = set(),set()
        mvs = [[0,1],[0,-1],[1,0],[-1,0]]
        qu = []
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1: 
                    fr.add((i,j))
                elif grid[i][j]:
                    seen.add((i,j))
                    qu += [(i,j)]

        while qu and fr:
            temp = []
            done = False
            for pos in qu:
                if pos in fr: fr.remove(pos)
                if not fr: 
                    done = True
                    break
                seen.add(pos)
                for r,c in mvs:
                    R,C = pos[0]+r,pos[1]+c
                    if all([0<=R<len(grid),0<=C<len(grid[0]),(R,C) not in seen]):
                        if grid[R][C]: temp += [(R,C)]
            if done: break
            qu = temp   
            ans += 1
        
        if not fr: return ans
        return -1

#Date: October 29, 2021
#https://leetcode.com/problems/arithmetic-slices/submissions/

def numberOfArithmeticSlices(nums):
        
    #O(n) top-down dp + basic math. An arithmetic array with length x (xEZ+, x>=3) has sigma i=3 to x {i-2} possible subarrays that can be derived. We will expand an arithmetic array for as long as possible as we traverse nums.
    
    ans = 0
    curr,temp = [],0
    for n in nums:
        if len(curr)==1 or not curr: 
            curr += [n]
            continue
        if n-curr[-1]==curr[-1]-curr[-2]:
            curr += [n]
            temp += len(curr)-2
        else:
            ans += temp
            curr,temp = [curr[-1],n],0
    ans += temp
    return ans

#Date: October 30, 2021 (failed the contest unfortnately)
#https://leetcode.com/problems/two-best-non-overlapping-events/submissions/

def maxTwoEvents(events):
        
    #An O(nlogn) dp + binary search solution. Same idea as weighted scheduling except if we choose to take two jobs, we take job profit + dp[previous none overlapping job profit]
    
    import bisect
    
    events.sort(key=lambda x:x[1])
    ans = 0
    bs,dp = [events[i][1] for i in range(len(events))], [events[0][2]]
    for i in range(1,len(events)): dp += [max(dp[-1],events[i][2])]
    
    for i in range(len(events)):
        prev = bisect.bisect_right(bs,events[i][0]-1)
        ans = max(ans,events[i][2]+(dp[prev-1] if prev else 0))
    
    return ans

#Date: October 31, 2021 🎃
#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/

# class Node:
#     def __init__(self, test, prev, next, child):
#         self.test = test
#         self.prev = prev
#         self.next = next
#         self.child = child
        
def flatten(head):
        
    #brute force dfs solution. For each node with a child, traverse till the end of both paths (current node and child node). If their final nodes are distinct (different layers) append the child's layer to the current node's.
    
    def helper(curr):
        
        childi,childf,curri,currf = curr.child,curr.child,curr,curr
        while currf.next:
            if currf!=curri and currf.child: helper(currf)
            currf = currf.next
        while childf.next:
            if childf!= childi and childf.child: helper(childf)
            childf = childf.next
        
        if currf != childf: #diff layers
            curri.child = None
            temp = curri.next
            curri.next = childi
            childi.prev = curri
            childf.next = temp
            if temp: temp.prev = childf
            
    curr = head
    while curr:
        if curr.child: helper(curr)
        curr = curr.next
    
    return head

#Date: October 31, 2021
#https://leetcode.com/problems/plates-between-candles/

from collections import deque
class Solution:
    def __init__(self):
        self.ans = []
    def platesBetweenCandles(self, string,queries):
        
        #O(n) psa + dp solution, query = [psa[op+dpr[op]]-psa[ed-dpl[ed]]]
        #psa = prefix sum array for plates up till a certain index
        #dpl[i], dpr[i] = closest candle to left and right of an index respectively
        #Note: everything is 1-indexed
        
        psa,dpl,dpr = [0],[None],deque([None])
        
        for i in range(len(string)):
            dpri = -(i+1)
            psa += [(psa[-1]+1 if string[i]=='*' else psa[-1])]
            dpl += [0 if string[i]=='|' else (dpl[-1]+1 if type(dpl[-1])==int else None)]
            dpr.appendleft(0 if string[dpri]=='|' else (dpr[0]+1 if type(dpr[0])==int else None))
        dpr.appendleft(None)
        dpr.pop()
        
        for q in queries:
            op,ed = q[0]+1,q[1]+1
            if op==ed or any([dpr[op]==None,dpl[ed]==None]): self.ans += [0]
            else: 
                temp = psa[ed-dpl[ed]]-psa[op+dpr[op]]
                self.ans += [temp if temp>0 else 0]
        
        return self.ans

#Date: November 1, 2021
#https://leetcode.com/problems/unique-paths-iii/submissions/

class Solution:
    def __init__(self):
        self.ans = 0
    def uniquePathsIII(self, grid):
        
        #O(2^n) brute force backtracking/dfs
        
        opr,opc,blocks = None,None,0
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j]<0: blocks += 1 
                elif grid[i][j]==1: opr,opc = i,j
                    
        def dfs(seen,r,c):
            seen.add((r,c))
            if grid[r][c]==2:
                if len(seen)==len(grid)*len(grid[0])-blocks: self.ans += 1
                seen.remove((r,c))
                return
            for R,C in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if all([(R,C) not in seen,0<=R<len(grid),0<=C<len(grid[0])]):
                    if grid[R][C]!=-1: dfs(seen,R,C)
            seen.remove((r,c))
        
        dfs(set(),opr,opc)
        
        return self.ans

#Date: November 3, 2021
#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        
        #reverse post-order dfs; construct the LL bottom-up. 
        #Note: Only connections are altered, nodes themselves are never disconnected
        
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root 

#Date: November 2, 2021
#https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumOfLeftLeaves(self, root) -> int:
        
        #intuitive dfs
        
        def dfs(node,left=False):
            if not node: return
            if left and not any([node.left,node.right]):
                print(node.test)
                self.ans += node.test
                return
            dfs(node.left,True)
            dfs(node.right)
        dfs(root)
        return self.ans

#Date: November 4, 2021
#https://leetcode.com/problems/wiggle-subsequence/submissions/

def wiggleMaxLength(nums):
        
    #An O(n) dp solution. Remove all elements that generate continuouse + or - differences and then take len(new nums) - 1
    
    p,n = 1,1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]>0: p=n+1
        elif nums[i]-nums[i-1]<0: n=p+1
    return max(p,n)

#Date: November 4, 2021
#https://leetcode.com/problems/arranging-coins/submissions/

def arrangeCoins(sn):
        
    #O(1) arithmetic series solution, Sn = n((1+n)/2), 0 = n^2+n-2Sn (positive root = desired answer)
    
    import math
    
    def quad():
        d = math.sqrt(1+8*sn)
        res1 = (-1 + math.sqrt(1+4*2*sn))/(2)
        res2 = (-1 - math.sqrt(1+4*2*sn))/(2)
        return max(res1,res2)
    
    return int(quad())

#Date: November 5, 2021
#https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

def getIntersectionNode(headA,headB):
        
    #O(n) time cacheing solution
    
    seen = set()
    while headA:
        seen.add(headA)
        headA = headA.next
    
    while headB:
        if headB in seen: return headB
        headB = headB.next

#Date: November 5, 2021
#https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(head):
        
        #O(n) solution; dp is the directional derivative of the linked list's node testues. This allows us to determine all the stationary/critical nodes
        
        dp,prev = [], None
        resmax,resmin = -1,-1
        fcrit,rcrit = None,None
        
        while head:
            if not prev or head.test==prev: dp += [0]
            elif head.test>prev: dp += [1]
            else: dp += [-1]
            prev = head.test
            head = head.next

        for i in range(1,len(dp)):
            if (dp[i]==1 and dp[i-1]==-1) or (dp[i]==-1 and dp[i-1]==1): #local min and max respectively
                curr = i-1
                if not fcrit: 
                    fcrit,rcrit = curr,curr
                    continue
                resmax = curr-fcrit
                resmin = min((resmin if resmin!=-1 else float('inf')),curr-rcrit)
                rcrit = curr
        return [resmin,resmax]
 
#Date: November 5, 2021
#https://leetcode.com/problems/single-number-iii/

def singleNumber(self, nums):
        
    #O(n) time and O(1) memory two-pass bitwise solution. Partition the numbers into two groups who have and dont have the rightmost binary 1 of the xor of the unique numbers respectively. All the repeating numbers should cancel out
    
    #This is the best explanation I've ever watched: https://www.youtube.com/watch?v=L-EaPf5tD5A
    
    ans,xor = [0,0],0
    for n in nums: xor^=n
    xor &= -xor
    for n in nums:
        if not xor&n: ans[0] ^= n
        else: ans[1] ^= n 
    return ans

#Date: November 6, 2021
#https://leetcode.com/problems/multiply-strings/submissions/

def multiply(num1,num2):
        
        #O(n) solutiuon by converting each digit using unicode integers. '0' starts at 48
        
        res1 = sum([(ord(num1[i])-48)*10**(abs(i)-1) for i in range(-1,-(len(num1)+1),-1)])
        res2 = sum([(ord(num2[i])-48)*10**(abs(i)-1) for i in range(-1,-(len(num2)+1),-1)])
        return str(res1*res2)

#Date: November 7, 2021
#https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/

def largestRectangleArea(heights):
        
    #O(n) time index-based stack solution; the stack is always increasing (key=heights[index]). As we traverse "heights", we append an index to stack if it can increase the possible volume (i.e heigher height). Otherwise, we calculate + pop the stack with the indexes we have that are > current index
    
    #Note: for the popped heights, we must account for their left and rightbound limits
    
    stack,ans=[-1],0
    heights += [0]
    
    for i in range(len(heights)):
        if heights[i] >= heights[stack[-1]]: 
            stack += [i]
            continue
        rb = stack[-1]
        while stack and heights[stack[-1]]>heights[i]:
            ans = max(ans,(rb-stack[-2])*heights[stack.pop()])
        stack += [i]
    
    return ans

#Date: November 7, 2021
#https://leetcode.com/problems/unique-binary-search-trees/

from cachetools import cached
class Solution:
    @cached
    def numTrees(self, n: int) -> int:
        if n in [0,1]: return 1
        return sum([self.numTrees(n-i)*self.numTrees(i-1) for i in range(1,n+1)]) 

    #A recursive approach with memoization dp
    #Key point: n=0 or n=1 --> 1 tree (base case)
    #Key point: given a particular node that we need to fill in (while n=some testue):

    #1. the number of nodes that can be filled in = n
    #2. the number of nodes that can be potential left children  = i-1 (while 1<=i<=n)
    #3. the number of nodes that can be potential right children = n-i

    #Therefore, the number of testid BST that we can general from that node is equitestent to the sum of the products of trees we can generate to the left and right respectively for all possible 'i' testues

    #Date: November 10, 2021
    #https://leetcode.com/problems/minimum-testue-to-get-positive-step-by-step-sum/

    def minStarttestue(nums):
        
        #basic O(n) arithmetic + intuition solution; keep transient prefix sum as you traverse the array and if the ps ever drops to 0 or below, add the missing amount to ans and reset ps as if ans was updated from the start
        
        ans,curr = 0,0
        for n in nums:
            curr += n
            if curr<=0: 
                ans += abs(curr)+1
                curr = 1
        return (ans if ans else 1)

#Date: November 11, 2021 (I feel like my skill hit a plato)
#https://leetcode.com/problems/remove-linked-list-elements/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next

def removeElements(head,test):
        
    #Intuitive traversal solution
    
    curr,prev = head,None
    while curr:
        if curr.test==test:
            if not prev: curr,head = [curr.next]*2
            else: 
                prev.next,curr = [curr.next]*2
            continue
        prev,curr = curr,curr.next
    
    return head

#Date: November 12, 2021
#https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(temperatrues):
        
    #O(n) index-based stack (where temperatures of those indices are kept in decreasing order), pop when theres a greater temeperature
    
    stack,ans = [],[0 for _ in range(len(temperatures))]
    for i in range(len(temperatures)):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            curr = stack.pop()
            ans[curr] = i-curr
        stack += [i]
    return ans

#Date: November 13, 2021
#https://leetcode.com/problems/most-beautiful-item-for-each-query/

def maximumBeauty(items,queries):
        
    #O(n) time and O(1) memory; sort items and queries (while keeping track of indices) by testue and prices respectively. Then traverse over items and only increment if the item gets too expensive for its associated testue (which should be the most beautiful for tht given price)
    
    ans = [0]*len(queries)
    queries = sorted([[i,j] for i,j in enumerate(queries)], key=lambda x:x[1], reverse=True)
    items.sort(key=lambda x:x[1], reverse=True)
    i,broke = 0,False
    for q in queries:
        while items[i][0]>q[1]:
            i += 1
            if i>=len(items): 
                broke = True
                break
        if broke: break
        ans[q[0]] = items[i][1]
    return ans

#Date: November 13, 2021
#https://leetcode.com/problems/check-whether-two-strings-are-almost-equitestent/

def checkAlmostEquitestent(word1,word2):
        
    #Intuitive
    
    from collections import Counter
    x,y = Counter(word1), Counter(word2)
    
    for n in x:
        if abs(x[n]-y[n]) > 3: return False
    for n in y:
        if abs(x[n]-y[n]) > 3: return False
    return True

#Date: November 13, 2021
#https://leetcode.com/problems/iterator-for-combination/submissions/

from itertools import combinations
class CombinationIterator:
    
    #intuitive full search solution using itertools
    
    def __init__(self, characters: str, combinationLength: int):
        self.comb = list(combinations(sorted(characters),combinationLength))
        self.i = -1
        
    def next(self) -> str:
        self.i += 1
        return ''.join(self.comb[self.i])

    def hasNext(self) -> bool:
        if self.i >= len(self.comb)-1: return False
        return True

#Date: November 14, 2021
#https://leetcode.com/problems/largest-divisible-subset/submissions/

def largestDivisibleSubset(nums):
        
        #traditional O(n^2) dp approach. dp[i] will hold (index built upon, ans to sub-problem, current index) 
        
        nums.sort()
        dp,ans = [[None,1] for _ in range(len(nums))],[]
        
        for i in range(len(nums)):
            initi = dp[i][1]
            for j in range(i):
                if not nums[i]%nums[j] and (pot:=initi+dp[j][1])>dp[i][1]:
                    dp[i][0],dp[i][1] = j,pot
            dp[i] += [i]
        
        curr = max(dp,key=lambda x:x[1])
        while True:
            ans += [nums[curr[2]]]
            if curr[0]==None: break
            curr = dp[curr[0]]
        
        return ans

#Date: November 15, 2021
#https://leetcode.com/problems/testid-number/submissions/

def isNumber(s):
        
    #The question of a million edge cases. 
    #An O(n) intuitive solution; lay out scneraios of testidity for each potentially testid character
    
    newint,seenint,dec,e = True,False,False,False
    for i,j in enumerate(s):
        if newint and j in ['+','-']:
            newint = False
            continue
        elif j.isnumeric():
            if newint: newint = False
            seenint = True
            continue
        elif j=='.' and (seenint or i==0 or s[i-1] in ['+','-']) and (not e) and not dec:
            if not i: newint = False
            dec = True
            continue
        elif j in ['e','E'] and (not e) and seenint:
            e,newint,seenint = True,True,False
            continue
        return False
    if not seenint: return False
    return True

#Date: November 17, 2021
#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/

def findDisappearedNumbers(nums):
        
    #intuitive
    
    return {n for n in range(1,len(nums)+1)} - set(nums)

#Date: November 18, 2021
#https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

def findKthNumber(m,n,k):
        
    #An O(min(n,m)lognm) binary search solution. We want to narrow down to a testue where it has k testues that its greater than in the matrix. 
    
    #Something i'm still unsure about tbh: how to we prove that l,r will always narrow down to a testue that exists on the matrix?
    
    l,r = 1,m*n
    if n<m: n,m=m,n
    while l<r:
        mid = (l+r)//2
        count = sum([min(n,mid//i) for i in range(1,m+1)])
        if count<k: l=mid+1 #mid+1 because we just proved it cant be mid
        else: r=mid
    return r

def hammingDistance(x,y):
        
    #inutive xor solution (the xor of two distinct bits is always 1)
    
    return sum([1 for b in str(bin(x^y))[2:] if int(b)])

#Date: November 19, 2021
#https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/

def singleNonDuplicate(nums):
        
    #binary search; we continuously narrow our search to subarray's with odd length subarrays
    #odd length subarray = the target must be in there
    
    l,r=0,len(nums)-1
    while l<r:
        m=(l+r)//2
        if all([nums[m]!=nums[m+1],nums[m]!=nums[m-1]]): return nums[m]
        elif nums[m]==nums[m+1]:
            if (m-l)%2: r=m-1
            else: l=m+2
        else:
            if (r-m)%2: l=m+1
            else: r=m-2
    return nums[l]

#Date: November 20,2021
#https://leetcode.com/problems/number-of-testid-words-for-each-puzzle/

from collections import Counter
class Solution:
    def findNumOftestidWords(self, words,puzzles):
        
        #make bitmask for words (keep freq map of this too) and for puzzles. then, enumerate over each submask of each puzzle mask and see if it exists in the freq map (aka see if matches a word(s)) upon testidation of the first condition by left shifting the first puzzle letter
        
        ans = []
        bfrq = Counter(list(map(self.mask,words)))
        
        for p in puzzles:
            p,first,res = self.mask(p),1<<(ord(p[0])-ord('a')),0
            curr = p
            while curr: #formula to generate all submasks
                if (curr in bfrq) and (curr|first == curr): 
                    res += bfrq[curr]
                curr=(curr-1)&p
            ans += [res]
        return ans
    
    def mask(self,x):
            mask = 0
            for c in x:
                mask |= 1<<(ord(c)-ord('a'))
            return mask

#Date: November 20, 2021
#https://leetcode.com/problems/delete-node-in-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        
        #recursive approach with 3 conditions:
        #1. if we have leaf, just delete it
        #2. if we have one child, let child replace parent
        #3. if we have 2 children, take the max of left subtree or min of right subtree nd recurse on min/max node

        if not root: return root
        elif key < root.test: root.left = self.deleteNode(root.left, key)
        elif key > root.test: root.right = self.deleteNode(root.right, key)
        else:
            if all([not root.left,not root.right]): root = None
            elif not root.left: root = root.right
            elif not root.right: root = root.left
            else:
                rep = self.helpmax(root.left)
                root.test = rep.test
                root.left = self.deleteNode(root.left, rep.test)
        return root

    def helpmax(self, root):
        curr = root
        while curr.right:
            curr = curr.right
        return curr

#Date: November 22, 2021
#https://leetcode.com/problems/count-primes/

def countPrimes(n):
        
        #sieve of eratosthenes (lol i finally learned wht this is)
        
        dp,i=[True for i in range(n)],2
        while i*i<=n: #this is the condition coz if u multiply by less than 'i', you've alrdy accounted for tht
            if dp[i]:
                for j in range(i*i,n,i): dp[j]=False
            i+=1     
        return sum([1 for i in range(2,n) if dp[i]])

#Date: November 24, 2021
#https://leetcode.com/problems/intertest-list-intersections/

def intertestIntersection(arr1,arr2):
        
        #O(n) time two pointers approach (each pointer traverses arr1 and arr2 respectively). op,ed comparisons are intuitive and pointers are incremented based on which one ends first; since the intertests are disconjunct, if an intertest ends, there will be nothing else that will be able to overlap it unless it overlaps the matching intertest of the other arr as well (which is intestid)
        
        ans = []
        i,j = 0,0
        while i<len(arr1) and j<len(arr2):
            op,ed = max(arr1[i][0],arr2[j][0]),min(arr1[i][1],arr2[j][1])
            if op<=ed: ans += [[op,ed]]
            if arr1[i][1]<arr2[j][1]: i+=1
            else: j+=1
        return ans

#Date: November 26, 2021
#https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
        
        #Intuitive soution (jus be careful of 0s)
        
        import numpy
        ans = []
        if (z:=nums.count(0)):
            if z>1: return [0]*len(nums)
            else: 
                prod=1
                for n in nums:
                    if n: prod *= n
                return [(0 if x else prod) for x in nums ]
        prod = numpy.prod(nums)
        for n in nums:
            ans += [prod//n]
        return ans

#Date: November 27, 2021
#https://leetcode.com/problems/all-paths-from-source-to-target/submissions/

class Solution:
    def allPathsSourceTarget(self,graph):
            
            #intuitive bfs
            
            from collections import deque
            self.ans = []
            ed,dq = len(graph)-1,deque([[0,[0],{0}]]) #[[curr,[traversed],{seen}],...]
            while dq:
                for _ in range(len(dq)):
                    if dq[0][0]==ed: self.ans += [dq[0][1]]
                    else:
                        for possi in graph[dq[0][0]]:
                            if possi not in dq[0][-1]: dq += [[possi,dq[0][1]+[possi],dq[0][-1]|{possi}]]
                    dq.popleft()
            return self.ans

#Date: November 28, 2021
#https://leetcode.com/problems/k-radius-subarray-averages/

def getAverages(nums,k):
        
    #intuitive prefix sum array O(n) solution
    
    def testid(i):
        if 0<=i<len(nums): return True
        return False
    
    psa = [0]
    for n in nums: psa += [psa[-1]+n]
    l,r = -k,k
    ans = []
    for i in range(len(nums)):
        if all([testid(r),testid(l)]): ans += [(psa[r+1]-psa[l])//(2*k+1)]
        else: ans += [-1]
        l += 1
        r += 1
    return ans

#Date: November 28, 2021
#https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

def minimumDeletions(nums):
        
    #check from both sides, from left, and from right,
    
    if not nums: return 0
    maxi,mini = nums.index(max(nums)),nums.index(min(nums))
    return min(max(maxi,mini)+1,len(nums)-min(maxi,mini),min(maxi,mini)+1+len(nums)-max(maxi,mini))

#Date: November 28, 2021
#https://leetcode.com/problems/largest-component-size-by-common-factor/submissions/

class Solution:
    def largestComponentSize(self, nums):
         
        #O(n^1.5) factorization and union-find solution with path compression to slightly optimize. 
        #dsu[i] = next node or [end size]
        
        self.dsu = {n:[1] for n in nums}
        self.ans = 1
        facs = defaultdict(list)
        
        def find(test):
            if type(self.dsu[test])==list: return test
            self.dsu[test]=find(self.dsu[test])
            return self.dsu[test]
        
        def union(ds1,ds2):
            u1,u2 = find(ds1),find(ds2)
            if u1!=u2: self.dsu[u1],self.dsu[u2] = u2,[self.dsu[u1][0]+self.dsu[u2][0]]
            self.ans = max(self.ans,self.dsu[u2][0])
            return
        
        for n in nums:
            if n!=1: facs[n] += [n]
            for fac in range(2,int(n**0.5)+1):
                if not n%fac:
                    facs[fac] += [n]
                    if fac**2 != n: facs[n//fac] += [n]

        for f in facs:
            for i in range(1,len(facs[f])): 
                union(facs[f][i],facs[f][0])
        return self.ans

#Date: November 28, 2021
#https://leetcode.com/problems/accounts-merge/

def accountsMerge(accounts):
        
    #Intuitive O(n^2) hashmap solution (like a simplified dsu union-find)
    
    from collections import defaultdict
    accs,used = {},defaultdict(int)
    for ems in accounts:
        exi=False
        possi=set(ems[1:])
        for prev in list(accs):
            if possi&accs[prev]:
                if not exi:
                    accs[prev]|=possi
                    exi=True
                    alr = prev
                else:
                    accs[alr]|=accs[prev]
                    accs.pop(prev)
        if not exi: 
            accs[(ems[0],used[ems[0]])] = possi
            used[ems[0]] += 1
    return [[x[0]]+sorted(list(accs[x])) for x in accs]

#Date: November 29, 2021
#https://leetcode.com/problems/maximal-rectangle/submissions/

def maximalRectangle(matrix):
        
    #O(mn) time; dp through implement index-based stack solution from "largest rectangle" for each distinct row in the matrix 
    
    if not matrix: return 0
    
    #rmr to extend to max left and right bound 
    def solve(arr):
        res,stack = 0,[-1]
        arr += [-1]
        for i in range(len(arr)):
            rb=stack[-1]
            while arr[stack[-1]]>arr[i]:
                temp = stack.pop()
                res = max(res,arr[temp]*(rb-stack[-1]))
            stack += [i]
        return res
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j])
            if i and matrix[i][j]: matrix[i][j] += matrix[i-1][j]
    
    return max(solve(x) for x in matrix)

#Date: November 30, 2021
#https://leetcode.com/problems/minimum-window-substring/submissions/

def minWindow(s,t):
        
    #O(m+n) time sliding window + queue solution. Essentially, we want to prioritize gathering all the required characters from 't' first (the parallel action would be to expand our window rightwards). Otherwise, upon traversing a character that would create an excess of the reqired characters, we contract our left pointer on the condition that the required characters are still present (i.e have[s[dq[0]]]>base[s[dq[0]]])
    
    from collections import Counter,deque,defaultdict
    have,base = defaultdict(int),Counter(t)
    need,ans = len(base),[float('-inf'),float('inf')]
    op,ed,dq = None,None,deque()
    
    for i in range(len(s)):
        if s[i] not in base: continue
        have[s[i]] += 1
        if not dq: op=i
        if need and have[s[i]]==base[s[i]]: need -= 1
        while dq and have[s[dq[0]]]>base[s[dq[0]]]: have[s[dq.popleft()]] -= 1
        dq += [i]
        op = dq[0]
        if not need: 
            ed=i
            ans = min(ans,[op,ed],key=lambda x:x[1]-x[0])
            
    if need: return ''
    return s[ans[0]:ans[1]+1]

#Date: December 1, 2021
#https://leetcode.com/problems/odd-even-linked-list/

def oddEvenList(head):
        
    #Intuitive O(n) time and O(1) space solution; keep track of the most recent odd and even nodes respectively and attach them to the current node depending on if current node index is odd or even + update ro or re
    
    if (not head) or not head.next: return head

    ro,re,se = head,head.next,head.next
    curr,count = head.next.next,1
    while curr:
        if count%2:
            ro.next = curr
            ro = curr
        else:
            re.next = curr
            re = curr
        count += 1
        curr = curr.next
    re.next,ro.next = None,None #to avoid cycles coz re or ro might still be connected to an unmanipulated node
    ro.next = se
    return head

#Date: December 3, 2021
#https://leetcode.com/problems/stream-of-characters/submissions/

class StreamChecker:
    
    #Implementation of trie (but words are reversed) solution
    #Note: the suffix of stream gotta be a word in words
    #Note: #cut off the branch if we're done with the word (i.e if u have 'xaa' and 'aa' for instance then the 'xaa' is pre much negligible coz the latter is a suffix of the former) 
    
    def __init__(self,words):
        self.stream = ''
        self.trie = TrieNode() #root
        for w in words:
            curr = self.trie
            for i in range(len(w)):
                if curr.children==None: break
                if not w[~i] in curr.children: curr.children[w[~i]] = TrieNode(w[~i]) 
                if i!=len(w)-1: curr = curr.children[w[~i]]
                else: curr.children[w[~i]].children = None
        
    def query(self, letter: str) -> bool:
        self.stream += letter
        i,curr = 0,self.trie.children
        while i<len(self.stream):
            if self.stream[~i] not in curr: return False #no words are testid suffixes rip
            if curr[self.stream[~i]].children==None: return True #reached end of word
            curr = curr[self.stream[~i]].children
            i+=1
        return False #stream happens to be a suffix of the word instead
            
class TrieNode:
    def __init__(self,testue=None,):
        self.test = testue
        self.children = {}
    
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

#Date: December 4, 2021
#https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

class Solution:
    def rob(self,root):
        
        #bottom up O(n) dp+pairs; dp of node = (with node res, without node res)
        
        def dfs(node):
            if not node: return (0,0) 
            l,r = dfs(node.left),dfs(node.right)
            node.test = (node.test+l[1]+r[1],max(l)+max(r))
            return node.test
        dfs(root)
        
        return max(root.test)

#Date: December 5, 2021
#https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

def minOperations(nums):
        
        #An important thing to realize is tht the only type of array that ultimately fulfill both conditions is a strictly contiguous subarray. So now the idea is to take each number 'n' in nums and have it either act as the maximum of minimum of a potential subarray. We then wanna check how many distinct numbers fall under the range in question (either n+len(nums)-1 or n-len(nums)+1). with brute force this is O(n^2) but we can optimize to O(nlogn) by using binary search and comparing indices to figure out how many numbers are in the appropriate range.
        
        import bisect 
        lorig = len(nums)
        nums = sorted(set(nums))
        res = float('inf')
        for i in range(len(nums)):
            res = min(res,lorig-i+bisect.bisect_left(nums,nums[i]-lorig+1)-1)
        return res

#Date: December 5, 2021
#https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/submissions/

def minCostToMoveChips(position):
        
        #O(n) even,odd intuitive solution
        
        from collections import Counter
        frq = Counter(position)
        e,o = sum([frq[x] for x in frq if not x%2]), sum([frq[x] for x in frq if x%2])
        return min(e,o)

#Date: December 6, 2021
#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/

def maxVowels(s,k):
        
    #O(n) solution; intuitive psa (of how many vowels there have been up till now) + sliding window
    
    vwls = {'a','e','i','o','u'}
    ans,psa = 0,[0]
    for i in range(len(s)): psa += [(psa[i] if s[i] not in vwls else psa[i]+1)]
    for i in range(k,len(psa)): ans = max(ans,psa[i]-psa[i-k])
    return ans

#Date: December 7, 2021
#https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, test=0, left=None, right=None):
#         self.test = test
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(root):
        
        #2 dfs (first make reverse psa then operate of the tree directly)
        
        def dfs1(node):
            if not node: return 0
            node.test+=dfs1(node.left)+dfs1(node.right)
            return node.test
        
        def dfs2(node):
            if not node: return
            self.ans += abs((node.left.test if node.left else 0)-(node.right.test if node.right else 0))
            dfs2(node.left)
            dfs2(node.right)
        
        self.ans = 0
        dfs1(root);dfs2(root)
        return self.ans

#Date: December 8, 2021
#https://leetcode.com/problems/jump-game-iii/submissions/

def canReach(arr,start):
        
    #general O(n) brute force bfs
    
    from collections import deque
    dq,seen=deque([start]),set()
    while dq:
        if arr[dq[0]]==0: return True
        curr=dq.popleft()
        pos=arr[curr]
        seen.add(curr)
        if curr+pos<len(arr) and curr+pos not in seen: dq += [curr+pos]
        if curr-pos>=0 and curr-pos not in seen: dq += [curr-pos]
    return False

#Date: December 11, 2021
#https://leetcode.com/contest/biweekly-contest-67/problems/find-subsequence-of-length-k-with-the-largest-sum/

def maxSubsequence(nums,k):
        
    #greedy
    
    from collections import Counter
    prev = sorted(nums)
    need = Counter([prev[~i] for i in range(k)])
    ans = []
    for n in nums:
        if need[n]: 
            ans += [n]
            need[n] -= 1
    return ans

def goodDaysToRobBank(security,time):
        
    #O(n) dp solution
    #dpl and dpr will be prefix and sufix arrays that track the number of days to the left and right respectively where the number of guarads either stayed the same or increased.
    #if dpl[i] and dpr[i] all >= time on a given day, that day is a "good day"
    
    ans = []
    dpl,dpr = [0 for _ in range(len(security))], [0 for _ in range(len(security))]
    for i in range(1,len(security)): 
        dpl[i] = dpl[i-1]+1 if security[i-1]>=security[i] else 0
        dpr[~i] = dpr[~(i-1)]+1 if security[~(i-1)]>=security[~i] else 0
    for j in range(len(security)): 
        if all([dpl[j]>=time,dpr[j]>=time]): ans+=[j]
    return ans

#Date: December 11, 2021
#https://leetcode.com/problems/partition-equal-subset-sum/submissions/

def canPartition(nums):
        
    #O(n^2) 1-D dp solution; if type(dp[i])==int then we can add up to tht total sum of 'i'
    #Note: for each number in nums, increment the dp marking number so theres no overlap
    #Note: only update dp[i] if it still == False
    
    tot=sum(nums)
    targ=tot//2
    dp=[0]+[False for _ in range(targ)]

    if tot%2: return False
    
    count = 0
    for n in nums:
        count += 1
        for i in range(len(dp)):
            if all([type(dp[i])==int,dp[i]<count,i+n<len(dp),type(dp[i+n])==bool]): dp[i+n]=count

    return (True if dp[-1] else False)

#Date: December 12, 2021
#https://leetcode.com/problems/nth-magical-number/submissions/

def nthMagicalNumber(n,a,b):
        
    #case 1: if they divisible then its pre intuitive
    if (not a%b) or not b%a: return (n*min(a,b))%(10**9+7)
    
    #case 2: if they arent then then we can binary search under this condition
    
    #let n = a number: it is the n//a=Ath multiple of a, it is the n//b=Bth multiple of b, it is the n//lcm(a,b)=Cth multiple that can be divided by both a and b. Thus it is the A+B-Cth magical number
    
    import math
    lcm = a*b//math.gcd(a,b)
    l,r = 1,min(a,b)*n
    while l<r:
        m=(l+r)//2
        if m//a+m//b-m//lcm<n: l=m+1 #havent reached nth number yet
        else: r=m #because we arent doing r = m-1, we can guarantee we narrow down on the number itself
    return l%(10**9+7)

#Date: December 12, 2021
#https://leetcode.com/problems/domino-and-tromino-tiling/submissions/

def numTilings(n):
        
    #O(n) dp solution
    #dp = perfect fit
    #dpm = perfect fit with piece missing either above or below (not distinctively tho)
    
    dp,dpm = [1,2]+[0]*(n-2), [0]+[1]*(n-1)
    for i in range(2, n):
        dp[i] = dp[i-1]+dp[i-2]+dpm[i-1]*2
        dpm[i] = dp[i-2]+dpm[i-1]
    return dp[n-1]%(10**9+7)

#Date: December 14, 2021
#https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, test=0, next=None):
#         self.test = test
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        
        #intuitive solution in application of the diagram
        #prev,con = the two nodes in between which we will possibly insert the current node we are finding a placement for
        #pprev,curr = node before current node, current node we are operating on
        
        lllen = 0; curr=head
        while curr:
            lllen +=1
            curr = curr.next
        
        for i in range(1,lllen):
            prev,con=None,head
            pprev,curr = None,head
            for j in range(i): pprev,curr=curr,curr.next
            while True:
                if con==curr: break
                if curr.test>con.test: 
                    prev,con = con,con.next
                    continue
                pprev.next=(curr.next if curr.next else None)
                if prev: prev.next=curr
                curr.next=con
                if not prev: head=curr
                break
        return head

#Date: December 15, 2021
#https://leetcode.com/problems/minimum-height-trees/

def findMinHeightTrees(n,edges):
        
    #graph theory, cropping technique. If you remove leaves of minimum height tree, height -= 1 but the answer would stay the same. In that regard, we can just crop out all the leaves until the vertices are the leaves (the answers themselves).
    #we can implement O(n) bfs for this
    
    from collections import deque
    
    edgs = {i:set() for i in range(n)}
    for u,v in edges: edgs[u].add(v); edgs[v].add(u)
    dq=deque([i for i in range(n) if len(edgs[i])==1])
    
    nodes=n
    while nodes>2:
        new=set()
        for i in range(len(dq)):
            temp=dq.popleft()
            for pos in edgs[temp]:
                if pos in new: continue
                edgs[pos].remove(temp)
                if len(edgs[pos])==1: dq += [pos]; new.add(pos)
            edgs.pop(temp)
            nodes-=1
            
    if not edges: return [0]
    return list(dq)
    
#Date: December 17, 2021
#https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

def atMostNGivenDigitSet(digits,n):
        
    #digit optimization + dp; first pre-compute all possibilities of number with a length less than n itself.
    #then to compute possibilites that have length==n, at each digit of n (from left to right), lets call tht pos, find out how many digits are less than pos and add on possible combinations to the the global answer. In relation to tht, we must fufill the condition that there is a digit that is equal to pos in digits if we want to move to the next pos, otherwise it would be pointless because we've already considered all other possibilities
    
    digits = set([int(x) for x in digits])
    ans=sum([len(digits)**i for i in range(1,len(str(n)))])
    
    for i,j in enumerate(str(n)):
        j=int(j)
        les = sum([1 for x in digits if x<j])
        ans += les*len(digits)**(len(str(n))-i-1)
        if j not in digits: break 
        if i==len(str(n))-1: ans += 1 
            
    return ans

#Date: December 18, 2021
#https://leetcode.com/problems/making-a-large-island/submissions/

class Solution:
    def largestIsland(self,grid):
        
        #make dsu of existing islands then check possible connections between islands without modifying the dsu
        
        def find(pos):
            if type(self.dsu[pos])==list: return pos
            self.dsu[pos]=find(self.dsu[pos])
            return self.dsu[pos]
        
        def union(pos1,pos2):
            res1,res2 = find(pos1),find(pos2)
            if res1!=res2: self.dsu[res1],self.dsu[res2]=res2,[self.dsu[res1][0]+self.dsu[res2][0]]
        
        def testid(i,j):
            if all([0<=i<len(grid),0<=j<len(grid[0])]): return True
            return False
        
        self.dsu={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: continue
                self.dsu[(i,j)]=[1] 
                if testid(i-1,j) and grid[i-1][j]: union((i,j),(i-1,j))
                if testid(i,j-1) and grid[i][j-1]: union((i,j),(i,j-1))
        
        if not self.dsu: return 1
        ans,curr=max([(self.dsu[x][0] if type(self.dsu[x])==list else 0) for x in self.dsu]),0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    curr=1+sum([self.dsu[x][0] for x in {find((I,J)) for I,J in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if (testid(I,J) and grid[I][J])}])
                    ans = max(curr,ans)
        
        return ans
                    
#Date: December 18, 2021
#https://leetcode.com/problems/decode-string/

def decodeString(s):
        
    #O(n) double stack solution with conditions (ordering is pre important)
    
    ans=''
    stk1,stk2 = [],[]
    num=''
    for c in s:
        if c.isnumeric(): num+=c
        elif c=='[' and num: 
            stk1+=[int(num)]
            if len(stk1)-2==len(stk2): stk2 += [''] #must be nested bracket without string in the first layer of nesting
            num=''
        elif c==']' and stk1:
            if len(stk1)>1: stk2[-2] += stk2[-1]*stk1.pop(); stk2.pop() 
            else: ans += stk1.pop()*stk2.pop()
        elif not stk1: ans += c
        elif len(stk1)>len(stk2): stk2 += [c]
        elif len(stk1)==len(stk2): stk2[-1] += c
    return ans

#Date: December 20, 2021
#https://leetcode.com/submissions/detail/604688325/

def numDistinct(self, s: str, t: str) -> int:
        
        #intertest dp (easy implementation but tricky thought process tbh)
        
        #each dp[i][j] gotta be at least dp[i-1][j] coz its assuming we cut the current char
        #nd if the chars are the same we also add dp[i-1][j-1] (these are the new possibilities/number of subsequences without this requirement that add on the prexsisting ways of getting 'x' subsequences)
        #dp[i-1][j] for a case where characters are the same would be equitestent to previous ways of fufilling this requirement
        
        dp = [[1]+[0 for _ in range(len(t))] for __ in range(len(s)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i-1][j]
                if s[i-1]==t[j-1]: dp[i][j] += dp[i-1][j-1]
        return dp[-1][-1]

#Date: December 20, 2021
#https://leetcode.com/problems/power-of-two/submissions/

def isPowerOfTwo(self, n: int) -> bool:
        
    #intuitive O(31) bit-manipulation
    
    from collections import Counter
    if n>0 and Counter(bin(n))['1']==1: return True
    return False

#Date: December 21, 2021
#https://leetcode.com/problems/reorder-list/

def reorderList(head):
        
        #Intuitive O(n) time and space solution
        #prev-->left, left-->right, right-->None, prev=right
        
        nodes=[]
        curr=head
        while curr: nodes+=[curr]; curr=curr.next
        
        l,r,prev=0,len(nodes)-1,None
        while l<=r:
            if prev!=None: prev.next=nodes[l]
            nodes[l].next=nodes[r]; nodes[r].next=None
            prev=nodes[r]
            l+=1; r-=1
        
        return nodes[0]

#Date: December 22, 2021
#https://leetcode.com/problems/course-schedule-ii/

def findOrder(numCourses, prereq):
        
    #Intuitive O(V+E) topological sort, but jus gotta make sure its guaranteed to be a DAG
    
    from collections import defaultdict,deque
    
    adj,unvis=defaultdict(list),{i for i in range(numCourses)}
    for p in prereq: adj[p[1]] += [p[0]]
    
    def dfs(node,pars):
        nonlocal unvis,cyc
        if node in adj:
            for pos in adj[node]:
                if pos in pars: cyc=True; return #cycle found
                if pos in unvis: unvis.remove(pos); dfs(pos,pars|{pos})
        ans.appendleft(node)
        
    ans = deque()
    while unvis:
        cyc,curr=False,unvis.pop()
        dfs(curr,{curr})
        if cyc: return []
    
    return ans

#Date: December 24, 2021
#https://leetcode.com/contest/biweekly-contest-48/problems/maximum-number-of-consecutive-testues-you-can-make/

def getMaximumConsecutive(coins):
        
        #intuitive greedy
        
        coins.sort()
        curr=1
        for x in coins:
            if x>curr: break
            curr += x
        return curr
            
         #ex: 1,1,1,3
         #u can make 0-3 with the first 3 1s, then since you can alrdy make 3 with previous digits, then u can now make a maximum of 6
         
         #counter-ex: 1,1,1,5
         #u can make 0-3 with the first 3 1s, but bcuz 5>4 (the next number u want to make) 4 is thus impossible to make

#Date: December 24, 2021
#https://leetcode.com/problems/basic-calculator-ii/

def calculate(s):
        
        #O(3n) bemas intuition with linked list (deque used to simulate); prolly could be faster tho
        
        from collections import deque
        
        curr=''
        op,num = deque(),deque()
        m,d = 0,0
        for i,c in enumerate(s):
            if c.isnumeric():
                curr += c
            elif c in ['/','+','-','*']: #python cant detect empty char in string for sum reason
                if c=='*' : m += 1
                elif c=='/': d += 1
                op += [c]; num += [int(curr)]
                curr = ''
        if curr: num += [int(curr)]
        
        for i in range(1,len(num)):
            if op[i-1]=='*': 
                num[i] *= num[i-1]; num[i-1]=''
            elif op[i-1]=='/': num[i]=num[i-1]//num[i]; num[i-1]=''

        for _ in range(m+d): num.remove('')
        for _ in range(m): op.remove('*')
        for _ in range(d): op.remove('/')
        
        for i in range(1,len(num)):
            if op[i-1]=='+': num[i]+=num[i-1]
            else: num[i]=num[i-1]-num[i]
        
        return num[-1]
    
#Date: December 25, 2021
#https://leetcode.com/contest/biweekly-contest-68/problems/find-all-possible-recipes-from-given-supplies/

def findAllRecipes(recipes, ingredients, supplies):
        
        #topological sort the nodes then iterate through everything to check testid meals
        
        from collections import defaultdict,deque
        supplies = set(supplies)
        adj = defaultdict(list)
        unvis=supplies|set(recipes)
        
        fin = {x[0]:x[1] for x in zip(recipes,ingredients)}
        
        for i in range(len(ingredients)):
            for j in ingredients[i]:
                adj[j] += [recipes[i]]
        
        def dfs(node,pars):
            nonlocal unvis,adj,fin
            if node in adj:
                for pos in adj[node]:
                    if pos in pars: #cycle found
                        fin[pos]=False; fin[node]=False
                        continue
                    if pos in unvis: 
                        unvis.remove(pos); dfs(pos,pars|{pos})
            ans.appendleft(node)
            
        ans = deque()
        while unvis:
            curr=unvis.pop()
            dfs(curr,{curr})
        
        res = []
        for x in ans:
            if x not in fin: continue
            if type(fin[x])==bool: continue
            if all([(y in supplies) or (y in fin and fin[y]==True) for y in fin[x]]):
                res += [x]
                fin[x]=True
            else:
                fin[x]=False
        
        return res

#Date: December 26, 2021
#https://leetcode.com/problems/candy/submissions/

def candy(ratings):
        
        #Intuitive O(n) two-pass; first pass = satisfies condition of only being greater than left neighbor if needed and second pass = satisfies condition of being greater than right neighbor as well when necessary
        
        ans=[1 for _ in range(len(ratings))]
        
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]: ans[i] = 1+ans[i-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]: ans[i] = max(ans[i],1+ans[i+1])
                
        return sum(ans)

#Date: December 26, 2021
#https://leetcode.com/problems/number-complement/submissions/

def findComplement(num):
        
        #find log2(num) and then use xor on tht
        
        import math
        return num^sum([2**i for i in range(int(math.log(num,2))+1)])

#Date: December 27, 2021
#https://leetcode.com/problems/check-if-a-parentheses-string-can-be-testid/submissions/

def canBetestid(s,locked):
        
        #O(n) two pass solution (pre slick problem tbh)
        
        #first u wanna balance the locked ')' by any means possible while making sure its testid lol
        
        if len(s)%2: return False
        bal, start = 0,None
        for i in range(len(s)):
            bal += (-1 if (s[i]==')' and int(locked[i])) else 1)
            if bal==1: start=i 
            if bal<0: return False
        
        #now that all locked ')' are balanced, all tht should be left are locked '(' and unlocked brackets
        #if there are and odd number of those things, the answer should be false
        
        if bal%2: return False
        
        #now if the remainder is even we jus traverse (but reverse this time) again with same motive as first traversal up till the point where bal begins tipping positive then we check if the remaining unlocked are odd or even

        bal=0
        for i in range(len(s)-1,start-1,-1):
            bal += (-1 if (s[i]=='(' and int(locked[i])) else 1)
            if bal<0: return False
        
        if bal%2: return False
        return True

#Date: December 28, 2021
#https://leetcode.com/problems/network-delay-time/submissions/

import collections
import heapq
import itertools
class PriorityQueue(collections.UserDict):
        
    def __init__(self):
        super().__init__(self)
        self.heap = []
        self.counter = itertools.count()

    def pq_add(self, task, priority):
        if task in self: self.pq_remove(task)
        record = [priority, next(self.counter), task]
        self[task] = record
        heapq.heappush(self.heap, record)

    def pq_remove(self, task):
        if task in self:
            record = self.pop(task)
            record[-1] = None

    def pq_pop(self):
        while self.heap:
            priority, _, task = heapq.heappop(self.heap)
            if task != None:
                del self[task]
                return [task,priority]
        else:
            raise RuntimeError('Heap is empty.')

    def info(self,task):
        if task not in self: return False
        return self[task]
            
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        
        #dijkstra implementation 

        def solve(adj,stt): 

            if not adj or len(adj)==1: return 0
            unvis = {i for i in range(len(adj))}
            pq = PriorityQueue()
            for i in range(len(adj)): pq.pq_add(i,float('inf'))
            pq.pq_add(stt,0)

            while unvis:
                curr,dis = pq.pq_pop()
                for i in range(len(adj[curr])):
                    if i in unvis and adj[curr][i]!=None and pq.info(i)[0] > dis+adj[curr][i]: pq.pq_add(i,dis+adj[curr][i])
                unvis.remove(curr)
                if type(dis)==float: return -1
                if not unvis: return dis
        
        adj = [[None for _ in range(n)] for  __ in range(n)]
        for v in times: adj[v[0]-1][v[1]-1] = v[2]
        return solve(adj,k-1)

#Date: December 29, 2021
#https://leetcode.com/problems/number-of-digit-one/

def countDigitOne(n):
        
    #O(logn) mathematical solution
    #intertests of new 1s: 0-9, 10-99, 100-999, 1000,9999... 
        #each intertest yields 1,10,100,etc. new '1's respectively
    #conditions for FULL yield when %upper bound+1: 1 <=, 19 <=, 199 <=...
    #conditions for PARTIAL yielf when %upper bound+1: None, 10 <= < 19,  100 <= < 199, 1000 <= < 1999 ... 
    
    ans = 0
    for i in range(len(str(n))):
        curr = 10**(i+1)
        hi,lo = int('1'+'9'*i), int('1'+'0'*i)
        ans += (n//curr) * 10**i
        if (pot:=n%curr) >= hi: ans += 10**i
        elif lo <= pot < hi: 
            ans += pot - lo + 1
    return ans

#Date: December 30, 2021
#https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/

def minCostConnectPoints(coords):
        
    #Kruskal's algo; in this case since we wanna choose V-1 E out of approx. coords^2 E the solution should have a general complexity of O(n^2)
    #we'll use a DSU to detect cycles
    
    def find(x,dsu):
        if dsu[x]==-1: return x
        dsu[x] = find(dsu[x],dsu)
        return dsu[x]
    
    def union(x,y,dsu):
        res1,res2 = find(x,dsu),find(y,dsu)
        if res1==res2: return False #cycle 
        dsu[res1] = res2
        return True
    
    if len(coords)==1: return 0
    
    dis,dsu = {},{}
    for i in range(len(coords)):
        dsu[tuple(coords[i])] = -1
        for j in range(i+1,len(coords)): 
            dis[(tuple(coords[i]),tuple(coords[j]))] = abs(coords[i][0]-coords[j][0])+abs(coords[i][1]-coords[j][1])
    

    count,ans = 0,0
    for pair in sorted(dis,key=lambda _:dis[_]):
        if not union(pair[0],pair[1],dsu): continue
        ans += dis[pair]; count += 1
        if count==len(coords)-1: return ans

#Date: January 1, 2022
#https://leetcode.com/problems/burst-balloons/

def maxCoins(nums):
        
    #an O(n^3) bottom up approach (focus on which balloon we should burst last) + intertest dp 
    #dp[i][j] = ans for intertest of i -> j where i,j are indices
    #Note: dp[i][j] is etestuated relative to the left and right boundaries (i.e l,r in the code)
    
    n = len(nums); nums += [1]
    dp = [[0 for _ in range(n)] for __ in range(n)]

    for count in range(n):
        for i in range(n):
            j=i+count
            if j>=n: break
            l,r = nums[i-1], nums[j+1]
            dp[i][j]= max(l*r*nums[x] + (dp[i][x-1] if x>i else 0) + (dp[x+1][j] if x<j else 0) for x in range(i,j+1))
    
    return dp[0][-1]

#Date: January 1, 2022
#https://leetcode.com/problems/uncrossed-lines/submissions/

def maxUncrossedLines(nums1,nums2):
        
    #Longest common subsequence dp; using LCS ensures tht lines acc never cross coz each line would be ahead of one another
    
    dp = [[0 for _ in range(len(nums1)+1)] for __ in range(len(nums2)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1 if nums1[j-1]==nums2[i-1] else 0)
    return dp[-1][-1]

#Date: January 1, 2022
#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

def numPairsDivisibleBy60(time):
        
        #Intuitive O(n) solution
        
        from collections import defaultdict
        ans = 0
        ot = defaultdict(int)
        for t in time: ot[t%60] += 1
        for t in time: 
            comp = 60-t%60
            ot[t%60] -= 1
            ans += ot[comp if comp!=60 else 0]
        return ans

#Date: January 2, 2022
#https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/submissions/

def nearestExit(maze,entrance):
        
    #intuitive O(mn) BFS
    
    from collections import deque
    seen,dq = set(), deque([tuple(entrance)])
    ans = 0 

    def testid(i,j):
        if 0<=i<len(maze) and 0<=j<len(maze[0]) and maze[i][j]=='.': return True
        return False
    
    def end(i,j):
        if i==0 or i==len(maze)-1 or j==0 or j==len(maze[0])-1: return True
        return False

    while dq:
        for x in range(len(dq)):
            curr=dq.popleft()
            seen.add(curr)
            i,j = curr[0],curr[1]
            if curr!=tuple(entrance) and end(i,j): return ans
            for I,J in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if testid(I,J) and (I,J) not in seen: seen.add((I,J)); dq += [(I,J)]
        ans += 1
    
    return -1
 
 #Date: January 2, 2022
 #https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

def minCost(maxt,edges,fees):
        
    #a O(mn) 2D dp approach, the general thought is: after travelling a distance 'x' what is the minimum cost to reach node 'y'?
    
    n=len(fees)
    dp = [[float('inf')]*n for __ in range(maxt+1)]; dp[0][0] = fees[0]
    ans = float('inf')
    
    for i in range(1,maxt+1):
        for op,ed,dis in edges: 
            if dis<=i:
                dp[i][op] = min(dp[i][op], dp[i-dis][ed]+fees[op])
                dp[i][ed] = min(dp[i][ed], dp[i-dis][op]+fees[ed])
        ans=min(ans,dp[i][n-1])
        
    return (ans if type(ans)==int else -1)

#Date: January 2, 2022
#https://leetcode.com/problems/find-the-town-judge/submissions/

def findJudge(n,trust):
        
    #trivial intutition
    
    trst = {i:[0,0] for i in range(1,n+1)} #trusted, trusts
    for x,y in trust:
        trst[y][0] += 1; trst[x][1] += 1
    
    for pos in trst: 
        if trst[pos][0]==n-1 and not trst[pos][1]: return pos
    return -1

#Date: January 5, 2022
#https://leetcode.com/problems/ugly-number-ii/

def nthUglyNumber(n):
        
    #intuitive O(nlogn) time and O(n) space heap solution
    
    import heapq
    seen={1}
    pq = [1]; heapq.heapify(pq)
    for _ in range(n-1):
        curr=heapq.heappop(pq)
        for x in [2,3,5]:
            if x*curr not in seen:
                heapq.heappush(pq,x*curr)
                seen.add(x*curr)
    return heapq.heappop(pq)

#Date: Jnauary 5,2022
#https://leetcode.com/problems/car-pooling/submissions/

def carPooling(trips,n):
        
    #sort by start time and append end time + ppl into pq, check at each significant point of time if it exceeds max 
    #if it does then jus return false
    
    import heapq
    trips.sort(key=lambda x:x[1])
    pq=[]
    curr=0
    for ppl,op,ed in trips:
        while pq and pq[0][0] <= op: 
            curr -= heapq.heappop(pq)[1]
        curr += ppl
        if curr>n: return False
        heapq.heappush(pq,(ed,ppl))
    return True

#Date: January 6, 2022
#https://leetcode.com/problems/count-of-smaller-numbers-after-self/

def countSmaller(nums):
    
    #basic binary search (could be worse case O(n^2) tho)
    #essentially we traverse backwords and build a sorted array of previously traversed elements then we BS to find how many elements the current one is greater than
    
    import bisect
    ins = []
    res = [0 for _ in range(len(nums))]
    for i in range(len(nums)-1,-1,-1):
        res[i] = bisect.bisect_left(ins,nums[i])
        bisect.insort(ins,nums[i])
    return res

#Date: January 6, 2022
#https://leetcode.com/problems/frog-jump/

def canCross(stones):
        
    #simple brute force dfs+memo
    
    def dfs(curr,jump):
        if curr==self.targ: return True
        if (curr,jump) in self.seen: return False
        self.seen.add((curr,jump))
        return (dfs(curr+jump+1,jump+1) if curr+jump+1 in self.stones else False) or (dfs(curr+jump-1,jump-1) if curr+jump-1 in self.stones and curr+jump-1 else False) or (dfs(curr+jump,jump) if curr+jump in self.stones else False)
    
    self.seen,self.stones,self.targ = set(),set(stones), stones[-1]
    return dfs(0,0)

#Date: January 7, 2022
#https://leetcode.com/problems/cherry-pickup-ii/submissions/

def cherryPickup(grid):

    #typical dfs + memo approach
    
    def testid(j):
        if 0<=j<len(grid[0]): return True
        return False 
    
    @cache
    def dfs(i,j1,j2):
        if not testid(j1) or not testid(j2): return 0
        res = grid[i][j1]+grid[i][j2] // (2 if j1==j2 else 1)
        if i!=len(grid)-1: res += max(dfs(i+1,J,JJ) for J in [j1,j1+1,j1-1] for JJ in [j2,j2+1,j2-1])
        return res
    return dfs(0, 0, len(grid[0]) - 1)

#Date: January 7, 2022
#https://leetcode.com/problems/capitalize-the-title/

def capitalizeTitle(title):
        
    title = title.lower()
    
    arr = title.split()
    for i in range(len(arr)):
        if len(arr[i])<=2: continue
        arr[i] = arr[i][0].upper() + arr[i][1:]
    
    return ' '.join(arr)

#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
def pairSum(head):
        
    if not head: return 0
    
    curr=head
    arr=[]
    ans = float('-inf')
    while curr:
        arr += [curr.test]
        curr = curr.next
    
    l,r = 0,len(arr)-1
    while l<r:
        ans = max(ans,arr[l]+arr[r])
        l+=1; r-=1
    ans = max(ans,arr[l]+arr[r])
    
    return ans

#https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
def longestPalindrome(words):

        #you could iterate everything and try to find its complement
        
        #gotta be O(n)
        
        from collections import Counter
        ans=0
        pos=0
        comp = Counter(words)
        it = [x for x in comp]
        for x in it:
            co = x[1]+x[0]
            if co==x: 
                if comp[x] >= 2: ans += (comp[x]//2)*4
                if comp[x]%2: pos=2
                continue
            ans += min(comp[x],comp[co])*4
            comp[x],comp[co] = 0,0
        return ans+pos

#https://leetcode.com/problems/robot-bounded-in-circle/submissions/
def isRobotBounded(instructions):
        
    #intutive solution; find net mouvement after each maximum circle instruction (4 directions)
    
    curr,pos=0,[0,0]
    mvs={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0),-1:(-1,0),-2:(0,-1),-3:(1,0)}
    for x in instructions*4:
        if x=='L': curr += 1
        elif x=='R': curr -= 1
        else:
            if curr>=4 or curr<=-4: curr%=4
            i,j=mvs[curr]
            pos[0] += i; pos[1] += j
    if pos==[0,0]: return True
    return False

def numDecodings(s):

    #seems like a typical O(N) memo problem, for each s --> however many s[1:] and s[2:] possibilities. Edge cases to be dealt seperately once it becomes len(s) in [1,2]
    
    self.memo={}
    def testid(s):
        if len(s)==2 and s[0]=='0': return False
        if 0<int(s)<27: return 1
        return 0
    
    def solve(s):
        if s in self.memo: return self.memo[s]
        if len(s)==1:
            if int(s): return 1
            return 0
        if len(s)==2: return testid(s) + (testid(s[0])&testid(s[1]))
        self.memo[s] = (solve(s[1:]) if testid(s[0]) else 0) + (solve(s[2:]) if testid(s[:2]) else 0)
        return self.memo[s]
    
    return solve(s)

#https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/

def insertIntoBST(root,test):
        
    curr=root
    if not root: return TreeNode(test)
    while True:
        if test<curr.test:
            if not curr.left: curr.left=TreeNode(test); break
            else: curr=curr.left
        elif test>curr.test:
            if not curr.right: curr.right=TreeNode(test); break
            else: curr=curr.right
    return root

#https://leetcode.com/problems/coin-change/

def coinChange(coin,amount):
        
    #it appears to be typical O(n^2) 1-D dp. we only need to calculate up to the desired amount and we always attempt to minimize # of coins that form components that form "amount"
    
    dp=[0]+[float('inf') for _ in range(amount)]
    for n in coins:
        for i in range(len(dp)):
            if type(dp[i])==int and i+n<len(dp): dp[i+n]=min(dp[i+n],dp[i]+1)
    return dp[-1] if type(dp[-1])==int else -1

#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/
def findMinArrowShots(points):
        
        #seems like a greedy problem where u shoot in priority of overlaps, should be nlogn or n 
        #ok so looks like we were right; when we take out a balloon, just take out as many as u can along with it
        
        import bisect
        
        points.sort(key=lambda x:x[0])
        pp=[x[0] for x in points]
        
        i,ans = 0,0
        while i<len(points):
            mined=points[i][1]
            while i<len(points) and points[i][0]<=mined:
                mined=min(mined,points[i][1]); i+=1
            ans+=1
        return ans

#https://leetcode.com/problems/jump-game-iv/submissions/
def minJumps(arr):
        
        #a simple graph bfs
        
        from collections import deque
        
        conc=defaultdict(list)
        for i,j in enumerate(arr): conc[j] += [i]
        
        def testid(i):
            if 0<=i<len(arr): return True
            return False
        
        ans=0
        dq,seen=deque([0]),{0}
        while dq:
            for i in range(len(dq)):
                curr=dq.popleft(); seen.add(curr)
                if curr==len(arr)-1: return ans
                dq += [x for x in [curr+1 if testid(curr+1) else None,curr-1 if testid(curr-1) else None]+conc[arr[curr]] if x!=None and x not in seen]
                conc[arr[curr]]=[]
            ans+=1
        return ans

#https://leetcode.com/problems/interleaving-string/submissions/
def isInterleave(s1,s2,s3):

        #this seems like a brute force + dp memo question coz u can interleave a certain substring of s3 and have the same remaining substrings of s1 and s2 left.
        #so yea lol
        
        if len(s1)+len(s2)!=len(s3): return False
        
        @cache
        def dfs(curr,rem1,rem2):
            if len(curr)==len(s3): return True
            return (dfs(curr+rem1[0],rem1[1:],rem2) if (rem1 and rem1[0]==s3[len(curr)]) else False) or (dfs(curr+rem2[0],rem1,rem2[1:]) if (rem2 and rem2[0]==s3[len(curr)]) else False)
        
        return dfs('',s1,s2) 

#https://leetcode.com/problems/russian-doll-envelopes/submissions/
def maxEnvelopes(envs):
        
    #just apply LIS and pay attention to avoid collisions with cases between equal widths but height1<height2
    
    import bisect
    arr=[x[1] for x in sorted(envs,key=lambda x:(x[0],-x[1]))] 
    stack=[]
    for x in arr:
        if stack and (i:=bisect.bisect_left(stack,x))<len(stack): stack[i]=x
        else: stack += [x]
    return len(stack)

#https://leetcode.com/problems/maximize-distance-to-closest-person/submissions/
def maxDistToClosest(seats):
        
    #O(n) dpl dpr typa problem
    
    dpl,dpr=[float('inf') for _ in range(len(seats))],[float('inf') for _ in range(len(seats))]
    for i in range(len(seats)):
        if seats[i]: dpl[i]=0
        elif i: dpl[i]=dpl[i-1]+1
    for i in range(len(seats)-1,-1,-1):
        if seats[i]: dpr[i]=0
        elif i<len(seats)-1: dpr[i]=dpr[i+1]+1
    return max(min(i,j) for i,j in zip(dpl,dpr))

#https://leetcode.com/problems/minimum-falling-path-sum-ii/
def minFallingPathSum(grid):
        
        #O(mn) top-down dp, looks like its jus dp[i][j] += dp[i-1][j], and then we sweep the row to see find out the real dp[i][j]
    
        if all([len(grid)==1,len(grid[0])==1]): return grid[0][0]
    
        def helper(i):
            psl,psr=[grid[i][0]],[0]*(len(grid[0])-1)+[grid[i][-1]]
            for j in range(1,len(grid[0])):
                psl += [min(grid[i][j],psl[-1])]
            for j in range(len(grid[0])-2,-1,-1):
                psr[j] = min(grid[i][j],psr[j+1])
            for j in range(len(grid[0])):
                grid[i][j] = min(psl[j-1] if j-1>=0 else float('inf'),psr[j+1] if j+1<len(grid[0]) else float('inf'))
            
        for i in range(len(grid)):
            if not i: helper(i); continue
            for j in range(len(grid[0])):
                grid[i][j] += grid[i-1][j]
            helper(i)
        return min(grid[-1])

#https://leetcode.com/problems/solving-questions-with-brainpower/submissions/
def mostPoints(questions):
        
    #points, brainpower
    #should be O(n) memo (this happens to be over tle by a lil bit)
    
    #you can take or skip
    #if u iterate backawards u can find max when time is up by 1-d dp
    
    dp = [0 for _ in range(len(questions))]
    for i in range(len(questions)-1,-1,-1):
        dp[i] = max(dp[i+1] if i+1<len(questions) else 0, questions[i][0]+(dp[1+i+questions[i][1]] if 1+i+questions[i][1]<len(questions) else 0))
    return dp[0]

#https://leetcode.com/problems/range-sum-query-2d-immutable/submissions/
class NumMatrix:

    def __init__(self, matrix):
        self.lookup = defaultdict(int)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.lookup[(i, j)] = self.lookup[(i-1, j)] + self.lookup[(i, j-1)] - self.lookup[(i-1, j-1)] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.lookup[(row2, col2)] - self.lookup[(row1-1, col2)] - self.lookup[(row2, col1-1)] + self.lookup[(row1-1, col1-1)]

#https://leetcode.com/problems/koko-eating-bananas/submissions/
def minEatingSpeed(piles,h):
        
        #BS O(nlogn) solution
        
        import math
        l,r=1,max(piles)
        while l<r:
            m=(l+r)//2; tot=sum(math.ceil(p/m) for p in piles)
            if tot>h: l=m+1
            else: r=m
        return l

#https://leetcode.com/problems/stone-game-iv/
def winnerSquareGame(n):
        
    #A nice O(n^1.5) time dp solution
    #dp[i] = if current player can force the opponent into a losing state
    #this is pre much jus a top-down intuitive approach
    
    #e.g if I got 2 left, I can take 2 and force a win. Therefore if someone can force me into 2, I'll lose...
    #the key point is "assuming both players play optimally". ^^thts wht it means
    
    sqr=[i**2 for i in range(1,int(n**0.5)+1)]
    dp=[False for _ in range(n+1)]
    for i in range(1,n+1):
        for s in sqr:
            if i-s<0: break
            elif not dp[i-s]: dp[i]=True; break
    return dp[-1]

#https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
def minimumCost(cost):
        
    #greedy
    
    cost.sort(reverse=True)
    ans=0
    for i in range(len(cost)):
        if not (i+1)%3: continue
        ans += cost[i]
    return ans

#https://leetcode.com/problems/count-the-hidden-sequences/
def numberOfArrays(differences, lower: int, upper: int) -> int:
        
    #if min max dont work: no possibilities
    
    arr=[0]
    mini,maxi = 0,0
    for x in differences: 
        arr += [arr[-1]+x]
        mini = min(mini,arr[-1]); maxi = max(maxi,arr[-1])
    
    diff= lower-mini
    
    if maxi+diff>upper: return 0

    return 1+upper-(maxi+diff)

#https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/
def highestRankedKItems(grid, pricing, start: List[int], k: int):
        
    #typical bfs
    
    from collections import deque
    ans = []
    dq= deque([tuple(start)])
    seen = {tuple(start)}
    lo,hi = pricing
    
    def testid(i,j):
        if 0<=i<len(grid) and 0<=j<len(grid[0]): return True
        return False
    
    while dq and len(ans)<k:
        temp = []
        for _ in range(len(dq)):
            i,j=dq.popleft()
            if lo<=grid[i][j]<=hi: temp += [[i,j]]
            for I,J in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                if testid(I,J) and grid[i][j] and (I,J) not in seen:
                    dq += [(I,J)]; seen.add((I,J))

        ans += sorted(temp, key=lambda x:(grid[x[0]][x[1]], x[0],x[1]))
    
    return ans[:k]
     
#https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
def numberOfWays(cor):
        
    #Bruhhh I chocked so hard on the contest
    #the solution itself is acc very intuitive. jus divide 2 by 2 literally and multiply possibilities.  
    
    arr = [i for i,j in enumerate(cor) if j=='S']
    if not len(arr) or len(arr)%2: return 0
    ans = 1
    for i in range(1,len(arr)-1,2):
        ans *= arr[i+1]-arr[i]
    return ans % (10**9+7)    

#https://leetcode.com/problems/stamping-the-grid/
def possibleToStamp(grid,h,w):
        
    #O(mn) time/space
    #2-d psa the whole grid to see which positions are stampable first
    #then use 2-d difference array (acc more like defaultdict) to check if theres any unstamped positions 
    
    from collections import defaultdict
    dp=defaultdict(int)
    stmp = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j]: grid[i][j]=1
            else: grid[i][j]=0
            dp[(i,j)] = grid[i][j]+dp[(i-1,j)]+dp[(i,j-1)]-dp[(i-1,j-1)]
            if dp[(i,j)]-dp[(i,j-w)]-dp[(i-h,j)]+dp[(i-h,j-w)]==h*w: stmp += [[i,j]]

    da = defaultdict(int)
    for i,j in stmp:
        if dp[(i,j)]:
            da[(i+1,j+1)] += 1
            da[(i-h+1,j-w+1)] += 1
            da[(i+1,j-w+1)] -= 1
            da[(i-h+1,j+1)] -= 1
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j]: continue
            grid[i][j] = (grid[i-1][j] if i>0 else 0) + (grid[i][j-1] if j>0 else 0) - (grid[i-1][j-1] if i>0 and j>0 else 0) + da[(i,j)]
            if not grid[i][j]: return False
    
    return True

#https://leetcode.com/problems/sequential-digits/submissions/
def sequentialDigits(low,high):
        
    #intuitive O(1) solution
    
    self.ans = []
    
    def dfs(curr,n):
        if low<=curr<=high: self.ans += [curr]
        if curr>high or n==10: return
        dfs(curr*10+n,n+1)
    
    for i in range(1,10): dfs(i,i+1)
    return sorted(self.ans)     

#https://leetcode.com/problems/flower-planting-with-no-adjacent/submissions/
def gardenNoAdj(n,paths):
        
    #It's just O(n) greedy coz of the fact that each vertice only has 3 edges so there will always be an open spot
    
    from collections import defaultdict
    ans = [None for _ in range(n)]
    edges = defaultdict(list)
    for x,y in paths: 
        x -= 1; y -= 1
        edges[x] += [y]; edges[y] += [x]
    for i in range(n):
        used = {ans[j] for j in edges[i]}
        flw = 1
        while flw in used: flw += 1
        ans[i] = flw
    return ans

#https://leetcode.com/problems/couples-holding-hands/
def minSwapsCouples(row):
        
    #O(n) time/space dsu solution
    #if considering 2 chairs at a time, you can either make a full swap with another couple or a partial swap
    #full swap = get rid of two pairs in one swap
    #partial swap = need 2+ swaps for 3+ pairs
    
    #Therefore... 
    #size 2 dsu = done
    #size 4 dsu = 1 swap
    #everything else:
        #you will have at least 6 people to deal with (this would be 2 swaps), 8 would be 3 ...
        #so building off of this you'll need to swap (numnber of chairs-1 in question) times. 
        
    #constestts are loose so rebuilding the dsu after each swap is also possible tho its tedious
    
    
    self.dsu = {n:[1] for n in range(len(row))}
    
    def find(x):
        if type(self.dsu[x])==list: return x
        self.dsu[x] = find(self.dsu[x])
        return self.dsu[x]
    
    def union(x,y):
        res1,res2 = find(x), find(y)
        if res1!=res2: 
            self.dsu[res2][0] += self.dsu[res1][0]
            self.dsu[res1] = res2
            
    comp = {}
    for i in range(len(row)):
        comp[row[i]+1 if not row[i]%2 else row[i]-1] = i
    
    for i in range(len(row)):
        if not i%2: union(i,i+1)
        union(i,comp[row[i]])
    
    ans = 0
    for x in self.dsu:
        if self.dsu[x]==[4]: ans += 1
        elif type(self.dsu[x])==list and self.dsu[x][0]>4: ans += (self.dsu[x][0]//2)-1

    return ans

#https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/
class Solution:
    def findMaximumXOR(self,nums):
        
        #O(n) greedy + bitwise trie
        
        root = node()
        for n in nums:
            temp=bin(n)[2:]
            curr=root
            for x in ('0'*(32-len(temp))+temp):
                x=int(x)
                if not curr.next[x]: curr.next[x] = node(x)
                curr = curr.next[x]

        ans=0
        for n in nums:
            temp=bin(n)[2:]
            bitn = ('0'*(32-len(temp))+temp)
            res = '0b'
            curr=root
            for i in range(32): 
                comp = (int(bitn[i])+1)%2
                curr = curr.next[comp] if curr.next[comp] else curr.next[int(bitn[i])]
                res += str(curr.test)
            ans = max(ans,n^int(res,2))
        return ans
        
class node:
    def __init__(self,test=None):
        self.test = test
        self.next = [0,0]
        
        

 
