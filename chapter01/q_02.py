# 2-1
print('==== 2-1 ====')
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if(place in get_place): #ここから記述（ヒント：in演算子を用いて、条件分岐）
        print(place + "のチケットが当選しました！")
    elif(place in wait_place): #ここから記述（ヒント：in演算子を用いて、条件分岐
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")


# 2-2
print('==== 2-2 ====')
get_place += wait_place
# print(get_place)

for place in all_place:
    if(place in get_place):
        print(f"{get_place[0]}と{get_place[1]}と{get_place[2]}のチケットが当選しました！")
    # elif(place in get_place): 
    #     print(place + "のチケットが当選しました！")
    elif(place in wait_place): 
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")