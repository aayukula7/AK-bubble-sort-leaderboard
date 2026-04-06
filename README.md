# Leaderboard sorter (Bubble sort)
I chose to use bubble sort as it is a sorting method I am comfortable using, it is easy to visualize, and it was ideal for my app idea (as it clearly shows how scores move up in a leaderboard). 

## Demo

<img width="576" height="378" alt="Screenshot 2026-04-06 170437" src="https://github.com/user-attachments/assets/038f5246-f058-4556-a76d-1ac1b6f3d9e8" />

### Decomposition
- Take user input of names and scores
- Compare adjacent scores
- Swap if needed
- Repeat until sorted

### Pattern Recognition
- Repeated comparisons between players
- Highest scores move to the top

### Abstraction
- User only enters names and scores
- Sorting is handled internally

### Algorithm Design
- Input → player scores
- Process → Bubble sort comparisons and swaps
- Output → sorted leaderboard

## Steps to Run

pip install -r requirements.txt  
python app.py  

## Hugging Face Link
https://huggingface.co/spaces/aayukula7/AK-bubble-sort-leaderboard

## Testing & Verification

Tested with:
- Already sorted input
  <img width="603" height="376" alt="Screenshot 2026-04-06 174030" src="https://github.com/user-attachments/assets/e06c5ddf-9700-4e14-9719-695096a8b970" />

- Reverse order
  <img width="624" height="416" alt="image" src="https://github.com/user-attachments/assets/69cfa43d-924a-4838-b623-4595c1947760" />

- Invalid input
  <img width="581" height="213" alt="Screenshot 2026-04-06 173857" src="https://github.com/user-attachments/assets/a3ad4859-7743-407f-8ff9-5bd14ac8fe79" />


All outputs were correct

## Author
Aayushi Kularaj

## Acknowledgement
Explanations were obtained from OpenAI's ChatGPT to help undertand concepts used in the program. All code was understood, writted, and tested by me. 
