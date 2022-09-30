# PSA Hackathon
server and client folders are separate, client side has reactjs with tailwind set up
server side has auth.py for authentication

run ```npm run dev``` in client folder to run the app, i've alr set up the react scripts command in package.json to run it
your server and client will both be started

client side runs at 3000
server side runs at 3001

in your clientside env file put this
```
# use this when you talk to the api
API_ENDPOINT = "http://localhost:3001"
```

in your serverside env file put this
```
FLASK_secret = "123secret"
JWT_secret = "456secret"
```