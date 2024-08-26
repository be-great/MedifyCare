# Run app using virtualenv
```bash
./init.sh
```

# Run app using Docker
## build the image
```bash
docker build -t auth .
```
## run it 
```bash
docker run -d -p 5000:5000 auth
```
