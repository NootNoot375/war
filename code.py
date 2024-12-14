import random

player1List = [i for i in range(2, 15)] * 4
player2List = []
warList = []

def isWon():
    return len(player1List) == 0 or len(player2List) == 0

def runTurn():
    if isWon():
        return
    rand1 = random.randint(0, len(player1List) - 1)
    player1Move = player1List[rand1]
    player1List.pop(rand1)
    rand2 = random.randint(0, len(player2List) - 1)
    player2Move = player2List[rand2]
    player2List.pop(rand2)
    print(f"Player 1 Plays a {player1Move}")
    print(f"Player 2 Plays a {player2Move}")
    if player1Move > player2Move:
        player1List.append(player2Move)
        print("Player 1 Win")
    elif player1Move < player2Move:
        player2List.append(player1Move)
        print("Player 2 Win")
    else:
        print("WAR")
        warHappens()

def warHappens():
    if isWon():
        return
    for _ in range(4):
        rand1 = random.randint(0, len(player1List) - 1)
        warList.append(player1List[rand1])
        player1List.pop(rand1)
        rand2 = random.randint(0, len(player2List) - 1)
        warList.append(player2List[rand2])
        player2List.pop(rand2)
    player1war = player1List[-1]
    player2war = player2List[-1]
    print(f"Player 1 Plays a {player1war}")
    print(f"Player 2 Plays a {player2war}")
    if player1war > player2war:
        print("Player 1 Win")
        player1List.extend(warList)
    elif player1war < player2war:
        print("Player 2 Win")
        player2List.extend(warList)
    else:
        print("WAR")
        warHappens()

def logicWork():
    value = input("\nActions:\nNextTurn to start the next round\nViewScores will tell you how many cards each player has left\n\nWhat would you like to do:  ")
    if value.lower() == "nextturn":
        runTurn()
    elif value.lower() == "viewscores":
        print(f"Player 1 has {len(player1List)} cards left.\nPlayer 2 has {len(player2List)} cards left.")
        logicWork()

logicWork()


