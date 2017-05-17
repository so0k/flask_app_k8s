# Imgur script

Simple script to get all image urls from an album

## Getting started

1.  Go to Imgur and register a client:
    https://api.imgur.com/oauth2/addclient

2.  Add secrets:
    ```bash
     echo 'IMGUR_CLIENT_ID=<client-id>
    IMGUR_CLIENT_SECRET=<client-secret>
    IMGUR_ALBUM_ID=<album-id>' > .secrets
    ```

3.  Build container image for script
    ```bash
    docker build -t imgur_script .
    ```

4.  Run script in container
    ```bash
    docker run -it --rm --env-file .secrets imgur_script
    ```