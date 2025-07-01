#!/usr/bin/env python
# coding: utf-8

# In[12]:


from set_3_sample_data import social_graph

def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following']:
        if from_member in social_graph[to_member]['following']:
            return('friends')
        else:
            return('follower')
    elif from_member in social_graph[to_member]['following']:
        return('followed by')
    else: 
        return('no relationship')

from set_3_sample_data import board1, board2, board3, board4, board5, board6, board7

def tic_tac_toe(board):
    n = len(board)

    def all_same(cells):
        first = cells[0]
        if first == '':
            return None
        return first if all(cell == first for cell in cells) else None

    # Check rows
    for row in board:
        winner = all_same(row)
        if winner:
            return winner

    # Check columns
    for col in range(n):
        col_cells = []
        for row in range(n):
            col_cells.append(board[row][col])
        winner = all_same(col_cells)
        if winner:
            return winner

    # Main diagonal
    diagonal = [board[i][i] for i in range(n)]
    winner = all_same(diagonal)
    if winner:
        return winner

    # Second diagonal
    second_diagonal = [board[i][n - 1 - i] for i in range(n)]
    winner = all_same(second_diagonal)
    if winner:
        return winner

    return "NO WINNER"


from set_3_sample_data import legs

def eta(first_stop, second_stop, route_map):
    time_elapsed = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), data in route_map.items():
            if start == current_stop:
                time_elapsed = time_elapsed + data['travel_time_mins']
                current_stop = end
                break

    return(time_elapsed)


# In[ ]:





# In[ ]:




