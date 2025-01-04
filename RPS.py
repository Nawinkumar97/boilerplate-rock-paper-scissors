def player(last_move, history=[]):
    # Reset or update history
    if last_move:
        history.append(last_move)
    else:
        history.clear()

    # Map moves to their counters
    move_counters = {'R': 'P', 'P': 'S', 'S': 'R'}
    next_move = 'S'  # Default move

    # Only attempt predictions if history is long enough
    if len(history) >= 4:
        # Extract all 4-move patterns from the history
        pattern_list = [''.join(history[i:i+4]) for i in range(len(history) - 3)]

        # Construct possible future patterns based on recent history
        recent_sequence = ''.join(history[-3:])
        possible_next_patterns = [recent_sequence + move for move in 'RPS']

        # Count occurrences of each possible pattern in history
        pattern_counts = {pattern: pattern_list.count(pattern) for pattern in possible_next_patterns}

        # Determine the most likely next move and counter it
        if pattern_counts:
            likely_pattern = max(pattern_counts, key=pattern_counts.get)
            predicted_move = likely_pattern[-1]
            next_move = move_counters[predicted_move]

    return next_move
