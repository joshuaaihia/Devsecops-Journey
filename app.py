def insecure_eval(user_input):
    # ❌ This is insecure on purpose (bad practice)
    return eval(user_input)

if __name__ == "__main__":
    print(insecure_eval("2 + 2"))
