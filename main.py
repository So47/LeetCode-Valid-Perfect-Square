class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        def get_sqrt(num):
            if num < 2:
                return num

            left,right = 2, num // 2

            while left <= right:
                mid = (left + right) // 2
                product = mid * mid

                if product > num:
                    right = mid - 1
                elif product < num:
                    left = mid + 1
                else:
                    return mid
            return right        

        sqrt_num = get_sqrt(num)
        return sqrt_num * sqrt_num == num
        
        # if num < 2:
        #     return num
        # left,right = 2, num // 2

        # while left <= right:
        #     mid = (left + right) // 2
        #     product = mid * mid

        #     if product > num:
        #         right = mid - 1
        #     elif product < num:
        #         left = mid + 1
        #     else:
        #         return True
        # return False        
