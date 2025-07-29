def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    # Empty or only whitespace
    if hey_bob == "":
        return "Fine. Be that way!"
    
    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)
    
    # Yelling question (most specific - must come first)
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    # Just yelling
    elif is_yelling:
        return "Whoa, chill out!"
    # Just question
    elif is_question:
        return "Sure."
    # Normal statement
    else:
        return "Whatever."