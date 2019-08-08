# nums = (1,1,2,3,1)
# def arrayCheck(nums):
#   if nums == (1,2,3):
#     print("True")
#   else:
#     print("False")
# print(arrayCheck(nums))
#################
# nums = (1,1,2,3,1)

# def arrayCheck(nums):
#     for i in range(len(nums)):
#         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3 :
#             return True
#     return False
# print(arrayCheck(nums))
###################################
# nums = (1, 1, 2, 4, 1)

# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3 :
#             return True
#     return False
# print(arrayCheck(nums))
######################
# words = 'hello'
# def string_bits(words):
#         result = ""
#         for i in range(0, len(words)):
#                 if i %2 == 0:
#                         result += words[i]
#         return result
# print(string_bits(words))

######################################
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

# words = ('Hiabc', 'abc')
# def end_other(a, b):
#         a = a.lower()
#         b = b.lower()
#         return (b.endswith(a) or a.endswith(b))
# print(end_other(words))

###########################################
words = The
def doubleChar(words):
  if words = T :
    print(T*T)
  elif words = h :
    print(h*h) 
  elif words = e:
    print(e*e)
  return
print(doubleChar(words))
