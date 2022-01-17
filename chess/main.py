from abc import ABC, abstractmethod
from dataclasses import dataclass
import typing


class OutOfBoundsException(Exception):
    """
    Cannot Move Piece to that Location
    """

class SpecialMoveException(Exception):
    """
    Raise a special move case.
    """


class Piece(ABC):
    type = None # Black or white
    
    def same_color(self, first_color, second_color):
        return first_color == second_color

    def in_bounds(self, x,y):
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False
        return True

    @abstractmethod
    def move(self):
        """
        Move will take in a location and will reutrn true if we can move a piece
        and false if we cannot.
        """
        raise NotImplementedError

@dataclass
class MoveData:
    """
    Class for storing move state
    """
    x: int
    y: int




class Pawn(Piece):
    
    def __init__(self, piece_type)  -> None:
        self.has_moved = False
        self.type = piece_type 
        Piece.__init__(self)

    def move(self, board_state: typing.List[typing.List[Piece]], source: MoveData, destination: MoveData) -> bool:
        """
        Return bool of if we can move a piece

        Pawns can move in x ways
        1. Move 1 space forward
        2. Move 2 spaces forward
        3. move 1 space diagonally

        Constraints
        Black pieces can only move negatively
        White pieces can only move positively
        Cannot move to a square with a piece of the same color
        """
        if not self.in_bounds(destination.x, destination.y):
            return False
        # pawns can only move
        if self.type == "white":
            if (source.x - destination.x) < 0:
                return False
        
        if board_state[destination.x][destination.y] is not None and self.same_color(self.type, board_state[destination.x][destination.y].type):
            return False
        
            
        
        


class Knight(Piece):
    pass

class Queen(Piece):
    pass

class Rook(Piece):
    pass

class Bishop(Piece):
    pass

class King(Piece):
    pass

        

class PieceFactory:
    """
    Class responsible for creating new pieces.
    """

    def __call__(self, piece_name, piece_type) -> Piece:
        if piece_name == 'pawn':
            return Pawn(piece_type=piece_type)
        elif piece_name == "knight":
            return Knight(piece_type=piece_type)
        elif piece_name == "queen":
            return Queen(piece_type=piece_type)
        elif piece_name == "bishop":
            return Bishop(piece_type=piece_type)
        elif piece_name == "rook":
            return Rook(piece_type=piece_type)
        elif piece_name == "king":
            return King(piece_type=piece_type)


class Board:
    """
    The board is responsible for getting a pieces position and moving a piece.
    """
    def __init__(self):

        self._board_state = self._build_initial_game_state()
    
    def _build_initial_game_state(self):
        piece_factory = PieceFactory()
        board_matrix = [[None for _ in range(8)] for _ in range(8)]
        # build front row of pawns for both sides

        for i in range(8):
            board_matrix[1][i] = piece_factory("pawn", "white")
            board_matrix[6][i] = piece_factory("pawn", "black")
        #build special pieces

        #rooks
        board_matrix[0][0] = piece_factory('rook', "white")
        board_matrix[0][7] = piece_factory('rook', "white")
        board_matrix[7][0] = piece_factory('rook', "black")
        board_matrix[7][7] = piece_factory('rook', "black")

        # knight
        board_matrix[0][1] = piece_factory('knight', "white")
        board_matrix[0][6] = piece_factory('knight', "white")
        board_matrix[7][1] = piece_factory('knight', "black")
        board_matrix[7][6] = piece_factory('knight', "black")
        
        # bishop
        board_matrix[0][2] = piece_factory('bishop', "white")
        board_matrix[0][5] = piece_factory('bishop', "white")
        board_matrix[7][2] = piece_factory('bishop', "black")
        board_matrix[7][5] = piece_factory('bishop', "black")

        # kings
        board_matrix[0][5] = piece_factory('king', "white")
        board_matrix[7][4] = piece_factory('king', "black")

        # queens
        board_matrix[0][4] = piece_factory('queen', "white")
        board_matrix[7][5] = piece_factory('queen', "black")

        return board_matrix

    
    def get(self, x, y):
        """
        Get the state at the board in the position of x, and y.
        """
        return self._board_state[x][y]

    def _set_state(self,x, y, payload):
        self._board_state[x][y] = payload
    
    def put(self, source: MoveData, destination: MoveData):
        """
        If source -> destination is valid:
            Move our our piece
        """
        piece: typing.Union[Piece,None] = self.get(source.x, source.y)

        if piece is None:
            return
        elif not piece.move(self._board_state, source, destination):
            return
        # Delete curr_position
        self._set_state(source.x, source.y, None)
        self._set_state(destination.x, destination.y, piece)
        