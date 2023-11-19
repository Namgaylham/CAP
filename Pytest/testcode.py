import unittest
from unittest.mock import patch
from io import StringIO
import os
import turtle as t
class TestPingPongGame(unittest.TestCase):

    def setUp(self):
        # Set up any initial state for the tests
        pass

    def tearDown(self):
        # Clean up any resources used for the tests
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_score_update(self, mock_stdout):
        # Test if the score updates correctly
        player_a_score = 0
        player_b_score = 0
        #update_score(player_a_score, player_b_score)
        self.assertEqual(mock_stdout.getvalue().strip(), "Player A: 0 Player B: 0")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('os.system')
    def test_wall_collision(self, mock_os_system, mock_stdout):
        # Test if the wall collision updates the score and plays the sound
        ball = t.Turtle()
        ball.goto(400, 0)
        ball_dx = 1.5
        player_a_score = 0
        player_b_score = 0

        handle_wall_collision(ball, ball_dx, player_a_score, player_b_score)

        self.assertEqual(ball.xcor(), 0)
        self.assertEqual(ball_dx, -1.5)
        self.assertEqual(player_a_score, 1)
        self.assertEqual(mock_stdout.getvalue().strip(), "Player A: 1 Player B: 0")
        mock_os_system.assert_called_with("afplay wallhit.wav&")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('os.system')
    def test_paddle_collision(self, mock_os_system, mock_stdout):
        # Test if the paddle collision updates the ball direction and plays the sound
        ball = t.Turtle()
        ball.goto(340, 0)
        ball_dx = 1.5
        player_a_score = 0
        player_b_score = 0
        paddle_right = t.Turtle()
        paddle_right.goto(350, 0)

        handle_paddle_collision(ball, ball_dx, paddle_right, player_a_score, player_b_score)

        self.assertEqual(ball.xcor(), 340)
        self.assertEqual(ball_dx, -1.5)
        self.assertEqual(mock_stdout.getvalue().strip(), "Player A: 0 Player B: 0")
        mock_os_system.assert_called_with("afplay paddle.wav&")

if __name__ == '__main__':
    unittest.main()


