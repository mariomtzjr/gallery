# gallery


### Set up
Run de follow commands:
`docker-compose build`
`docker-compose up`

### Create a superuser
To use the next command is necessary kown the container id. To knows it, you have to run this command first `docker ps`. The output column wich name is CONTAINER ID has the value we need to create a super user.

`docker exec -it container_id python manage.py createsuperuser`

### Endpoints

- album/listar: Get all albums
- album/crear: Create a new album
- album/delete: Delete an album
- album/<id_album>/image_gallery: Get all photos of an album (id_album represents current album)
- album/<id_album>/upload_image/: Upload a new photo from current album (id_album)
- admin: Site of Administration of django is enable (You need a supersuper to sign in)

