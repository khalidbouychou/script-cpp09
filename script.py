# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: khbouych <khbouych@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/20 19:43:15 by khbouych          #+#    #+#              #
#    Updated: 2024/03/20 19:45:27 by khbouych         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

import random

for n in range(2, 3000):
    for data in range(10):
        input = list(range(n))
        if (data == 0):
            input = input[::-1]
        else:
            random.shuffle(input)
        out_args = input
        input = [str(x) for x in input]
        input = " ".join(input)
        command = "../PmergeMe " + input + " > res.txt"
        os.system(command)
        after = open("res.txt").read().split("After   :")[1].split("\n")[0]
        after = after.split(" ")
        after = [int(x) for x in after if x.strip()]
        if (after != sorted(out_args)):
            print (command)
            exit()
        print ("OK", "n: ", n, "data: ", data)