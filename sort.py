class Solution:
    def bubble_sort(self, nums):

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

    def selection_sort(self, nums):
        
        for i in range(len(nums)):
            m = i
            for j in range(i, len(nums)):
                if nums[j] < nums[m]:
                    m = j

            nums[i], nums[m] = nums[m], nums[i]

        return nums

    def insertion_sort(self, nums):

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

    # mid element as pivot
    def quick_sort(self, nums):
        def recursion(head, tail):
            if tail <= head:
                return

            left, right = head, tail
            mid = left + (right - left) // 2

            pivot = nums[mid]

            while left <= right:
                if nums[left] < pivot:
                    left += 1
                elif nums[right] > pivot:
                    right -= 1
                elif right >= left:
                    nums[right], nums[left] = nums[left], nums[right]
                    left += 1
                    right -= 1

            # too buggy
            recursion(head, right)
            recursion(left, tail)

        recursion(0, len(nums) - 1)

    # last element as pivot
    def quick_sort(self, nums):
        def recursion(head, tail):

            # 1. **
            if tail <= head + 1:
                return

            pivot = nums[tail - 1]
            left, right = head, tail - 2

            # 2. equal has to go in too
            while left <= right:
                # 3. elements <= pivot, go to right
                # so that the recursion(head, right) will be more smooth
                if nums[left] <= pivot:
                    left += 1
                else:
                    # left will never be equal to right + 1
                    nums[left], nums[right] = nums[right], nums[left]
                    nums[right + 1], nums[right] = nums[right], nums[right + 1]
                    # `left` remains the same
                    right -= 1

            # 4. the range is really important
            recursion(head, right)
            recursion(right + 2, tail)

        # python always excludes the right edge
        recursion(0, len(nums))
        return nums

    def quick_sort_list_comprehension(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) - 1]

        l = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        r = [v for v in nums if v > pivot]

        return self.quick_sort_list_comprehension(l) + eq + self.quick_sort_list_comprehension(r)

    def merge_sort(self, nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        L = self.merge_sort(nums[:mid])
        R = self.merge_sort(nums[mid:])

        a = b = i = 0

        while a < len(L) and b < len(R):

            if L[a] < R[b]:
                nums[i] = L[a]
                a += 1
            else:
                nums[i] = R[b]
                b += 1

            i += 1

        while a < len(L):
            nums[i] = L[a]
            i += 1
            a += 1

        while b < len(R):
            nums[i] = R[b]
            i += 1
            b += 1

        return nums


    def heap_sort(self, nums):

        # func heapify (log n)
        def heapify(start, end):
            i = start

            l = 2 * i + 1
            r = 2 * i + 2

            while l < end or r < end:
                idx = i

                if l < end and nums[l] > nums[idx]:
                    idx = l
                
                if r < end and nums[r] > nums[idx]:
                    idx = r

                if idx == i:
                    break
                else:
                    nums[i], nums[idx] = nums[idx], nums[i]

                    i = idx
                    l = 2 * i + 1
                    r = 2 * i + 1

            return

        # main
        n = len(nums)

        # n/2 * log n = O(nlogn)
        for i in range(n - 1, -1, -1):
            heapify(i, n)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)

        return nums


arr = [6,5,3,1,8,7,2,4]
s = Solution()
result = s.heap_sort(arr)

print(result)