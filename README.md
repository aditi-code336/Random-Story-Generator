# Random Story Generator

## Overview
This project is a simple Python-based random story generator that creates short stories by combining predefined sentence fragments. Each execution produces a unique narrative using randomness.

It demonstrates basic concepts like string manipulation, data structures, and the use of Python’s standard library.

## How It Works
The program stores different parts of a story (sentence starters, characters, time, place, and actions) in tuples.  
Using the `random` module, it selects one element from each tuple and concatenates them into a complete story.

Every run generates a different output.

## Tech Stack
- Language: Python  
- Library: random (standard library)

## Features
- Generates a new story on every run  
- No external dependencies  
- Easy to extend with additional story elements  
- Beginner-friendly implementation

## How to Run
1. Ensure Python is installed on your system  
2. Save the script as `story_generator.py`  
3. Run the program:
   ```bash
   python story_generator.py
