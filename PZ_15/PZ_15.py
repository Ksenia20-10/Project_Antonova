# Вариант 4
# Работа с базой данных. Приложение "Библиотека"

import sqlite3
from datetime import datetime
# Cоздание бд и табл
def create_db():
    """Создаёт базу данных и таблицу 'Каталог'"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Каталог (
            Код_книги INTEGER PRIMARY KEY AUTOINCREMENT,
            Жанр TEXT,
            Страна_издания TEXT,
            Серия TEXT,
            Автор TEXT,
            Название_книги TEXT,
            Год_выпуска INTEGER,
            Аннотация TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("База данных 'library.db' и таблица 'Каталог' созданы.")

def add_book(genre, country, series, author, title, year, description):
    """Добавляет книгу в таблицу"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Каталог (Жанр, Страна_издания, Серия, Автор, Название_книги, Год_выпуска, Аннотация)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (genre, country, series, author, title, year, description))

    conn.commit()
    conn.close()
    print(f"Книга '{title}' добавлена.")


def add_sample_books():
    """Добавляет 10 книг для примера"""
    books = [
        ("Роман", "Россия", "Русская классика", "Достоевский Ф.М.", "Преступление и наказание", 1866,
         "Роман о теории и морали"),
        ("Роман", "Россия", "Русская классика", "Толстой Л.Н.", "Война и мир", 1869, "Эпопея о войне 1812 года"),
        ("Фантастика", "Англия", "Космическая опера", "Лем С.", "Солярис", 1961, "Психологическая фантастика"),
        ("Детектив", "Англия", "Шерлок Холмс", "Дойл А.К.", "Собака Баскервилей", 1902, "Мистический детектив"),
        ("Поэзия", "Россия", "Серебряный век", "Есенин С.А.", "Черный человек", 1925, "Поэма-исповедь"),
        ("Фэнтези", "Англия", "Властелин колец", "Толкин Дж.Р.Р.", "Братство кольца", 1954,
         "Начало эпического путешествия"),
        ("Роман", "Франция", "Зарубежная классика", "Дюма А.", "Граф Монте-Кристо", 1844, "Роман о мести и прощении"),
        ("Научпоп", "Россия", "Наука", "Хокинг С.", "Краткая история времени", 1988, "О космологии для всех"),
        ("Детектив", "Швеция", "Миллениум", "Ларссон С.", "Девушка с татуировкой дракона", 2005,
         "Триллер о журналистском расследовании"),
        ("Роман", "США", "Американская проза", "Хемингуэй Э.", "Старик и море", 1952, "Повесть о борьбе и достоинстве"),
    ]

    for book in books:
        add_book(*book)
    print("\n--- Добавлено 10 книг ---\n")

def show_all_books():
    """Выводит все книги из таблицы"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Каталог")
    books = cursor.fetchall()

    conn.close()

    if not books:
        print("Таблица пуста.")
        return

    print("\n" + "=" * 80)
    print("СПИСОК ВСЕХ КНИГ:")
    print("=" * 80)
    for book in books:
        print(f"Код: {book[0]} | {book[3]} - '{book[4]}' ({book[5]} г.) | Жанр: {book[1]} | Страна: {book[2]}")
    print("=" * 80 + "\n")

def search_by_author(author):
    """Поиск книг по автору"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Каталог WHERE Автор LIKE ?", (f"%{author}%",))
    results = cursor.fetchall()
    conn.close()

    print(f"\n--- Поиск по автору '{author}': найдено {len(results)} книг ---")
    for book in results:
        print(f"  {book[3]} - '{book[4]}' ({book[5]} г.)")
    return results


def search_by_year(year):
    """Поиск книг по году выпуска"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Каталог WHERE Год_выпуска = ?", (year,))
    results = cursor.fetchall()
    conn.close()

    print(f"\n--- Поиск по году '{year}': найдено {len(results)} книг ---")
    for book in results:
        print(f"  {book[3]} - '{book[4]}'")
    return results


def search_by_genre(genre):
    """Поиск книг по жанру"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Каталог WHERE Жанр LIKE ?", (f"%{genre}%",))
    results = cursor.fetchall()
    conn.close()

    print(f"\n--- Поиск по жанру '{genre}': найдено {len(results)} книг ---")
    for book in results:
        print(f"  {book[3]} - '{book[4]}' ({book[5]} г.)")
    return results

def delete_by_code(book_code):
    """Удаление книги по коду"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Каталог WHERE Код_книги = ?", (book_code,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    print(f"Удалено книг по коду {book_code}: {deleted}")
    return deleted


def delete_by_author(author):
    """Удаление всех книг автора"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Каталог WHERE Автор LIKE ?", (f"%{author}%",))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    print(f"Удалено книг автора '{author}': {deleted}")
    return deleted


def delete_old_books(year):
    """Удаление книг старше указанного года"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Каталог WHERE Год_выпуска < ?", (year,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    print(f"Удалено книг, изданных до {year} года: {deleted}")
    return deleted

def update_genre(book_code, new_genre):
    """Изменить жанр книги по коду"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Каталог SET Жанр = ? WHERE Код_книги = ?", (new_genre, book_code))
    conn.commit()
    updated = cursor.rowcount
    conn.close()

    print(f"Изменён жанр книги {book_code} на '{new_genre}': {updated}")
    return updated

def update_year_by_author(author, new_year):
    """Изменить год выпуска всех книг автора"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Каталог SET Год_выпуска = ? WHERE Автор LIKE ?", (new_year, f"%{author}%"))
    conn.commit()
    updated = cursor.rowcount
    conn.close()

    print(f"Обновлён год выпуска для книг автора '{author}' на {new_year}: {updated}")
    return updated


def add_to_description(book_code, additional_text):
    """Добавить текст к аннотации книги"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Аннотация FROM Каталог WHERE Код_книги = ?", (book_code,))
    result = cursor.fetchone()

    if result:
        new_description = result[0] + " " + additional_text if result[0] else additional_text
        cursor.execute("UPDATE Каталог SET Аннотация = ? WHERE Код_книги = ?", (new_description, book_code))
        conn.commit()
        print(f"Аннотация книги {book_code} дополнена.")
    else:
        print(f"Книга с кодом {book_code} не найдена.")

    conn.close()

def main():
    print("=" * 60)
    print("ПРИЛОЖЕНИЕ 'БИБЛИОТЕКА'")
    print("Работа с базой данных SQLite")
    print("=" * 60 + "\n")

    create_db()

    add_sample_books()

    show_all_books()

    print("\n" + "=" * 40)
    print("ПОИСК КНИГ")
    print("=" * 40)
    search_by_author("Достоевский")
    search_by_year(1954)
    search_by_genre("Детектив")

    print("\n" + "=" * 40)
    print("РЕДАКТИРОВАНИЕ КНИГ")
    print("=" * 40)
    update_genre(1, "Психологический роман")
    update_year_by_author("Лем", 1962)
    add_to_description(3, "Классика научной фантастики.")

    show_all_books()

    print("\n" + "=" * 40)
    print("УДАЛЕНИЕ КНИГ")
    print("=" * 40)
    delete_by_code(10)
    delete_by_author("Хемингуэй")
    delete_old_books(1900)

    show_all_books()

    print("\n" + "=" * 40)
    print("Работа программы завершена.")
    print("=" * 40)

if __name__ == "__main__":
    main()