# if (조건) : (실행)

age = 55

if age >= 60 : print("기준보다 나이가 많습니다.")
else : print("기준보다 나이가 적습니다.")

# if - elif
if age >= 100:
    print("초고령")
elif age >= 60:
    print("고령")
elif age >= 40:
    print("중년")
elif age >= 20:
    print("청년")
else:
    print("미성년")