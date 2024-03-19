# File: programming_language.py

from datetime import datetime


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamically typed."""
        return self.typing.lower() == 'dynamic'


# Record the current time
start_time = datetime.now()

# Estimate: 10 minutes

# Record the actual time
end_time = datetime.now()
execution_time = end_time - start_time
print("Actual time:", execution_time)
