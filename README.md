## build the image
```bash
docker build -t auth .
```
## run it 
```bash
docker run -d -p 5000:5000 auth
```
## To list avai packages 

```bash
pip index versions flask-login
```