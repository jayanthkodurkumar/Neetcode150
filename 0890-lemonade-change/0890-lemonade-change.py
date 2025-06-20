class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for i in range(len(bills)):
            bill = bills[i]
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif bill == 20:
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True
