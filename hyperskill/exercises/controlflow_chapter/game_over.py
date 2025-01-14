final_score = 0
win_count = 0
loss_count = 0
while True:
    scores = input().split() # Reading input seperated by a space
    if scores == "C":
        win_count += 1
        if win_count == 2:
            final_score += 1
    elif scores == "I":
        loss_count += 1
        if loss_count == 3:
            final_score -= 1
    if final_score == 2:
        print("You won")
        break
    elif final_score == -3:
        print("You lose")
        break

print(scores)