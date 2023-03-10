import pandas as pd
from fuzzywuzzy import process


def creating_user_book_list(df):
    print("Введите названиея книг и их оценки.")
    print("#### Для выхода введите exit на месте первого аругмента.###")

    user_book_list = []
    grade_list = []

    while True:
        end_of_input = input()
        if end_of_input == "exit":
            break

        book_name = book_name_input(df)
        grade = grade_input()

        user_book_list.append(book_name)
        grade_list.append(grade)

    user_book_list = pd.DataFrame({'id_book': user_book_list,
                                   'user': -1,
                                   'grade': grade_list})
    return user_book_list


def book_name_input(df):
    all_book = df["name"].drop_duplicates().tolist()

    while True:
        book_name = input("Название книги: ")

        list_similar_book_titles = process.extract(book_name, all_book)
        for book, _ in list_similar_book_titles:
            print(book)

        if book_name not in all_book:
            print("Введеной книги нет в базе.")
            continue
        return book_name


def displaying_the_most_similar_results():

    return


def grade_input():
    while True:
        try:
            grade = int(input("Оценка книги: "))
            if grade not in list(range(1, 11)):
                raise ValueError
        except ValueError:
            print("Оценкой должно быть число в пределах от 1 до 10.")
            continue
        return grade


def main():
    df = pd.read_csv(
        r"C:\Programming\GitHub\book_recomendation_system\data\data.csv", index_col=0)
    print(creating_user_book_list(df))


if __name__ == "__main__":
    main()
