class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new = 0
        last = False
        for ind in range(len(flowerbed)):
            if flowerbed[ind] == 0:
                if last is False and (ind==len(flowerbed)-1 or flowerbed[ind+1]==0):
                    last = True
                    new += 1
                else:
                    last = False
            else:
                last = True

        if new >= n:
            return True
        else:
            return False
