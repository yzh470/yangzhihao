import random

def guess_number_game():
    target = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    
    print("欢迎来到猜数字游戏！")
    print("我已经生成了一个 1-100 之间的整数。")
    print(f"你最多有 {max_attempts} 次机会来猜出这个数字。")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\n请输入你猜测的数字（第 {attempts + 1} 次）："))
        except ValueError:
            print("输入无效！请输入一个整数。")
            continue
        
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("请输入 1-100 之间的数字！")
            continue
        
        if guess < target:
            print("猜小了！")
        elif guess > target:
            print("猜大了！")
        else:
            print(f"恭喜你猜对了！答案是 {target}")
            print(f"你总共用了 {attempts} 次猜对了！")
            return
    
    print(f"\n游戏结束！你已经用完了 {max_attempts} 次机会。")
    print(f"正确答案是：{target}")

if __name__ == "__main__":
    guess_number_game()
