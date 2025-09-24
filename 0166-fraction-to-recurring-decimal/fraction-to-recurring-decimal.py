class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0 or denominator < 0) and not (numerator < 0 and denominator < 0):
            res.append('-')

        integer = abs(numerator) // abs(denominator)
        res.append(str(integer))

        remainder = abs(numerator) % abs(denominator)
        print(remainder)
        if remainder == 0:
            return ''.join(res)

        res.append('.')
        seen = {}
        denominator = abs(denominator)

        while remainder != 0:
            if remainder in seen:
                res.insert(seen[remainder], "(")
                res.append(")")
                break
            
            seen[remainder] = len(res)
            remainder *= 10
            # print(remainder // denominator)
            res.append(str(remainder // denominator))
            remainder %= denominator
        # print(res)
        return ''.join(res)





