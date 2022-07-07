def bishop_and_pawn(bishop, pawn):
    import string
    
    # Transform the input coordinates to numbers
    input_positions = [bishop, pawn]
    alphabet = list(string.ascii_lowercase)
    
    input_positions_transformed =[]
    for i in input_positions:
        letter, number = i[0], i[1]
        
        for idx,letter_position in enumerate(alphabet):
            if letter == letter_position:
                letter = idx+1
     
        input_positions_transformed.append((int(number)-1)*8+letter)  
        
    Bishop_position, Pawn_position = input_positions_transformed[0],input_positions_transformed[1]
       
    # Find all possible squares that bishop can move to
    all_chess_positions = []
    for i in range(1,65):
        all_chess_positions.append(i)
        
    bishop_possible_moves = []
    for position in all_chess_positions:
    
        if position == Bishop_position:
            print("Position of Bishop:",position)
            
            # Calculate in which line bishop is
            if position % 8 == 0:
                Horizontal_line = int(position/8)
                print("Horizontal line:", Horizontal_line)
            else:
                Horizontal_line = position/8
                Horizontal_line = int(Horizontal_line) +1
                print("Horizontal line:", Horizontal_line)
    
            # Find the spesific position of bishop on each line
            position_in_line = position - (Horizontal_line-1)*8
            print("Position in the line:", position_in_line)
            
            # Calculate the space horizontally left and right from the position on the spesific line
            space_to_the_LEFT = - (position_in_line  - 1)
            print("space on the left:",space_to_the_LEFT)
            space_to_the_RIGHT = - position_in_line  + 8
            print("space on the right:",space_to_the_RIGHT)
            print("----------------")
    
        
            # move UP or Down 
            print("Possible squares that the Bishop can land: ")
            for i in range(space_to_the_LEFT, space_to_the_RIGHT+1):
                
                # move UP left or right
                move_UP = position + (abs(i)*8) + i
                if (
                    move_UP < 65 and move_UP > 0 and
                    move_UP!=position
                    ):
                    print(move_UP)
                    bishop_possible_moves.append(move_UP)
                    
                # move DOWN left or right   
                move_DOWN = position - (abs(i)*8) + i
                if (
                    move_DOWN < 65 and move_DOWN > 0 and
                    move_DOWN!=position
                    ):
                    print(move_DOWN)
                    bishop_possible_moves.append(move_DOWN)   
                              
    # Final check             
    print("Pawn_coordinates: ",Pawn_position)
    if Pawn_position in bishop_possible_moves:
        print("Lucky Bishop!")
        return(True)
    else:
        print("Lucky Pawn!")
        return(False)
        
        
bishop = "a1"
pawn = "h8"
bishop_and_pawn(bishop,pawn)       
        
        