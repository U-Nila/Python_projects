quiz=[

    {
        "question":"1. who is the chief minister of tamilnadu?",
        "option":["A. modi","B. stalin","c. vijay","D. ajith"]  ,
        "answer":"B" 
    },  
    {
        "question":"2. which one is national fruit?",
        "option":["A. Mango","B. apple","c. orange","D. banana"],
        "answer":"A"
    },
    {
        "question":"3. which is your favorite colour?",
        "option":["A. blue","B.black","C. green"],
        "answer":"A"
    }
] 
score=0
for q in quiz:
    print("\n"+ q["question"])
    for option in q["option"]:
       print(option)
    user_input=input("your answer(A/B/C/D):").upper()
    if user_input==q["answer"]:
        print("correct")
        score=score+1
    else:
        print(f"wrong answer!!{q["answer"]}")

    print("\n quiz completed")

print(f"your final score:{score} out of {len(quiz)}")

       