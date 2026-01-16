DISCLAIMER = "⚠️ Educational purposes only. This is not financial advice."

def format_response(
    text: str,
    add_disclaimer: bool = False
) -> str:
    """
    Formats the final response sent to the user.
    Adds disclaimer when required.
    """

    text = text.strip()

    if add_disclaimer and DISCLAIMER not in text:
        text = f"{text}\n\n{DISCLAIMER}"

    return text
