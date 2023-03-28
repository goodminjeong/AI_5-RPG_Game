import random
import time


class Character:
    # 캐릭터의 모체가 되는 클래스
    def __init__(self, name, hp, power, mp, m_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.m_power = m_power

    # 일반공격 함수
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}님이 쓰러졌습니다. {self.name}님이 전투에서 승리하였습니다!")
            print("전투가 종료되었습니다.")
            quit()

    # 마법공격 함수
    def m_attack(self, other):
        damage = random.randint(self.m_power - 2, self.m_power + 2)
        use_mp = 0
        if self.mp >= damage * 0.8:
            use_mp = damage * 0.8
        else:
            print("마력이 부족합니다. 일반공격을 실시합니다.")
            self.attack(other)
            return
        monster.hp = max(monster.hp - damage, 0)
        self.mp = int(max(self.mp - use_mp, 0))
        if self.mp == 0:
            print("마력을 모두 사용하였습니다. 다음에는 마법공격이 불가능합니다.")
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}님이 쓰러졌습니다. {self.name}님이 전투에서 승리하였습니다!")
            print("전투가 종료되었습니다.")
            quit()

    # 캐릭터의 상태 표시 함수
    def show_status(self):
        print(
            f"{self.name}의 상태\nHP {self.hp}/{self.max_hp}\nMP {self.mp}/{self.max_mp}")


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power

    # 일반공격 함수
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}님이 쓰러졌습니다. {self.name}님이 전투에서 승리하였습니다!")
            print("전투가 종료되었습니다.")
            quit()

    # 몬스터의 상태 표시 함수
    def show_status(self):
        print(
            f"{self.name}의 상태\nHP {self.hp}/{self.max_hp}")

# 전투 진행 함수


def battle(self, other):
    while True:
        if self == player:
            while True:
                attack_type = str(
                    input("공격 유형을 선택하십시오(숫자 입력). 1: 일반공격, 2: 마법공격 (전투를 끝내고 싶다면 0을 누르세요)\n"))
                if attack_type == "1":
                    player.attack(monster)
                    monster.attack(player)
                    self.show_status()
                    other.show_status()
                    time.sleep(1)
                    print("\n")
                elif attack_type == "2":
                    player.m_attack(monster)
                    monster.attack(player)
                    self.show_status()
                    other.show_status()
                    time.sleep(1)
                    print("\n")
                elif attack_type == "0":
                    return print("전투가 종료되었습니다.")
                else:
                    continue
        elif self == monster:
            monster.attack(player)
            while True:
                attack_type = str(
                    input("당신 차례입니다. 공격 유형을 선택하십시오(숫자 입력). 1: 일반공격, 2: 마법공격 (전투를 끝내고 싶다면 0을 누르세요)\n"))
                if attack_type == "1":
                    player.attack(monster)
                    self.show_status()
                    other.show_status()
                    time.sleep(1)
                    print("\n")
                    break
                elif attack_type == "2":
                    player.m_attack(monster)
                    self.show_status()
                    other.show_status()
                    time.sleep(1)
                    print("\n")
                    break
                elif attack_type == "0":
                    return print("전투가 종료되었습니다.")
                else:
                    continue

# 선공을 위한 가위바위보 게임 함수


def rps():
    rps = input("\n선공을 잡기 위한 가위바위보 게임을 시작합니다. 가위/바위/보 중 하나를 입력하시오: ")
    monster_rps = random.choice(["가위", "바위", "보"])
    while True:
        if (rps == "가위" and monster_rps == "보") or (rps == "바위" and monster_rps == "가위") or (rps == "보" and monster_rps == "바위"):
            print(f"{player_name}: {rps}, {monster_name}: {monster_rps}")
            print(f"{player_name}님이 이겼습니다. 공격을 시작하세요\n")
            battle(player, monster)
            break
        elif (rps == "가위" and monster_rps == "바위") or (rps == "바위" and monster_rps == "보") or (rps == "보" and monster_rps == "가위"):
            print(f"{player_name}: {rps}, {monster_name}: {monster_rps}")
            print(f"{monster_name}가 이겼습니다. 공격이 시작됩니다\n")
            time.sleep(1.5)
            battle(monster, player)
            break
        elif rps == monster_rps:
            print(f"{player_name}: {rps}, {monster_name}: {monster_rps}")
            rps = input("\n비겼습니다. 다시 입력해주십시오(가위/바위/보): ")
            monster_rps = random.choice(["가위", "바위", "보"])
            continue
        else:
            rps = input("\n잘못 눌렀습니다. 다시 선택해주세요.(가위/바위/보): ")
            monster_rps = random.choice(["가위", "바위", "보"])
            continue


# 플레이어 생성
player_name = input("캐릭터의 이름을 지어주세요: ")
player_hp = random.randint(100, 120)
player_mp = random.randint(40, 60)
player_power = random.randint(10, 20)
player_m_power = random.randint(15, 30)
player = Character(player_name, player_hp, player_power,
                   player_mp, player_m_power)
player.show_status()

# 몬스터 생성
monster_name = random.choice(["고블린", "메두사", "트롤"])
monster_hp = random.randint(100, 120)
monster_power = random.randint(10, 20)
monster = Monster(monster_name, monster_hp, monster_power)
monster.show_status()

# 가위바위보 게임으로 시작
rps()
