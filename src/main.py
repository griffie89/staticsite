from textnode import TextNode, TextType  # Import your class and enum from textnode.py

def main():
    # Create a TextNode instance
    text_node = TextNode("Hello, World!", TextType.BOLD, "https://boot.dev")
    # Print the instance, which uses the __repr__ method
    print(text_node)

if __name__ == "__main__":
    main()