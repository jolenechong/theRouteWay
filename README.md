# PSA Hackathon

### Setting Up
in your clientside env file put this
```
# use this when you talk to the api
REACT_APP_API_ENDPOINT=http://localhost:3001
```

in your serverside env file put this
```
FLASK_secret = "123secret"
```

Install the necessary libraries in the frontend (./client) and backend (./server)
In Frontend: ```npm i``` to install all libraries needed as listed in package.json

### Running the App
We need 2 terminals to run teh frontend and backend of the App.
client side runs at 3000
server side runs at 3001

First Terminal for Backend:
```
cd server
py main.py
```
Second Terminal for Frontend:
```
cd client
npm run start
```

Test the App with these information:
- Source PORT: T7
- Destination PORT: Y2
- When are you departing: Try Anytime

OR
- Source PORT: T2
- Destination PORT: X4
- When are you departing: Try Anytime

OR
- Source PORT: U3
- Destination PORT: Y2
- When are you departing: Try Anytime

### About the App Directories
AI_Train has the files with code needed to generate training dataset and train our AI model into our model.h5 file in server.

ml.py and training.csv are in root, training.csv is our training dataset we used for past deliveries in order to train our AI model.