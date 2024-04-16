class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            genre TEXT
        )
    """
    CREATE_GENRES_TABLE = """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    CREATE_BOOKS_TABLE = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            price INTEGER,
            picture TEXT,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    """
    DROP_GENRES_TABLE = "DROP TABLE IF EXISTS genres"
    DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books"
    POPULATE_GENRES = """
        INSERT INTO genres (name) VALUES ('фантастика'),
        ('драма'), ('романтика'), ('хоррор')
    """
    POPULATE_BOOKS = """
        INSERT INTO books (name, author, price, picture, genre_id) VALUES ('Бегущий в лабиринте', 'Джером Сэлинджер', 2000, 'images/book1.jpg', 1),
        ('Властелин Колец', 'Джон Толкин', 1000, 'images/book2.jpg', 2),
        ('Кафе Ночи', 'Артур Конан Дойл', 3000, 'images/book3.jpg', 3),
        ('Таракани', 'Артур Конан Дойл', 3000, 'images/book4.jpg', 4)
    """