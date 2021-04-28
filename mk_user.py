#!/usr/bin/env/ python3
# -*- coding: utf8 -*-
"""Sampling python code that creates users and displays them."""

from app import db, User

def create_my_user(first_name, last_name, hobbies):
    """Simple user creation funstion"""
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()

if __name__ == "__main__":
    create_my_user("Matt", "Walter", "boxing")
    users = User.query.all()
    print(users)
    create_my_user("John", "Doe", "golfing")
    user = User.query.filter_by(first_name="John").first()
    print(user)