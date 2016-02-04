# -*- coding: utf-8 -*-
import sys
import os
import regex
import codecs

dbpath = os.path.realpath('../models')
sys.path.append(dbpath)

from cleo import Command, InputArgument, InputOption
from user_model import UserModel
from auth_token_model import AuthTokenModel

class LoginUserWithCredentials(Command):

    name = 'user:login'

    description = 'Logs in a user'

    arguments = [
        {
            'name': 'username',
            'description': 'Username',
            'required': True
        },
        {
            'name': 'password',
            'description': 'Password',
            'required': True
        }
    ]

    def __init__(self):
        super(LoginUserWithCredentials, self).__init__()

    def execute(self, i, o):
        """
        Executes the command.

        :type i: cleo.inputs.input.Input
        :type o: cleo.outputs.output.Output
        """
        
        # Read parameters
        username = i.get_argument('username')
        password = i.get_argument('password')

        user = UserModel.getByUsername(username)
        token = user.generateToken(password)
        token.save()
        print token
        print AuthTokenModel.getByAttributeSingle('id', token.id)








        
