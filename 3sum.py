class Solution:
    def threeSum(self, nums):
        triplets = []
        dictionary = {}
        for index, value in enumerate(nums) :
            if (value not in dictionary) :
                dictionary[value] = []

            dictionary[value].append(index)

        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)) :
                remnant = -(nums[i] + nums[j])
                if (remnant in dictionary) :
                    dict_rem = dictionary[remnant]
                    if i in dict_rem: dict_rem.remove(i)
                    if j in dict_rem: dict_rem.remove(j)
                    if (len(dict_rem) >= 1) :
                        thistuple = (nums[i], nums[j], remnant)
                        thistuple = sorted(thistuple)
                        if (thistuple not in triplets) :
                            triplets.append(thistuple)

        return triplets

s = Solution()
nums = [-7,-4,-6,6,4,-6,-9,-10,-7,5,3,-1,-5,8,-1,-2,-8,-1,5,-3,-5,4,2,-5,-4,4,7]
# result = s.threeSum(nums)
# print(result)

# answer = [[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,2,7],[-9,3,6],[-9,4,5],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-1,8],[-7,2,5],[-7,3,4],[-6,-2,8],[-6,-1,7],[-6,2,4],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-3,-2,5],[-3,-1,4],[-2,-1,3],[-1,-1,2]]


answer = [[-7,3,4],[-7,2,5],[-7,-1,8],[-4,-2,6],[-4,-1,5],[-4,-4,8],[-4,-3,7],[-6,-1,7],[-6,-2,8],[-6,2,4],[-10,4,6],[-9,3,6],[-5,-1,6],[-8,2,6],[-9,4,5],[-8,4,4],[-3,-1,4],[-9,2,7],[-10,5,5],[-10,3,7],[-10,2,8],[-8,3,5],[-2,-1,3],[-5,2,3],[-1,-1,2],[-5,-2,7],[-5,-3,8]]

sorted(answer, key=lambda tup: answer[0])

print(answer)