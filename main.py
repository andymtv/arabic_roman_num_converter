
class ConvertArabicRomanNum():
    __doc__ = '''
    Info:   It converts numbers in both numeric systems from 1 to 3999.
            If you want to convert from Arabic to Roman, pass a Arabic Numeric System number to arabic_num=''
            If you want to convert from Roman to Arabic, pass a Roman Numeric System number to roman_num=''
    '''
    roman_nums = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    def __init__(self, arabic_num=0, roman_num=''):
        self.arabic_num = arabic_num
        self.roman_num = roman_num

    def convert(self):
        if self.arabic_num and not self.roman_num:
            roman_nums = list(ConvertArabicRomanNum.roman_nums.items())
            I = roman_nums[0][1]
            V = roman_nums[1][1]
            X = roman_nums[2][1]
            L = roman_nums[3][1]
            C = roman_nums[4][1]
            D = roman_nums[5][1]
            M = roman_nums[6][1]
            n = self.arabic_num
            thousands = n // 1000
            five_hundreds = (n - (thousands*1000)) // 500
            hundreds = (n - (thousands*1000) - (five_hundreds*500)) // 100
            five_tens = (n - (thousands*1000) - (five_hundreds*500) - (hundreds*100)) // 50
            tens = (n - (thousands*1000) - (five_hundreds*500) - (hundreds*100) - (five_tens*50)) // 10
            fives = (n - (thousands*1000) - (five_hundreds*500) - (hundreds*100) - (five_tens*50) - (tens*10)) // 5
            units = (n - (thousands*1000) - (five_hundreds*500) - (hundreds*100) - (five_tens*50) - (tens*10) - (fives*5)) // 1
            r_thousands = thousands*M
            r_five_hundreds = five_hundreds*D
            r_hundreds = hundreds*C
            r_five_tens = five_tens*L
            r_tens = tens*X
            r_fives = fives*V
            r_units = units*I
            roman_num_string = ''.join([r_thousands, r_five_hundreds, r_hundreds, r_five_tens, r_tens, r_fives, r_units])
            return roman_num_string
        elif self.roman_num and not self.arabic_num:
            roman_nums = list(ConvertArabicRomanNum.roman_nums.items())
            units = roman_nums[0][0]
            fives  = roman_nums[1][0]
            tens = roman_nums[2][0]
            five_tens = roman_nums[3][0]
            hundreds = roman_nums[4][0]
            five_hundreds = roman_nums[5][0]
            thousands = roman_nums[6][0]
            roman_num_string = self.roman_num
            arabian_num = 0
            for item in roman_num_string:
                arabian_num += thousands if item == 'M' else 0
                arabian_num += five_hundreds if item == 'D' else 0
                arabian_num += hundreds if item == 'C' else 0
                arabian_num += five_tens if item == 'L' else 0
                arabian_num += tens if item == 'X' else 0
                arabian_num += fives if item == 'V' else 0
                arabian_num += units if item == 'I' else 0
            return arabian_num
        else:
            print('Type a value from 1 to 3,999,999 with Roman or Arabian formats')


n1 = ConvertArabicRomanNum(roman_num='MDDCX')
print(n1.convert())

