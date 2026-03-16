
def main():
    list = [19, 19, 5, 5, 5, 5, 5]
    number1 = 0
    number2 = 0
    for line in list:
        if line == 19:
            if number1 != 2:
                number1 += 1
        if line == 5:
            if number2 != 3:
                number2 += 1
    return (True if number1 == 2 and number2 == 3 else False)

def tmrin2(number):
    result = [number]
    lumber = number
    for _ in range(number-1):
        re = lumber+2
        lumber = re
        result.append(lumber)
        
    print(result)



def tmrin3():
    list = [
        0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210,
        220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410,
        420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610,
        620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810,
        820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990
    ]
    number = 0
    for _ in range(len(list)):
        if number not in list:
            return False
        number = number+10
    return True
print(tmrin3())