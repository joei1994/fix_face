To run this project:   
1. clone this project and navigate to project directory
2. run conda create -n <virtual_env_name> python=3.6 
3. run conda activate <virtual_env_name>  
4. run pip install -r requirements.txt 
5. run docker pull wachirawitjoei/fix_face 
6. run docker run -d -p 80:80 --name <container_name> wachirawitjoei/fix_face
7. run python client.py -i <image_path> e.g. python client.py -i ./images/messi.jpg
