Steps to run project

1. clone this project
2. open terminal and set WD to PythonFastApi
3. start local docker instance
4. create image by running: docker build -t image_iris . 
5. run image in container: docker run --name container_iris -p 8000:8000 image_iris
6. you may test the /predict api-endpoint by visiting url/docs
7. you can run automated test to test the api-endpoint by simply running client.py in your local (ensure you have 
installed required packages mentioned in requirements.txt in local)


This model is also deployed to streamlit cloud
