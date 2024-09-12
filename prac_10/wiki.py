import wikipedia


def get_wikipedia_page(title):
    try:
        page = wikipedia.page(title)
        print(f"\n{page.title}")
        print(f"{page.summary[:500]}...")  # Print the first 500 characters of the summary
        print(f"{page.url}\n")
    except wikipedia.DisambiguationError as e:
        print("\nWe need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.PageError:
        print(f'\nPage id "{title}" does not match any pages. Try another id!')
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def main():
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        get_wikipedia_page(title)


if __name__ == "__main__":
    main()
