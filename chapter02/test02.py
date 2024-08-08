#test02.py

while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
        ##ここに書く
        if number == 1:
            raise ValueError("invaalid literal for int() with base 10: 'hoge'")
        elif number == 2:
            raise IndexError('string index out of range')
        elif number == 3:
            print('↓')
            print('例外を発生させませんでした')
            print('↓')
            print('もう一度選択しましょう')
        # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
        ##ここに書く
        else:
            print('↓')
            print('終了します')
            break
    except ValueError as e:
        print('↓')
        print('ValueError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')
    except IndexError as e:
        print('↓')
        print('IndexError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')

print('↓')
print('無限ループを終了します')