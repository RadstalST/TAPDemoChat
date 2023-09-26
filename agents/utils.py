import re


def split_document_chat(text):
    # Define regular expressions to match the patterns
    text = text.replace("\n", " ")
    user_pattern = re.compile(r'<\|user\|>(.*?)<\|eos\|>')
    ai_pattern = re.compile(r'<\|ai\|>(.*?)<\|eos\|>')

    # Find all user and AI messages
    user_messages = user_pattern.findall(text)
    ai_messages = ai_pattern.findall(text)
    print(user_messages,ai_messages)
    # Create a list of dictionaries
    conversation = []
    while text:
        # Find the first <eof> marker
        eof_match = re.search(r'<\|eos\|>', text)

        if eof_match:
            # Determine the sender based on the position of the <eof> marker
            eof_position = eof_match.start()
            sender = 'user' if '<|user|>' in text[:eof_position] else 'ai'

            # Find the message and remove the processed text
            message_match = user_pattern.search(text) if sender == 'user' else ai_pattern.search(text)
            if message_match:
                message = message_match.group(1).strip()
                text = text[message_match.end():]  # Remove processed text

                # Add the message to the conversation
                if message:
                    conversation.append({"who": sender, "message": message})
        else:
            break  # Exi
    return conversation
