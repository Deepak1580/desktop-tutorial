a = input("ENTER YOUR NAME: ")
print("                                          HELLO", a, "!!!")
print("WELCOME TO QUIZ MASTER !!!".center(100))
print("LET'S START\n".center(100))
print("NOTE:(If you know the answer please type the option A,B,C,D.(Option must be in capital letters .)\n")
print("Q-1. What is the capital of India ?  ")
print("(A) Jaipur (B) Chandigarh (C) Delhi (D) Gurgaon")
lifeline_used = False
while True:
    b = input("Answer: ")
    if b == "C":
        print("Correct Answer")
        break
    else:
        print("Wrong Answer, Try again.\n")
        print("But you have ONE lifeline: 50:50")
        g = input("Would you like to take lifeline (Yes/No): ")

        if g == "Yes":
            lifeline_used = True
            print("OK, here is your lifeline:")
            print("Q-1. What is the capital of India?")
            print("(B) Chandigarh (C) Delhi")
            h = input("Answer: ")

            if h == "C":
                print("Correct Answer")
                print("Press Enter for the next question.")
            else:
                print("Wrong Answer, The Answer is (C) Delhi.")
                print("You don't know the capital of India.")
                print("press Enter for the next question:")

            break

        elif g == "No":
            print("OK, you will use lifeline in next question.")
            t = input("Answer: ")
            if t == "C":
                print("Correct Answer")
                lifeline_used = False
            else:
                print("Wrong Answer, The Answer is (C) Delhi.")
                print("You don't know the capital of India.")
                print("Press Enter for the next question:")

            break

print("LET'S MOVE ON NEXT QUESTION!!")
i = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q2="Q-2. The Nobel Prize for Physics in 2022 was awarded for work in which field ?"
print(Q2)
print("(A) Black Holes (B) Quantum Entaglement (C) Gravitation Waves (D) Nuclear Fusion")
while True:
    f = input("Answer:")
    if f == "B":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")

            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q2)
                print(" (B) Quantum Entaglement (D) Nuclear Fusion")
                h = input("Answer: ")

                if h == "B":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (B) Quantum Entaglement ")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "B":
                     print("Correct Answer")
                     lifeline_used = False
                else:
                     print("Wrong Answer, The Answer is (B) Quantum Entaglement ")
                     print("Press Enter for the next question:")
                     break

print("LET'S MOVE ON NEXT QUESTION!!")
i2 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q3="Q-3. Which Indian Mathematician has been called 'Man Who Knew Infinity' ?"
print(Q3)
print("(A) Arayabhatta (B) Bhaskar (C) C.V. Raman (D) Ramanujan")
while True:
    f = input("Answer:")
    if f == "D":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q3)
                print("(A) Arayabhatta (D) Ramanujan")
                h = input("Answer: ")

                if h == "D":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (D) Ramanujan")
                    print("press Enter for the next question:")
                    break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "D":
                 print("Correct Answer")
                 print("Press Enter for the next question.")
                lifeline_used = False

            else:

                print("Wrong Answer, The Answer is (D) Ramanujan")

                print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i3 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q4="Q-4. What was the earliest civilisation of Indian Subcontinent ?"
print(Q4)
print("(A) Harappan (B) Rakhigarhi (C) Dholavira (D) Lothal")
while True:
    f = input("Answer:")
    if f == "A":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q4)
                print("(A) Harappan (B) Rakhigari")
                h = input("Answer: ")

                if h == "A":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (A) Harappan ")

                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "A":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (A) Harappan ")
                    print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i4 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q5="Q-5. Where and When war  national anthem first sung ?"
print(Q5)
print("(A) Gujarat,1911 (B) Kolkata,1911 (C) Kolkata,1947  (D) Gujarat,1947 ")
while True:
    f = input("Answer:")
    if f == "B":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q5)
                print("(B) Kolkata,1911 (C) Kolkata,1947 ")
                h = input("Answer: ")

                if h == "B":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (B) Kolkata,1911.")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "B":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (B) Kolkata,1911.")
                    print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i5 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q6="Q-6. What is the equation of relativity ?"
print(Q6)
print("(A) E=mc^2 (B) E=mc.c (C) F.d = mc^2 (D) All are correct ")
while True:
    f = input("Answer:")
    if f == "D":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q6)
                print("(A) E=mc^2  (D) All are correct")
                h = input("Answer: ")

                if h == "D":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (D) All are correct.")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "D":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (D) All are correct.")
                    print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i7 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q7="Q-7. Who is known as the 'Father of the Computer' ?"
print(Q7)
print("(A) Charles Babbage (B) Alan Turing (C) ) John von Neumann (D) Bill Gates ")
while True:
    f = input("Answer:")
    if f == "A":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q7)
                print("(A) Charles Babbage (B) Alan Turing ")
                h = input("Answer: ")

                if h == "A":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (A) Charles Babbage.")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "A":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (A) Charles Babbage.")
                    print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i8 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q8="Q-8. Which planet is known as the 'Morning Star' ?"
print(Q8)
print("(A) Mars (B) Venus (C) Mercury (D) Saturn")
while True:
    f = input("Answer:")
    if f == "B":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q8)
                print("(B) Venus (C) Mercury ")
                h = input("Answer: ")

                if h == "B":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (B) Venus.")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "B":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (B) Venus.")
                    print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i8 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q9="Q-9. The first man to travel into space was ?"
print(Q9)
print("(A) Neil Armstrong (B)  Rakesh Sharma (C) Buzz Aldrin (D) Yuri Gagarin")
while True:
    f = input("Answer:")
    if f == "D":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q9)
                print("(A) Neil Armstrong (D) Yuri Gagarin")
                h = input("Answer: ")

                if h == "D":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (D) Yuri Gagarin.")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "D":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (D) Yuri Gagarin.")
                    print("Press Enter for the next question:")

                break

print("LET'S MOVE ON NEXT QUESTION!!")
i9 = input("Press ENTER for next Question:")
print("OK, Let's move on next question.\n")

Q10="Q-10.The World War II ended in which year ?"
print(Q10)
print("(A) 1942 (B) 1943 (C) 1945 (D) 1947 ")
while True:
    f = input("Answer:")
    if f == "C":
        print("Correct Answer.")
        print("Great,you have Good knowledge. ")
        break
    else:
        print("Wrong Answer, Try again.")
        if not lifeline_used:
            print("But you have ONE lifeline: 50:50")
            u = input("Would you like to take lifeline (Yes/No): ")
            if u == "Yes":
                lifeline_used = True
                print("OK, here is your lifeline:")
                print(Q10)
                print("(C) 1945 (D) 1947")
                h = input("Answer: ")

                if h == "C":
                    print("Correct Answer")
                    print("Press Enter for the next question.")
                else:
                    print("Wrong Answer, The Answer is (C) 1945.")
                    print("press Enter for the next question:")

                break

            elif u == "No":
                print("OK, you will use lifeline in next question.")
                t = input("Answer: ")
                if t == "C":
                    print("Correct Answer")
                    lifeline_used = False
                else:
                    print("Wrong Answer, The Answer is (C) 1945.")
                    print("Press Enter for the next question:")

                break

print("IT'S TIME TO END THIS GAME !!")
i10 = input("Press ENTER to end the game:")
print("\n")

print("Great, You completed the game !!!\n")
y = "NICE TO PLAY WITH YOU !!"
print(y.center(100))
print("                                         GOOD BYE", a, "!!!")
z = "HAVE A NICE DAY"
print(z.center(100))
print("Thanks for using my service\n")
print("Click on Run button to Play again.")


















