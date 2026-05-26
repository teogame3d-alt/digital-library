import digital_library as dl


def test_borrow_and_return_updates_state():
    lib = dl.Library("Test Library")
    book = dl.Book("The Little Prince", "Antoine", 1943)
    reader = dl.Reader("Ana", "ana@example.com")

    lib.add_book(book)
    assert book.available is True

    assert lib.borrow_book(reader, "The Little Prince") is True
    assert book.available is False
    assert lib.total_successful_borrows == 1

    assert lib.return_book(reader, "The Little Prince") is True
    assert book.available is True


def test_save_and_load_roundtrip(tmp_path):
    lib = dl.Library("Test Library")
    lib.add_book(dl.Book("Ion", "Rebreanu", 1920, category="Classic"))
    lib.add_book(dl.Book("Baltagul", "Sadoveanu", 1930, category="Classic", available=False))

    out = tmp_path / "library.json"
    lib.save_to_file(str(out))

    # Load into a new instance and compare
    lib2 = dl.Library("Test Library")
    lib2.load_from_file(str(out))

    assert len(lib2.books) == 2
    assert lib2.books[0].title == "Ion"
    assert lib2.books[1].available is False


def test_search_by_author_case_insensitive(capsys):
    lib = dl.Library("Test Library")
    lib.add_book(dl.Book("Ion", "Liviu Rebreanu", 1920))
    lib.add_book(dl.Book("Baltagul", "Mihail Sadoveanu", 1930))

    found = lib.search_by_author("liviu rebreanu")
    assert len(found) == 1
    assert found[0].title == "Ion"


def test_snapshot_summarizes_library_state():
    lib = dl.Library("Test Library")
    reader = dl.Reader("Ana", "ana@example.com")
    lib.add_book(dl.Book("Ion", "Liviu Rebreanu", 1920, category="Classic"))
    lib.add_book(dl.Book("Clean Code", "Robert C. Martin", 2008, category="Software"))

    assert lib.borrow_book(reader, "Ion") is True

    snapshot = lib.snapshot()
    assert snapshot["total_books"] == 2
    assert snapshot["available_books"] == 1
    assert snapshot["borrowed_books"] == 1
    assert snapshot["categories"] == ["Classic", "Software"]
