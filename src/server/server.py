#!/usr/bin/env python3

import pickle
import socket

from src.server.intelligence.agent import Agent

HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                # print('Connected by', addr)
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    pacman_food_board_coords, pacman_board_coords, cost, heuristic, board = pickle.loads(data)
                    agent = Agent.getInstance(pacman_food_board_coords, pacman_board_coords, cost, heuristic, board)
                    solution = agent.astar_search()
                    conn.sendall(pickle.dumps(solution))
