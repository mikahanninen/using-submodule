from CustomLibrary import custom_keyword


def minimal_task():
    val = custom_keyword("abc")
    print(f"abc is now {val}")
    print("Done.")


if __name__ == "__main__":
    minimal_task()
