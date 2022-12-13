##
## EPITECH PROJECT, 2020
## groundhog
## File description:
## Makefile
##

all:
	cp main.py groundhog
	chmod +x groundhog

clean:

fclean: clean
	rm groundhog

re: fclean all