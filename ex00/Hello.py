"""Simple greetings stored in a list, tuple, set, and dictionary."""


def main() -> None:
    """Display the requested greeting variations."""
    # Base containers provided in the subject.
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # Update each container with the requested messages.
    ft_list[1] = "World!"
    ft_tuple = (ft_tuple[0], "France!")
    ft_set.remove("tutu!")
    ft_set.add("Paris! ")
    ft_dict["Hello"] = "42Paris!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
