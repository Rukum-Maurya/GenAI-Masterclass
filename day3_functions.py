def get_count(message):
    try:
        # We try to execute our normal logic
        word_list = message.split()
        word_counts = {}

        for word in word_list:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        
        # Return the finished dictionary
        return word_counts
    
    except Exception as e:
        # If an error happens (e.g., the input wasn't a string)
        # We catch the error and return a safe dictionary instead of crashing
        return {"Error": "Invalid input. Please provide a text string."}
    
# --- Testing our Function ----

# Test 1: Normal behavior
print("Test 1 result:", get_count("AI is great and AI is the future"))

# Test 2: The Safety Net (passing an integer instead of a string)
print("Test 2 Result:",get_count(404))
    
