# import os
#
# from environs import Env
# from dataclasses import dataclass
#
#
# @dataclass
# class Bots:
#     bot_token: str
#     admin_token: int
#     database: str
#
#
# @dataclass
# class Settings:
#     bot: Bots
#
#
# def get_settings(path: str):
#     env = Env()
#     env.read_env(path)
#     return Settings(
#         bot=Bots(
#             bot_token=env.str("TOKEN_API"),
#             admin_token=env.int("ADMIN_TOKEN"),
#             database=env.str("DATABASE"),
#         )
#     )
#
#
# settings = get_settings('config.py')
#
# print(os.environ)
