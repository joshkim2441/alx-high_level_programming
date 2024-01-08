#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """Inverts int operators == and !=."""

    def __eq__(self, other):
        """Overrides == operator with != behaviour."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides != operator with == behaviour."""
        return super().__eq__(other)
