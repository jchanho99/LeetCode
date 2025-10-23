class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 5: "V", 10: "X", 50: "L", \
                 100: "C", 500: "D", 1000: "M"}
        divs = [1000, 500, 100, 50, 10, 5, 1]
        answer: str = ""

        pt = 0
        while pt < len(divs):
            t = num//divs[pt]
            num %= divs[pt]
            if t < 4:
                answer += (roman[divs[pt]]*t)
            elif t == 4:
                answer += (roman[divs[pt]]+roman[divs[pt-1]])
            elif 4 < t <= 8:
                answer += (roman[divs[pt-1]]+roman[divs[pt]]*(t-5))
            else:
                answer += (roman[divs[pt]]+roman[divs[pt-2]])

            pt += 2

        return answer
